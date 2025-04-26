import os

def search_and_log_files(directory, file_types, log_file):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(tuple(file_types)):
                matching_files.append(os.path.join(root, file))

    if matching_files:
        with open(log_file, 'w') as f:
            for file_path in matching_files:
                f.write(file_path + '\n')
        print(f"Search complete. Found {len(matching_files)} files. Results logged in '{log_file}'.")
    else:
        print("Search complete. No files found matching the specified types.")

if __name__ == "__main__":
    directory = input("Enter the directory to search: ").strip()
    search_and_log_files(directory, ['.txt', '.docx', '.jpg'], 'files.log')