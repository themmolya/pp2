import shutil
import os

# Ensure directory exists
os.makedirs("test_dir", exist_ok=True)

# Move file
if os.path.exists("sample.txt"):
    shutil.move("sample.txt", "test_dir/sample.txt")
    print("File moved.")
else:
    print("sample.txt not found.")