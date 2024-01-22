odoo.define('algolia_integration.AlgoliaFacetFilter', function(require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.AlgoliaFacetFilter = publicWidget.Widget.extend({
        selector: '.oe_algolia_facet_filter',
        events: {
            'click .facet-value-checkbox': '_onFacetValueCheckboxClick',
            'click .clear-facets': '_onClearFacetsClick'
        },

        /**
         * @override
         */
        start: function() {
            this._super.apply(this, arguments);
            this.algoliaSearch = new algolia_integration.AlgoliaSearch();
            this._renderFacets();
        },

        /**
         * Render the facets based on Algolia's response.
         */
        _renderFacets: function() {
            var self = this;
            this.algoliaSearch.search.helper.on('result', function(content) {
                self.$el.empty();
                _.each(content.facets, function(facets, facetName) {
                    self.$el.append(self._createFacetList(facetName, facets));
                });
            });
        },

        /**
         * Create HTML for a single facet list.
         */
        _createFacetList: function(facetName, facets) {
            var $facetList = $('<div/>', { 'class': 'facet-list', 'data-facet': facetName });
            var $title = $('<h5/>').text(facetName);
            $facetList.append($title);

            _.each(facets, function(count, value) {
                var $label = $('<label/>', { 'class': 'facet-value-label' });
                var $checkbox = $('<input/>', {
                    'type': 'checkbox',
                    'class': 'facet-value-checkbox',
                    'data-facet': facetName,
                    'data-value': value
                });
                var $value = $('<span/>', { 'class': 'facet-value-name' }).text(value);
                var $count = $('<span/>', { 'class': 'facet-value-count' }).text('(' + count + ')');

                $label.append($checkbox).append($value).append($count);
                $facetList.append($label);
            });

            return $facetList;
        },

        /**
         * Handle clicking on a facet value checkbox.
         */
        _onFacetValueCheckboxClick: function(event) {
            var $checkbox = $(event.currentTarget);
            var facetName = $checkbox.data('facet');
            var value = $checkbox.data('value');
            this.algoliaSearch.toggleFacetRefinement(facetName, value);
        },

        /**
         * Handle clicking on the clear facets button.
         */
        _onClearFacetsClick: function() {
            this.algoliaSearch.clearRefinements();
        }
    });

    return {
        AlgoliaFacetFilter: publicWidget.registry.AlgoliaFacetFilter
    };
});