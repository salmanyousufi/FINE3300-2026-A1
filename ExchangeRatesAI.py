import csv
import sys

class CurrencyConverter:
    """Handles currency conversion between USD and CAD."""
    
    def __init__(self, usdcad_rate: float):
        # The rate represents Canadian Dollars per 1 USD
        self.usdcad_rate = usdcad_rate

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        from_curr = from_currency.strip().upper()
        to_curr = to_currency.strip().upper()

        if from_curr == to_curr:
            return amount
        elif from_curr == 'USD' and to_curr == 'CAD':
            return amount * self.usdcad_rate
        elif from_curr == 'CAD' and to_curr == 'USD':
            return amount / self.usdcad_rate
        else:
            raise ValueError("Unsupported currency pair. Please use USD or CAD.")

def main():
    filename = "BankOfCanadaExchangeRate.2026.csv"
    
    # Parse the CSV file to extract the latest rate
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = list(csv.DictReader(f))
            if not reader:
                print("Error: The CSV file is empty.")
                sys.exit(1)
            
            # Extract the last row of the dataset
            last_row = reader[-1]
            
            # Dynamically locate the FXAUSDCAD key in case of whitespace in headers
            rate_key = next((k for k in last_row.keys() if k and 'FXAUSDCAD' in k.upper()), 'FXAUSDCAD')
            latest_rate = float(last_row[rate_key])
            
    except FileNotFoundError:
        print(f"Error: Ensure '{filename}' is in the same directory as this script.")
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error extracting exchange rate from the CSV: {e}")
        sys.exit(1)

    # Initialize converter
    converter = CurrencyConverter(latest_rate)
    
    # Interactive Prompts
    try:
        amount_input = input("Enter the numerical amount to convert: ")
        # Strip out common formatting characters if the user includes them
        amount = float(amount_input.replace('$', '').replace(',', '').strip())
        
        from_currency = input("Enter the source currency (USD or CAD): ")
        to_currency = input("Enter the target currency (USD or CAD): ")
        
        # Perform conversion
        converted_amount = converter.convert(amount, from_currency, to_currency)
        
        # Display formatted output
        print(f"\nFinal Converted Amount: ${converted_amount:,.2f} {to_currency.strip().upper()}")
        
    except ValueError as e:
        print(f"\nInvalid input: {e}")

if __name__ == "__main__":
    main()