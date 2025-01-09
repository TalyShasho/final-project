from Scr.average import get_average_valence_grid
from Scr.dif_resp_to_music_type import plot_valence_histogram
from Scr.correlation_musictyoe_emotionalresp import calculate_pearson_correlation
from Scr.correlation_musictyoe_emotionalresp import correlations_to_dataframe

file_path = '/mnt/data/compiled_data.xlsx'  
average_valence = get_average_valence_grid(file_path)

plot_valence_histogram(average_valence)


correlations = calculate_pearson_correlation(average_valence)
correlation_df = correlations_to_dataframe(correlations)
