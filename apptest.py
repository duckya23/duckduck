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

# 定義處理函數
def handle_other(event):
    buttons_template_message = TemplateSendMessage(
        alt_text='其它功能來了鴨',
        template=ButtonsTemplate(
            thumbnail_image_url='https://png.pngtree.com/png-vector/20190831/ourlarge/pngtree-gear-vector-icon-template-png-image_1717225.jpg',
            title='其它功能鴨！',
            text='記帳鴨博士的其它功能',
            actions=[
                URIAction(
                    label='新手教學',
                    uri='https://sites.google.com/view/duckteaching/%E9%A6%96%E9%A0%81',
                ),
                URIAction(
                    label='服務條款',
                    uri='https://sites.google.com/view/ducktermserver/%E9%A6%96%E9%A0%81'
                ),
                MessageAction(
                    label='Line Pay 連結',
                    text='Line Pay 連結',
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template_message)

def handle_terms(event):
    confirm_template_message = TemplateSendMessage(
        alt_text='服務條款',
        template=ConfirmTemplate(
            text='歡迎使用來記帳鴨！',
            actions=[
                MessageAction(
                    label='同意',
                    text='我同意服務條款'
                ),
                MessageAction(
                    label='不同意',
                    text='我不同意服務條款'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, confirm_template_message)

def handle_charts(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='點擊選項來查看圖表',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i0.wp.com/rookiesavior.net/wp-content/uploads/2021/01/1550239523.png?fit=500%2C355&ssl=1',
                    action=PostbackAction(
                        label='月收支圖表',
                        display_text='月收支圖表',
                        data='action=努力不一定會成功，但不努力會很輕鬆'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://pic2.zhimg.com/v2-706be7f956613c2b4f0431482b858dc9_b.png',
                    action=PostbackAction(
                        label='年收支圖表',
                        display_text='年收支圖表',
                        data='action=興趣不能當飯吃，但總比吃飯當興趣好'
                    )
                )]))



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
    text = event.message.text
    if text in ['服務條款', '同意服務條款']:
        handle_terms(event)
    elif text in ['圖表', '查看圖表']:
        handle_charts(event)
    else:
        handle_other(event) # 這裡是其他處理函數的統合
        

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
