# input_validation_check.py
patterns = ["request.", "input(", "req.body", "req.query"]

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith((".py", ".js")):
            with open(os.path.join(root, file), errors="ignore") as f:
                for i, line in enumerate(f, 1):
                    if any(p in line for p in patterns):
                        print(f"User Input Found → {file}:{i} | {line.strip()}")
