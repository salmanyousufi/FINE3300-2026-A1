from ExchangeRates import ExchangeRates

def main():
    # Instantiate class as taught in Lecture # 4
    converter = ExchangeRates('BankOfCanadaExchangeRate.2026.csv')

    # Prompt user as instructed on the Assignment sheet
    amount = float(input("Enter the amount you would like to convert: "))
    from_currency = input("Enter the currency you would like to convert from (USD or CAD): ")
    to_currency = input("Enter the currency you would like to convert to (USD or CAD): ")

    result = converter.convert(amount, from_currency, to_currency)

    if result is not None:
        to_curr_clean = to_currency.strip().upper()
        # Formatted currency string (rounded to 2 decimal places with dollar sign)
        print(f"\nConverted Amount: ${result:,.2f} {to_curr_clean}")

if __name__ == "__main__":
    main()