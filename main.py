from Scr.average import get_average_valence_grid
from Scr.dif_resp_to_music_type import plot_valence_histogram
from Scr.correlation_musictyoe_emotionalresp import calculate_pearson_correlation
from Scr.correlation_musictyoe_emotionalresp import correlations_to_dataframe
from tools.data_filter import filter_to_new_excel  # Import the function

# Define folder path and selected columns
folder_path = r"C:\Users\Home\Desktop\Studies\Phyton\projects 2024-2025\Project_2\data\trial_data"
selected_columns = ['session', 'music_type', 'valence_rating', 'RT']  # Specify the columns you need
final_folder_path = r"C:\Users\Home\Desktop\Studies\Phyton\projects 2024-2025\Project_2\data"

# Call the function from functions.py
filter_to_new_excel(folder_path, selected_columns, final_folder_path)

file_path = '/mnt/data/compiled_data.xlsx'  
average_valence = get_average_valence_grid(file_path)

plot_valence_histogram(average_valence)


correlations = calculate_pearson_correlation(average_valence)
correlation_df = correlations_to_dataframe(correlations)
