import pytest
from password_policy import check_password, strength, suggest_fix


@pytest.mark.parametrize("password, expected", [
    ("Abcdef1!", []),
    ("short", ["too short", "no uppercase", "no digit", "no special"]),
    ("A" * 65, ["too long", "no lowercase", "no digit", "no special"]),
    ("PASSWORD", ["common", "no lowercase", "no digit", "no special"]),
    ("123456", ["too short", "common", "no uppercase", "no lowercase", "no special"]),
    ("ABCDEFG1", ["no lowercase", "no special"]),
    ("abcdefg!", ["no uppercase", "no digit"]),
    ("abcdefg1", ["no uppercase", "no special"]),
    ("ABCDEFG!", ["no lowercase", "no digit"]),
])
def test_check_password_cases(password, expected):
    assert check_password(password) == expected


def test_strength_good_and_strong():
    assert strength("Abcdef1!") == "good"
    assert strength("Abcdefghijk1!X") == "strong"


def test_strength_weak_and_very_weak():
    assert strength("Abcdefg!") == "weak"
    assert strength("abc") == "very weak"


@pytest.mark.parametrize("issues, expected", [
    ([], "none needed"),
    (["too short", "no uppercase"], "add more characters"),
    (["common", "no digit"], "avoid common passwords"),
    (["no digit"], "add digit"),
    (["too long"], "shorten it"),
])
def test_suggest_fix_cases(issues, expected):
    assert suggest_fix(issues) == expected
