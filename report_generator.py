import pandas as pd
from datetime import datetime
from inventory_manager import load_inventory, filter_vulnerable, count_by_department


def generate_report(csv_path: str = "inventory.csv") -> str:
    df = load_inventory(csv_path)
    vulnerable = filter_vulnerable(df)
    by_dept = count_by_department(df).reset_index()
    by_dept.columns = ["Department", "Server Count"]

    month = datetime.now().strftime("%Y-%m")
    output_path = f"report_{month}.xlsx"

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        vulnerable.to_excel(writer, sheet_name="Vulnerable Servers", index=False)
        by_dept.to_excel(writer, sheet_name="By Department", index=False)
        df.to_excel(writer, sheet_name="Full Inventory", index=False)

    print(f"Report generated → {output_path}")
    return output_path


if __name__ == "__main__":
    generate_report()
