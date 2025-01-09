import pandas as pd

data_path = r"C:\Users\tshas\OneDrive\Documentos\python 2\final_project\data\compiled_data.xlsx"

def calculate_average_valence(data):
    """definition of variable calculate_average_valence"""
    return data.groupby(['Subject', 'music_type']).mean().reset_index()


# from excell file
def get_average_valence_grid(file_path):
    """Calculates the valence rates from the excell file."""
    data = pd.read_excel( data_path, sheet_name='Sheet1')
    data_filtered = data[['Subject', 'music_type', 'valence_rating']] #relevant rows
    return calculate_average_valence(data_filtered)
