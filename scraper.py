from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'_username':'itsmemari0', 
          '_password':'chessgoditsmemari0'
         }

# Post the payload to the site to log in
#https://interactif.cepsum.umontreal.ca/CapNet/login.coba
s = session.post("https://www.chess.com/login_check", data=payload)
print(s)
# Navigate to the next page and scrape the data
s = session.get('https://www.chess.com/today')
print(s)
soup = BeautifulSoup(s.text, 'html.parser')
print(soup.find('img')['src'])