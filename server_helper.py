import requests

class RestHelper:
    def __init__(self):
        self.filename = "/home/pi/casper_home_page/index.html"
        self.server_host_name = "http://localhost:3000/"

    def get_traffic (self, location):
        payload = {'to': location}
        url = self.server_host_name + "traffic"
        res = requests.get(url, payload)
        self.store_response(res.text)

    def get_direction (self, location):
        payload = {'to': location}
        url = self.server_host_name + "directions"
        print(url)
        res = requests.get(url, payload)
        self.store_response(res.text)

    def get_weather (self):
        url = self.server_host_name + "weather"
        res = requests.get(url)
        self.store_response(res.text)

    def get_current_movies(self):
        url = self.server_host_name + "movies"
        res = requests.get(url)
        self.store_response(res.text)

    def store_response(self, html_text):
        f = open(self.filename, 'w')
        f.write(html_text)
        f.close()