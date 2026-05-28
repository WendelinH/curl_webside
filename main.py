from flask import Flask, request, Response
from colorama import Fore, Back, Style

app = Flask(__name__)

@app.route("/")
def index():
    accepted = request.headers.get('Accept')
    if "text/html" in accepted:
        return Response("<body style='background-color:#232323;'><h1 style='color: #dfdfdf'>Hallo WELT</h1></body>",content_type="text/html")
    return Response(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}Hallo WELT\n",content_type="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0")