from dotenv import load_dotenv
import os

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
api_url = {
        "APOD":f"https://science.nasa.gov/wp-json/wp/v2/apod-basic",
        "NeoWs":f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key={NASA_API_KEY}",
        "DONKI":f"https://api.nasa.gov/DONKI/notifications?startDate=2014-05-01&endDate=2014-05-08&type=all&api_key={NASA_API_KEY}"}

TIMEOUT = 5

