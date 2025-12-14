# config_risk_scan.py
config_files = [".env", "config.py", "settings.py"]

for f in config_files:
    if os.path.exists(f):
        print(f"\n⚠️ Config file found: {f}")
        with open(f) as file:
            for line in file:
                if "DEBUG" in line or "SECRET" in line:
                    print("  →", line.strip())
