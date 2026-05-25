import csv
import random
from faker import Faker

fake = Faker()

OS_OPTIONS = ["Ubuntu 22.04", "CentOS 8", "Windows Server 2019", "Debian 11", "Windows Server 2022"]
DEPARTMENTS = ["IT", "Finance", "HR", "Operations", "Security", "R&D"]

def generate_inventory(filepath: str = "inventory.csv", rows: int = 1000) -> None:
  with open(filepath, "w", newline="") as f:
      writer = csv.DictWriter(f, fieldnames=["hostname", "ip", "os", "ram_gb", "department", "active"])
      writer.writeheader()
      for _ in range(rows):
          writer.writerow({
              "hostname": fake.hostname(),
              "ip": fake.ipv4_private(),
              "os": random.choice(OS_OPTIONS),
              "ram_gb": random.choice([2, 4, 8, 16, 32, 64]),
              "department": random.choice(DEPARTMENTS),
              "active": random.choice([True, False]),
          })
  print(f"Generated {rows} rows → {filepath}")

if __name__ == "__main__":
      generate_inventory()

