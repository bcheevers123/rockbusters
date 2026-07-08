"""One-off script to create the Rockbusters Google Sheet with correct tabs and headers."""

import json
import gspread
from google.oauth2.service_account import Credentials

CREDS_JSON = r"""PASTE_CREDS_HERE"""

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds_dict = json.loads(CREDS_JSON)
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
gc = gspread.authorize(creds)

sh = gc.create("Rockbusters")
print(f"Created sheet: {sh.url}")
print(f"Sheet ID: {sh.id}")

# Rename first tab and set headers
ws_users = sh.sheet1
ws_users.update_title("users")
ws_users.append_row(["user_id", "display_name", "created_at"])

ws_guesses = sh.add_worksheet(title="guesses", rows=1000, cols=10)
ws_guesses.append_row(["user_id", "set_id", "clue_number", "is_correct", "guessed_at"])

ws_reveals = sh.add_worksheet(title="daily_reveals", rows=1000, cols=10)
ws_reveals.append_row(["user_id", "set_id", "reveal_date"])

print("Tabs and headers created.")
print(f"\nSheet ID to use in Render: {sh.id}")
print(f"\nNow share this sheet with: rockbusters-sheets@rockbusters.iam.gserviceaccount.com (Editor)")
print("(Or run: sh.share('rockbusters-sheets@rockbusters.iam.gserviceaccount.com', perm_type='user', role='writer'))")
