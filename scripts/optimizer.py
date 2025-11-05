import json, random, time
from pathlib import Path
from datetime import datetime, timedelta

REPORTS = Path("reports")
REPORTS.mkdir(exist_ok=True)

def simulate_cost_data(days=7):
    base = 120.0
    data = []
    for i in range(days):
        date = (datetime.utcnow() - timedelta(days=days - i)).strftime("%Y-%m-%d")
        cost = round(base + random.uniform(-10, 15), 2)
        data.append({"date": date, "cost_usd": cost})
    total = sum(d["cost_usd"] for d in data)
    return {"total_cost": total, "daily_costs": data}

def simulate_vm_actions():
    vms = ["optimizer-vm1", "optimizer-vm2"]
    actions = []
    for vm in vms:
        avg_cpu = round(random.uniform(3, 60), 2)
        action = "deallocated" if avg_cpu < 10 else "active"
        actions.append({"vm": vm, "avg_cpu_72h": avg_cpu, "action": action})
    return actions

def simulate_after_cost(before_total):
    reduction = round(before_total * random.uniform(0.15, 0.35), 2)
    after_total = round(before_total - reduction, 2)
    return {"total_cost": after_total, "savings": reduction}

def main():
    before = simulate_cost_data()
    actions = simulate_vm_actions()
    after = simulate_after_cost(before["total_cost"])

    (REPORTS / "cost_before.json").write_text(json.dumps(before, indent=2))
    (REPORTS / "actions.json").write_text(json.dumps(actions, indent=2))
    (REPORTS / "cost_after.json").write_text(json.dumps(after, indent=2))

    print("Simulation complete. Reports saved in ./reports")

if __name__ == "__main__":
    main()
