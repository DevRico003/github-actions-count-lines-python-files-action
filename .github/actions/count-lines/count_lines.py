import os

def count_lines():
    total_lines = 0
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file)) as f:
                    total_lines += len(f.readlines())
    return total_lines

if __name__ == "__main__":
    print(f"Total lines in Python files: {count_lines()}")