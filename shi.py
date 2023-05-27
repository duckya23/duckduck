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
line_bot_api = LineBotApi('cA4Y+naWER+/PyaAYGacJOO6GznxzUz/vUHhFzmY2eVvIczqzh7InjUL9h2IPo50NOyMXbbZXrNUYySlyd2CXHtlKYTDlkhIdGitB/ZKTvULCJnDf4PoVKyHgZRp7FIuHZcLErYwgQ2/Xd1ZRiFr4QdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('05a15941e79753db37de1062d1cec8dd')
#line_bot_api.push_message('你自己的ID', TextSendMessage(text='你可以開始了'))


def is_number(input_str):
    try:
        float(input_str)  # 嘗試將輸入轉換為浮點數
        return True  # 成功轉換，輸入是一個數字
    except ValueError:
        return False  # 轉換失敗，輸入不是一個數字

@handler.add(MessageEvent, message=TextMessage)
def handle_message2():
    message = text=event.message.text
    if is_number(message): # 當message是數字，執行這個
        with open('food.csv', 'r') as file: # 讀取food金額
            food =int( file.read())            
        food +=float(message) 
        with open('food.csv', 'w+') as file: # 寫入food金額
            file.write(str(food))
        reply_text = f'已儲存金額 {a} 鴨！'  # 建立回覆訊息
        line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
    else : # 當message不是數字，執行這個
        line_bot_api.reply_message(event.reply_token, TextSendMessage("您輸入的不是數字鴨！"))

@handler.add(MessageEvent, message=TextMessage)        
def handle_message9(event):
    message = text = event.message.text
        
    elif re.match('飲食',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入餐飲金額鴨!')) 
        handle_message2()