# -*- coding: utf-8 -*-
from collective.behavior.automaticrelateditems.utils import get_related
from plone import api
from zope.publisher.browser import BrowserView

import json


class AutomaticRelatedItemsView(BrowserView):

    """Json view to return automatically generated related items."""

    def setup(self):
        self.tags = self.request.get('tags[]', [])
        # when there is just one item it comes as a string
        if type(self.tags) is str:
            self.tags = [self.tags]

    def related_items(self, tags):
        """Return a dictionary with {path: title} of related items

        :param tags: List of tags to search related items
        :type tags: list
        :returns: A list of related items path
        :rtype: list
        """
        data = {}
        for path in get_related(tags):
            obj = api.content.get(path=path)
            data[path] = obj.Title()
        return data

    def __call__(self):
        self.setup()
        data = self.related_items(self.tags)
        response = self.request.response
        response.setHeader('content-type', 'application/json')
        return response.setBody(json.dumps(data))
