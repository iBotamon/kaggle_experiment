# Kaggle LINE Notification Program
# ----------------------------------
# Inspired by: https://amalog.hateblo.jp/entry/kaggle-snippets
# ----------------------------------
# Usage:
#     1. Publish personal access token via https://notify-bot.line.me/my/
#     2. Input the token into YOUR_ACCESS_TOKEN
#     3. Embed this code into Kaggle project
#     4. Run it!

import requests

def line_notice(msg):
    line_notify_token = YOUR_ACCESS_TOKEN #TOKEN
    line_notify_api = 'https://notify-api.line.me/api/notify'
    message = '\n' + msg
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)
