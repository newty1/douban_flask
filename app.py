from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return  render_template("index.html")
@app.route('/index')
def home():  # put application's code here
    #return  render_template("index.html")
    return index()
@app.route('/movie')
def movie():  # put application's code here
    datalist=[]
    con=sqlite3.connect("movie.db")
    cur=con.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)  #后面指针指向的内容会被清空，所以得前面创建一个datalist
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return  render_template("movie.html",movie=datalist)
@app.route('/score')
def score():  # put application's code here
    score = []#电影评分
    num=[]#每个评分所对应电影条数
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score ,count(score) from movie250 group by score "
    data = cur.execute(sql)  # 后面指针指向的内容会被清空，所以得前面创建一个datalist
    for item in data:
        score.append((item[0]))
        num.append(item[1])
    cur.close()
    con.close()
    return  render_template("score.html",score=score,num=num)#页面接受变量
@app.route('/word')
def word():  # put application's code here
    return  render_template("word.html")
@app.route('/team')
def team():  # put application's code here
    return  render_template("team.html")
if __name__ == '__main__':
    app.run(debug=True)
