from functions.level_2.one_median import get_median_value


def test__get_median_value__median_odd_length():
    items = [1, 3, 2, 4, 5]

    actual_result = get_median_value(items)
    assert actual_result == 4


def test__get_median_value__median_empty_list():

    items = []
    actual_result = get_median_value(items)

    assert actual_result == None


