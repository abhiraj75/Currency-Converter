# 💱 Currency Converter (Python CLI)

A simple command-line currency converter built with Python that uses real-time exchange rates from FreeCurrencyAPI. It supports multiple international currencies and securely handles API keys using environment variables.

---

## 🚀 Features

- Convert between 30+ global currencies
- Real-time exchange rates
- Secure API key handling with `.env`
- Clean CLI interface
- Error handling for invalid inputs

---

## 🛠️ Tech Stack

- Python 3
- Requests
- python-dotenv
- FreeCurrencyAPI

---

## 📦 Installation (Manual Setup)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/currency-converter.git
cd currency-converter

2️⃣ Install Required Libraries
Run the following commands:

pip install requests
pip install python-dotenv

3️⃣ Setup Environment Variables
Create a .env file in the project root folder:

API_KEY=your_freecurrencyapi_key_here

⚠️ Make sure .env is added to .gitignore.

4️⃣ Run the Program
python main.py
