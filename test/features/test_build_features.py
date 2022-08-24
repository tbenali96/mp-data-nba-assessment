import numpy as np
import pandas as pd
from pandas._testing import assert_frame_equal
from src.features.build_features import remove_irrelevant_columns, fill_na_with_mean


class TestFeatures:
    def test_remove_irrelevant_columns(self):
        # given
        dataframe = pd.DataFrame(
            {'col1': [1, 2, 3], 'col2': ['A', 'B', np.nan], 'irrelevant_col': [4, 5, 6]}
        )

        # when
        dataframe_without_irrelevant_columns = remove_irrelevant_columns(
            dataframe, columns=['irrelevant_col']
        )

        # then
        assert_frame_equal(
            dataframe_without_irrelevant_columns,
            pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', np.nan]}),
        )

    def test_fill_na_with_mean(self):
        # given
        dataframe = pd.DataFrame(
            {'col1': [1, 2, 3, 4], 'col2': [4, np.nan, 8, np.nan]}, dtype=np.float64
        )

        # when
        dataframe_without_nan_values = fill_na_with_mean(
            dataframe, col_with_nan_values=['col2']
        )
        print(dataframe_without_nan_values)

        # then
        assert_frame_equal(
            dataframe_without_nan_values,
            pd.DataFrame(
                {'col1': [1, 2, 3, 4], 'col2': [4, 6, 8, 6]}, dtype=np.float64
            ),
        )
