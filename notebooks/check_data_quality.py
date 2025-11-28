"""
Basic data quality checks for the synthetic evidence-ready AI tables.

- Checks for missing IDs and timestamps.
- Validates that user_id in fact_interactions exists in dim_users.
- Prints simple counts to help debug pipelines.

This is illustrative and aligned with the "evidence-ready" design in the paper.
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("../synthetic_data")

def main():
  interactions = pd.read_csv(DATA_DIR / "fact_interactions.csv")
  tasks = pd.read_csv(DATA_DIR / "fact_tasks.csv")
  users = pd.read_csv(DATA_DIR / "dim_users.csv")

  print("=== Basic shape checks ===")
  print("fact_interactions:", interactions.shape)
  print("fact_tasks:", tasks.shape)
  print("dim_users:", users.shape)

  # Missing key checks
  print("\n=== Missing key checks ===")
  for col in ["request_id", "user_id", "task_id", "created_at"]:
    if col in interactions.columns:
      missing = interactions[col].isna().sum()
      print(f"Missing in fact_interactions.{col}: {missing}")

  # Referential integrity: user_id must exist in dim_users
  print("\n=== Referential integrity: user_id ===")
  missing_users = ~interactions["user_id"].isin(users["user_id"])
  print("Interactions with user_id not in dim_users:", missing_users.sum())

  # Simple distribution sanity check
  print("\n=== Outcome quality score summary ===")
  if "outcome_quality_score" in interactions.columns:
    print(interactions["outcome_quality_score"].describe())

  print("\nData quality checks complete.")

if __name__ == "__main__":
  main()
