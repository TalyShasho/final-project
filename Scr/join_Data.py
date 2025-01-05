import os
import pandas as pd

# Define root folder path
root_folder = r"C:\Users\tshas\OneDrive\Documentos\python 2\final_project\data"

# Placeholder for compiled data
compiled_data = []

# Traverse subject folders
for subject_folder in os.listdir(root_folder):
    if subject_folder.startswith("sub-"):  # Ensure folder matches "sub-XX" pattern
        subject_path = os.path.join(root_folder, subject_folder)
        if os.path.isdir(subject_path):
            # Define the path to the 'func' folder
            func_folder = os.path.join(subject_path, "func")
            if os.path.exists(func_folder):
                # Look for the specific file
                subject_id = subject_folder  # e.g., "sub-01"
                target_file_name = f"{subject_id}_task-music_run-01_events.tsv"
                target_file_path = os.path.join(func_folder, target_file_name)
                
                if os.path.exists(target_file_path):
                    # Load the file (assuming it's a TSV file)
                    data = pd.read_csv(target_file_path, sep='\t')
                    # Add subject ID for reference
                    data["Subject"] = subject_id
                    compiled_data.append(data)
                else:
                    print(f"File not found for {subject_id}: {target_file_name}")

# Combine all data into a single DataFrame
if compiled_data:
    final_df = pd.concat(compiled_data, ignore_index=True)

    # Save to Excel
    output_file = "compiled_data.xlsx"
    final_df.to_excel(output_file, index=False)
    print(f"Data compiled successfully into {output_file}")
else:
    print("No matching data found.")

