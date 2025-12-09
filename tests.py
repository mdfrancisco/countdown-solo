import pytest
from countdown_game import CoundownGame

@pytest.fixture
def sample_dict(tmp_path):
    test_dict = tmp_path/"words.txt"
    test_dict.write_text("""
    countdown
    count
    town
    down
    own
    no
    on                                    
    """.strip())

    return test_dict

@pytest.fixture
def game():
    return CoundownGame()

def test_load_dictionary(sample_dict, game):
    words = game.load_dictionary(sample_dict)

    assert "down" in words
    assert "own" in words
    assert "countdown" in words

def test_find_matching_words(sample_dict, game):
    letters = "owqndt"

    dictionary = game.load_dictionary(sample_dict)
    matches = set(game.find_matching_words(letters, dictionary))

    assert matches == {"down", "town", "no", "on", "own"}

def test_find_matching_words_no_match(sample_dict, game):
    letters = "abcdef"

    dictionary = game.load_dictionary(sample_dict)
    matches = game.find_matching_words(letters, dictionary)

    assert matches == []

def test_game_round_score(sample_dict, game):
    letters = "townqqqbb"

    dictionary = game.load_dictionary(sample_dict)
    matches = game.find_matching_words(letters, dictionary)
    score = game.display_results(letters, matches)

    assert score == 4

def test_game_max_score(sample_dict, game):
    letters = "countdown"

    dictionary = game.load_dictionary(sample_dict)
    matches = game.find_matching_words(letters, dictionary)
    score = game.display_results(letters, matches)

    assert score == 18
