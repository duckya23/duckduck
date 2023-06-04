import pymysql
import pandas as pd
import numpy as np
from pylab import mpl 
import matplotlib.pyplot as plt

# 建立與 MySQL 資料庫的連接
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

# 擷取 duckduck 資料表的數據
mpl.rcParams["font.sans-serif"] = ['Microsoft JhengHei']
mpl.rcParams["axes.unicode_minus"] = False

query = "SELECT month, income, expend FROM userduck"
data = pd.read_sql(query, connection)
income_values = data['income'].values
expend_values = data['expend'].values
x_labels = data['month'].values
bar_width = 0.35
bar_positions1 = np.arange(len(income_values))
bar_positions2 = bar_positions1 + bar_width

query2 = "SELECT 飲食, 服裝, 住宿, 交通, 教育, 玩樂 FROM expend"
data2 = pd.read_sql(query2, connection)
food_values = data2['飲食'].values
clothing_values = data2['服裝'].values
accommodation_values = data2['住宿'].values
transportation_values = data2['交通'].values
education_values = data2['教育'].values
play_values = data2['玩樂'].values

colors = ['mistyrose', 'lavender', 'lemonchiffon', 'honeydew', 'aliceblue', 'seashell']
values = [sum(food_values), sum(clothing_values), sum(accommodation_values), 
          sum(transportation_values), sum(education_values), sum(play_values)]
labels = ['飲食', '服裝', '住宿', '交通', '教育', '玩樂']

plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, radius=1)
plt.title(u"月支出占比圓餅圖")
plt.savefig('finpie.jpg')
plt.clf()  


# 繪製兩個長條圖
plt.bar(bar_positions1, income_values, width=bar_width, label='收入',color= 'lightblue')
plt.bar(bar_positions2, expend_values, width=bar_width, label='支出',color='mistyrose')


plt.xticks(bar_positions1 + bar_width / 2, x_labels)
plt.title('月收入趨勢分析圖')
plt.xlabel(u"月份")
plt.ylabel(u"金額(元)")
plt.legend(loc="upper right")

plt.show()
plt.savefig("groupbar.jpg")
plt.clf()  

connection.close()

