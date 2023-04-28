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
 

@app.route("/callback", methods=['POST'])
def handle_callback():
    message = event.message.text
    
    if re.match('其它功能',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='其它功能來了鴨',
        template=ButtonsTemplate(
            thumbnail_image_url='https://png.pngtree.com/png-vector/20190831/ourlarge/pngtree-gear-vector-icon-template-png-image_1717225.jpg',
            title='其它功能鴨！',
            text='記帳鴨博士的其它功能',
            actions=[
                MessageAction(
                    label='新手教學',
                    text='新手教學',
                ),
                MessageAction(
                    label='服務條款',
                    text='服務條款'
                ),
                MessageAction(
                    label='Line Pay 連結',
                    text='Line Pay 連結',
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif re.match('服務條款',message):
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
        
    elif re.match('圖表',message):
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
                    ),
                    ImageCarouselColumn(
                        image_url='https://pic2.zhimg.com/v2-706be7f956613c2b4f0431482b858dc9_b.png',
                        action=PostbackAction(
                            label='哈哈哈你以為有什麼',
                            display_text='哈哈哈哩鴨',
                            data='action=興趣不能當飯吃，但總比吃飯當興趣好'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
    elif re.match('記帳',message):
        flex_message = TextSendMessage(text='快來記帳鴨',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="收入", text="收入鴨!")),
                                   QuickReplyButton(action=MessageAction(label="支出", text="支出鴨!"))
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
        
    elif re.match('預算',message):
        flex_message = TextSendMessage(text='快來設定預算鴨',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="飲食預算", text="飲食預算")),
                                   QuickReplyButton(action=MessageAction(label="日用預算", text="日用預算")),
                                   QuickReplyButton(action=MessageAction(label="居家預算", text="居家預算")),
                                   QuickReplyButton(action=MessageAction(label="交通預算", text="交通預算")),
                                   QuickReplyButton(action=MessageAction(label="服飾預算", text="服飾預算")),
                                   QuickReplyButton(action=MessageAction(label="娛樂預算", text="娛樂預算")),
                                   QuickReplyButton(action=MessageAction(label="醫療預算", text="醫療預算")),
                                   QuickReplyButton(action=MessageAction(label="美容預算", text="美容預算")),
                                   QuickReplyButton(action=MessageAction(label="教育預算", text="教育預算")),
                                   QuickReplyButton(action=MessageAction(label="其它預算", text="其它預算"))
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
        
      
    elif re.match('飲食預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少飲食預算鴨！'))    
    elif re.match('日用預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少日用預算鴨!')) 
    elif re.match('居家預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少居家預算鴨!'))    
    elif re.match('交通預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少交通預算鴨!')) 
    elif re.match('服飾預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少服飾預算鴨!'))    
    elif re.match('娛樂預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少娛樂預算鴨!')) 
    elif re.match('醫療預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少醫療預算鴨!'))    
    elif re.match('美容預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少美容預算鴨!')) 
    elif re.match('教育預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少教育預算鴨!'))    
    elif re.match('其它預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少其它預算鴨!'))
    elif re.match('我同意服務條款',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('非常感謝您同意我們的條款，我們期待本程式能夠為您提供優質的服務。'))    
    elif re.match('我不同意服務條款',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('由於您使用本應用程式進行記帳，為了協助您分析收入，本程式需要使用您所提供的資訊進行分析。然而，因為您選擇不同意服務條款，本程式無法為您提供相關分析功能。因此，我們建議您重新考慮是否同意服務條款，以確保您能夠使用本程式的全部功能。如果您重新選擇同意服務條款後，即可再次使用本程式。'))    
    elif re.match('支出',message):
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
    elif re.match('收入',message):
        flex_message = TextSendMessage(text='選擇收入類別鴨！',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="薪資", text="薪資")),
                                   QuickReplyButton(action=MessageAction(label="獎金", text="獎金")),
                                   QuickReplyButton(action=MessageAction(label="理財", text="理財")),
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('飲食',message):
        total = 0
        reply_message = TextSendMessage(text='請輸入餐飲費金額')
        line_bot_api.reply_message(event.reply_token, reply_message)

        # 接收使用者輸入的訊息
        message_event = event.message
        if isinstance(message_event, TextMessage):
            try:
                # 將輸入的金額轉成整數，並累加到 total 變數中
                amount = int(message_event.text)
                total += amount

                # 回覆使用者訊息
                reply_message = TextSendMessage(text=f'已累加 {amount} 元，目前總共 {total} 元')
                line_bot_api.reply_message(event.reply_token, reply_message)
            except ValueError:
                # 如果輸入的不是數字，則回覆錯誤訊息
                reply_message = TextSendMessage(text='請輸入正確的金額')
                line_bot_api.reply_message(event.reply_token, reply_message)

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
      
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
