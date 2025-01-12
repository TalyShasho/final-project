import pandas as pd
import os
import re

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

            # Load only the first 15 rows of PPG data (first row is the header)
            ppg_filepath = os.path.join(ppg_folder, ppg_file)
            try:
                ppg_data = pd.read_csv(ppg_filepath, nrows=15)  # Limit to first 15 rows (header is row 0)
            except Exception as e:
                print(f"Error loading PPG file {ppg_file}: {e}")
                continue

            # Add session and subject_id to PPG data
            ppg_data['subject_id'] = subject_id
            ppg_data['session'] = session

            # Append to the list
            all_ppg_data.append(ppg_data)

    if not all_ppg_data:
        raise ValueError("No PPG data could be loaded. Ensure the files are correctly formatted.")

    # Concatenate all PPG data into a single DataFrame
    merged_ppg_data = pd.concat(all_ppg_data, ignore_index=True)

    # Check if the merged data exceeds Excel's row limit
    max_rows = 1048576  # Excel's row limit
    if len(merged_ppg_data) > max_rows:
        print(f"Warning: The dataset exceeds Excel's row limit of {max_rows} rows. Splitting data across multiple sheets.")

        # Split the data into chunks of max_rows
        for i in range(0, len(merged_ppg_data), max_rows):
            chunk = merged_ppg_data.iloc[i:i+max_rows]
            sheet_name = f"Sheet_{i//max_rows + 1}"

            # Write each chunk to a new sheet in the Excel file
            with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
                chunk.to_excel(writer, index=False, sheet_name=sheet_name)
                print(f"Writing data to {sheet_name}")
    else:
        # If the data fits in one sheet, save it
        merged_ppg_data.to_excel(output_path, index=False)
        print(f"Merged PPG data saved to {output_path}")

# Example usage
ppg_folder = r"C:\Users\tshas\OneDrive\Documentos\python 2\2\data\PPG_data"  # folder containing PPG files
output_path = r"C:\Users\tshas\OneDrive\Documentos\python 2\2\data\PPG_data.xlsx"  # Path to save the merged PPG data

try:
    merge_ppg_data(ppg_folder, output_path)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

