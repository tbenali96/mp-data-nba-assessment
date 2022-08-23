import os
import pandas as pd
from src.visualizations.create_visualizations import plot_target_distribution, plot_correlation_matrix, \
    plot_histogram_points_per_game


class TestVisualizations:
    def test_plot_target_distribution_creates_an_image(self):
        # given
        dataframe = pd.DataFrame({'col1': [1, 2, 3, 4], 'target': [0, 0, 1, 1]})

        # when
        plot_target_distribution(dataframe, "../visualizations", "target")

        # then
        assert os.path.exists("target_distribution.png") == True

    def test_plot_correlation_matrix_creates_an_image(self):
        # given
        dataframe = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [0, 0, 1, 1], 'col3': [10, 8, 20, 15]})

        # when
        plot_correlation_matrix(dataframe, "../visualizations")

        # then
        assert os.path.exists("correlation_matrix.png") == True

    def test_plot_histogram_points_per_game_creates_an_image(self):
        # given
        dataframe = pd.DataFrame({'col1': [1, 2, 3, 4], 'target': [0, 0, 1, 1], 'PTS': [10, 8, 20, 15]})

        # when
        plot_histogram_points_per_game(dataframe, "../visualizations", 'target')

        # then
        assert os.path.exists("points_per_game.png") == True
