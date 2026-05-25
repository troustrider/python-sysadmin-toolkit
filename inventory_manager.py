import pandas as pd

def load_inventory(filepath: str = "inventory.csv") -> pd.DataFrame:
  return pd.read_csv(filepath)

def filter_vulnerable(df: pd.DataFrame) -> pd.DataFrame:
  return df[(df["os"].str.contains("Windows Server")) | (df["ram_gb"] < 4)]

def count_by_department(df: pd.DataFrame) -> pd.Series:
  return df.groupby("department")["hostname"].count().sort_values(ascending=False)

def show_summary(filepath: str = "inventory.csv") -> None:
  df = load_inventory(filepath)
  print(f"Total servers: {len(df)}")

  vulnerable = filter_vulnerable(df)
  print(f"Vulnerable/outdated: {len(vulnerable)}")

  print("\nServers per department:")
  print(count_by_department(df).to_string())