"""
Python script that displays weather forecast for next 3 days of a region based on zipcode.
Note: To access this, please get API Key from openweathermap.org
"""
import requests

zipcode = input("Enter Zipcode ::")
apikey = ""

url = f"https://api.openweathermap.org/data/2.5/forecast?zip={zipcode}&appid={apikey}"

response = requests.get(url).json()

dates_used = []
for i in response.get("list"):
    dt_txt = i.get("dt_txt")
    current_date = str(dt_txt[8:10])
    if len(dates_used) < 3:
        if current_date in dates_used:
            continue
        else:
            print("Date:", dt_txt)
            print("Min Temp:", i.get("main").get("temp_min"))
            print("Min Temp:", i.get("main").get("temp_max"))
            print("\n")
            dates_used.append(current_date)

