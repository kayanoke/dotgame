#GUI
import tkinter
#多重ループ
import itertools

# 64 * 6, 32 * 12, 16 * 24, 8 * 48
dotsize = 32
xlength = 12
ylength = 12
width = 2
iconPath = 'icon/'
soundPath = 'sound/'
xsize = dotsize * xlength
ysize = dotsize * ylength

# 画像をクリックしたときの処理
def changecolor(color):
    global scorep
    if color == 'red':
        scorep += 1
        result = 'green'
    elif color == 'green':
        scorep += 5
        result = 'blue'
    elif color == 'blue':
        scorep += 57
        result = 'white'
    elif color == 'white':
        scorep += 212
        result = 'black'
    elif color == 'black':
        scorep += 10000
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
    global scorep
    xx = event.x // dotsize
    yy = event.y // dotsize
    xxx = xx * dotsize
    yyy = yy * dotsize
    #canvas.delete('tangle'+str(xx)+str(yy))
    color = canvas.itemcget('tangle'+str(xx).zfill(3)+str(yy).zfill(3),'fill')
    canvas.itemconfig('tangle'+str(xx).zfill(3)+str(yy).zfill(3),fill=changecolor(color))
    #canvas.create_rectangle(xxx,yyy,xxx+dotsize,yyy+dotsize,width=3,outline='white',fill='green',tags='tangle'+str(i)+str(j))
    score['text'] = 'score : '+str(scorep)

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
        canvas.create_rectangle(x,y,x+dotsize,y+dotsize,width=width,outline='white',fill='red',tags='tangle'+str(i).zfill(3)+str(j).zfill(3))

score = tkinter.Label(text='score : 0',font=('',15))
score.place(x=xsize/2, y=ysize+5)
scorep = 0

# キャンバスにボタンイベントを追加
canvas.bind('<Button-1>', event_function)

# ウィンドウの大きさ、位置を設定
root.geometry(str(xsize)+'x'+str(ysize+30)+'+225+200')

root.resizable(width=False, height=False)
root.mainloop()
