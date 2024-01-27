package CODSOFT.Java_Programming;

import java.util.Scanner;

class BankAccount 
{
    private double balance;
    public BankAccount(double initialBalance) 
    {
        this.balance = initialBalance;
    }

    public double getBalance() 
    {
        return balance;
    }

    public void deposit(double amount) 
    {
        if (amount > 0) 
        {
            balance += amount;
            System.out.println("Deposit successful!");
        } 
        else 
        {
            System.out.println("Invalid Deposit Amount");
        }
    }

    public void withdraw(double amount) 
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;
            System.out.println("Withdrawal successful!"); 

        } 
        else 
        {
            System.out.println("Invalid Withdrawal Amount or Insufficient Funds");
        }
    }
}

class ATM {
    private BankAccount userAccount;

    public ATM(BankAccount userAccount) 
    {
        this.userAccount = userAccount;
    }

    public void displayMenu() 
    {
        System.out.println("\nATM Menu:");
        System.out.println("1) Withdraw");
        System.out.println("2) Deposit");
        System.out.println("3) Check Balance");
        System.out.println("4) Exit");
    }

    public void processOption(int option) 
    {
        Scanner scanner = new Scanner(System.in);

        switch (option) 
        {
            case 1:
                System.out.print("Enter Withdrawal Amount: ");
                double withdrawAmount = scanner.nextDouble();
                userAccount.withdraw(withdrawAmount);
                break;
            case 2:
                System.out.print("Enter Deposit Amount: ");
                double depositAmount = scanner.nextDouble();
                userAccount.deposit(depositAmount);
                break;
            case 3:
                System.out.println("Current Balance: " + userAccount.getBalance());
                break;
            case 4:
                System.exit(0);
                break;
            default:
                System.out.println("Invalid option");
        }
    }
}

class Main 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter initial account balance: ");
        double initialBalance = scanner.nextDouble();

        BankAccount userAccount = new BankAccount(initialBalance);
        ATM atm = new ATM(userAccount);

        while (true) 
        {
            atm.displayMenu();
            System.out.print("\nEnter your choice: ");
            int userChoice = scanner.nextInt();

            atm.processOption(userChoice);
        }
    }
}