"""
Generate synthetic datasets for the evidence-ready AI schema.

This script creates CSV files for:
- fact_interactions.csv
- fact_tasks.csv
- dim_users.csv
- dim_teams.csv
- dim_experiments.csv

All data is synthetic and for demonstration only.
"""

import csv
import random
from datetime import datetime, timedelta

NUM_USERS = 50
NUM_TEAMS = 5
NUM_TASKS = 200
NUM_PERIODS = 4  # e.g., weeks

random.seed(42)

def gen_users():
  teams = [f"team_{i}" for i in range(1, NUM_TEAMS + 1)]
  roles = ["agent", "senior_agent", "manager"]
  regions = ["NA", "EU", "APAC"]

  users = []
  for i in range(1, NUM_USERS + 1):
    users.append({
      "user_id": f"user_{i}",
      "role": random.choice(roles),
      "tenure_band": random.choice(["0-6m", "6-12m", "1-3y", "3y+"]),
      "team_id": random.choice(teams),
      "region": random.choice(regions),
      "is_synthetic": "true"
    })
  return users, teams

def gen_teams(team_ids):
  teams = []
  for tid in team_ids:
    teams.append({
      "team_id": tid,
      "function": "internal_support",
      "queue_type": random.choice(["triage", "specialised"]),
      "lead_name": f"Lead_{tid}"
    })
  return teams

def gen_experiments():
  return [
    {
      "experiment_id": "exp_001",
      "arm_id": "control",
      "arm_name": "Control",
      "description": "No explanation",
      "start_date": "2025-01-01",
      "end_date": "2025-12-31",
      "targeting_rules": "all_agents"
    },
    {
      "experiment_id": "exp_001",
      "arm_id": "explanation",
      "arm_name": "Explanation",
      "description": "Show model rationale",
      "start_date": "2025-01-01",
      "end_date": "2025-12-31",
      "targeting_rules": "all_agents"
    }
  ]

def gen_tasks(users):
  base_date = datetime(2025, 1, 1)
  tasks = []
  interactions = []

  for t in range(1, NUM_TASKS + 1):
    task_id = f"task_{t}"
    creator = random.choice(users)
    created_at = base_date + timedelta(days=random.randint(0, 60))
    num_interactions = random.randint(1, 4)

    ai_calls = 0
    escalations = 0
    last_time = created_at
    quality = random.uniform(0.4, 0.95)

    for k in range(num_interactions):
      user = random.choice(users)
      request_id = f"{task_id}_req_{k}"
      treatment_arm = random.choice(["control", "explanation"])
      latency_ms = random.randint(200, 1500)
      action_type = random.choice(["accept", "edit", "ignore", "escalate"])
      if action_type == "escalate":
        escalations += 1
      ai_calls += 1

      last_time = last_time + timedelta(minutes=random.randint(1, 30))
      interactions.append({
        "request_id": request_id,
        "user_id": user["user_id"],
        "task_id": task_id,
        "session_id": f"session_{t}",
        "task_type": random.choice(["triage", "drafting", "summarisation"]),
        "model_version": "gpt-x.y",
        "prompt_template_id": "triage_v1",
        "treatment_arm": treatment_arm,
        "response_tokens": random.randint(50, 200),
        "latency_ms": latency_ms,
        "action_type": action_type,
        "outcome_quality_score": f"{quality:.3f}",
        "created_at": last_time.isoformat()
      })

    resolution_at = last_time + timedelta(minutes=random.randint(5, 60))
    resolution_time_sec = int((resolution_at - created_at).total_seconds())

    tasks.append({
      "task_id": task_id,
      "period_start": created_at.date().isoformat(),
      "period_end": resolution_at.date().isoformat(),
      "first_ai_request_at": created_at.isoformat(),
      "resolution_at": resolution_at.isoformat(),
      "num_ai_calls": ai_calls,
      "num_escalations": escalations,
      "resolution_time_sec": resolution_time_sec,
      "outcome_quality_score": f"{quality:.3f}"
    })

  return tasks, interactions

def write_csv(path, fieldnames, rows):
  with open(path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

def main():
  users, team_ids = gen_users()
  teams = gen_teams(team_ids)
  experiments = gen_experiments()
  tasks, interactions = gen_tasks(users)

  write_csv("dim_users.csv",
            ["user_id", "role", "tenure_band", "team_id", "region", "is_synthetic"],
            users)

  write_csv("dim_teams.csv",
            ["team_id", "function", "queue_type", "lead_name"],
            teams)

  write_csv("dim_experiments.csv",
            ["experiment_id", "arm_id", "arm_name", "description",
             "start_date", "end_date", "targeting_rules"],
            experiments)

  write_csv("fact_tasks.csv",
            ["task_id", "period_start", "period_end", "first_ai_request_at",
             "resolution_at", "num_ai_calls", "num_escalations",
             "resolution_time_sec", "outcome_quality_score"],
            tasks)

  write_csv("fact_interactions.csv",
            ["request_id", "user_id", "task_id", "session_id", "task_type",
             "model_version", "prompt_template_id", "treatment_arm",
             "response_tokens", "latency_ms", "action_type",
             "outcome_quality_score", "created_at"],
            interactions)

  print("Synthetic CSVs written in current directory.")

if __name__ == "__main__":
  main()
