from tkinter import *
root = Tk()
root.title("┬──┬ ノ( ゜-゜ノ)")
root.iconbitmap('catcringe.ico')

MyLeftPos = (root.winfo_screenwidth() - 500) / 2
myTopPos = (root.winfo_screenheight() - 300) / 2

root.geometry("%dx%d+%d+%d" % (530, 110, MyLeftPos, myTopPos))
root.resizable(False, False)

frameCnt = 48
animgif = [PhotoImage(file='tenor.gif', format='gif -index %i' % (i))
           for i in range(frameCnt)]

Vertical = Frame(root, bg='black', height=120, width=2)
Vertical.place(x=155, y=2)

def update(ind):
    frame = animgif[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    anim.configure(image=frame)
    root.after(100, update, ind)

anim = Label(root)
anim.pack(side=LEFT)

text = Label(
    root,
    font=('Comic Sans MS', 26, 'bold', 'italic'),
    foreground='snow',
    background='dodger blue',
    text="King Aj Magalona \n Monkayo, June 2001"
)

text.pack(side=RIGHT)

root.after(0, update, 0)
root.mainloop()
