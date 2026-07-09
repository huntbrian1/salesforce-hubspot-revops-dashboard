"""
RevOps Salesforce + HubSpot Synthetic Dataset: Python Starter

Run:
    python starter_analysis.py

Requires:
    pandas matplotlib sqlite3
"""

import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
DB = BASE / "data" / "full_dataset" / "revops_salesforce_hubspot.db"
OUTPUT_DIR = BASE / "visuals" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB)

lead_funnel = pd.read_sql("""
SELECT lead_month,
       SUM(leads) AS leads,
       SUM(mqls) AS mqls,
       SUM(sqls) AS sqls,
       SUM(opportunity_leads) AS opportunity_leads,
       ROUND(1.0 * SUM(mqls) / NULLIF(SUM(leads), 0), 3) AS mql_rate,
       ROUND(1.0 * SUM(sqls) / NULLIF(SUM(mqls), 0), 3) AS sql_rate
FROM vw_lead_funnel
GROUP BY lead_month
ORDER BY lead_month
""", conn)

pipeline = pd.read_sql("""
SELECT stage_name,
       COUNT(*) AS opps,
       SUM(open_pipeline_amount) AS open_pipeline,
       SUM(expected_revenue) AS expected_revenue,
       SUM(CASE WHEN is_stale = 1 THEN 1 ELSE 0 END) AS stale_opps
FROM vw_pipeline_health
WHERE stage_name NOT IN ('Closed Won','Closed Lost')
GROUP BY stage_name
ORDER BY open_pipeline DESC
""", conn)

sync_health = pd.read_sql("""
SELECT error_type,
       COUNT(*) AS errors
FROM sync_errors
WHERE status = 'Open'
GROUP BY error_type
ORDER BY errors DESC
""", conn)

print("\nLead Funnel:")
print(lead_funnel.tail(8))

print("\nPipeline Health:")
print(pipeline)

print("\nOpen Sync Errors:")
print(sync_health)

# Simple charts for dashboard sketching
ax = lead_funnel.plot(x="lead_month", y=["leads","mqls","sqls","opportunity_leads"], figsize=(10,5), marker="o")
ax.set_title("Lead Funnel Over Time")
ax.set_xlabel("Month")
ax.set_ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "lead_funnel_over_time.png", dpi=160)
plt.close()

ax = pipeline.plot(kind="bar", x="stage_name", y="open_pipeline", figsize=(9,5), legend=False)
ax.set_title("Open Pipeline by Stage")
ax.set_xlabel("Stage")
ax.set_ylabel("Open Pipeline Amount")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "open_pipeline_by_stage.png", dpi=160)
plt.close()

ax = sync_health.plot(kind="bar", x="error_type", y="errors", figsize=(10,5), legend=False)
ax.set_title("Open Sync Errors by Type")
ax.set_xlabel("Error Type")
ax.set_ylabel("Open Errors")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "open_sync_errors_by_type.png", dpi=160)
plt.close()

print("\nSaved charts:")
print(OUTPUT_DIR / "lead_funnel_over_time.png")
print(OUTPUT_DIR / "open_pipeline_by_stage.png")
print(OUTPUT_DIR / "open_sync_errors_by_type.png")




