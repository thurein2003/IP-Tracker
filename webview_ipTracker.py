from flask import Flask, render_template, request
import socket
from ip2geotools.databases.noncommercial import DbIpCity
from colorama import Fore
import pyfiglet

app = Flask(__name__)

def printDis(ip):
    ans = DbIpCity.get(ip, api_key="free")
    return f"IP address : {ans.ip_address}<br>Location : {ans.city}, {ans.country}<br>Coordinates : {ans.longitude}, {ans.latitude}"

@app.route('/')
def index():
    name = "EchTit"
    font = pyfiglet.figlet_format(name)
    return f"""
    <html>
    <head>
    <style>
    body {{
        background-color: black;
        color: white;
        font-family: Arial, sans-serif;
    }}
    .container {{
        width: 50%;
        margin: 10 auto;
        text-align: center;
        padding: 20px;
        border: 1px solid white;
        border-radius: 10px;
        margin-top: 200px;
    }}
    </style>
    </head>
    <body>
    <div class="container">
    <pre>{Fore.RED + font}</pre>
    <form action='/result' method='post'>
    <label for='choice'>Choose:</label>
    <select id='choice' name='choice'>
    <option value='1'>Go with IP address</option>
    <option value='2'>Go with Url address</option>
    </select><br>
    <input type='text' id='input' name='input'><br>
    <input type='submit' value='Submit'>
    </form>
    </div>
    </body>
    </html>
    """

@app.route('/result', methods=['POST'])
def result():
    choice = int(request.form['choice'])
    input_val = request.form['input']
    if choice == 1:
        ip_address = input_val
        result = printDis(ip_address)
    elif choice == 2:
        url_address = input_val
        ip_address = socket.gethostbyname(url_address)
        result = printDis(ip_address)
    else:
        result = "Try again!"
    return f"""
    <html>
    <head>
    <style>
    body {{
        background-color: black;
        color: white;
        font-family: Arial, sans-serif;
    }}
    .container {{
        width: 50%;
        margin: 10 auto;
        text-align: center;
        padding: 20px;
        border: 1px solid white;
        border-radius: 10px;
        margin-top: 100px;
    }}
    </style>
    </head>
    <body>
    <div class="container">
    <pre>{result}</pre>
    </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
