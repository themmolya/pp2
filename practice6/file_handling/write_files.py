# Create and write to a file

with open("sample.txt", "w") as f:
    f.write("Hello, this is line 1\n")
    f.write("Hello, this is line 2\n")

print("File written successfully.")

# Append data
with open("sample.txt", "a") as f:
    f.write("This is appended line\n")

print("Data appended.")