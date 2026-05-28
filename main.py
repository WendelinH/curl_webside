from flask import Flask, request, Response
from flask_accept import accept_fallback
from colorama import Fore, Back, Style

app = Flask(__name__)

@app.route("/")
@accept_fallback
def index():
    return Response(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Hallo WELT\n",content_type="text/plain")

@index.support("text/html")
def index_html():
    return Response("<body style='background-color:#232323;'><h1 style='color: #dfdfdf'>Hallo WELT</h1></body>",content_type="text/html")

if __name__ == '__main__':
    app.run(host="0.0.0.0")