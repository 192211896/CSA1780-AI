from itertools import permutations

def solve_crypt_arithmetic(puzzle: str):
    # Split the puzzle into components
    left_side, result = puzzle.replace(" ", "").split("=")
    words = left_side.split("+")

    # Find unique characters
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        print("Too many unique letters; a solution is not possible.")
        return

    # Generate all possible digit permutations
    digits = "0123456789"
    for perm in permutations(digits, len(unique_chars)):
        # Create a mapping of characters to digits
        char_to_digit = dict(zip(unique_chars, perm))

        # Replace characters with digits in the words and result
        words_values = ["".join(char_to_digit[char] for char in word) for word in words]
        result_value = "".join(char_to_digit[char] for char in result)

        # Skip if any word or result has leading zero
        if any(word[0] == "0" for word in words_values) or result_value[0] == "0":
            continue

        # Check if the equation is satisfied
        if sum(map(int, words_values)) == int(result_value):
            print("Solution found!")
            print(" + ".join(words_values), "=", result_value)
            return

    print("No solution found.")

# Input the crypt-arithmetic problem
print("Enter a crypt-arithmetic problem in the form 'WORD1 + WORD2 = RESULT'")
puzzle = input("Problem: ")
solve_crypt_arithmetic(puzzle)
