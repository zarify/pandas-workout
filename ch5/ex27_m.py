import marimo

__generated_with = "0.9.20"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import numpy as np
    return mo, np, pd


@app.cell
def __(pd):
    df = pd.read_excel(
        "../data/titanic3.xls"
    )
    df.head()
    return (df,)


@app.cell
def __(df):
    null_counts = df.isnull().sum()
    print(null_counts)

    return (null_counts,)


@app.cell
def __(df):
    df['home.dest2'] = df['home.dest'].str.replace(r'([A-Za-z]+),\s*([A-Za-z]+)', r'\2')
    df['home_city_state'] = df['home.dest2'].apply(lambda x: x.split(',')[-1] if isinstance(x, str) and ',' in x else "unknown")
    df['home_city_state'].value_counts()

    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
