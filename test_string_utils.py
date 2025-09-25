import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
        ("04 апреля 2023", "04 апреля 2023"),
    ]
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),        # пустая строка
        (" ", " "),      # строка с пробелом
        ("123abc", "123abc"),  # начинается с цифры
    ]
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected




@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        (" sky pro", "sky pro"),        # удаляет только начальные пробелы
        ("   04 апреля", "04 апреля"),
        ("", ""),                       # пусто
    ]
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "skypro"),     # нет начальных пробелов — без изменений
        (" skypro ", "skypro "),  # конечный пробел остаётся
        (" ", ""),                # один пробел => удалится
    ]
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected




@pytest.mark.parametrize(
    "s, sym, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "yP", True),
        ("Привет", "ри", True),
        ("123", "2", True),
   ]
)
def test_contains_positive(s, sym, expected):
    assert string_utils.contains(s, sym) is expected


@pytest.mark.parametrize(
    "s, sym, expected",
    [
        ("SkyPro", "x", False),
        ("", "a", False),           # в пустой строке ничего нет
        (" ", "  ", False),         # искомая подстрока длиннее
        ("abc", "abcd", False),     # искомая строка длиннее исходной
    ]
)
def test_contains_negative(s, sym, expected):
    assert string_utils.contains(s, sym) is expected




@ pytest.mark.parametrize(
    "s, sym, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("aaaa", "a",""),   # удалит всё
        ("12-34-56", "-", "123456"),
    ]
)
def test_delete_symbol_positive(s, sym, expected):
    assert string_utils.delete_symbol(s, sym) == expected


@pytest.mark.parametrize(
    "s, sym, expected",
    [
        ("SkyPro", "x", "SkyPro"),  # нечего удалять
        ("", "a", ""),              # пустая строка — без изменений
        (" ", "  ", " "),           # не найдёт, вернёт как есть
    ]
)
def test_delete_symbol_negative(s, sym, expected):
    assert string_utils.delete_symbol(s, sym) == expected