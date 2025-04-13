import pytest
from string_utils import StringUtils

def test_capitalize_positive():
    utils = StringUtils()
    
    # Позитивные тесты
    assert utils.capitalize("skypro") == "Skypro"  # Ожидаем "Skypro"
    assert utils.capitalize("hello world") == "Hello world"  # Ожидаем "Hello world"

def test_capitalize_negative():
    utils = StringUtils()
    
    # Негативные тесты
    assert utils.capitalize("") == ""  # Ожидаем пустую строку
    with pytest.raises(TypeError):  # Ожидаем ошибку при передаче не строки
        utils.capitalize(123)  # Передаем число вместо строки



import pytest
from string_utils import StringUtils

def test_trim_positive():
    utils = StringUtils()
    
    # Позитивные тесты
    assert utils.trim("   skypro") == "skypro"  # Ожидаем "skypro"
    assert utils.trim("   hello world") == "hello world"  # Ожидаем "hello world"

def test_trim_negative():
    utils = StringUtils()
    
    # Негативные тесты
    assert utils.trim("") == ""  # Ожидаем пустую строку
    with pytest.raises(TypeError):  # Ожидаем ошибку при передаче не строки
        utils.trim(123)  # Передаем число вместо строки



@pytest.mark.parametrize("input_string, symbol, expected_output", [
    # Позитивные тесты
    ("SkyPro", "k", "SyPro"),  # Удаляем 'k'
    ("Hello World", "o", "Hell Wrld"),  # Удаляем 'o'

    # Негативные тесты
    ("SkyPro", "x", "SkyPro"),  # 'x' отсутствует, строка остается без изменений
    ("Test String", "", "Test String")  # Пустая строка не должна изменять исходную строку
])
def test_delete_symbol(input_string, symbol, expected_output):
    utils = StringUtils()
    assert utils.delete_symbol(input_string, symbol) == expected_output

# Позитивные тесты
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "s", False),  # Тест на чувствительность к регистру
    ("SkyPro", "x", False),
    ("", "a", False),
    ("123", "2", True),
    (" ", " ", True),
    ("Hello, World!", "World", True),  # Проверка на наличие подстроки
    ("Hello, World!", "world", False),  # Чувствительность к регистру
])
def test_contains(string, symbol, expected):
    utils = StringUtils()
    assert utils.contains(string, symbol) == expected

    # Негативные тесты

def test_contains_with_none():
    utils = StringUtils()
    with pytest.raises(TypeError):
        utils.contains(None, "a")

