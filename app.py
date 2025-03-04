from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Welcome</title>
        <style>
            body {
                background-color: #121212;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
            h1 {
                font-size: 3em;
                font-weight: bold;
                transition: text-shadow 0.3s ease-in-out;
            }
            h1:hover {
                text-shadow: 0 0 20px #00ffff;
            }
        </style>
    </head>
    <body>
        <h1>Hello, This is STEVEN AZIAVULA!</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
