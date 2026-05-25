import seaborn as sns
import matplotlib.pyplot as plt

def show_plot_4x4(scatter: bool, box: bool, y, x1, x2, x3, x4, title:list):
    if(scatter):
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        sns.scatterplot(x=x1, y=y, ax=axes[0, 0])
        sns.scatterplot(x=x2, y=y, ax=axes[0, 1])
        sns.scatterplot(x=x3, y=y, ax=axes[1, 0])
        sns.scatterplot(x=x4, y=y, ax=axes[1, 1])

        axes[0, 0].set_title(f"{title[0]} vs {title[4]}")
        axes[0, 1].set_title(f"{title[1]} vs {title[4]}")
        axes[1, 0].set_title(f"{title[2]} vs {title[4]}")
        axes[1, 1].set_title(f"{title[3]} vs {title[4]}")
        
        plt.tight_layout()
        plt.show()

    if(box):
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        sns.boxplot(x=x1, ax=axes[0, 0])
        sns.boxplot(x=x2, ax=axes[0, 1])
        sns.boxplot(x=x3, ax=axes[1, 0])
        sns.boxplot(x=x4, ax=axes[1, 1])

        axes[0, 0].set_title(f"{title[0]} vs {title[4]}")
        axes[0, 1].set_title(f"{title[1]} vs {title[4]}")
        axes[1, 0].set_title(f"{title[2]} vs {title[4]}")
        axes[1, 1].set_title(f"{title[3]} vs {title[4]}")

        plt.tight_layout()
        plt.show()