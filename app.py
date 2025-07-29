
from flask import Flask, render_template, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Koneksi ke Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("market-1-467405-88c302d95d37.json", scope)
client = gspread.authorize(creds)

SHEET_NAME = "RempahProduk"  # Sesuaikan dengan nama spreadsheet kamu

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produk")
def produk():
    sheet = client.open(SHEET_NAME).sheet1
    data = sheet.get_all_records()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
