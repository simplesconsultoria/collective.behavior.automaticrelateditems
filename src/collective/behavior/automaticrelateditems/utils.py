# -*- coding: utf-8 -*-
from collections import Counter
from collective.behavior.automaticrelateditems.interfaces import IAutomaticRelatedItemsSettings
from plone import api


def get_related(tags):
    """Calculate related items based on tags

    :param tags: List of tags to search related items
    :type tags: list
    :returns: A list of related items path
    :rtype: list
    """
    # get how many items should be added
    record = dict(name='count', interface=IAutomaticRelatedItemsSettings)
    count = api.portal.get_registry_record(**record)

    # search every tag
    brains = []
    for t in tags:
        brains += api.content.find(Subject=t, review_state='published')

    # brains are not singleton, then we need to get paths
    paths = [b.getPath() for b in brains]

    # count how many times a path appear
    related = Counter(paths).most_common(count)

    # take out counts
    related = [r[0] for r in related]

    return related
