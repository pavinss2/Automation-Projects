import os

def compare_directories(dir_a, dir_b):
    # List files in both directories
    files_a = set(os.listdir(dir_a))
    files_b = set(os.listdir(dir_b))

    # Files in B but not in A
    unique_to_b = files_b - files_a
    if unique_to_b:
        print(f"Files in {dir_b} but not in {dir_a}:")
        for file in unique_to_b:
            print(file)

    # Files in A but not in B
    unique_to_a = files_a - files_b
    if unique_to_a:
        print(f"Files in {dir_a} but not in {dir_b}:")
        for file in unique_to_a:
            print(file)

# Input for directory paths
dir_a = input("Enter the path for Directory A: ")
dir_b = input("Enter the path for Directory B: ")

compare_directories(dir_a, dir_b)
