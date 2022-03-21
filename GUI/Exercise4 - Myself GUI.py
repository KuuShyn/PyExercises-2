from tkinter import *
import os

def find(name, path):
    for root, _, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

main = Tk()
main.title("┬──┬ ノ( ゜-゜ノ)")

main.iconbitmap(find('catcringe.ico', 'C:'))

MyLeftPos = (main.winfo_screenwidth() - 500) / 2
myTopPos = (main.winfo_screenheight() - 300) / 2

main.geometry("%dx%d+%d+%d" % (530, 110, MyLeftPos, myTopPos))
main.resizable(False, False)

frameCnt = 48
animgif = [PhotoImage(file=find('tenor.gif', 'C:'), format='gif -index %i' % (i))
           for i in range(frameCnt)]

def update(ind):
    frame = animgif[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    anim.configure(image=frame)
    main.after(100, update, ind)

anim = Label(main)
anim.pack(side=LEFT)

main.after(0, update, 0)

Vertical = Frame(main, bg='black', height=120, width=2)
Vertical.place(x=155, y=2)

text = Label(
    main,
    font=('Comic Sans MS', 26, 'bold', 'italic'),
    foreground='snow',
    background='dodger blue',
    text="King Aj Magalona \n Monkayo, June 2001"
)

text.pack(side=RIGHT)

main.mainloop()
