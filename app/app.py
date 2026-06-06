from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>IaC Cloud Lab - Flask</title>
        <style>
            body {
                background-color: #1a1a1a;
                color: #ffbf00;
                font-family: monospace;
                padding: 50px;
            }
            h1 {
                border-bottom: 2px solid #ffbf00;
                padding-bottom: 10px;
            }
            .box {
                border: 1px solid #ffbf00;
                padding: 20px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>IaC Cloud Lab</h1>
        <div class="box">
            <p>Tryb: pełna automatyzacja</p>
            <p>Aplikacja demonstracyjna: Flask</p>
            <p>Aprowizacja infrastruktury: Terraform</p>
            <p>Konfiguracja systemu: Ansible</p>
            <p>Status: Sukces</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
