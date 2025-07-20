import os

# Set your root folder path here
ROOT_DIR = "./"  # Use "." if running from the site root
OLD_URL = "https://70birds.github.io/"
NEW_URL = "https://70birds.pages.dev/"

count = 0

for subdir, dirs, files in os.walk(ROOT_DIR):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(subdir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if OLD_URL in content:
                new_content = content.replace(OLD_URL, NEW_URL)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1
                print(f"Updated: {filepath}")

print(f"\n✅ Finished. {count} HTML files updated.")
