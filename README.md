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

💻 Usage

Enter the base currency (e.g., USD, INR, EUR)

Enter the amount you want to convert

View converted values

Type q to quit

🧪 Example

```bash

Enter The Base Currency (q for quit): USD
Enter The Amount You Want To Convert: 100

Converted Amounts:
-------------------------
EUR: 92.45
INR: 8324.10
JPY: 14823.55