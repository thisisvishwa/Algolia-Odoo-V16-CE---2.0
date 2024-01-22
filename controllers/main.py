from odoo import http
from odoo.http import request

class SearchController(http.Controller):

    @http.route('/shop/algolia_search', type='json', auth='public', website=True)
    def algolia_search(self, **post):
        search_query = post.get('search_query', '')
        if not search_query:
            return {
                'error': 'Empty search query',
                'results': []
            }

        algolia_integration = request.env['algolia.integration'].sudo()
        results = algolia_integration.search_products(search_query)

        return {
            'error': None,
            'results': results
        }

    @http.route('/shop/algolia_suggestions', type='json', auth='public', website=True)
    def algolia_suggestions(self, **post):
        search_query = post.get('search_query', '')
        if not search_query:
            return {
                'error': 'Empty search query',
                'suggestions': []
            }

        algolia_integration = request.env['algolia.integration'].sudo()
        suggestions = algolia_integration.get_suggestions(search_query)

        return {
            'error': None,
            'suggestions': suggestions
        }

    @http.route('/shop/algolia_facet_filter', type='json', auth='public', website=True)
    def algolia_facet_filter(self, **post):
        search_query = post.get('search_query', '')
        filters = post.get('filters', {})
        
        algolia_integration = request.env['algolia.integration'].sudo()
        results = algolia_integration.filter_search_results(search_query, filters)

        return {
            'error': None,
            'results': results
        }