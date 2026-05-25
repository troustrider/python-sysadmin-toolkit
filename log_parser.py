def parse_auth_log(filepath: str) -> dict:
    failed_ips: set = set()
    ip_counts: dict = {}

    with open(filepath, "r") as f:
        for line in f:
            if "Failed password" in line:
                parts = line.split()
                if "from" in parts:
                    ip = parts[parts.index("from") + 1]
                    failed_ips.add(ip)
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1

    return {
        "unique_ips": failed_ips,
        "counts": ip_counts,
        "total_attempts": sum(ip_counts.values())
    }

def print_summary(data: dict) -> None:
    print(f"\nTotal failed attempts: {data['total_attempts']}")
    print(f"Unique attacking IPs: {len(data['unique_ips'])}")
    print("\nAttempts per IP:")
    for ip, count in sorted(data["counts"].items(), key=lambda x: x[1], reverse=True):
        print(f"  {ip}: {count} attempts")