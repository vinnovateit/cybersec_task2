# dependency_mapper.py
files = ["requirements.txt", "package.json"]

for f in files:
    if os.path.exists(f):
        print(f"\n📦 Dependencies in {f}:\n")
        with open(f) as file:
            print(file.read())
