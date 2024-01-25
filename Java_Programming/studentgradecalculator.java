package CODSOFT.Java_Programming;

import java.util.Scanner;

public class studentgradecalculator 
{
    public static void main(String[] args) 
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Student Grade Calculator");
        System.out.print("\nEnter the number of subjects: ");
        int Subjects = s.nextInt();
        int[] Marks = new int[Subjects];
        int total = 0;
        System.out.println("\nEnter the marks");
        for (int i = 0; i < Subjects; i++) 
        {
            System.out.print("Subject " + (i + 1) + ": ");
            Marks[i] = s.nextInt();
            total += Marks[i];
        }
        double average = (double) total / Subjects;
        char grade = calculateGrade(average);
        System.out.println("\nResults:");
        System.out.println("Total Marks: " + total);
        System.out.printf("Average Percentage: %.2f%%\n", average);
        System.out.println("Grade: " + grade);
    }
    private static char calculateGrade(double average) 
    {
        if (average >= 90) 
        {
            return 'A';
        } 
        else if (average >= 80) 
        {
            return 'B';
        } 
        else if (average >= 70) 
        {
            return 'C';
        } 
        else if (average >= 60) 
        {
            return 'D';
        }
        else 
        {
            return 'F';
        }
    }
}