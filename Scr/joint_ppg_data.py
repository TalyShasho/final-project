import os
import re
import pandas as pd

def merge_ppg_data(ppg_folder, output_path):
    # Print all files in the directory for debugging
    print(f"Files in the specified folder: {os.listdir(ppg_folder)}")

    # Get all PPG files
    ppg_files = [f for f in os.listdir(ppg_folder) if re.match(r"sub-\d{2}_sess\d_PPG\.csv", f)]

    if not ppg_files:
        raise ValueError("No PPG files found in the specified folder.")
    
    print(f"Matched PPG files: {ppg_files}")

    # Placeholder for merged data
    all_ppg_data = []

    for ppg_file in sorted(ppg_files):  # Sort to process in order
        # Extract subject_id and session from filename
        match = re.match(r"sub-(\d{2})_sess(\d)_PPG\.csv", ppg_file)
        if match:
            subject_id = int(match.group(1))  # Extract subject ID
            session = int(match.group(2))  # Extract session number

            print(f"Processing file: {ppg_file} (subject_id: {subject_id}, session: {session})")

            # Load the entire PPG data
            ppg_filepath = os.path.join(ppg_folder, ppg_file)
            try:
                ppg_data = pd.read_csv(ppg_filepath)  # Load the CSV file

                # Calculate interval to select 15 evenly spaced rows
                total_rows = len(ppg_data)
                if total_rows < 15:
                    print(f"File {ppg_file} has less than 15 rows; including all rows.")
                    selected_rows = ppg_data
                else:
                    interval = max(1, total_rows // 15)
                    selected_rows = ppg_data.iloc[::interval].head(15)

                # Add session and subject_id to the selected rows using .loc
                selected_rows.loc[:, 'subject_id'] = subject_id
                selected_rows.loc[:, 'session'] = session

                # Append to the list
                all_ppg_data.append(selected_rows)
            except Exception as e:
                print(f"Error loading PPG file {ppg_file}: {e}")
                continue

    if not all_ppg_data:
        raise ValueError("No PPG data could be loaded. Ensure the files are correctly formatted.")

    # All PPG data into a single DataFrame
    merged_ppg_data = pd.concat(all_ppg_data, ignore_index=True)

    # Save to Excel
    merged_ppg_data.to_excel(output_path, index=False)
    print(f"Merged PPG data saved to {output_path}")

# maine
ppg_folder = r"C:\Users\tshas\Downloads\PPG_data\PPG_data"  # folder containing PPG files
output_path = r"C:\Users\tshas\OneDrive\Documentos\python 2\final_project\data\PPG_data.xlsx"  # Path to save the merged PPG data

try:
    merge_ppg_data(ppg_folder, output_path)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

