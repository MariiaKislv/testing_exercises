import pytest

from functions.level_2.three_first import first

def test__first__with_items():
    items = [1, 2, 3]

    actual_result = first(items)

    assert actual_result == 1

def test__first__with_empty_list():
    items = []

    actual_result = first(items, default=None)

    assert actual_result == None

def test__first__with_default_value():
    items = []
    default_value = 42

    actual_result = first(items, default=default_value)

    assert actual_result == default_value

def test_first_with__default_value_string():
    items = []
    default_value = "default"

    actual_result = first(items, default=default_value)

    assert actual_result == default_value

def test_first_with_default_value_not_set():
    items = []
    with pytest.raises(AttributeError):
        first(items)