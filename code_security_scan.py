# code_security_scan.py
import os

PATTERNS = {
    "Hardcoded Secret": ["password =", "secret =", "api_key", "token ="],
    "Command Execution": ["os.system", "subprocess", "exec(", "eval("],
    "Unsafe Deserialization": ["pickle.load", "yaml.load"],
    "File Handling": ["open(", "write(", "unlink("],
}

for root, _, files in os.walk("."):
    for file in files:
        if file.endswith((".py", ".js")):
            path = os.path.join(root, file)
            with open(path, errors="ignore") as f:
                for i, line in enumerate(f, 1):
                    for issue, patterns in PATTERNS.items():
                        for p in patterns:
                            if p in line:
                                print(f"[{issue}] {path}:{i} → {line.strip()}")
