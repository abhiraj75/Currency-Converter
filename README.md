💱 Currency Converter (Python CLI)

A command-line currency converter built with Python that fetches real-time exchange rates using FreeCurrencyAPI. The project securely manages API keys using environment variables and follows best practices for clean code structure.

🚀 Features

🌍 Supports 30+ global currencies

🔄 Real-time exchange rates

🔐 Secure API key management using .env

💻 Simple and clean CLI interface

⚠️ Basic error handling for invalid inputs

🛠️ Tech Stack

Python 3

requests

python-dotenv

REST API integration

📦 Installation (Manual Setup)
1️⃣ Clone the Repository
git clone https://github.com/your-username/currency-converter.git
cd currency-converter

2️⃣ Install Required Libraries
pip install requests
pip install python-dotenv

3️⃣ Setup Environment Variables

Create a .env file in the project root directory:

API_KEY=your_freecurrencyapi_key_here


⚠️ Make sure .env is added to your .gitignore file to prevent exposing your API key.

4️⃣ Run the Program
python main.py

💻 Usage

Enter the base currency (e.g., USD, INR, EUR)

Enter the amount to convert

View converted values

Press q to quit the program

Example
Enter The Base Currency (q for quit): USD
Enter The Amount You Want To Convert: 100

Converted Amounts:
-------------------------
EUR: 92.45
INR: 8324.10
JPY: 14823.55