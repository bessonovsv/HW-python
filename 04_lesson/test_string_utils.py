import pytest
from string_utils import StringUtils


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("skypro", "Skypro"),
        ("скайпро", "Скайпро")
    ],
)
def test_capitalize_positive(input_text, expected_output):
    utils = StringUtils()
    assert utils.capitalize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),
        (" ", " "),
        ("123", "123")
    ],
)
def test_capitalize_negative(input_text, expected_output):
    utils = StringUtils()
    assert utils.capitalize(input_text) == expected_output


@pytest.mark.parametrize(
    "startswith, removeprefix",
    [
        (" Skypro", "Skypro"),
        (" Скайпро", "Скайпро")
    ],
)
def test_trim_positive(startswith, removeprefix):
    utils = StringUtils()
    assert utils.trim(startswith) == removeprefix


@pytest.mark.parametrize(
    "startswith, removeprefix",
    [
        ("", ""),
        (" ", ""),
        (" 123", "123")
    ],
)
def test_trim_negative(startswith, removeprefix):
    utils = StringUtils()
    assert utils.trim(startswith) == removeprefix


@pytest.mark.parametrize(
    "string, symbol, expected_result",
    [
        ("Skypro", "S", True),
        ("Скайпро", "й", True),
        ("123", "2", True),
        (" ", " ", True),
        ("$", "$", True)
    ],
)
def test_contains_positive(string, symbol, expected_result):
    utils = StringUtils()
    result = utils.contains(string, symbol)
    assert result == expected_result


@pytest.mark.parametrize(
    "string, symbol, expected_result",
    [
        (" 123", "4", False),
        (" Skypro", "U", False),
        (" Skypro", "s", False),
        (" Скайпро", "Ё", False),
        ("A", "B", False),
        ("", "В", False)
    ],
)
def test_contains_negative(string, symbol, expected_result):
    utils = StringUtils()
    result = utils.contains(string, symbol)
    assert result == expected_result


@pytest.mark.parametrize(
    "string, symbol, new_result",
    [
        ("Skypro", "S", "kypro"),
        ("Скайпро", "й", "Скапро"),
        ("123", "2", "13"),
        (" ", " ", ""),
        ("$", "$", "")
    ],
)
def test_delete_symbol_positive(string, symbol, new_result):
    utils = StringUtils()
    result = utils.delete_symbol(string, symbol)
    assert result == new_result


@pytest.mark.parametrize(
    "string, symbol, new_result",
    [
        ("Skypro", "d", "Skypro"),
        ("Скайпро", "д", "Скайпро"),
        ("123", "4", "123"),
        ("А", "В", "А")
    ],
)
def test_delete_symbol_negative(string, symbol, new_result):
    utils = StringUtils()
    result = utils.delete_symbol(string, symbol)
    assert result == new_result
