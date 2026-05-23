import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    import pandas as pd

    return (pd,)


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    By executing command below, we see, that the most popular genre is `pop` with significant difference from other genres.
    """)
    return


@app.cell
def _(high_pop):
    high_pop.groupby(by='playlist_genre').size().sort_values(ascending=False).head(5) #ty:ignore[no-matching-overload]
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


if __name__ == "__main__":
    app.run()
