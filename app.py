# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
客製化選單FlexSendMessage
"""
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
line_bot_api = LineBotApi('cA4Y+naWER+/PyaAYGacJOO6GznxzUz/vUHhFzmY2eVvIczqzh7InjUL9h2IPo50NOyMXbbZXrNUYySlyd2CXHtlKYTDlkhIdGitB/ZKTvULCJnDf4PoVKyHgZRp7FIuHZcLErYwgQ2/Xd1ZRiFr4QdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('05a15941e79753db37de1062d1cec8dd')

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
    if re.match('告訴我秘密',message):
        # Flex Message Simulator網頁：https://developers.line.biz/console/fx/
        flex_message = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents={
                     "type": "bubble",
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                         {
                             "type": "text",
                             "text": "Line Pay收據",
                             "weight": "bold",
                             "color": "#1DB446",
                             "size": "sm"
                         },
                         {
                             "type": "text",
                             "text": "鴨肉屠宰場",
                             "weight": "bold",
                             "size": "xxl",
                             "margin": "md"
                         },
                         {
                             "type": "text",
                             "text": "台北市鴨場區爆炒路四段928號",
                             "size": "xs",
                             "color": "#aaaaaa",
                             "wrap": True
                         },
                         {
                             "type": "separator",
                             "margin": "xxl"
                         },
                         {
                             "type": "box",
                             "layout": "vertical",
                             "margin": "xxl",
                             "spacing": "sm",
                             "contents": [
                             {
                                 "type": "box",
                                 "layout": "horizontal",
                                 "contents": [
                                 {
                                     "type": "text",
                                     "text": "鴨肉片",
                                     "size": "sm",
                                     "color": "#555555",
                                     "flex": 0
                                 },
                                 {
                                     "type": "text",
                                     "text": "$200",
                                     "size": "sm",
                                     "color": "#111111",
                                     "align": "end"
                                 }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "horizontal",
                                 "contents": [
                                 {
                                     "type": "text",
                                     "text": "鴨肉湯",
                                     "size": "sm",
                                     "color": "#555555",
                                     "flex": 0
                                 },
                                 {
                                     "type": "text",
                                     "text": "$260",
                                     "size": "sm",
                                     "color": "#111111",
                                     "align": "end"
                                 }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "horizontal",
                                 "contents": [
                                 {
                                     "type": "text",
                                     "text": "烤鴨片",
                                     "size": "sm",
                                     "color": "#555555",
                                     "flex": 0
                                 },
                                 {
                                     "type": "text",
                                     "text": "$240",
                                     "size": "sm",
                                     "color": "#111111",
                                     "align": "end"
                                 }
                                 ]
                             },
                             {
                                 "type": "separator",
                                 "margin": "xxl"
                             },
                             {
                                 "type": "box",
                                 "layout": "horizontal",
                                 "contents": [
                                 {
                                     "type": "text",
                                     "text": "總金額",
                                     "size": "sm",
                                     "color": "#555555"
                                 },
                                 {
                                     "type": "text",
                                     "text": "$700",
                                     "size": "sm",
                                     "color": "#111111",
                                     "align": "end"
                                 }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "horizontal",
                                 "contents": [
                                 {
                                     "type": "text",
                                     "text": "小費",
                                     "size": "sm",
                                     "color": "#555555"
                                 },
                                 {
                                     "type": "text",
                                     "text": "$70",
                                     "size": "sm",
                                     "color": "#111111",
                                     "align": "end"
                                 }
                                 ]
                             }
                             ]
                         },
                         {
                             "type": "separator",
                             "margin": "xxl"
                         },
                         {
                             "type": "box",
                             "layout": "horizontal",
                             "margin": "md",
                             "contents": [
                             {
                                 "type": "text",
                                 "text": "交易代碼",
                                 "size": "xs",
                                 "color": "#aaaaaa",
                                 "flex": 0
                             },
                             {
                                 "type": "text",
                                 "text": "#936923749813",
                                 "color": "#aaaaaa",
                                 "size": "xs",
                                 "align": "end"
                             }
                             ]
                         }
                         ]
                     },
                     "styles": {
                         "footer": {
                         "separator": True
                         }
                     }
                     }
         )
        line_bot_api.reply_message(event.reply_token, flex_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
