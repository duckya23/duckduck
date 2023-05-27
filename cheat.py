###假的預算與支出
    elif re.match('預算與結餘',message):
        flex_message = TextSendMessage(text='快來設定預算鴨',
                               quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="結餘&預算表格", text="好的現在為您開啟表格!鴨鴨!")),
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
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存飲食預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('日用預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少日用預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存日用預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('居家預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少居家預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存居家預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('交通預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少交通預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存交通預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('服飾預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少服飾預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存服飾預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('娛樂預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少娛樂預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存娛樂預算了鴨!")
        else:
            print("請重新輸入鴨!")
    
    elif re.match('醫療預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少醫療預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存醫療預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('美容預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少美容預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存美容預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('教育預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少教育預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存教育預算了鴨!")
        else:
            print("請重新輸入鴨!")

    elif re.match('其他預算',message):
        line_bot_api.reply_message(event.reply_token,TextSendMessage('鴨鴨！你要設定多少其他預算鴨！'))
        user_input = input("請輸入一個數字：")
        if user_input.isdigit():
            print("已幫您儲存其他預算了鴨!")
        else:
            print("請重新輸入鴨!")

import pandas as pd

# 建立一個空的資料框(DataFrame)來儲存預算資料
budget_df = pd.DataFrame(columns=['名稱類別', '預算', '結餘'])

# 預算類別清單
budget_categories = ['飲食', '日用', '居家', '交通', '服飾', '娛樂', '醫療', '美容', '教育', '其他']

# 輸入各項預算
for category in budget_categories:
    if category == '飲食':
        user_input = input(f"請輸入{category}預算：")
        if user_input.isdigit():
            budget_df = budget_df.append({'名稱類別': category, '預算': int(user_input), '結餘': int(user_input) - food}, ignore_index=True)
            print(f"已幫您儲存{category}預算了鴨！")
        else:
            print("請重新輸入鴨！")
    elif category == '交通':
        user_input = input(f"請輸入{category}預算：")
        if user_input.isdigit():
            budget_df = budget_df.append({'名稱類別': category, '預算': int(user_input), '結餘': int(user_input) - transportation}, ignore_index=True)
            print(f"已幫您儲存{category}預算了鴨！")
        else:
            print("請重新輸入鴨！")
    else:
        user_input = input(f"請輸入{category}預算：")
        if user_input.isdigit():
            budget_df = budget_df.append({'名稱類別': category, '預算': int(user_input), '結餘': int(user_input)}, ignore_index=True)
            print(f"已幫您儲存{category}預算了鴨！")
        else:
            print("請重新輸入鴨！")

# 顯示表格
print(budget_df)


