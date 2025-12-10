import pytest
import builtins

from countdown_game import (
    load_dictionary,
    find_matching_words,
    get_user_input,
    score_words,
    VOWEL_STACK
)

@pytest.fixture
def sample_dict(tmp_path):
    """Provide a temporary dictionary file for testing."""
    test_dict = tmp_path / "words.txt"
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
def vowel_stack():
    """Provide a copy of the vowel stack."""
    return VOWEL_STACK[:]

## Dictionary Tests
def test_load_dictionary(sample_dict):
    """Check that words are loaded correctly from a dictionary file."""
    words = load_dictionary(sample_dict)

    assert "down" in words
    assert "own" in words
    assert "countdown" in words

def test_find_matching_words(sample_dict):
    """Check that valid words are found from a set of letters."""
    letters = "owqndtaey"
    dictionary = load_dictionary(sample_dict)

    matches = set(find_matching_words(letters, dictionary))

    assert matches == {"down", "town", "no", "on", "own"}


def test_find_matching_words_no_match(sample_dict):
    """Check that no matches are returned if no words can be formed."""
    letters = "abcdefgh"
    dictionary = load_dictionary(sample_dict)

    matches = find_matching_words(letters, dictionary)

    assert matches == []


## Scoring Tests

def test_game_round_score(sample_dict):
    """Check that a normal round score is calculated correctly."""
    letters = "townqqqbb"
    dictionary = load_dictionary(sample_dict)

    matches = find_matching_words(letters, dictionary)
    score, longest_words = score_words(matches)

    assert set(longest_words) == {"town"}
    assert score == 4


def test_game_max_score(sample_dict):
    """Check that full 9-letter words score 18 points."""
    letters = "countdown"
    dictionary = load_dictionary(sample_dict)

    matches = find_matching_words(letters, dictionary)
    score, longest_words = score_words(matches)

    assert set(longest_words) == {"countdown"}
    assert score == 18

def test_score_words_no_match(sample_dict):
    """Verify that scoring returns 0 score and empty list for no matches."""
    letters = "uuuxxxxqq"
    dictionary = load_dictionary(sample_dict)

    matches = find_matching_words(letters, dictionary)
    score, longest_words = score_words(matches)

    assert score == 0
    assert longest_words == []

## User Input Tests

def test_get_user_input_restart(monkeypatch):
    """Test restarting selection if ratio of vowels/consonants invalid."""
    #first attempt: 9 consonants (invalid), second attempt: 3 vowels, 6 consonants (valid)
    inputs = iter([ 
        "c","c","c","c","c","c","c","c","c", 
         "v","v","v","c","c","c","c","c","c" ])
    monkeypatch.setattr(builtins, "input", lambda x: next(inputs))
    
    vowel_stack = ["A","E","I"]
    consonant_stack = ["B","C","D","F","G","H"]
    
    letters = get_user_input(vowel_stack, consonant_stack)
    
    vowel_count = sum(1 for l in letters if l in "AEIOU")
    consonant_count = sum(1 for l in letters if l not in "AEIOU")
    assert vowel_count >= 3
    assert consonant_count >= 4
    assert len(letters) == 9