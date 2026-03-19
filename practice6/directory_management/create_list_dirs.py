import os

# Create nested directories
os.makedirs("test_dir/sub_dir", exist_ok=True)
print("Directories created.")

# List files and folders
print("\nDirectory contents:")
print(os.listdir("test_dir"))

# Get current working directory
print("\nCurrent directory:", os.getcwd())