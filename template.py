import os

# ── Project Structure ──────────────────────────────────────────────
structure = [
    ".env",
    "requirements.txt",
    ".gitignore",

    # frontend
    "frontend/index.html",
    "frontend/style.css",
    "frontend/script.js",

    # backend
    "backend/main.py",
    "backend/config.py",
    "backend/prompt.py",
    "backend/chain.py",
]

# ── Generator ──────────────────────────────────────────────────────
for path in structure:
    # create parent folders if they don't exist
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
        print(f"  📁 Created folder  : {folder}/")

    # create file only if it doesn't already exist
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass  # empty file
        print(f"  ✅ Created file    : {path}")
    else:
        print(f"  ⏭️  Already exists  : {path}")

print("\n🎉 Project structure ready!")