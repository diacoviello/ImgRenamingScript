from pathlib import Path

path = Path("hello.py")

print(path)


# Getting the home directory of the current user
print(path.home())

print(path.exists())

# Checking whether the path represent the path to a file
print(path.is_file())

# Checking whether the path represents the path to a directory
print(path.is_dir())

# suffix of the path
print(path.suffix)

print(path.stem)

print(path.parent)

# Print the absolute path
print(path.absolute())

