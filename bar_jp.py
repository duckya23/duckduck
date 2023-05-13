import matplotlib.pyplot as plt
from matplotlib import font_manager

from pylab import mpl 

mpl.rcParams["font.sans-serif"] = ['Microsoft JhengHei']
mpl.rcParams["axes.unicode_minus"] = False


# 生成fig
plt.figure(figsize=(8, 5), dpi=50)

# 電影名字，每部電影對應的票房
month = [u'1月',u'2月',u'3月',u'4月',u'5月', u'6月',u'7月',u'8月',u'9月',u'10月',u'11月',u'12月']
income = [20000,22000,20000,11000,25000,23000,26000,22000,20000,27000,19000,21000]
expend = [11000,8000,8000,9000,10000,9500,10000,8500,8000,12000,9300,9400]
x = range(len(month))

# 使用 plt.bar 顯示柱狀圖
# plt.bar: 填入的x座標必須全是數字
# plt.bar(x, movie_BoxOffice, width=0.2, color=['b','r','g','y','c','m','y','k','c','g','g'])
width = 0.3
plt.bar(x, income, width, label="收入")
plt.bar([i+width for i in x], expend, width, label="支出")

# 修改刻度,以電影名字顯示
plt.xticks([i+width for i in x],month )

# 增加標題，座標描述
plt.xlabel(u"月份")
plt.ylabel(u"金額(元)" )

# 圖形註釋
plt.legend( loc="upper right")

# 圖形儲存到該檔案路徑下
plt.savefig("bar_jp.png")

plt.show()