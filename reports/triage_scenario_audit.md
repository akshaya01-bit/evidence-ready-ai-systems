# Triage Scenario Audit (Synthetic Data)

This report illustrates how the evidence-ready AI system can support an internal
audit of a triage use case using **synthetic data**.

## Scope

- Scenario: Support agents triaging incoming tickets with an AI assistant.
- Population: Synthetic agents and tasks generated via `synthetic_data/generate_synthetic_data.py`.
- Experiment: `exp_001` with two arms: `control` (no explanation) and `explanation`.

## Data sources

- `fact_interactions.csv` — interaction-level events, including action_type and treatment_arm.
- `fact_tasks.csv` — task-level aggregates, including resolution_time_sec.
- `dim_users.csv` — user attributes (role, tenure_band, team_id).
- `dim_experiments.csv` — experiment arms and metadata.

All datasets are synthetic and follow the schema in `schema/tables_schema.sql`.

## Key questions

1. How often do agents fully accept vs. edit vs. escalate AI suggestions?
2. Does the explanation arm change escalation behaviour?
3. Are there visible differences by role or tenure band?

## Example findings (synthetic)

Using the example analysis script in `notebooks/example_analysis.py`:

- Acceptance rate is approximately 0.6–0.7 across arms.
- Escalation rates remain low in both arms.
- Outcome quality scores are similar between control and explanation in this synthetic run.

These numbers are **illustrative only** and not based on real operational data.

## Audit trail

The audit can be reproduced by:

1. Regenerating synthetic data using `synthetic_data/generate_synthetic_data.py`.
2. Running the quality checks in `notebooks/check_data_quality.py`.
3. Running `notebooks/example_analysis.py` to compute metrics.
4. Verifying that metrics and slices match the expectations defined in `config/experiments.yaml` and `config/metrics.yaml` (see below).

This demonstrates how an evidence-ready system can support structured audits without exposing sensitive logs.
