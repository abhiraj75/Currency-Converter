import requests

API_KEY = "fca_live_oNSQfRamKggbFdoJvwwbSLCpW2wV8U4goQ0frr3g"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies= ",".join(CURRENCIES)
    url=f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response=requests.get(url)
        data=response.json()
        return data["data"]
    except Exception :
        print("Currency Not Yet Integrated")
        return None

while True:
    base=input("Enter The Base Currency (q for quit): ").upper()
    if base == "Q":
        break

    data=convert_currency(base)
    if not data:
        continue
    del data[base]
    amount=input("Enter The Amount You Want To Convert (q for quit):").upper()
    if amount == "Q":
        break
    try:
        for ticker,value in data.items():
            print(f"{ticker}:{value*float(amount)}")
    except Exception:
        print("Please Enter A Valid Amount!")