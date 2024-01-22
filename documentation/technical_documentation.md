# Algolia Integration for Odoo eCommerce - Technical Documentation

## Table of Contents

1. Introduction
2. Installation
3. Configuration
4. Customization
5. Security
6. Testing
7. Internationalization

## 1. Introduction

This document provides technical details for the integration of Algolia search within the Odoo Version 16 Community Edition eCommerce website. It covers the installation process, configuration steps, customization options, security considerations, testing procedures, and internationalization support.

## 2. Installation

To install the Algolia integration module, follow these steps:

1. Copy all module files to your Odoo addons directory.
2. Update the Odoo app list by navigating to Apps > Update Apps List.
3. Install the module by searching for 'Algolia Integration' and clicking the 'Install' button.

## 3. Configuration

After installation, configure the module by setting up the Algolia API keys and other parameters:

1. Navigate to the Odoo Backend module.
2. Go to Settings > Algolia Integration.
3. Enter your Algolia `Application ID` and `API Key`.
4. Configure the `Algolia Index Name` and other synchronization settings.

## 4. Customization

Customize the search experience by modifying the templates and styles:

- Edit `views/algolia_search_template.xml` to change the search input UI.
- Modify `views/algolia_facet_filter_template.xml` for facet filter UI changes.
- Update `views/algolia_search_results_page_template.xml` for search results display.
- Adjust `static/src/css/algolia_styles.css` for custom styling.

## 5. Security

Security rules and access control are defined in:

- `security/ir.model.access.csv` for model access permissions.
- `security/algolia_integration_security.xml` for record rules and access rights.

Ensure that API keys and sensitive data are stored securely and not exposed to the frontend.

## 6. Testing

The `tests/test_algolia_integration.py` file contains test cases for the integration. Run tests using Odoo's testing framework to ensure functionality:

```sh
odoo-bin -d <database_name> --test-enable --log-level=test --stop-after-init -i algolia_integration
```

## 7. Internationalization

The `i18n/algolia_integration.pot` file contains translatable terms. To add translations:

1. Duplicate the `.pot` file and rename it with the appropriate locale code (e.g., `fr.po` for French).
2. Translate the terms within the file.
3. Load the translations into Odoo.

For further details on each step, refer to the respective sections in this documentation.