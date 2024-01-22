odoo.define('algolia_integration.AlgoliaSearch', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var Widget = require('web.Widget');

    var AlgoliaSearch = Widget.extend({
        events: {
            'keyup #algolia_search_input': '_onKeyUp',
            'click .algolia_result_item': '_onClickResultItem',
        },
        start: function () {
            this.algoliaClient = algoliasearch('YOUR_ALGOLIA_APPLICATION_ID', 'YOUR_SEARCH_ONLY_API_KEY');
            this.algoliaIndex = this.algoliaClient.initIndex('Algolia Index Name');
            return this._super.apply(this, arguments);
        },
        _onKeyUp: function (ev) {
            var self = this;
            var query = $(ev.currentTarget).val();
            if (query.length > 0) {
                this.algoliaIndex.search(query, {
                    hitsPerPage: 10,
                    typoTolerance: true
                }).then(function (responses) {
                    self._renderResults(responses.hits);
                });
            } else {
                this._clearResults();
            }
        },
        _onClickResultItem: function (ev) {
            var $target = $(ev.currentTarget);
            var url = $target.data('url');
            window.location.href = url;
        },
        _renderResults: function (hits) {
            var $resultsContainer = $('#algolia_results_container');
            $resultsContainer.html('');
            _.each(hits, function (hit) {
                var $item = $('<div/>', {
                    'class': 'algolia_result_item',
                    'data-url': hit.url,
                    'text': hit.name
                });
                $resultsContainer.append($item);
            });
        },
        _clearResults: function () {
            $('#algolia_results_container').html('');
        }
    });

    return AlgoliaSearch;
});

$(document).ready(function () {
    var algoliaSearch = new algolia_integration.AlgoliaSearch();
    algoliaSearch.attachTo($('#algolia_search_input').parent());
});