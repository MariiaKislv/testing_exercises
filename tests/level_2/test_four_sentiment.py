from functions.level_2.four_sentiment import check_tweet_sentiment

def test__check_tweet_sentiment__good_words():

    text = 'I like blue colour'
    good_words = {'like', 'love'}
    bad_words = {'hate', 'terrible'}

    actual_result = check_tweet_sentiment(text, good_words, bad_words)

    assert actual_result == 'GOOD'

def test__check_tweet_sentiment__bad_words():

    text = 'I hate blue colour'
    good_words = {'like', 'love'}
    bad_words = {'hate', 'terrible'}

    actual_result = check_tweet_sentiment(text, good_words, bad_words)

    assert actual_result == 'BAD'

def test__check_tweet_sentiment__nautral_words():

    text = 'I like blue colour, but I hate yellow'
    good_words = {'like', 'love'}
    bad_words = {'hate', 'terrible'}

    actual_result = check_tweet_sentiment(text, good_words, bad_words)

    assert actual_result == None

def test__check_tweet_sentiment__no_text():

    text = ' '
    good_words = {'like', 'love'}
    bad_words = {'hate', 'terrible'}

    actual_result = check_tweet_sentiment(text, good_words, bad_words)

    assert actual_result == None