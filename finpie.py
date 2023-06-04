import pymysql
import pandas as pd
import numpy as np
from pylab import mpl
import matplotlib.pyplot as plt

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database='test'
)
mpl.rcParams["font.sans-serif"] = ['Microsoft JhengHei']
mpl.rcParams['axes.unicode_minus'] = False
query = "SELECT 飲食, 服裝, 住宿, 交通, 教育, 玩樂 FROM expend"
data = pd.read_sql(query, connection)

#提數據
food_values = data['飲食'].values
clothing_values = data['服裝'].values
accommodation_values = data['住宿'].values
transportation_values = data['交通'].values
education_values = data['教育'].values
play_values = data['玩樂'].values

colors = ['mistyrose', 'lavender', 'lemonchiffon', 'honeydew', 'aliceblue', 'seashell']
values = [sum(food_values), sum(clothing_values), sum(accommodation_values), 
          sum(transportation_values), sum(education_values), sum(play_values)]
labels = ['飲食', '服裝', '住宿', '交通', '教育', '玩樂']

plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, radius=1)
plt.title(u"月支出占比圓餅圖")
plt.savefig('finpie.jpg')
plt.show()
connection.close() 
