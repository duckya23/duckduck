import matplotlib.pyplot as plt 
from pylab import mpl 

mpl.rcParams["font.sans-serif"] = ['Microsoft JhengHei']
mpl.rcParams["axes.unicode_minus"] = False

sorts = [u"飲食",u"服裝",u"住宿",u"交通",u"教育",u"玩樂"]
fee = [2400,3000,7000,700,530,600]



plt.pie(fee,labels=sorts,explode=(0,0,0,0,0,0),
        autopct="%1.1f%%", colors = ['mistyrose' ,'lavender', 'lemonchiffon', 'honeydew', 'aliceblue', 'seashell'],startangle=180
)
plt.show()
plt.savefig("pie.png")

# import matplotlib.pyplot as plt

# labels = [u"飲食",u"服裝",u"住宿",u"交通",u"教育",u"玩樂"]
# values = [2400,300,7000,700,530,600]
# colors = ['r', 'g', 'b', 'y','black','pink']
# explode = (0,0,0,0,0,0)
# plt.figure(figsize=(10,10)) # 設定圖表區寬高

# plt.pie(
# values, # 數值
# labels = labels, # 項目標題
# colors = colors, # 指定圓餅圖的顏色
# explode = explode, # 設定分隔的區塊位置
# autopct = "%1.1f%%", # 項目百分比格式
# pctdistance = 0.8, # 數值文字與圓心距離
# # shadow = True, # 圓餅圖陰影開啟/關閉
# startangle = 90, # 繪製起始角度
# radius = 0.5 # 圓餅圖的半徑，預設是1
# )

# plt.legend(loc = "right") # 設定 legnd 的位置
# plt.show()
# plt.savefig("pie.png")

