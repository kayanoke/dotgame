#GUI
import tkinter
#多重ループ
import itertools

dotsize = 64
xlength = 6
ylength = 6
iconPath = 'icon/'
soundPath = 'sound/'
xsize = dotsize * xlength
ysize = dotsize * ylength

# 画像をクリックしたときの処理
def changecolor(color):
    if color == 'red':
        result = 'green'
    elif color == 'green':
        result = 'blue'
    elif color == 'blue':
        result = 'white'
    elif color == 'white':
        result = 'black'
    elif color == 'black':
        result = 'yellow'
    elif color == 'yellow':
        result = 'purple'
    elif color == 'purple':
        result = 'pink'
    else:
        result = 'red'
    return result

# 画像をクリックしたときの処理
def event_function(event):
    global dotsize
    xx = event.x // 64
    yy = event.y // 64
    xxx = xx * 64
    yyy = yy * 64
    #canvas.delete('tangle'+str(xx)+str(yy))
    color = canvas.itemcget('tangle'+str(xx)+str(yy),'fill')
    canvas.itemconfig('tangle'+str(xx)+str(yy),fill=changecolor(color))
    #canvas.create_rectangle(xxx,yyy,xxx+dotsize,yyy+dotsize,width=3,outline='white',fill='green',tags='tangle'+str(i)+str(j))

# ウィンドウ（フレーム）の作成
root = tkinter.Tk()
# ウィンドウの名前を設定
root.title("d.o.t")

# 画像表示用のキャンバス作成
canvas = tkinter.Canvas(bg="black", width=xsize, height=ysize)
canvas.place(x=0, y=0) # 左上の座標を指定

#canvas.create_rectangle(←x,↑y,→x,↓y,width=枠幅,outline=枠色,fill=中色,tags=タグ)
#canvas.create_rectangle(10,30,64,128,width=2,outline='white',fill='red',tags='tangle2')
# 6回繰り返す。
for i, j in itertools.product(range(xlength),range(ylength)):
        x = i * dotsize
        y = j * dotsize
        canvas.create_rectangle(x,y,x+dotsize,y+dotsize,width=3,outline='white',fill='red',tags='tangle'+str(i)+str(j))

# キャンバスにボタンイベントを追加
canvas.bind('<Button-1>', event_function)

# ウィンドウの大きさ、位置を設定
root.geometry(str(xsize)+'x'+str(ysize)+'+200+200')

root.resizable(width=False, height=False)
root.mainloop()
