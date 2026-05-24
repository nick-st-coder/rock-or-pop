import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    return pd, plt, sns


@app.cell
def _(pd):
    high_pop = pd.read_csv("../data/raw/spotify/high_popularity_spotify_data.csv")
    return (high_pop,)


@app.cell
def _(high_pop):
    high_pop.describe()
    return


@app.cell
def _(high_pop):
    high_pop.shape
    return


@app.cell
def _(high_pop):
    high_pop.info()
    return


@app.cell
def _(high_pop):
    high_pop.isna().sum()
    return


@app.cell
def _(high_pop):
    high_pop.duplicated().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(high_pop):
    high_pop.groupby(by='playlist_genre').size().sort_values(ascending=False).head(5) #ty:ignore[no-matching-overload]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We see, that the most popular genre is `pop` with significant difference from other genres.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(high_pop):
    high_pop.groupby("playlist_genre")["track_popularity"].mean().sort_values(ascending=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    While popular songs are most likely to be `gaming` or `pop`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _():
    target_genres = ['rock', 'pop', 'hip-hop']
    return (target_genres,)


@app.cell
def _(high_pop, target_genres):
    top_three = high_pop[high_pop['playlist_genre'].isin(target_genres)].groupby(by='playlist_genre').agg({
        'track_popularity':'mean',
        'energy':'mean',
        'danceability':'mean',
        'playlist_genre':'count',
        'loudness':'mean',
        'liveness':'mean',
        'valence':'mean',
        'tempo':'mean',
        'duration_ms':'mean'
    })

    top_three
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The most popular music must be energetic, danceable, not loud, can be perfomed live, lasts about 2 minutes and it's happy.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(high_pop):
    high_pop["track_popularity"].hist(bins=30)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    `Left-skewed distribution` - most of the songs popularity parameter is between 65-75
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _():
    numeric_features = ['energy', 'tempo', 'danceability', 'loudness', 'liveness',
    'valence', 'speechiness', 'track_popularity', 'instrumentalness']
    return (numeric_features,)


@app.cell
def _(high_pop, numeric_features, plt, sns):
    corr = high_pop[numeric_features].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')

    plt.title("Correlation in music")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Highly `energetic` tracks tend to be loud and positive.
    - `Instrumental` songs tend to be quiet.
    - `Loud` music usually not instrumental, danceable, can be performed live, positive and energetic.
    - `Danceable` music is usually has a lot of lyrics in it, positive and loud.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(high_pop):
    high_pop.columns.to_list()[:11]
    return


@app.cell
def _(high_pop):
    energy = high_pop['energy']
    dance = high_pop['danceability']
    loud  = high_pop['loudness']
    valence = high_pop['valence']
    pop = high_pop['track_popularity']
    return dance, energy, loud, pop, valence


@app.cell
def _(dance, energy, loud, plt, pop, sns, valence):
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    sns.scatterplot(x=energy, y=pop, ax=axes[0, 0])
    sns.scatterplot(x=dance, y=pop, ax=axes[0, 1])
    sns.scatterplot(x=loud, y=pop, ax=axes[1, 0])
    sns.scatterplot(x=valence, y=pop, ax=axes[1, 1])

    axes[0, 0].set_title("Energy vs Popularity")
    axes[0, 1].set_title("Danceability vs Popularity")
    axes[1, 0].set_title("Loudness vs Popularity")
    axes[1, 1].set_title("Valence vs Popularity")

    plt.tight_layout()
    plt.show()
    return


@app.cell
def _():
    import sys
    sys.path.insert(0, '..')
    # from src.utils.plot import show_plot_4x4

    # show_plot_4x4(True, True, pop, energy, dance, loud, valence)
    return


@app.cell
def _(plt, sns):
    def show_plot_4x4(scatter: bool, box: bool, y, x1, x2, x3, x4):
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))

        if(scatter):
            sns.scatterplot(x=x1, y=y, ax=axes[0, 0])
            sns.scatterplot(x=x2, y=y, ax=axes[0, 1])
            sns.scatterplot(x=x3, y=y, ax=axes[1, 0])
            sns.scatterplot(x=x4, y=y, ax=axes[1, 1])

            axes[0, 0].set_title("Energy vs Popularity")
            axes[0, 1].set_title("Danceability vs Popularity")
            axes[1, 0].set_title("Loudness vs Popularity")
            axes[1, 1].set_title("Valence vs Popularity")
        
            plt.tight_layout()
            plt.show()

        if(box):
            sns.boxplot(x=x1, y=y, ax=axes[0, 0])
            sns.boxplot(x=x2, y=y, ax=axes[0, 1])
            sns.boxplot(x=x3, y=y, ax=axes[1, 0])
            sns.boxplot(x=x4, y=y, ax=axes[1, 1])

            axes[0, 0].set_title("Energy vs Popularity")
            axes[0, 1].set_title("Danceability vs Popularity")
            axes[1, 0].set_title("Loudness vs Popularity")
            axes[1, 1].set_title("Valence vs Popularity")

            plt.tight_layout()
            plt.show()

    return (show_plot_4x4,)


@app.cell
def _(dance, energy, loud, pop, show_plot_4x4, valence):
    show_plot_4x4(True, True, pop, energy, dance, loud, valence)
    return


if __name__ == "__main__":
    app.run()
