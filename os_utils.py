import subprocess
import platform
import shutil

def check_disk_space(partition: str, threshold: float = 20.0) -> dict:
      usage = shutil.disk_usage(partition)
      free_pct = (usage.free / usage.total) * 100
      return {
          "partition": partition,
          "total_gb": round(usage.total / (1024**3), 2),
          "free_gb": round(usage.free / (1024**3), 2),
          "free_pct": round(free_pct, 1),
          "alert": free_pct < threshold
      }

def check_ping(ip: str) -> bool:
    flag = "-n" if platform.system() == "Windows" else "-c"
    result = subprocess.run(
        ["ping", flag, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

