import pytest

from com.dtmilano.android.distance import levenshtein_distance


def test_levenshtein_distance():
    # None is passed on purpose, to verify the ValueError, so the type errors are expected
    with pytest.raises(ValueError):
        levenshtein_distance(None, "any")  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        levenshtein_distance("any", None)  # type: ignore[arg-type]
    assert levenshtein_distance("", "") == 0
    assert levenshtein_distance(b"", b"") == 0
    assert levenshtein_distance("", "a") == 1
    assert levenshtein_distance("aaapppp", "") == 7
    assert levenshtein_distance("frog", "fog") == 1
    assert levenshtein_distance("fly", "ant") == 3
    assert levenshtein_distance("elephant", "hippo") == 7
    assert levenshtein_distance("hippo", "elephant") == 7
    assert levenshtein_distance("hippo", "zzzzzzzz") == 8
    assert levenshtein_distance("hippo", b"zzzzzzzz") == 8
    assert levenshtein_distance(b"hippo", "zzzzzzzz") == 8
    assert levenshtein_distance(b"hippo", b"zzzzzzzz") == 8
    assert levenshtein_distance("hello", "hallo") == 1
