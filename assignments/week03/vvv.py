balance = 1000
pin = "1234567"
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
   print("PIN accepted")
   while True:
       print("\n1. Check Balance")
       print("2. Withdraw")
       print("3. Deposit")
       print("4. Exit")
       choice = input("Choose option: ")
       if choice == "1":
           print(f"Your balance is: ${balance:.2f}")
       elif choice == "2":
           amount = float(input("Enter amount to withdraw: "))
           if amount <= 0:
               print("Amount must be positive.")
           elif amount > balance:
               print("Insufficient funds.")
           else:
               balance -= amount
               print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
       elif choice == "3":
           amount = float(input("Enter amount to deposit: "))
           if amount <= 0:
               print("Amount must be positive.")
           else:
               balance += amount
               print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
       elif choice == "4":
           print("Thank you for using the ATM. Goodbye!")
           break
       else:
           print("Invalid option. Please try again.")
else:
   print("Invalid PIN")