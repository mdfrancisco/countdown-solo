from collections import Counter
import random

class CoundownGame:
    def __init__(self):
        self.rounds = 4

    def load_dictionary(self, file):
        """Load dictionary words using a set."""
        with open(file) as f:
            return set(f.read().split())
        
    def get_user_input(self):
        """Let the user choose 9 letters (vowel or consonant) and randomly draws from the stack and return the final list."""
        vowel_stack = ["A","A","A","E","E","E",
                    "I","I","I","O","O","O",
                    "U","U","U","U"]

        consonant_stack = ["B","B","C","C","D","D","D","D","F","F","G","G","G",
                        "H","H","J","K","L","L","L","L","M","M","N","N","N",
                        "P","P","Q","R","R","R","R","S","S","S","S","T","T","T",
                        "V","V","W","W","X","Y","Y","Z"]

        letters = []
        vowels_count = 0
        consonants_count = 0

        print("\nChoose 9 letters. Type 'v' for vowel, 'c' for consonant.")

        while len(letters) < 9:
            user_input = input(f"Pick letter {len(letters)+1}/9 (v/c): ").strip().lower()
            if user_input not in ("v", "c"):
                print("Invalid choice. Type 'v' or 'c'.")
                continue

            if user_input == "v":
                stack = vowel_stack
                is_vowel = True
            else:
                stack = consonant_stack
                is_vowel = False

            #Draw a random letter from the stack
            letter = random.choice(stack)
            letters.append(letter)

            if is_vowel:
                vowels_count += 1
                print(f"Vowel chosen: {letter}")
            else:
                consonants_count += 1
                print(f"Consonant chosen: {letter}")

        if vowels_count < 3 or consonants_count < 4:
            print("You must choose at least 3 vowels and 4 consonants. Starting over.")
            return self.choose_letters()

        return letters


    def find_matching_words(self, letters, dictionary):
        """Find all words in the dictionary that can be made with the given letters."""

        #Count all the occurrences of each letter the user input
        letters_counter = Counter(letters)
        
        matching_words = []

        #Iterates through each word in the dictionary
        for word in dictionary:
            word_counter = Counter(word)
            valid = True

            #Check each letter in the word
            for char in word:
                #If the word uses more of a letter than the letters provided
                if word_counter[char] > letters_counter.get(char, 0):
                    valid = False
                    break

            if valid:
                matching_words.append(word)

        return matching_words

    def display_results(self, letters, matching_words):
        """Display letters and longest length matching words to the user."""
        # print(f"Letters: {' '.join(letters.upper())}")

        if matching_words:
            #Checks for the lenght of the longest word which would be the score for the current round
            max_length = max(len(word) for word in matching_words)
            longest_words = [word for word in matching_words if len(word) == max_length]

            print(f"Longest words ({max_length} letters):")
            print(", ".join(longest_words))
            print(f"Round Score: {max_length}")

            return max_length
        else:
            print("No valid words can be formed from these letters.")
            return 0

    def start_game(self):
        """Starts the game and display total score to the user."""

        with open("words_alpha.txt") as f:
            dictionary = set(f.read().split())

        print("Welcome to the Countdown Letters Game!")

        total_score = 0

        for i in range(1, self.rounds):  
            letters = self.get_user_input()
            letters = "".join(letter.lower() for letter in letters)

            print("\nLetters drawn:")
            print(" ".join(letter.upper() for letter in letters))

            matching_words = self.find_matching_words(letters, dictionary)
            round_score = self.display_results(letters, matching_words)
            total_score += round_score


        print(f"\nGame Over")
        print(f"You completed 4 rounds with a total score of {total_score}. \n")    


if __name__ == "__main__":
    game = CoundownGame()
    game.start_game()
