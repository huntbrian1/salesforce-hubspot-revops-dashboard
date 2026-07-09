# Randomized CRM Upload Samples

This folder contains the smaller randomized subset designed for free/developer Salesforce and HubSpot accounts.

It is derived from the full synthetic dataset in `data/full_dataset/`, but it is intentionally sampled so the CRM demo remains manageable while preserving realistic relationships across companies, contacts, leads, opportunities, campaigns, sync errors, and data-quality records.

Randomization seed: `20260704`

## Salesforce

Use `salesforce_upload_sample_free_account/` for Salesforce imports.

Recommended order:

1. `00_salesforce_users_reference_create_manually.csv`
2. `01_salesforce_accounts_import.csv`
3. `02_salesforce_leads_import.csv`
4. `03_salesforce_contacts_import.csv`
5. `04_salesforce_opportunities_import.csv`
6. `05_salesforce_campaigns_import.csv`
7. Optional/reference files for campaign members, tasks, sync errors, and data-quality audit records.

## HubSpot

Use `hubspot_upload_sample_free_account/` for HubSpot imports.

Recommended order:

1. `01_hubspot_companies_import.csv`
2. `02_hubspot_contacts_import_DEDUPED.csv`
3. Optional: `03_hubspot_deals_optional_import.csv`
4. Reference files for campaigns and marketing activity summary.

## Supporting files

- `README_IMPORT_STRATEGY.md`: source import notes and sampling explanation.
- `system_file_mapping.csv`: file-by-file purpose mapping.
- `full_reference_existing_dataset/`: reference copy of the original full CSV dataset used to build the import samples.
