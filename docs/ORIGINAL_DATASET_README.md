# RevOps Salesforce + HubSpot Synthetic Dataset

This is a synthetic B2B RevOps dataset designed for a Salesforce + HubSpot consulting / Revenue Operations Analyst portfolio project.

## Business scenario

A growth-stage B2B company uses HubSpot for marketing automation and Salesforce for sales pipeline management. Leadership does not fully trust pipeline, attribution, or lifecycle reporting because the systems have sync issues, field ownership gaps, duplicate records, stale opportunities, and inconsistent follow-up SLAs.

Your job: analyze the funnel, diagnose CRM health, prioritize fixes, and build a dashboard that a RevOps consultant could present to a client.

## Tables

- `salesforce_users.csv`: SDRs, AEs, RevOps, Marketing Ops, CSMs, and managers
- `salesforce_accounts.csv`: Salesforce-style accounts with segment, industry, region, PE-backed flag, and CRM health score
- `salesforce_leads.csv`: lead lifecycle, lead score, source, owner, HubSpot ID, Salesforce ID, assignment, and first-touch SLA
- `salesforce_contacts.csv`: converted/customer contacts linked to accounts
- `salesforce_opportunities.csv`: pipeline, stage, close date, amount, stale flags, campaign attribution
- `salesforce_tasks.csv`: sales activities across calls, emails, meetings, demos, follow-ups, and manual notes
- `salesforce_campaigns.csv`: campaign metadata and budgets
- `campaign_members.csv`: lead/contact campaign engagement
- `hubspot_form_submissions.csv`: HubSpot form conversions and UTM data
- `hubspot_email_events.csv`: email engagement events
- `sync_errors.csv`: HubSpot/Salesforce sync issues
- `data_quality_audit.csv`: field-level CRM audit output
- `field_mapping.csv`: simplified HubSpot-to-Salesforce field mapping and system-of-record logic
- `data_dictionary.csv`: quick reference for fields and sample values

## SQLite database

`revops_salesforce_hubspot.db` includes all CSV tables plus these views:

- `vw_lead_funnel`
- `vw_pipeline_health`
- `vw_campaign_roi`
- `vw_sync_health`
- `vw_rep_activity`
- `vw_account_crm_health`

## Portfolio project ideas

### 1. CRM Health Scan
Build a dashboard with:
- Total open sync errors
- Open critical/high errors
- Avg days to resolve
- Missing HubSpot/Salesforce IDs
- Duplicate-email risk
- Data quality audit by field
- Recommended fixes

### 2. Funnel + SLA Dashboard
Build a dashboard with:
- Leads → MQLs → SQLs → Opportunities → Customers
- MQL rate and SQL rate by source
- Avg speed-to-lead by source, segment, and owner
- First-touch SLA breach rate
- Lead score distribution
- Form submissions by source and conversion score

### 3. Pipeline Hygiene Dashboard
Build a dashboard with:
- Open pipeline by stage
- Stale opportunities by stage and owner
- Expected revenue by forecast category
- Closed-won revenue by month
- Opportunities missing next steps
- Accounts with low CRM health but high pipeline

### 4. Campaign ROI Dashboard
Build a dashboard with:
- Budget vs influenced opportunity revenue
- Won revenue-to-budget ratio
- Campaign engagement rate
- Top campaigns by expected revenue
- Lead source quality by MQL/SQL/opportunity rate

## Suggested Python work

- Use pandas to calculate SLA hours from assigned date to first touch.
- Build a lead scoring calibration table: compare score buckets to SQL/opportunity/customer rates.
- Detect duplicate emails and account matching gaps.
- Train a simple logistic regression or random forest to predict SQL or opportunity creation from lead source, segment, score, and engagement.
- Export cleaned tables for Power BI or Tableau.

## Suggested SQL work

Open `starter_queries.sql` for queries covering:
- Lead funnel
- Pipeline health
- Campaign ROI
- Sync errors
- Data quality audit

## Suggested dashboard layout

Page 1: Executive Summary
- Open pipeline
- Closed-won revenue
- Lead-to-MQL rate
- SQL rate
- Stale pipeline %
- Open sync errors

Page 2: Funnel Operations
- Funnel over time
- Conversion by source
- SLA by owner/source
- Lead score quality

Page 3: CRM / Integration Health
- Sync errors by type
- Errors by source/target system
- Missing ID rates
- Field mapping ownership
- Recommended remediation backlog

Page 4: Pipeline Hygiene
- Pipeline by stage
- Stale opps by owner
- No-next-step opps
- High-pipeline / low-CRM-health accounts

## What to say in an interview

“I built a synthetic Salesforce + HubSpot RevOps dataset to mirror the kind of CRM health, lifecycle, attribution, and pipeline-hygiene problems a RevOps consulting team solves. I used SQL to model the pipeline and funnel, Python to analyze data quality and SLA issues, and dashboarding logic to translate the findings into client-facing recommendations.”
