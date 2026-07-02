"""Reset the leaderboard by clearing all data rows from Google Sheets (keeps headers)."""

import json
import os
import sys

import gspread


def main():
    creds_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    sheet_id = os.environ.get("GOOGLE_SHEETS_ID", "")

    if not creds_json or not sheet_id:
        print("ERROR: GOOGLE_SERVICE_ACCOUNT_JSON and GOOGLE_SHEETS_ID must be set", file=sys.stderr)
        sys.exit(1)

    creds_dict = json.loads(creds_json)
    client = gspread.service_account_from_dict(
        creds_dict,
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )

    sh = client.open_by_key(sheet_id)

    for tab_name in ["guesses", "daily_reveals", "users"]:
        ws = sh.worksheet(tab_name)
        all_vals = ws.get_all_values()
        if len(all_vals) <= 1:
            print(f"{tab_name}: already empty ({len(all_vals)} rows total)")
            continue
        data_rows = len(all_vals) - 1
        ws.delete_rows(2, len(all_vals))
        print(f"{tab_name}: cleared {data_rows} data rows")

    print("Leaderboard reset complete.")


if __name__ == "__main__":
    main()
