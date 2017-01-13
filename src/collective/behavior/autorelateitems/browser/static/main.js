var AutoRelateItems = (function() {
  function AutoRelateItems() {
    // Define texts
    this.relatedItemsHelpMessage = 'Click on browse button to search for related items or click on Suggest related items to automatically load some related items by tags (this button needs tags field filled).';
    this.buttonLabel = 'Suggest related items';
    this.buttonToolTip = 'Click on this button to load related items suggestions';

    this.render();
  }

  AutoRelateItems.prototype.render = function() {
    // Create HTML templates
    var helpTemplate = '<span class="formHelp">' + this.relatedItemsHelpMessage + '</span>';
    var buttonTemplate =
      '<input type="button" '+
              'value="' + this.buttonLabel + '" ' +
              'title="' + this.buttonToolTip + '" ' +
              'class="suggestRelatedItems">';
    this.relatedItemTemplate =
      '<span id="form-widgets-IRelatedItems-relatedItems-{count}-wrapper" ' +
            'class="option">' +
        '<label for="form-widgets-IRelatedItems-relatedItems-{count}">' +
          '<input type="checkbox" ' +
                 'name="form.widgets.IRelatedItems.relatedItems:list" ' +
                 'checked="checked" ' +
                 'id="form-widgets-IRelatedItems-relatedItems-{count}" ' +
                 'title="None" ' +
                 'value="{path}" ' +
                 'class="contenttree-widget relationlist-field">' +
          '<span class="label">{title}</span>' +
        '</label>' +
      '</span>';

    // Define jquery selectors
    $helpLabel = $('#formfield-form-widgets-IRelatedItems-relatedItems > label,' +
                   '#formfield-form-widgets-relatedItems > label,');
    $relatedItemsInput = $('#formfield-form-widgets-IRelatedItems-relatedItems-widgets-query,' +
                           '#formfield-form-widgets-relatedItems-widgets-query');
    this.$tags = $('#form-widgets-IDublinCore-subjects');
    this.$relatedItems = $(
      '#form-widgets-relatedItems-input-fields,' +
      '#form-widgets-IRelatedItems-relatedItems-input-fields'
    );

    // Change interface
    $helpLabel.append(helpTemplate);
    $relatedItemsInput.append(buttonTemplate);
    this.$loadButton = $('.suggestRelatedItems');

    // Bind events
    this.$loadButton.on('click', $.proxy(this.onClick, this));
    this.$tags.on('change keyup paste', $.proxy(this.onChangeTags, this));
    this.$tags.trigger('change');
  };

  AutoRelateItems.prototype.onClick = function(e) {
    e.preventDefault();
    $.ajax({
      url: portal_url + '/@@automatic-related-items',
      data: {
        tags: this.$tags.val().split('\n')
      }
    }).done($.proxy(this.addRelated, this));
  };

  AutoRelateItems.prototype.onChangeTags = function(e) {
    e.preventDefault();
    if (this.$tags.val() === '') {
      this.$loadButton.attr('disabled', 'disabled');
    } else {
      this.$loadButton.removeAttr('disabled');
    }
  };

  AutoRelateItems.prototype.addRelated = function(data) {
    $('.relationlist-field').parents('span').remove();
    var k, v, i, rendered;
    var hasIRelatedItems = $('#formfield-form-widgets-IRelatedItems-relatedItems').length > 0;

    i = 0;
    for (k in data) {
      v = data[k];
      rendered = this.relatedItemTemplate
                     .replace(/\{count\}/g, i)
                     .replace(/\{path\}/g, k)
                     .replace(/\{title\}/g, v);
      if (!hasIRelatedItems) {
        rendered = rendered.replace(/IRelatedItems./g, '');
      }
      this.$relatedItems.append(rendered);
      i += 1;
    }
  };

  return AutoRelateItems;
})();


$(function(){
  if ((/\+\+add\+\+/.test(location.pathname) ||
       /\/edit$/.test(location.pathname)) &&
      $('#formfield-form-widgets-relatedItems,' +
        '#formfield-form-widgets-IRelatedItems-relatedItems').length > 0) {
    new AutoRelateItems();
  }
});
