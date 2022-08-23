import pandas as pd
import plotly.express as px


def plot_target_distribution(df: pd.DataFrame, path: str, target_col: str):
    fig = px.pie(df, names=target_col, title='Distribution of the target')
    fig.write_image(f"{path}/target_distribution.png")


def plot_correlation_matrix(df: pd.DataFrame, path: str):
    correlation_matrix = df.corr()
    fig = px.imshow(correlation_matrix, text_auto=True, aspect="auto")
    fig.write_image(f"{path}/correlation_matrix.png")


def plot_histogram_points_per_game(df: pd.DataFrame, path: str, target_col: str):
    fig = px.histogram(df, x='PTS', color=target_col, title='Histogram of points per game')
    fig.write_image(f"{path}/points_per_game.png")


if __name__ == '__main__':
    data = pd.read_csv("../../data/raw/nba_logreg.csv")
    plot_target_distribution(df=data, path="../../visualizations", target_col='TARGET_5Yrs')
    plot_correlation_matrix(df=data, path="../../visualizations")
    plot_histogram_points_per_game(df=data, path="../../visualizations", target_col='TARGET_5Yrs')
