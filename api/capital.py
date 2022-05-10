from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import re

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        BASE_URL = "https://restcountries.com/v3.1"
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        
        country = dic.get("country")
        capital = dic.get("capital")
        
        if country:
            url = f"{BASE_URL}/name/{country}"
            res = requests.get(url)
            data = res.json()
            cap = data[0]["capital"]
            message = f"The capital of {country} is {cap}"
        elif capital:
            url = f"{BASE_URL}/capital/{capital}"
            res = requests.get(url)
            data = res.json()
            countr = str(data[0]["name"]["common"])
            message = f"{capital} is the capital of {countr}"
        else:
            message = "No, thats all wrong"
        
        self.wfile.write(message.encode())
        return

#E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.
