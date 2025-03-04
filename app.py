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
                padding: 20px;
                border: 2px solid #00ffff;
                border-radius: 15px;
                box-shadow: 0 0 10px #00ffff;
                transition: all 0.3s ease-in-out;
            }
            h1:hover {
                text-shadow: 0 0 20px #ff00ff;
                box-shadow: 0 0 25px #ff00ff;
                border-color: #ff00ff;
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
