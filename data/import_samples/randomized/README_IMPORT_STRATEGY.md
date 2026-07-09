# RevOps Salesforce + HubSpot Upload Package - Randomized Sample

This package uses the **same original synthetic Salesforce + HubSpot RevOps dataset**. It does **not** create a new dataset.

The previous upload sample was practical but not randomized enough for every object. This version fixes that by using randomized/stratified samples while keeping the same system separation:

- **HubSpot** = marketing/source attribution, lifecycle movement, form/email engagement.
- **Salesforce** = accounts, leads, contacts, opportunities, campaigns, pipeline execution, CRM hygiene.
- **Power BI** = cross-system executive reporting layer.

## Sampling logic

Random seed: `20260704`

### Salesforce upload sample

- `02_salesforce_leads_import.csv`: 900 leads, randomized and stratified by `lead_source` + `lifecycle_stage`.
- `03_salesforce_contacts_import.csv`: 900 contacts, randomized and stratified by `persona` + `email_opt_in`.
- `04_salesforce_opportunities_import.csv`: 500 opportunities, randomized and stratified by `stage_name` + `lead_source`.
- `01_salesforce_accounts_import.csv`: 595 accounts needed to preserve relationships to the sampled leads, contacts, and opportunities.
- `05_salesforce_campaigns_import.csv`: all 36 original campaigns.
- `06_campaign_members_reference.csv`: campaign members tied to sampled leads/contacts.
- `07_salesforce_tasks_optional_reference.csv`: randomized task sample tied to sampled CRM records.
- `08_sync_errors_custom_object_import.csv`: all original sync errors.
- `09_data_quality_audit_custom_object_import.csv`: all original data-quality audit rows.

### HubSpot upload sample

- `02_hubspot_contacts_import.csv`: 900 randomized/stratified lead-derived contacts using the same source/lifecycle sample used for Salesforce leads.
- `01_hubspot_companies_import.csv`: 417 companies linked to those HubSpot contacts.
- `03_hubspot_deals_optional_import.csv`: optional HubSpot deals from the randomized Salesforce opportunity sample.
- `04_hubspot_campaigns_reference_not_native_import.csv`: campaign reference.
- `05_hubspot_marketing_activity_summary_reference.csv`: source/lifecycle engagement summary for dashboard reference.

## Why this matters

The randomized sample is less likely to over-represent one date range, source, stage, or object sequence. It should produce a more credible native Salesforce/HubSpot demo while staying small enough for free/developer accounts.

## Recommended import order

### HubSpot
1. `01_hubspot_companies_import.csv`
2. `02_hubspot_contacts_import.csv`
3. Optional: `03_hubspot_deals_optional_import.csv`
4. Keep campaign/activity summaries as reference unless your HubSpot tier supports the needed native objects.

### Salesforce
1. Create or map users using `00_salesforce_users_reference_create_manually.csv`
2. `01_salesforce_accounts_import.csv`
3. `02_salesforce_leads_import.csv`
4. `03_salesforce_contacts_import.csv`
5. `04_salesforce_opportunities_import.csv`
6. `05_salesforce_campaigns_import.csv`
7. Optional/reference: campaign members and tasks
8. Optional custom objects: sync errors and data-quality audit

## Portfolio framing

“I repackaged the same synthetic RevOps dataset into randomized Salesforce and HubSpot import samples. HubSpot models marketing source attribution and engagement, Salesforce models sales pipeline and CRM execution, and Power BI provides the executive cross-system reporting layer.”
