import requests
from io import BytesIO
from PIL import Image
from rich.console import Console
from rich import print
from rich_pixels import Pixels
import config 

console = Console()

def show_image(api_url):
    response = requests.get(api_url,timeout=config.TIMEOUT)
    img_response = requests.get(response.json()[0]["hdurl"])
    img = Image.open(BytesIO(img_response.content))  
    pixels = Pixels.from_image(img, resize=(80, 40))
    console.print(pixels)

def show_details(api_url,date="",img=False):
    response=requests.get(api_url,params={"api_key":config.NASA_API_KEY,"date":date},timeout=config.TIMEOUT)
    response_json= response.json()[0]
    print("="*90)
    print(f'Title: {response_json["title"]}\nDate: {response_json["date"]}\nImage Link: {response_json["hdurl"]}\n Permalink: {response_json["permalink"]}')
    return f'{show_image(api_url) if img else ""}'
