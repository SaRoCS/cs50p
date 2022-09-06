import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    coins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Error getting price")

response = response.json()
price = response["bpi"]["USD"]["rate_float"]
cost = price * coins
print(f"${cost:,.4f}")
