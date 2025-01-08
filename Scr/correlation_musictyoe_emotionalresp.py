import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
data_path = r"C:\Users\tshas\OneDrive\Documentos\python 2\final_project\data\compiled_data.xlsx"  # Update the path if needed
data = pd.read_excel(data_path, sheet_name="Sheet1")


# Ensure valence_rating is numeric
data["valence_rating"] = pd.to_numeric(data["valence_rating"], errors="coerce")

# Drop rows with missing values
cleaned_data = data.dropna(subset=["music_type", "valence_rating"])

# Define a color palette for different music types
unique_music_types = cleaned_data["music_type"].unique()
colors = sns.color_palette("tab10", len(unique_music_types))
color_map = dict(zip(unique_music_types, colors))

# Calculate correlation for each music type
correlations = cleaned_data.groupby("music_type").apply(
    lambda group: group["valence_rating"].corr(pd.Series(range(len(group))), method="pearson")
)

# Plot scatter plots for each music type
for music_type, subset in cleaned_data.groupby("music_type"):
    plt.figure(figsize=(8, 6))
    plt.scatter(
        x=range(len(subset)), 
        y=subset["valence_rating"], 
        color=color_map[music_type], 
        alpha=0.7
    )
    plt.title(f"Valence Ratings for Music Type: {music_type.capitalize()}", fontsize=14, fontweight="bold")
    plt.xlabel("Sample Index")
    plt.ylabel("Emocional Response")
    plt.legend([f"Correlation: {correlations[music_type]:.2f}"], loc="upper right")
    plt.grid(True)
    plt.show()

# Display the calculated correlations
print("Person coeficient between music type and emocioal response rating:")
print(correlations)
print ("No correlation was found betweeen any type of music and emocional response.")