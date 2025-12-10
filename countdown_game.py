from collections import Counter
import random

ROUNDS = 4

VOWEL_STACK = [
    "A","A","A","A","A","A","A","A","A",
    "E","E","E","E","E","E","E","E","E","E","E","E",
    "I","I","I","I","I","I","I","I","I",
    "O","O","O","O","O","O","O","O",
    "U","U","U","U"
]

CONSONANT_STACK = [
    "B","B","C","C","D","D","D","D","F","F","G","G","G",
    "H","H","J","K","L","L","L","L","M","M","N","N","N","N","N","N",
    "P","P","Q","R","R","R","R","R","R","S","S","S","S",
    "T","T","T","T","T","T","V","V","W","W",
    "X","Y","Y","Z"
]


def load_dictionary(file):
    '''
    Load dictionary words using a set.
    
    :param file: English words list text file
    '''
    with open(file) as f:
        return set(f.read().split())


def draw_letter(stack):
    '''
    Removes letter from the stack once picked.
    
    :param stack: Vowel or Consonant stack
    '''
    return stack.pop()

def get_user_input(vowel_stack, consonant_stack):

    while True:  #repeat until valid mix of letters

        letters = []
        vowels_count = 0
        consonants_count = 0

        print("\nChoose 9 letters. Type 'v' for vowel, 'c' for consonant.\n")

        for i in range(1, 10):
            #Prevent impossible selections:
            if len(vowel_stack) == 0:
                print("No vowels left —> forcing consonant.")
                choice = "c"
            elif len(consonant_stack) == 0:
                print("No consonants left —> forcing vowel.")
                choice = "v"
            else:
                choice = input(f"Pick letter {i}/9 (v/c): ").strip().lower()

            if choice not in ("v", "c"):
                print("Invalid input. Please type 'v' or 'c'.")
                continue

            if choice == "v":
                letter = draw_letter(vowel_stack)
                vowels_count += 1
            else:
                letter = draw_letter(consonant_stack)
                consonants_count += 1

            letters.append(letter)

            print("Current letters:", " ".join(letters))

        #validate ratio of v's and c's
        if vowels_count >= 3 and consonants_count >= 4:
            return letters
        
        print("\nInvalid selection. You must choose at least 3 vowels and 4 consonants. Starting over...")

        #put letters back into top stacks (reset)
        vowel_stack[:0] = [l for l in letters if l in "AEIOU"]
        consonant_stack[:0] = [l for l in letters if l not in "AEIOU"]


def find_matching_words(letters, dictionary):
    """Return all dictionary words that can be formed from the letters."""
    
    letters_counter = Counter(letters)
    matching_words = []

    for word in dictionary:
        word_counter = Counter(word)
        if all(word_counter[c] <= letters_counter.get(c, 0) for c in word):
            matching_words.append(word)

    return matching_words

def score_words(matching_words):
    if not matching_words:
        return 0, []

    max_length = max(len(word) for word in matching_words)
    longest_words = [w for w in matching_words if len(w) == max_length]
    score = 18 if max_length == 9 else max_length
    return score, longest_words

def display_round_results(letters, longest_words, score):
    print("Letters drawn:", " ".join(letters))
    if longest_words:
        print(f"Longest words ({len(longest_words[0])} letters):")
        print(", ".join(longest_words))
        print(f"Round Score: {score}")
    else:
        print("No valid words can be formed from these letters.")
        print(f"Round Score: {score}")


def start_game():
    print("Welcome to the Countdown Letters Game!")

    dictionary = load_dictionary("words_alpha.txt")
    total_score = 0

    vowel_stack = VOWEL_STACK[:]
    consonant_stack = CONSONANT_STACK[:]
    #shuffle stack once to mimic TV Game strategic shuffle
    random.shuffle(vowel_stack)
    random.shuffle(consonant_stack)

    for round_num in range(1, ROUNDS + 1):
        print(f"\n--- Round {round_num} ---")
        
        letters = get_user_input(vowel_stack, consonant_stack)
        letters_str = "".join(letter.lower() for letter in letters) 
        matching_words = find_matching_words(letters_str, dictionary)
        score, longest_words = score_words(matching_words)
        display_round_results(letters, longest_words, score)

        total_score += score

    print("\n------ Game Over ------")
    print(f"Total Score: {total_score}\n")

if __name__ == "__main__":
    start_game()
