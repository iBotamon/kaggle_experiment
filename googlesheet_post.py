# Kaggle Experiment Logger
# ---------------------------
# Inspired by: https://amalog.hateblo.jp/entry/kaggle-snippets
# ---------------------------
# Usage:
#     1. Make blank Google Spreadsheet
#     2. Tool -> Script Editor
#     3. Paste code in googlesheet_post.js
#     4. Publish as Web Application (enable access from all users)
#     5. Write down displayed URL and input into YOUR_ENDPOINT_URL
#     6. Embed this code in Kaggle project
#     7. Run it!

import json
import requests

def write_spreadsheet(*args):
    endpoint = YOUR_ENDPOINT_URL # URL
    requests.post(endpoint, json.dumps(args))
