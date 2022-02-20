'''
 * Program or Lab #: Program 7: Mastermind
 *
 * Programmer: John Adler
 *
 * Due Date: 11/16/17
 *
 * COMP141, Fall 2017
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program. 
 *
 * Description: This program is the game Mastermind. A code is input to be the
 *              secret code and a player will try to guess that code. The code
 *              has 4 non-repeating digits and the player has 12 guesses to
 *              guess that code. Each time the player guesses, the number of
 *              near matches and perfect matches are returned. Near matches are
 *              the number of digits the guess has in common with the code but
 *              are not in the same position as the code. Perfect matches are
 *              the number of digits the guess has in common with the code in
 *              those exact spots.
 *
 * Input: The user inputs the secret code and the guesses to find that code.
 *
 *
 * Output: The program outputs the number of near guesses and perfect guesses
 *         every time the user guesses the code. When the user runs out of guesses
 *         or finds the secret code, the appropriate 'You win!' or 'You lose!'
 *         statement is printed.
 *
'''

# This function counts the number of perfect matches between the guess and the code
# A perfect match is when a digit in guess is in the exact same position in code
# Parameters: code, a 4-digit string, guess, a 4-digit string
# Returns: the number of perfect matches between guess and code
def count_perfect_matches(code, guess):
    perfect_matches = 0
    for character in guess:
        if character in code:
            index1 = code.find(character)
            index2 = guess.find(character)
            if index1 == index2:
                perfect_matches += 1
    return perfect_matches

# This function counts the number of near matches between the guess and the code
# A near match is when a digit in guess is in code, but in a different position
# Parameters: code, a 4-digit string, guess, a 4-digit string
# Returns: the number of near matches between guess and code
def count_near_matches(code, guess):
    near_matches = 0
    for character in guess:
        if character in code:
            index1 = code.find(character)
            index2 = guess.find(character)
            if index1 != index2:
                near_matches += 1
    return near_matches
        

# This function determines if the passed in string has any characters repeated in it
# Parameters: guess, a string
# Returns: True if any characters are repeated, False otherwise
def repeated(guess):
    cha = guess[0]
    chb = guess[1:2]
    chc = guess[2:3]
    chd = guess[3:4]
    if (chb == cha) or (chc == cha) or (chd == cha) or (chb == chc) or (chb == chd) or (chc == chd):
        return True
    return False

# This function determines if the length of the guess is 4
# Parameters: guess, a string
# Returns: True if length of guess equals 4, False otherwise
def length(guess):
    if len(guess) == 4:
        return True
    else:
        return False

# This function determines if all of the characters in the guess are digits
# Parameters: guess, a string
# Returns: True if all characters are digits, False otherwise
def allnumbers(guess):
    if guess.isdigit():
        return True
    else:
        False
        
def main():
    code = input('Enter a 4 digit secret code: ')
    num_guesses = 0
    guess = input('Guess the 4 digit code: ')
    while (repeated(guess) == True) or (length(guess) == False) or (allnumbers(guess) == False):
        print("Bad input, try again.")
        guess = input('Enter another guess: ')
    near_matches = count_near_matches(code, guess)
    perfect_matches = count_perfect_matches(code, guess)
    print('There are', near_matches, 'near matches.')
    print('There are', perfect_matches, 'perfect matches.')
    num_guesses += 1
    while num_guesses < 12: 
        if code == guess:
            break
        else:
            guess = input('Enter another guess: ')
            while (repeated(guess) == True) or (length(guess) == False) or (allnumbers(guess) == False):
                print("Bad input, try again.")
                guess = input('Enter another guess: ')
            near_matches = count_near_matches(code, guess)
            if code == guess:
                break
            perfect_matches = count_perfect_matches(code, guess)
            print('There are', near_matches, 'near matches.')
            print('There are', perfect_matches, 'perfect matches.')
            num_guesses += 1
    if num_guesses == 12: # This determines whether the user won or lost
        print('You used all 12 of your guesses! You lose!')
        print('The secret code was:', code)
    else:
        print('You solved the secret code!')
        print('It took you', num_guesses, 'guesses to find the secret code.')

main()
