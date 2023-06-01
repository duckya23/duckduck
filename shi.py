def is_number(input_str):
    try:
        float(input_str)  # 嘗試將輸入轉換為浮點數
        return True  # 成功轉換，輸入是一個數字
    except ValueError:
        return False  # 轉換失敗，輸入不是一個數字

@handler.add(MessageEvent, message=TextMessage)
def handle_message2():
    message = text=event.message.text
    with open('Account_number.csv', 'r') as file:
    Account_number =int( file.read())

    if message.isdigit(): # 當message是數字，執行這個
        with open('food.csv', 'r') as file: # 讀取food金額
            food =int( file.read())            
        food +=float(message) 
        with open('food.csv', 'w+') as file: # 寫入food金額
            file.write(str(food))
        Account_number+=1
        import time
        localtime = time.asctime( time.localtime(time.time()) )
        import csv
        my_dict_food = {}
        filename = 'my_dict_food.csv'
        # 開啟 CSV 文件並追加字典內容
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # 檢查是否為空檔案，若是則寫入標題行
            if csvfile.tell() == 0:
                writer.writerow(['Key', 'Value1', 'Value2'])
            key = Account_number
            value1 = localtime
            value2 = float(message)
            my_dict_food[key] = [value1, value2]  # 使用鍵作為索引，將兩個值分配給該鍵
            # 寫入數據行
            for key, values in my_dict_food.items():
                writer.writerow([key] + values)
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
