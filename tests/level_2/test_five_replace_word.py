from functions.level_2.five_replace_word import replace_word

def test__replace_word__match_words():

    text = "I like blue colour"
    replace_from = 'like'
    replace_to = 'love'

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == "I love blue colour"

def test__replace_word__words_register():

    text = "I LIKE blue colour"
    replace_from = 'like'
    replace_to = 'love'

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == "I love blue colour"


def test__replace_word__no_match_words():

    text = "I like blue colour"
    replace_from = 'hate'
    replace_to = 'love'

    actual_result = replace_word(text, replace_from, replace_to)

    assert actual_result == "I like blue colour"



