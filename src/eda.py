import matplotlib.pyplot as plt
import seaborn as sns

def plot_importance(importance_df, save_path='reports/importance_plot.png'):
    """
    Generates the 'Human vs Nature' importance chart.
    """
    plt.figure(figsize=(12, 9))
    sns.set_theme(style="whitegrid")
    sns.barplot(x='Importance', y='Feature', data=importance_df.head(15), palette='plasma')
    plt.title('The True Drivers: Top 15 Specific Crop/Country Impacts', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
