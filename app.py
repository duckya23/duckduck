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

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('o7GVhWmLARWtKhOTf0uAOWCO5UY2m4HYZFDGURs+rhnK8OZMazcsEVKNO83iPkB6NOyMXbbZXrNUYySlyd2CXHtlKYTDlkhIdGitB/ZKTvXkQc5maB9YU4wJxJF9ZoFbWIWVwYi8NHxttXiGNAQtWAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('675c061bcf22f2da2eb9c2e3c2c95a0e')

#line_bot_api.push_message('你自己的ID', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('記帳',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到',
        template=ButtonsTemplate(
            thumbnail_image_url='https://cdn.pixabay.com/photo/2022/09/04/21/03/cartoon-duck-7432790_1280.png',
            title='來記帳鴨！',
            text='我是你的記帳鴨博士',
            actions=[
                
                MessageAction(
                    label='紀錄本日支出',
                    text='紀錄本日支出',
                    message='鴨鴨！你今天花了多少錢鴨！'
                ),
                  MessageAction(
                    label='紀錄本日收入',
                    text='紀錄本日收入'
                     )
              
                 ]
             )
         )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
  
    if re.match('服務條款',message):
        confirm_template_message = TemplateSendMessage(
            alt_text='服務條款',
            template=ConfirmTemplate(
                text='歡迎使用來記帳鴨！',
                actions=[
                    PostbackAction(
                        label='同意',
                        display_text='非常感謝您同意我們的條款，我們期待本程式能夠為您提供優質的服務。',
                        data='繼續使用本軟體'
                    ),
                    MessageAction(
                        label='不同意',
                        text='如果您重新選擇同意服務條款後，即可再次使用本程式。'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
        
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
