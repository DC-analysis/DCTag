from dctag import scores

import pytest


@pytest.mark.parametrize("feat,label", [
    ["ml_score_r1f", "RBC singlet focused"],
    ["ml_score_66a", "ML score 66A"],  # from dclab
])
def test_get_feature_label(feat, label):
    assert scores.get_feature_label(feat) == label


def test_get_dctag_score_dict():
    blood = scores.get_dctag_score_dict(name="blood")
    assert blood["ml_score_r1f"]["label"] == "RBC singlet focused"


def test_get_dctag_score_dict_error_wrong_name():
    with pytest.raises(FileNotFoundError):
        scores.get_dctag_score_dict(name="peter")
