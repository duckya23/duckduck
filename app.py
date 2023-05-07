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
    message = text = event.message.text
    if message == "記帳":
        bookeeping()
    else:
        print("我聽不懂")

def bookeeping(event):
    flex_message = TextSendMessage(text = '快來記帳鴨',
                                    quick_reply = QuickReply(items=[
                                        QuickReplyButton(action = MessageAction(label = "收入" , text = "收入鴨！")),
                                        QuickReplyButton(action = MessageAction(label = "支出" , text = "支出鴨！"))
                                    ]))
    line_bot_api.reply_message(event.reply_token, flex_message)
    if re.match("收入鴨！"): 
        flex_message = TextSendMessage(text='選擇收入類別鴨！',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="薪資", text="薪資")),
                                   QuickReplyButton(action=MessageAction(label="獎金", text="獎金")),
                                   QuickReplyButton(action=MessageAction(label="理財", text="理財")),
                                   QuickReplyButton(action=MessageAction(label="其他收入", text="其他收入")),
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    else:
        flex_message = TextSendMessage(text='選擇支出類別鴨！',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="飲食", text="飲食")),
                                   QuickReplyButton(action=MessageAction(label="交通", text="交通")),
                                   QuickReplyButton(action=MessageAction(label="娛樂", text="娛樂")),
                                   QuickReplyButton(action=MessageAction(label="醫療", text="醫療")),
                                   QuickReplyButton(action=MessageAction(label="服飾", text="服飾")),
                                   QuickReplyButton(action=MessageAction(label="美容", text="美容")),
                                   QuickReplyButton(action=MessageAction(label="教育", text="教育")),
                                   QuickReplyButton(action=MessageAction(label="居家(水電瓦斯)", text="居家(水電瓦斯)")),
                                   QuickReplyButton(action=MessageAction(label="日用(如:洗髮精)", text="日用(如:洗髮精)")),
                                   QuickReplyButton(action=MessageAction(label="其他", text="其他")),
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
