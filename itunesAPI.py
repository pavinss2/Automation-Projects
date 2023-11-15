import requests
import pandas as pd

# Sending the request to the iTunes API
response = requests.get("https://itunes.apple.com/search?entity=song&term=sorasora")
result = response.json()["results"]

# Initialize an empty list to store our dictionaries
data = []

# Iterate over each item in the result
for item in result:
    # Check if the artistId matches one of the specified IDs
    if item["artistId"] in [1595244333, 1586369098]:    #sora = 1595244333  yami = 1586369098
        # Create a dictionary with the relevant data
        artist_data = {
            "artistId": item["artistId"],
            "artistName": item["artistName"],
            "trackName": item["trackName"],
            "collectionName": item["collectionName"],
            "primaryGenreName" : item["primaryGenreName"],
            "trackViewUrl" : item["trackViewUrl"],
            "trackTimeMillis" : item["trackTimeMillis"]
            
        }
        # Append the dictionary to the data list
        data.append(artist_data)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
df
