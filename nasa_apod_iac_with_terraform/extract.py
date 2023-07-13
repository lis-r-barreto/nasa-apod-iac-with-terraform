import os
import requests
from datetime import date, timedelta

# APOD API URL
url = "https://api.nasa.gov/planetary/apod"

api_key = os.environ.get("NASA_API_KEY")

# Define the start and end dates
start_date = date(2023, 6, 1)
end_date = date(2023, 6, 30)

# Create a list to store the data for each date
data_list = []

# Iterate over the dates and make requests for each date
current_date = start_date
while current_date <= end_date:
    try:
        # Request parameters
        params = {
            "api_key": api_key,
            "date": current_date.strftime("%Y-%m-%d")  # Format the current date as "YYYY-MM-DD"
        }

        # Make a GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check if any error occurred in the API response

        # Convert the response to JSON
        data = response.json()

        # Add the data for the current date to the list
        data_list.append(data)

    except requests.exceptions.RequestException as e:
        print(f"Request error for date {current_date}: {e}")
    except Exception as e:
        print(f"Error for date {current_date}: {e}")

    # Move to the next date
    current_date += timedelta(days=1)