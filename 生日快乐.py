import time
from tkinter import *
import winsound

root=Tk()
root.title('夜曲一响，上台领奖')
root.iconbitmap('gift.ico')
root.geometry('+550+250')
fm1=Frame(root)
fm1.pack(side=TOP,padx=10, pady=10)
fm2=Frame(root)
fm2.pack()

answer=input('请输入您的生日(****年**月**日）：')
if answer=='2005年11月14日':
    print('好久不见.生日快乐。🎂')
    input('任意对话:')
    input('当然，这个程序还做不到同您对话。现在按\'enter\'打开礼物：')
    print('筹备中...')
    time.sleep(3)
    root.deiconify()
    print('''其实想放假的时候给你的，
贸然约您见面就算是交付礼物也略显唐突
但是这张专辑我想还是十一月送最合适，
以及如果我不询问是否一起回重庆的话(社恐），放假也可能见不了面。
于是写了这个小邀请函。''')
else:
    print('抱歉，您不是这份礼物的主人。')

albumtxt='''《十一月的肖邦》，周董第六张专辑。发行于2005年11月1日(与您的生日接近)。
2006年被评为年度十大专辑，其中《夜曲》获2006年最受欢迎音乐录像带，年度最佳歌曲。



如果您能看到这段话，说明此段程序运行的还算成功。请回复一个空闲的时段，
我会在图书馆东侧湖边将礼物交予您'''
textlabel=Label(fm1,
                text=albumtxt,
                justify=LEFT,
                padx=20,pady=10)
textlabel.pack(side=LEFT)

albumpic=PhotoImage(file='../生日计划/z.png')
imglabel=Label(
          fm1,
          image=albumpic)
imglabel.pack(side=RIGHT)

def play(event):
    global wav
    wav=winsound.PlaySound('jay.wav',winsound.SND_ASYNC)
    print(event)
def stop(event):
    winsound.PlaySound(wav,winsound.SND_PURGE)
def close(event):
    root.destroy()


seletion=['播放','停止','确定']
b=[]
for i in range(3):
    b.append(Button(fm2,text=seletion[i],width=20,height=1))
    b[i].pack(side=LEFT,anchor=NW)
b[0].bind('<ButtonRelease-1>',play)
b[1].bind('<ButtonRelease-1>',stop)
b[2].bind('<ButtonRelease-1>',close)

root.mainloop()
