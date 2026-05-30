import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import numpy as np

    high_pop = pd.read_csv('../data/raw/spotify/high_popularity_spotify_data.csv')
    low_pop = pd.read_csv('../data/raw/spotify/low_popularity_spotify_data.csv')
    return high_pop, low_pop, pd


@app.cell
def _(high_pop, low_pop):
    (high_pop.columns == low_pop.columns).all()
    return


@app.cell
def _(high_pop, low_pop):
    set(high_pop.columns) == set(low_pop.columns)
    return


@app.cell
def _(high_pop, low_pop):
    low_fixed_order = low_pop[high_pop.columns]
    return (low_fixed_order,)


@app.cell
def _(high_pop, low_fixed_order):
    (high_pop.columns == low_fixed_order.columns).all()
    return


@app.cell
def _(high_pop, low_fixed_order, pd):
    df = pd.concat([high_pop, low_fixed_order], ignore_index=True)
    return (df,)


@app.cell
def _(df, pd):
    df['track_album_release_date'] = pd.to_datetime(df['track_album_release_date'], errors='coerce')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(df):
    clean_df = df.drop(columns=['track_artist', 'track_href', 'uri', 'track_album_name', 'playlist_name', 'track_id',
    'track_name', 'track_album_id', 'id', 'type', 'playlist_id', 'analysis_url', 'time_signature', 'track_album_release_date'])
    return (clean_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(clean_df, df):
    clean_df['year_of_release'] = df['track_album_release_date'].dt.year
    clean_df['month_of_release'] = df['track_album_release_date'].dt.month
    return


@app.cell
def _(clean_df):
    clean_df['is_popular'] = clean_df['track_popularity'] > 68
    return


@app.cell
def _(clean_df):
    popular_genres = ['rock', 'pop', 'hip-hop']
    clean_df['is_popular_genre'] = clean_df['playlist_genre'].isin(popular_genres)
    return


@app.cell
def _(clean_df):
    clean_df
    return


if __name__ == "__main__":
    app.run()
