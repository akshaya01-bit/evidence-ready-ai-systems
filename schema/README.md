# Schema definitions

This directory contains SQL definitions for the core fact and dimension tables
described in the *Evidence-Ready AI Systems* paper:

- `fact_interactions` — interaction-level events (AI request/response + user action).
- `fact_tasks` — task-level panel (aggregated over time).
- `dim_users` — user attributes (role, tenure band, team, region).
- `dim_teams` — team attributes (function, queue type).
- `dim_experiments` — experiment arms and metadata.

These tables are intended to be populated with **synthetic data** in later versions
(v0.3.0 and above) and used to demonstrate analyses and audits.
