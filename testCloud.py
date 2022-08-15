import jieba
from matplotlib import pyplot as plt # 绘图 数据可视化
from wordcloud import WordCloud  #词云
from PIL import Image   #图片处理
import numpy as np     #矩阵运算
import sqlite3        #数据库

path3="stopword.txt"
def stopwordslist():  # 去停助词的函数
   stopwords = [line.strip() for line in open(path3, encoding='UTF-8').readlines()]
   return stopwords
stopwords = stopwordslist()

#数据准备工作
con =sqlite3.connect("movie.db")
cur =con.cursor()
sql ="select instroduction from movie250"
data =cur.execute(sql)
text =""
for item in data:
   text = text+ item[0]
cur.close()
con.close()
# 分词
cut=jieba.cut(text)
string=' '.join(cut)
string2=" "
for item in string:
   if item not in stopwords:
       string2= string2+item

print(string2)
#绘图
img =Image.open(r".\static\assets\img\Miki.jpg")#打开遮罩图片
img_arry =np.array(img) #将图片转换为数组
wc =WordCloud(
   background_color="white",
   mask=img_arry,
   font_path="FZSTK.TTF"
)
wc.generate_from_text(string2)

#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')# 是否显示坐标轴

plt.savefig(r".\static\assets\img\word.jpg",dpi=400)