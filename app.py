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
line_bot_api = LineBotApi('o7GVhWmLARWtKhOTf0uAOWCO5UY2m4HYZFDGURs+rhnK8OZMazcsEVKNO83iPkB6NOyMXbbZXrNUYySlyd2CXHtlKYTDlkhIdGitB/ZKTvXkQc5maB9YU4wJxJF9ZoFbWIWVwYi8NHxttXiGNAQtWAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('675c061bcf22f2da2eb9c2e3c2c95a0e')

#line_bot_api.push_message('1660929518', TextSendMessage(text='你可以開始了'))  #主動推波push message #要付費的

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
    message = event.message.text

    if re.match('告訴我秘密',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('才不告訴你哩！'))

  ##貼圖      
    elif re.match('貼圖',message):
        # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
        sticker_message = StickerSendMessage(
            package_id='˙789',
            sticker_id='10856'
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)

  ##圖片
    elif re.match('圖片',message):
        image_message = ImageSendMessage(     ##訊息:textmessage
            original_content_url='https://media.nownews.com/nn_media/thumbnail/2019/04/ceca31ba-1555497323-a017e0caf9119cc47e6729799c0161ba-800x400.jpg',
            preview_image_url='https://i.ytimg.com/vi/qjP6z2ilTWU/maxresdefault.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
  ##組圖訊息
    elif re.match('組圖訊息',message):
        imagemap_message = ImagemapSendMessage(
            base_url='https://i.imgur.com/wpM584d.jpg',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            video=Video(
                original_content_url='https://i.imgur.com/1BnZGQC.mp4',
                preview_image_url='https://imgur.com/SVhJU6w.jpg',
                area=ImagemapArea(
                    x=0, y=0, width=1040, height=585
                ),
                external_link=ExternalLink(# 影片結束後的連結
                    link_uri='https://marketingliveincode.com/',
                    label='查看更多...',
                ),
            ),
            actions=[
                URIImagemapAction(# 超連結
                    link_uri='https://marketingliveincode.com/',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(# 文字訊息
                    text='戳我幹嘛！',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
  
  ##選單功能 max4 
    elif re.match('其他功能',message):
        buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到',  #註解
        template=ButtonsTemplate(
            thumbnail_image_url='https://png.pngtree.com/png-vector/20190831/ourlarge/pngtree-gear-vector-icon-template-png-image_1717225.jpg',
            title='其他功能來了鴨',
            text='記帳鴨博士的其他功能',
            actions=[
                MessageAction(
                    label='新手教學',
                    text='新手教學'
                ),
                MessageAction(
                    label='服務條款',
                    text='查看服務條款'
                ),
                MessageAction(
                    label='Line Pay 連結',
                    text='Line Pay 連結'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
  ##多樣板 max10 按鈕max3
    elif re.match('多樣版',message):
        carousel_template_message = TemplateSendMessage(
            alt_text='免費教學影片',  ##不顯示
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='Python基礎教學',
                        text='萬丈高樓平地起',
                        actions=[  ##下方按鈕
                            MessageAction(
                                label='教學內容',
                                text='拆解步驟詳細介紹安裝並使用Anaconda、Python、Spyder、VScode…'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=270'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='Line Bot聊天機器人',
                        text='台灣最廣泛使用的通訊軟體',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='Line Bot申請與串接'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=2532'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='Telegram Bot聊天機器人',
                        text='唯有真正的方便，能帶來意想不到的價值',
                        actions=[
                            MessageAction(
                                label='教學內容',
                                text='Telegrame申請與串接'
                            ),
                            URIAction(
                                label='馬上查看',
                                uri='https://marketingliveincode.com/?page_id=2648'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)

  ##選擇按鈕
    elif re.match('選擇按鈕',message):
        confirm_template_message = TemplateSendMessage(
            alt_text='問問題',
            template=ConfirmTemplate(
                text='你喜這堂課嗎？',
                actions=[
                    PostbackAction(
                        label='喜歡',
                        display_text='超喜歡',
                        data='action=其實不喜歡'
                    ),
                    MessageAction(
                        label='愛',
                        text='愛喔'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)

  ##大圖案紐 max 10
    elif re.match('大圖案紐',message):
        image_carousel_template_message = TemplateSendMessage(
            alt_text='免費教學影片',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/wpM584d.jpg',
                        action=PostbackAction(
                            label='Python基礎教學影片',  ##不可超過12字元
                            display_text='萬丈高樓平地起',
                            data='action=努力不一定會成功，但不努力會很輕鬆'  ##部會看到
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/W7nI6fg.jpg',
                        action=PostbackAction(
                            label='LineBot聊天機器人',
                            display_text='台灣最廣泛使用的通訊軟體',
                            data='action=興趣不能當飯吃，但總比吃飯當興趣好'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)

  ##客製化選單  
    elif re.match('客製化選單',message):
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
        "text": "RECEIPT",
        "weight": "bold",
        "color": "#1DB446",
        "size": "sm"
      },
      {
        "type": "text",
        "text": "Brown Store",
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      },
      {
        "type": "text",
        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
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
                "text": "Energy Drink",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$2.99",
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
                "text": "Chewing Gum",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$0.99",
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
                "text": "Bottled Water",
                "size": "sm",
                "color": "#555555",
                "flex": 0
              },
              {
                "type": "text",
                "text": "$3.33",
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
            "margin": "xxl",
            "contents": [
              {
                "type": "text",
                "text": "ITEMS",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "3",
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
                "text": "TOTAL",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$7.31",
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
                "text": "CASH",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$8.0",
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
                "text": "CHANGE",
                "size": "sm",
                "color": "#555555"
              },
              {
                "type": "text",
                "text": "$0.69",
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
            "text": "PAYMENT ID",
            "size": "xs",
            "color": "#aaaaaa",
            "flex": 0
          },
          {
            "type": "text",
            "text": "#743289384279",
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

  ##快速鍵       
    elif re.match('快速鍵',message):
        flex_message = TextSendMessage(text='以下有雷，請小心',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                   QuickReplyButton(action=MessageAction(label="別按我", text="你按屁喔！爆炸了拉！！")),
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！")),
                                   QuickReplyButton(action=MessageAction(label="按我", text="按！"))
                               ]))
        line_bot_api.reply_message(event.reply_token, flex_message)

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message)) #message=使用者傳送
                                                      #textsendmessage 主要是傳送文字訊息
        #push_message line主動去推撥文字/發文 #reply_message 使用者戳了機器然才會回復

    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
