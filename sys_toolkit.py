import schedule
import time


def show_menu() -> None:
    print("\n=== SysAdmin Toolkit ===")
    print("1. Check ping")
    print("2. Check disk space")
    print("3. Parse auth.log")
    print("4. Network inventory")
    print("5. Threat intel")
    print("6. Generate inventory")
    print("7. Generate report")
    print("8. Start daemon")
    print("0. Exit")


def main() -> None:
    while True:
        show_menu()
        choice: str = input("\nSelect option: ").strip()
        if choice == "0":
            print("Bye.")
            break
        elif choice == "1":
            from os_utils import check_ping
            ip = input("Enter IP: ").strip()
            result = check_ping(ip)
            print(f"Ping {'OK' if result else 'FAILED'}")
        elif choice == "2":
            from os_utils import check_disk_space
            partition = input("Enter partition (e.g. C:\\): ").strip()
            print(check_disk_space(partition))
        elif choice == "3":
            from log_parser import parse_auth_log, print_summary
            print_summary(parse_auth_log("auth.log"))
        elif choice == "4":
            from network_models import Router, Server
            devices = [
                Router("gw-01", "10.0.0.1", "AA:BB:CC:DD:EE:FF", "OSPF"),
                Server("web-01", "10.0.0.2", "AA:BB:CC:DD:EE:01", "Ubuntu 22.04", 8),
                Server("db-01", "10.0.0.3", "AA:BB:CC:DD:EE:02", "Debian 11", 2),
            ]
            for device in devices:
                device.audit_device()
        elif choice == "5":
            from log_parser import parse_auth_log
            from threat_intel import print_threat_table
            data = parse_auth_log("auth.log")
            print_threat_table(data["counts"])
        elif choice == "6":
            from generate_inventory import generate_inventory
            generate_inventory()
        elif choice == "7":
            from report_generator import generate_report
            generate_report()
        elif choice == "8":
            start_daemon()
        else:
            print("Invalid option.")


def run_all_tools() -> None:
    from log_parser import parse_auth_log, print_summary
    from report_generator import generate_report

    print(f"\n[DAEMON] Running scheduled tasks at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        data = parse_auth_log("auth.log")
        print_summary(data)
    except FileNotFoundError:
        print("[DAEMON] auth.log not found, skipping.")

    generate_report()


def start_daemon() -> None:
    print("[DAEMON] Starting — tasks scheduled every hour. Press Ctrl+C to stop.")
    schedule.every(1).hour.do(run_all_tools)
    run_all_tools()
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
