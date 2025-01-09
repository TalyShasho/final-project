import matplotlib.pyplot as plt
import pandas as pd


def plot_valence_histogram(average_valence):
    """Generates a comparative histogram of valence between types of music."""
    plt.figure()
    average_by_music_type = average_valence.groupby('music_type')['valence_rating'].mean()
    average_by_music_type.plot(kind='bar', color=['blue', 'orange', 'green'])
    plt.title("Average Emotional Response by Music Type")
    plt.xlabel("Music Type")
    plt.ylabel("Average Emotional Response")
    plt.show()

