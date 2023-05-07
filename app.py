# -*- coding: utf-8 -*-
#載入LineBot所需要的套件
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)
#必須上自己的channel  access token
line_bot_api = LineBotApi('qFY0GtsFs+BSChiaHttVqThTCQXZyNtA537u3/dMhgoaowZ90o6HCucVXNZEX0BLNOyMXbbZXrNUYySlyd2CXHtlKYTDlkhIdGitB/ZKTvWL47rT73rV8vboOVAYZOCBoZCyUbnRFilJhM0JbP2RwQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1b6968f90a679b68802b533585423316')

line_bot_api.push_message('1660929518', TextSendMessage(text='你可以開始了'))  #主動推波push message #要付費的
# 監聽所有來自 /callback 的 Post Request

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
