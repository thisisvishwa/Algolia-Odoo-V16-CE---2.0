from odoo.tests.common import TransactionCase

class TestAlgoliaIntegration(TransactionCase):

    def setUp(self):
        super(TestAlgoliaIntegration, self).setUp()
        # Setup test data and dependencies
        self.AlgoliaIntegration = self.env['algolia_integration.algolia_integration']

    def test_api_integration(self):
        # Test the API integration with Algolia
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Integration',
            'api_key': 'fake_api_key',
            'index_name': 'test_index'
        })
        self.assertTrue(algolia_integration.synchronize_with_algolia(), "Synchronization with Algolia failed")

    def test_configuration_parameters(self):
        # Test the configuration parameters in the backend module
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Configuration',
            'api_key': 'fake_api_key',
            'index_name': 'test_index',
            'sync_frequency': 'daily'
        })
        self.assertEqual(algolia_integration.sync_frequency, 'daily', "Sync frequency configuration failed")

    def test_typo_tolerance(self):
        # Test typo-tolerance functionality
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Typo Tolerance',
            'api_key': 'fake_api_key',
            'index_name': 'test_index'
        })
        self.assertTrue(algolia_integration.typo_tolerance, "Typo tolerance is not enabled by default")

    def test_faceting_and_filtering(self):
        # Test faceting and filtering functionality
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Faceting and Filtering',
            'api_key': 'fake_api_key',
            'index_name': 'test_index'
        })
        self.assertTrue(algolia_integration.enable_faceting, "Faceting is not enabled by default")

    def test_search_performance(self):
        # Test search performance
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Search Performance',
            'api_key': 'fake_api_key',
            'index_name': 'test_index'
        })
        self.assertTrue(algolia_integration.search('test query'), "Search did not return any results")

    def test_mobile_responsiveness(self):
        # Test mobile responsiveness
        algolia_integration = self.AlgoliaIntegration.create({
            'name': 'Test Mobile Responsiveness',
            'api_key': 'fake_api_key',
            'index_name': 'test_index'
        })
        self.assertTrue(algolia_integration.is_mobile_friendly, "Search is not optimized for mobile devices")

    def test_odoo_version_compatibility(self):
        # Test Odoo version compatibility
        self.assertTrue(self.AlgoliaIntegration._check_odoo_version(), "Algolia integration is not compatible with Odoo Version 16 Community Edition") 

    def tearDown(self):
        # Clean up after tests
        algolia_integrations = self.AlgoliaIntegration.search([])
        algolia_integrations.unlink()
        super(TestAlgoliaIntegration, self).tearDown()