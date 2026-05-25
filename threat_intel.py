import requests
import time

def geolocate_ip(ip: str) -> dict:
  try:
      response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
      response.raise_for_status()
      data = response.json()
      return {
          "ip": ip,
          "country": data.get("country", "Unknown"),
          "org": data.get("org", "Unknown"),
          "city": data.get("city", "Unknown"),
      }
  except requests.RequestException as e:
      return {"ip": ip, "country": "ERROR", "org": str(e), "city": "ERROR"}

def print_threat_table(ip_counts: dict) -> None:
  print(f"\n{'IP':<18} {'Attempts':>8} {'Country':>8} {'Organization':<40}")
  print("-" * 78)
  for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
      geo = geolocate_ip(ip)
      print(f"{ip:<18} {count:>8} {geo['country']:>8} {geo['org']:<40}")
      time.sleep(0.5)