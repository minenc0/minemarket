from flask import Flask, render_template, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Koneksi ke Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("market-1-467405-88c302d95d37.json", scope)
client = gspread.authorize(creds)

# Spreadsheet ID dari link Google Sheets kamu
SPREADSHEET_ID = "1GRQKGZU6cBUcN99D-4bTdXUU2lus8hU_3Mn-AUlmATg"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produk")
def produk():
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    data = sheet.get_all_records()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

