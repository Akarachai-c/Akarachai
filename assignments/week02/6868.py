EXCHANGE_RATE = 35.5  # 1 USD = 35.5 THB
def main():
   print("Currency Converter")
   print("1. THB to USD")
   print("2. USD to THB")
   choice = input("Choose conversion direction (1 or 2): ")
   if choice == "1":
       amount = float(input("Enter amount in THB: "))
       result = amount / EXCHANGE_RATE
       print(f"\nFormula used: USD = THB / {EXCHANGE_RATE}")
       print(f"{amount:.2f} THB = {result:.2f} USD")
   elif choice == "2":
       amount = float(input("Enter amount in USD: "))
       result = amount * EXCHANGE_RATE
       print(f"\nFormula used: THB = USD * {EXCHANGE_RATE}")
       print(f"{amount:.2f} USD = {result:.2f} THB")
   else:
       print("Invalid choice. Please run the program again and enter 1 or 2.")

if __name__ == "__main__":
   main()