# Evidence-Ready AI Systems: Logging, Telemetry, and Experiment Infrastructure

This repository contains research artefacts for the paper:

> **Evidence-Ready AI Systems: Logging, Telemetry, and Experiment Infrastructure for Auditable AI Workflows**  
> Author: Akshaya Jayasankar

The paper proposes design principles, an architecture, and an evaluation plan for AI systems that are *evidence-ready*:
- logging schemas that support analysis and audits,
- telemetry pipelines that link AI behaviour to users, tasks, and outcomes,
- experiment hooks that allow credible evaluation, and
- reproducibility artefacts built around synthetic data.

## Repository structure

- `paper/`
  - `Evidence_Ready_AI_Systems.pdf` — current version of the concept paper.
- `schema/`
  - (v0.2.0+) SQL definitions for fact/dimension tables.
  - `events_schema.yaml` — logging schema for raw events that feed the tables.

- `synthetic_data/`
  - (v0.3.0+) scripts and example synthetic datasets.
- `notebooks/`
  - `example_analysis.py` — example analysis using the synthetic data.
- `check_data_quality.py` — basic data quality checks for the synthetic tables.
- `config/`
  - `experiments.yaml` — example configuration for experiments and metrics.
- `metrics.yaml` — registry of core metrics (quality, resolution time, escalation, acceptance).
- `reports/`
  - `triage_scenario_audit.md` — example audit report using the synthetic triage data.
- `metrics.yaml` — registry of core metrics (quality, resolution time, escalation, acceptance).

## Version roadmap

- **v0.1.0** – Paper PDF + repository skeleton.
- **v0.2.0** – Add SQL schemas for core fact/dimension tables.
- **v0.3.0** – Add synthetic data generator and example CSVs.
- **v1.0.0** – Add example analysis scripts and configuration files; mark as initial “evidence-ready” artefact bundle.

All data in this repository is **synthetic** and intended only for demonstrating infrastructure and analysis workflows.
