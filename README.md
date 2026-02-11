# 💱 Currency Converter (Python CLI)

A command-line currency converter built with Python that fetches real-time exchange rates using FreeCurrencyAPI. The project securely manages API keys using environment variables and follows best practices.

---

## 🚀 Features

- 🌍 Supports 30+ international currencies
- 🔄 Real-time exchange rates
- 🔐 Secure API key handling with `.env`
- 💻 Simple CLI interface
- ⚠️ Error handling for invalid input

---

## 🛠️ Tech Stack

- Python 3
- requests
- python-dotenv
- FreeCurrencyAPI (REST API)

---

# 📦 Installation (Manual Setup)

Copy and run the following commands:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/currency-converter.git
cd currency-converter

# 2️⃣ Install required libraries
pip install requests python-dotenv

# 3️⃣ Create .env file (Mac/Linux)
echo "API_KEY=your_freecurrencyapi_key_here" > .env

# For Windows (PowerShell)
# Set-Content -Path .env -Value "API_KEY=your_freecurrencyapi_key_here"

# 4️⃣ Run the program
python main.py

```

🧪 Example

```bash

Enter The Base Currency (q for quit): USD
Enter The Amount You Want To Convert (q for quit): 100

Converted Amounts:
-------------------------
AUD:141.3500146
BGN:166.50001941000002
BRL:519.70106607
CAD:135.52302638
CHF:76.86501121
CNY:691.09013563
CZK:2039.72026419
DKK:628.41711292
EUR:84.11281597
GBP:73.3463133
HKD:781.79212785
HRK:633.75808379
HUF:31806.40568706
IDR:1678350.3222663
ILS:308.04503095
INR:9058.8314663
ISK:12196.00162198
JPY:15448.70206015
KRW:145823.52607634
MXN:1719.8802031900002
MYR:392.20004094999996
NOK:952.26911677
NZD:165.54003044
PHP:5850.55105338
PLN:354.90005741
RON:428.32307736999996
RUB:7727.001447230001
SEK:889.05009497
SGD:126.5480127
THB:3123.00057617
TRY:4363.07062082
ZAR:1594.3602049800002