from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.5);
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            }
            h1 {
                font-size: 3.5rem;
                margin-bottom: 1rem;
            }
            p {
                font-size: 1.5rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, it's <span style="color: #ffcc00;">STEVEN AZIAVULA</span>!</h1>
            <p>Welcome to my Flask cloud app.</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
