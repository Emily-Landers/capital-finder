from http.server import BaseHTTPRequestHandler
from urllib import parse
#import requests

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        BASE_URL = "https://restcountries.com/v3.1"
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        
        country = dic.get("country")
        capital = dic.get("capital")
        
        message = f"The capital of {country} is {capital}"
        
        self.wfile.write(message.encode())
        return

#E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.
