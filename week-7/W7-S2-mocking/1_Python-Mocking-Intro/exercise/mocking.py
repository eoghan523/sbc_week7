
import requests


def fetch_data(url):
    """Function to fetch data from an API endpoint."""
    try: 
     response = requests.get(url)
     response.raise_for_status()  # Raise an error for bad responses
     return response.json()
    except requests.exceptions.RequestException as e:
       print("An error has occured: {e}")
       return None
    
def test_fetch_data():
   url = "https://bbc.com"
   data = fetch_data(url)

   print(data)

