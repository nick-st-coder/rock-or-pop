import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd

    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer

    return ColumnTransformer, OneHotEncoder, Pipeline, SimpleImputer, pd


@app.cell
def _(pd):
    df = pd.read_csv('../data/processed/spotify_clean.csv')
    return (df,)


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df.columns[df.isna().any()].to_list()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _():
    num_col = ['energy', 'tempo', 'danceability', 'loudness', 'liveness', 'valence', 'speechiness',
    'instrumentalness', 'duration_ms', 'acousticness', 'year_of_release', 'month_of_release']
    cat_col = ['playlist_genre', 'mode', 'key', 'playlist_subgenre', 'is_popular_genre']
    return cat_col, num_col


@app.cell
def _(OneHotEncoder, Pipeline, SimpleImputer):
    num_pipe = Pipeline([
        #since the only missing values are dates i'm using most frequent strategy
        ("impute", SimpleImputer(strategy='most_frequent'))
    ])

    cat_pipe = Pipeline([
        ("onehot", OneHotEncoder(handle_unknown='ignore'))
    ])
    return cat_pipe, num_pipe


@app.cell
def _(ColumnTransformer, cat_col, cat_pipe, num_col, num_pipe):
    transformer = ColumnTransformer([
        ("numeric", num_pipe, num_col),
        ("categorical", cat_pipe, cat_col)
    ])
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
    #### Baseline - `Random Forest`
    """)
    return


if __name__ == "__main__":
    app.run()
