import os

freeze_file = "freeze.txt"
os.system(f"pip install --upgrade pip wheel cmake setuptools make")

with open(freeze_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "==" in line:
            library = line.split("==")[0]
            print(f"\ninstalling Library : {library}\n")
            os.system(f"pip install --upgrade {library}")

os.system(f"python -m spacy download en_core_web_md")
