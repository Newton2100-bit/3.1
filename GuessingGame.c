#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// Random Number Game.
// Rules of the game -> You can be able to specify a certain Range.
/// The game is in the range between : eg 100 - 200 or 32 - 47
/// You can give the player a certain number of guesses.

/// What the player needs to do is to determine the random number that the computer has chosen
/// Between the specified range.
/// The player has a limited number of tries to get that random number.

/// If the player doesn't get the number in the specified number of tries, They lose the game
/// but you tell the player the random number that had been guessed.

/// WHAT GUIDES THE PLAYER TO CHOOSE THE NEXT NUMBER?
/// The program needs to tell the player whether the number that they have chosen
/// Is GREATER THAN or LESS THAN the Random Computer chosen number.

int main()
{
    int minimum, maximum, random_number, number_of_tries;
    srand(time(NULL));

    printf("Enter The Minimum Number of the Range:\n");
    scanf("%d", &minimum);

    printf("Enter the Maximum Number of the Range:\n");
    scanf("%d", &maximum);

    printf("Enter the Number of Tries you want to give:\n");
    scanf("%d", &number_of_tries);

    printf("The Range is : %d to -> %d : Max tries are : %d\n\n",minimum, maximum, number_of_tries);

    random_number = minimum + (rand() % (maximum - minimum + 1));

    // printf("The random Number Generated is : %d\n\n", random_number);

    while(true){// when tries gets to zero. The user was unable to guess the number.

        if(number_of_tries < 0){
            printf("You Lost: You did not find my number: Which Was : %d\n\n", random_number);
            break;
        }

        printf("ENTER YOUR GUESS:\n");
        int guess;
        scanf("%d", &guess);

        /// Tell the user whether their guess is Correct: Greater Than: or Less Than the Computer Random Number;
        if(guess == random_number){
            printf("Congratulations YOU WIN!: Your Guess %d was Correct as my guess %d:\n", guess, random_number);
            break;
        }
        else if(guess > random_number){
            printf("Your Guess %d: Is GREATER Than my Number. You have %d Tries Remaining\n",guess, number_of_tries);
        }
        else if(guess < random_number){
            printf("Your Guess %d: is LESS Than My Number. You have %d Tries Remaining\n",guess, number_of_tries);
        }

        number_of_tries--;
    }

    return 0;
}
