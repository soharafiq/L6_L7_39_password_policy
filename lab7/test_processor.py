from hypothesis import given, strategies as st
from processor import first_character_type, split_credentials, digit_ratio

values = st.one_of(st.text(), st.none(), st.integers(), st.lists(st.integers()))


@given(values)
def test_first_character_type_no_crash(value):
    result = first_character_type(value)
    assert result in ["digit", "letter", "symbol", "empty", "invalid"]
    if isinstance(value, str):
        if not value:
            assert result == "empty"
        elif value[0].isdigit():
            assert result == "digit"
        elif value[0].isalpha():
            assert result == "letter"
        else:
            assert result == "symbol"
    else:
        assert result == "invalid"


@given(values)
def test_split_credentials_no_crash(value):
    result = split_credentials(value)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and all(isinstance(part, str) for part in result)
    )
    if not isinstance(value, str) or ":" not in value:
        assert result is None
    elif not value.split(":", 1)[0].strip() or not value.split(":", 1)[1].strip():
        assert result is None
    else:
        assert result == tuple(part.strip() for part in value.split(":", 1))


@given(values)
def test_digit_ratio_no_crash(value):
    result = digit_ratio(value)
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0
    if not isinstance(value, str) or not value:
        assert result == 0.0
    else:
        expected = sum(char.isdigit() for char in value) / len(value)
        assert result == expected
