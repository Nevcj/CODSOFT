package CODSOFT.Java_Programming;

import java.util.Random;
import java.util.Scanner;

public class numbergame 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
            Random random = new Random();
            int lowerBound = 1;
            int upperBound = 10;
            int maxAttempts = 3;
            int score = 0;

            System.out.println("Number Guessing Game"); 
            
            do 
            {
                int targetNumber = random.nextInt(upperBound - lowerBound + 1) + lowerBound;
                int attempts = 0;
                boolean guessedCorrectly = false;
                System.out.println("\nThe number lies between " + lowerBound + " and " + upperBound + " [Only 3 Attempts]");
                
                while (attempts < maxAttempts) 
                {
                    System.out.print("\nEnter your guess: ");
                    int userGuess = scanner.nextInt();
                    attempts++;
                    if (userGuess == targetNumber) 
                    {
                        guessedCorrectly = true;
                        break;
                    } 
                    else if (userGuess < targetNumber) 
                    {
                        System.out.println("It is Lesser. Try again.");
                    } 
                    else 
                    {
                        System.out.println("It is Greater. Try again.");
                    }
                }

                if (guessedCorrectly) 
                {
                    System.out.println("\nCongratulations! You've guessed the number in " + attempts + " attempts.");
                    score++;
                } 
                else 
                {
                    System.out.println("\nSorry, you've reached the maximum number of attempts. The correct number is " + targetNumber);
                }
                System.out.print("\nPlay Again? [yes/no]: ");
            } 

            while (scanner.next().equalsIgnoreCase("yes"));
            System.out.println("\nYour score is " + score);
        }
    }