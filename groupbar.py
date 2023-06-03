import pymysql
import pandas as pd
import numpy as np
from pylab import mpl 
import matplotlib.pyplot as plt

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='test')

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

plt.bar(bar_positions1, income_values, 
        width=bar_width, label='收入',color= 'lightblue')

plt.bar(bar_positions2, expend_values, 
        width=bar_width, label='支出',color='mistyrose')

plt.xticks(bar_positions1 + bar_width / 2, x_labels)
plt.title('月收支趨勢分析圖')
plt.xlabel(u"月份")
plt.ylabel(u"金額(元)")
plt.legend(loc="upper right")

plt.show()
plt.savefig("groupbar.jpg")
connection.close()
