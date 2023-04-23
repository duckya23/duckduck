# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
按鈕樣板TemplateSendMessage
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
line_bot_api = LineBotApi('XWLJgAGvJkAEAUX//FG5CDpjWpAX5TLOK4mmHpKGU8Ae8XpDOBxLfPye5XIGyNjfNOyMXbbZXrNUYySlyd2CXHtlKYTDlkhIdGitB/ZKTvUNw56TGlbvys+fePpaIa8Es07TT5PwChrysZuwF0D08gdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('e166ee3bb76574f9d62f8861afcad5b7')

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
@handler.add(MessageEvent)
def handle_message(event):
    message = text =event.message.text
    if re.match('我要記帳',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到 ',
        template=ButtonsTemplate(
            thumbnail_image_url='https://cdn.pixabay.com/photo/2022/09/04/21/03/cartoon-duck-7432790_1280.png',
            title='來記帳鴨！',
            text='選單功能－TemplateSendMessage',
            actions=[ 
                
                MessageAction(
                    label='紀錄本日支出',
                    text='鴨鴨！你今天花了多少鴨！'
                ),
                MessageAction(
                    label='紀錄本日收入',
                    text='鴨鴨！你賺了多少錢鴨！'
                )
                
                
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    if re.match('服務條款',message):
        confirm_template_message = TemplateSendMessage(
            alt_text='服務條款',
            template=ConfirmTemplate(
                text='歡迎使用來記帳鴨！請在使用本服務之前，詳細閱讀以下使用條款。\n1. 本服務是一個記帳程式，可協助使用者記錄其財務資訊。\n2. 使用者需自行創建帳號並登錄使用本服務。使用者應確保其帳號及密碼的安全性，且不得將其帳號轉移、轉讓給任何第三方。\n3. 使用者應自行負責其財務資訊之準確性、完整性及合法性，本服務不對此承擔任何責任。\n4. 使用者應保證其使用本服務之行為符合法律法規及社會道德規範，且不得利用本服務從事任何違法、不道德或有損社會公共利益之行為。\n5. 本服務可能會收集使用者的個人資訊，並根據相關法律法規進行保護和使用。使用者應詳細閱讀本服務之隱私政策，以瞭解我們如何收集、使用和保護使用者的個人資訊。\n6. 本服務可能會因系統維護、升級或其他原因暫停服務，使用者應理解並接受此種情況。本服務不對因暫停服務而導致的損失承擔任何責任。\n7. 本服務可能會因技術故障、不可抗力等原因導致數據丟失，使用者應自行備份其財務資訊，本服務不對此承擔任何責任。\n8. 本服務可能會因使用者違反使用條款而對其帳號進行限制、暫停或解除。使用者如有違反使用條款的情況，應自行承擔相應的法律責任。\n9. 本服務可能會因業務調整或其他原因進行變更或終止，使用者應理解並接受此種情況。\n是否同意上述9個條款?1.同意2.不同意',
                actions=[
                    PostbackAction(
                        label='同意',
                        display_text='非常感謝您同意我們的條款，我們期待本程式能夠為您提供優質的服務。',
                        data='繼續使用本軟體'
                    ),
                    MessageAction(
                        label='不同意',
                        text='由於您使用本應用程式進行記帳，為了協助您分析收入，本程式需要使用您所提供的資訊進行分析。然而，因為您選擇不同意服務條款，本程式無法為您提供相關分析功能。因此，我們建議您重新考慮是否同意服務條款，以確保您能夠使用本程式的全部功能。如果您重新選擇同意服務條款後，即可再次使用本程式。'
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
