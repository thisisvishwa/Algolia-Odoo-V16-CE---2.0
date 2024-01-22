# Odoo eCommerce Algolia Search Integration

This module integrates Algolia search into Odoo Version 16 Community Edition to enhance the eCommerce website's search functionality. It provides fast, accurate, and user-friendly search capabilities with advanced features like typo-tolerance, faceting, and filtering.

## Features

- **Algolia REST API Integration**: Real-time synchronization of product data with Algolia.
- **Enhanced Search Performance**: Instant search suggestions and precision search algorithms.
- **Typo-Tolerance**: Error correction for misspelled search queries.
- **Faceting and Filtering**: Advanced search with dynamic filters.
- **Responsive Search Results Page**: Customizable and mobile-friendly design.
- **Backend Configuration**: Manage Algolia settings from the Odoo Backend module.

## Installation

1. Clone the repository into your Odoo addons directory:
   ```
   git clone [REPOSITORY_URL] [ODOO_ADDONS_PATH]/algolia_integration
   ```
2. Install the module by navigating to Apps in the Odoo backend and searching for 'Algolia Integration'.
3. Click 'Install' to install the module.

## Configuration

1. Navigate to the Odoo Backend module.
2. Open the Algolia Backend Configuration form (`algolia_backend_config_form`).
3. Enter your Algolia API keys and set the indexing frequency and synchronization triggers.
4. Configure additional Algolia parameters as needed.

## Usage

- Use the search bar (`algolia_search_input`) to start searching for products.
- Apply filters using the faceted search system (`algolia_facet_filter`).
- View search results on the responsive search results page (`algolia_results_container`).

## Customization

- Customize the appearance of the search results through the Odoo Backend module.
- Adjust the displayed product information, image size, and price visibility.

## Dependencies

- Odoo Version 16 Community Edition
- Algolia account with API keys

## Documentation

- User Guide: `documentation/user_guide.md`
- Technical Documentation: `documentation/technical_documentation.md`

## Support

For support, please contact [SUPPORT_EMAIL] or submit an issue in the repository.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This module is licensed under the [LICENSE_TYPE]. See the `LICENSE` file for more details.