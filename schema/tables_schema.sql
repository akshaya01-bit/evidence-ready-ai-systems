-- Core fact and dimension tables for an evidence-ready AI system.
-- All data will be synthetic in the example artefacts.

-- Fact table: interaction-level events (AI request/response + user action)
CREATE TABLE fact_interactions (
  request_id           VARCHAR(64) PRIMARY KEY,
  user_id              VARCHAR(64) NOT NULL,
  task_id              VARCHAR(64) NOT NULL,
  session_id           VARCHAR(64),
  task_type            VARCHAR(32),            -- e.g. triage, drafting, summarisation
  model_version        VARCHAR(64),
  prompt_template_id   VARCHAR(64),
  treatment_arm        VARCHAR(32),            -- e.g. control / explanation / counterfactual
  response_tokens      INT,
  latency_ms           INT,
  action_type          VARCHAR(16),            -- accept / edit / ignore / escalate
  outcome_quality_score FLOAT,                 -- synthetic scalar
  created_at           TIMESTAMP NOT NULL
);

-- Fact table: task-level panel (aggregated over time)
CREATE TABLE fact_tasks (
  task_id               VARCHAR(64),
  period_start          DATE,
  period_end            DATE,
  first_ai_request_at   TIMESTAMP,
  resolution_at         TIMESTAMP,
  num_ai_calls          INT,
  num_escalations       INT,
  resolution_time_sec   INT,
  outcome_quality_score FLOAT,
  PRIMARY KEY (task_id, period_start)
);

-- Dimension: users
CREATE TABLE dim_users (
  user_id      VARCHAR(64) PRIMARY KEY,
  role         VARCHAR(32),         -- e.g. agent, reviewer, manager
  tenure_band  VARCHAR(32),         -- e.g. 0-6m, 6-12m, 1-3y, 3y+
  team_id      VARCHAR(64),
  region       VARCHAR(32),
  is_synthetic BOOLEAN DEFAULT TRUE
);

-- Dimension: teams
CREATE TABLE dim_teams (
  team_id      VARCHAR(64) PRIMARY KEY,
  function     VARCHAR(64),         -- e.g. internal_support, ops, data
  queue_type   VARCHAR(64),         -- e.g. triage, specialised
  lead_name    VARCHAR(128)         -- synthetic label only
);

-- Dimension: experiments
CREATE TABLE dim_experiments (
  experiment_id   VARCHAR(64),
  arm_id          VARCHAR(64),
  arm_name        VARCHAR(64),
  description     TEXT,
  start_date      DATE,
  end_date        DATE,
  targeting_rules TEXT,
  PRIMARY KEY (experiment_id, arm_id)
);
