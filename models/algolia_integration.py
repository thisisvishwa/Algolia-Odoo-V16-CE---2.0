from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import logging

_logger = logging.getLogger(__name__)

class AlgoliaIntegration(models.Model):
    _name = 'algolia.integration'
    _description = 'Algolia Integration for Products'

    name = fields.Char(string='Integration Name', required=True)
    algolia_api_key = fields.Char(string='Algolia API Key', required=True)
    algolia_app_id = fields.Char(string='Algolia App ID', required=True)
    algolia_index_name = fields.Char(string='Algolia Index Name', default='odoo_products')
    is_active = fields.Boolean(string='Active', default=True)
    last_sync_date = fields.Datetime(string='Last Sync Date')

    @api.model
    def create(self, vals):
        if 'algolia_api_key' not in vals or 'algolia_app_id' not in vals:
            raise UserError('Algolia API Key and App ID are required to create an integration.')
        return super(AlgoliaIntegration, self).create(vals)

    def write(self, vals):
        if 'algolia_api_key' in vals or 'algolia_app_id' in vals:
            if not vals.get('algolia_api_key') or not vals.get('algolia_app_id'):
                raise UserError('Algolia API Key and App ID cannot be empty.')
        return super(AlgoliaIntegration, self).write(vals)

    def button_sync_with_algolia(self):
        self.ensure_one()
        if not self.is_active:
            raise UserError('Integration is not active.')
        self._sync_products_with_algolia()

    def _sync_products_with_algolia(self):
        headers = {
            'X-Algolia-API-Key': self.algolia_api_key,
            'X-Algolia-Application-Id': self.algolia_app_id,
        }
        products = self.env['product.template'].search_read([], ['name', 'description_sale', 'list_price', 'image_1920'])
        formatted_products = self._format_products_for_algolia(products)
        url = f'https://{self.algolia_app_id}.algolia.net/1/indexes/{self.algolia_index_name}'
        try:
            response = requests.put(url, json=formatted_products, headers=headers)
            response.raise_for_status()
            self.last_sync_date = fields.Datetime.now()
            _logger.info('Products successfully synchronized with Algolia.')
        except requests.exceptions.RequestException as e:
            _logger.error('Failed to synchronize with Algolia: %s', e)
            raise UserError('Failed to synchronize with Algolia.')

    def _format_products_for_algolia(self, products):
        algolia_products = []
        for product in products:
            algolia_products.append({
                'objectID': product['id'],
                'name': product['name'],
                'description': product['description_sale'],
                'price': product['list_price'],
                'image': product['image_1920'] and f"data:image/png;base64,{product['image_1920'].decode()}" or None,
            })
        return algolia_products

    @api.model
    def _scheduler_sync_with_algolia(self, domain=None):
        integrations = self.search(domain or [])
        for integration in integrations:
            if integration.is_active:
                integration._sync_products_with_algolia()