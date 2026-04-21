# Clean build artifacts for Jupyter Book
import shutil
import os

def remove_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Removed: {path}")

if __name__ == "__main__":
    remove_dir("_build")
    remove_dir("notes/_build")
    print("Clean complete.")
