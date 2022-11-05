from intrusion_detection.preprocessing.categorical_features import RareCategoryReplacer
import pandas as pd
from pandas.testing import assert_frame_equal


def test_rare_category_replacer_string():
    df = pd.DataFrame([{"a": "1"}] * 9 + [{"a": "2"}])
    expected_output = pd.DataFrame([{"a": "1"}] * 9 + [{"a": "is_rare"}])
    assert_frame_equal(
        RareCategoryReplacer(min_frequency=0.11).fit_transform(df), expected_output
    )
    assert_frame_equal(RareCategoryReplacer(min_frequency=0.1).fit_transform(df), df)


def test_rare_category_replacer_other_colums_should_not_be_touched():
    df = pd.DataFrame([{"a": "1", "b": 1}] * 9 + [{"a": "2", "b": 1}])
    expected_output = pd.DataFrame(
        [{"a": "1", "b": 1}] * 9 + [{"a": "is_rare", "b": 1}]
    )
    assert_frame_equal(
        RareCategoryReplacer(min_frequency=0.11, variables=["a"]).fit_transform(df),
        expected_output,
    )
    assert_frame_equal(
        RareCategoryReplacer(min_frequency=0.11).fit_transform(df),
        expected_output,
    )
    assert_frame_equal(
        RareCategoryReplacer(min_frequency=0.1, variables=["a"]).fit_transform(df),
        df,
    )
    assert_frame_equal(
        RareCategoryReplacer(min_frequency=0.1).fit_transform(df),
        df,
    )
