import pandas as pd

def merge_data(new_data_filepath, metadata_filepath, output_path):
    # Load the new data (processed data)
    new_data = pd.read_excel(new_data_filepath)

    # Load the metadata (file with session, music_type, valence_rating, RT)
    metadata = pd.read_excel(metadata_filepath)

    # Ensure both dataframes have the same number of rows
    if len(new_data) != len(metadata):
        raise ValueError("The two files must have the same number of rows.")

    # Add the columns from metadata to new_data
    combined_data = new_data.copy()
    combined_data['music_type'] = metadata['music_type']
    combined_data['valence_rating'] = metadata['valence_rating']
    combined_data['RT'] = metadata['RT']

    # Drop the 'time' column from PPG file
    if 'time' in combined_data.columns:
        combined_data.drop(columns=['time'], inplace=True)

    # Save the merged data to an Excel file
    combined_data.to_excel(output_path, index=False)


# maine
new_data_filepath = r"C:\Users\tshas\OneDrive\Documentos\python 2\2\data\PPG_data.xlsx"  # Path to the PPG processed data
metadata_filepath = r"C:\Users\tshas\OneDrive\Documentos\python 2\2\data\combined_data.xlsx"  # Path to the file with session, music_type, valence_rating, RT
output_path = r"C:\Users\tshas\OneDrive\Documentos\python 2\2\data\PGG_Trial_data.xlsx"  # Path to save the merged file

merge_data(new_data_filepath, metadata_filepath, output_path)
