import pytest
from password_policy import check_password, strength, suggest_fix


@pytest.mark.parametrize("password", [
    "Abcdef1!",
    "short",
    "A" * 65,
    "PASSWORD",
    "123456",
    "ABCDEFG1",
    "abcdefg!",
    "abcdefg1",
    "ABCDEFG!",
    "Abcdefghijk1!X",
])
def test_check_password_all_branches(password):
    assert isinstance(check_password(password), list)


def test_strength_all_outcomes():
    assert strength("Abcdef1!") == "good"
    assert strength("Abcdefghijk1!X") == "strong"
    assert strength("Abcdefg!") == "weak"
    assert strength("abc") == "very weak"


@pytest.mark.parametrize("issues, expected", [
    ([], "none needed"),
    (["too short"], "add more characters"),
    (["common"], "avoid common passwords"),
    (["no uppercase"], "add uppercase"),
    (["too long"], "shorten it"),
])
def test_suggest_fix_all_branches(issues, expected):
    assert suggest_fix(issues) == expected
