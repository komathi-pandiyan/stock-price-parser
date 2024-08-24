import requests
from bs4 import BeautifulSoup

def get_stock_price(ticker):
    """
    Fetch the stock price for a given ticker symbol from Google Finance.
    """
    url = f"https://www.google.com/finance/quote/{ticker}:NSE"
    
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the stock price in the page's HTML
        price_tag = soup.find('div', class_='YMlKec fxKbKc')
        
        if price_tag:
            price = price_tag.text
            return price
        else:
            return "Price not found"
    
    except requests.RequestException as e:
        return f"Error fetching data: {e}"

def execute_commands_from_file(file_path):
    """
    Read commands from a file and execute them.
    """
    try:
        with open(file_path, 'r') as file:
            commands = file.readlines()
        
        for command in commands:
            ticker = command.strip()  # Remove leading/trailing whitespace
            if ticker:  # Check if the line is not empty
                print(f"Fetching price for ticker: {ticker}")
                price = get_stock_price(ticker)
                print(f"The current price of {ticker} is {price}\n")
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

# Example usage
if __name__ == "__main__":
    file_path = 'stocks.txt'  # Path to your commands file
