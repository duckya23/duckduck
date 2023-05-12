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



#以下這段目前沒有作用
@handler.add(MessageEvent, message=TextMessage)
def handle_message2():
    message = text=event.message.text
    if re.match('我的金額',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('金額為多少鴨!')) 
    else :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#以下這段目前沒有作用
@handler.add(MessageEvent, message=TextMessage)
def handle_message3():
        line_bot_api.reply_message(event.reply_token,TextSendMessage('金額為多少鴨!')) 
        


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
def handle_message9(event):
    totala=0 
    message = text = event.message.text
    if re.match('其它功能',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='其它功能來了鴨',
        template=ButtonsTemplate(
            thumbnail_image_url='https://png.pngtree.com/png-vector/20190831/ourlarge/pngtree-gear-vector-icon-template-png-image_1717225.jpg',
            title='其它功能鴨！',
            text='記帳鴨博士的其它功能',
            actions=[
                MessageAction(
                    label='使用說明',
                    text='使用說明',
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
        
    elif re.match('使用說明',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('【使用說明】:\
                                                                     1.請先詳細看完服務條款並同意再進行本服務鴨，要看清楚鴨！呱！！\
                                                                     \
                                                                     2.點擊下列選單中的【記帳】會在鍵盤上方跳出小按鈕可以選擇輸入收入、支出、編輯資料！\
                                                                     \
                                                                     3.點擊下列選單中的【圖表】會有?種圖表可以詳細分析出您的月收支以及?\
                                                                     \
                                                                     4.點擊下列選單中的【預算】會在鍵盤上方跳出小按鈕可以選擇要設定的預算類別，點擊類別後再輸入金額鴨！\
                                                                     \
                                                                     5.點擊下列選單中的【其它功能】會跳出三個選項(使用說明、服務條款、Line Pay連結)鴨\
                                                                     (1)點擊【使用說明】會傳給您使用說明的詳細內容鴨\
                                                                     (2)點擊【服務條款】會跳出服務條款的頁面供您查看鴨\
                                                                     (3)點擊【Line Pay連結】會跳出Line Pay的連結設定，若一開始使用本服務已同意連結Line Pay ，若要終止請點擊【終止連結】按鈕若一開始使用本服務未使用連結Line Pay服務，若要啟動請點擊【連結】按鈕鴨！\
                                                                     \
                                                                     6.若對此記帳鴨服務有任何建議或是問題需修改，可以點選服務條款下的表單填寫，鴨博士會很開心能夠收到您們的建議和回饋喔！'))
        
# 定義LineBot回應訊息
#def handle_postback(event):
    # 判斷是否為 Postback 事件
#    if event.postback:
#        # 取得 Postback 資料
#        data = event.postback.data
        # 判斷 Postback 的 action
#        if data == 'action=send_message&message=嗨':
            # 回傳指定的訊息
#            line_bot_api.reply_message(
#                event.reply_token,
#                TextSendMessage(text='嗨')
#            )
    
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
                                   QuickReplyButton(action=MessageAction(label="其它預算", text="其它預算")),
                                   QuickReplyButton(action=MessageAction(label="結餘&預算表格", text="好的現在為您開啟表格!鴨鴨!"))
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
        
    
#     elif re.match('好的現在為您開啟表格!鴨鴨!',message):

#         from tkinter import *
#         from tabulate import tabulate
#         categories = ["飲食", "日用", "居家", "交通", "服飾", "娛樂", "醫療", "美容", "教育", "其它"]
#         budgets = [3000, 2000, 2500, 3500, 1000, 1500, 800, 500, 1200, 900]
#         balances = [10] * len(categories)

#         d = list(zip(categories, budgets, balances))
#         table = tabulate(d, headers=["類別", "預算", "結餘"], tablefmt="pipe")

# # 创建新窗口并显示表格
#         root = Tk()
#         root.title("預算表格")
#         root.geometry("400x400")
#         table_label = Label(root, text=table, justify=LEFT, font=("Courier", 12))
#         table_label.pack()
#         root.mainloop()
    elif re.match('飲食預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少飲食預算鴨！'))
    #飲食預算要用3000
    elif re.match('3000',message):
        totala+=3000
        line_bot_api.reply_message(event.reply_token,TextSendMessage('已經幫您儲存了鴨！'))
        
        
    elif re.match('日用預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少日用預算鴨!'))
    #日用預算要用2000
    elif re.match('2000',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
    elif re.match('居家預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少居家預算鴨!'))
    #居家預算要用2500
    elif re.match('2500',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
    elif re.match('交通預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少交通預算鴨!'))
    #交通預算要用3500
    elif re.match('3500',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
    elif re.match('服飾預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少服飾預算鴨!'))
    #服飾預算要用1000
    elif re.match('1000',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
    elif re.match('娛樂預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少娛樂預算鴨!'))
    #娛樂預算要用1500
    elif re.match('1500',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
    elif re.match('醫療預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少醫療預算鴨!'))
    #醫療預算要用800
    elif re.match('800',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
    elif re.match('美容預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少美容預算鴨!'))
    #美容預算要用500
    elif re.match('500',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))    
    elif re.match('教育預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少教育預算鴨!'))
    #教育預算要用1200
    elif re.match('1200',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
    elif re.match('其它預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少其它預算鴨!'))
    #醫療預算要用900
    elif re.match('900',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('幫你儲存了鴨！'))
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
                                   QuickReplyButton(action=MessageAction(label="其他支出", text="其他支出")),
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('收入',message):
        flex_message = TextSendMessage(text='選擇收入類別鴨！',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="薪資", text="薪資")),
                                   QuickReplyButton(action=MessageAction(label="獎金", text="獎金")),
                                   QuickReplyButton(action=MessageAction(label="理財", text="理財")),
                                   QuickReplyButton(action=MessageAction(label="其他收入", text="其他收入")),
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('飲食',message):
        #以下這段只是測試用，測試失敗
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入餐飲金額鴨!'))        
        amount =event.message.text
        line_bot_api.reply_message(event.reply_token, TextSendMessage("amount"))                   
    elif re.match('交通',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入交通金額鴨!')) 
    elif re.match('娛樂',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入娛樂金額鴨!')) 
    elif re.match('醫療',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入醫療金額鴨!')) 
    elif re.match('服飾',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入服飾金額鴨!')) 
    elif re.match('美容',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入美容金額鴨!')) 
    elif re.match('教育',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入教育金額鴨!'))
    elif re.match('居家(水電瓦斯)',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入居家(水電瓦斯)金額鴨!'))
    elif re.match('日用(如:洗髮精)',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入日用(如:洗髮精)金額鴨!'))
    elif re.match('其他支出',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入其他金額鴨!'))
    elif re.match('薪資',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入薪資收入金額鴨!')) 
    elif re.match('獎金',message):
        handle_message3()
        #line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入獎金收入金額鴨!')) 
    elif re.match('理財',message):
        #測試函數
        handle_message2()
        #line_bot_api.reply_message(event.reply_token,TextSendMessage('請輸入理財收入金額鴨!')) 
    elif re.match('其他收入',message):
        #以下這段只是測試用，測試失敗，先留者
        amount = text=event.message.text
        a = amount  # 儲存輸入的金額到變數 a 中
        reply_text = f'已儲存金額 {a} 鴨！'  # 建立回覆訊息
        line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
    elif re.match('回傳兩個訊息',message):
        #以下這段只是測試用，劉者以後可能用
        amount = event.message.text
        reply_arr = [TextSendMessage(amount),TextSendMessage("歡迎使用本軟體")]
        line_bot_api.reply_message(event.reply_token,reply_arr)
        amount = event.message.text
#         line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨!'))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(amount))
    elif re.match('查看totala',message):
        #以下這段只是測試用
        reply_text = f'目前飲食預算為 {totala} 鴨！'  # 建立回覆訊息
        line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
        

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
