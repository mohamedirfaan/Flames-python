from tkinter import *
from PIL import Image,ImageTk
text_font="Bauhaus 93"
main=Tk()
global name1,name2
name1=StringVar()
name2=StringVar()

load = Image.open("./images/heart.jpg")
rend = ImageTk.PhotoImage(load.resize((1500,1000)))
load1 = Image.open("./images/sibling.jpg")
rend1 = ImageTk.PhotoImage(load1.resize((1366,768)))
load2 = Image.open("./images/love.png")
rend2 = ImageTk.PhotoImage(load2.resize((1366,768)))
load3 = Image.open("./images/friends.jpg")
rend3 = ImageTk.PhotoImage(load3.resize((1366,768)))
load4 = Image.open("./images/affection.jpg")
rend4 = ImageTk.PhotoImage(load4.resize((1366,768)))
load5 = Image.open("./images/enemy.jpg")
rend5 = ImageTk.PhotoImage(load5.resize((1366,768)))
load6 = Image.open("./images/marriage.jpg")
rend6 = ImageTk.PhotoImage(load6.resize((1366,768)))
main.geometry("1500x1000")



def find():
    
    frname=name1.get()
    toname=name2.get()
    lena=len(name1.get())
    lenb=len(name2.get())
    a=list(frname.lower())
    b=list(toname.lower())
    print(a)
    print(b)
    
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==b[j]):
                a[i]='#'
                b[j]='#'
    count=0
    for i in a:
        if(i!='#'):
            count+=1
    for i in b:
        if(i!='#'):
            count+=1
    #print(count)
    r=['F','L','A','M','E','S']
    a=len(r)
    key=1
    index=0
    count1=0
    for i in range(1,10000):
        if key==count*5+1:
            break
        if index==a:
            index=0
        if(r[index]!='#'):
            if key%count==0 :
                r[index]='#'
            key+=1
        index+=1
    for i in r:
        if i!='#':
            relate=i
    relatedict={"F":"Friend","L":"Lover","A":"Affection","M":"Marriage","E":"Enemy","S":"Sibling"}
    print(relate,"\n",count,"\n",r)
    print("\n\nRelation ship status:",relatedict[relate],"\n\n")
    frame1=Frame(main,height=1500,width=1000,bg="gray")
    if(relatedict[relate]=='Sibling'):
        img=Label(frame1,image=rend1)
        img.pack(fill=BOTH)
    elif relatedict[relate]=='Lover':
        img=Label(frame1,image=rend2)
        img.pack(fill=BOTH)
    elif relatedict[relate]=='Friend':
        img=Label(frame1,image=rend3)
        img.pack(fill=BOTH)
    elif relatedict[relate]=='Affection':
        img=Label(frame1,image=rend4)
        img.pack(fill=BOTH)
    elif relatedict[relate]=='Marriage':
        img=Label(frame1,image=rend6)
        img.pack(fill=BOTH)
    elif relatedict[relate]=='Enemy':
        img=Label(frame1,image=rend5)
        img.pack(fill=BOTH)
    def del1():
      frame1.destroy()
    but=Button(frame1,text='return',command=del1,fg="black").place(x=20,y=20)
    frame1.place(x=0,y=0)
    
    entry_label=Label(main,text=relatedict[relate],font=(text_font,25),fg="black").place(x=625,y=500)
def main_page():
      frame=Frame(main,height=1000,width=1500,bg="gray")
      img=Label(frame,image=rend).pack(fill=BOTH)
      
      nameb=Entry(frame,font=(text_font,20),textvariable=name1).place(x=250,y=120)

      nameg=Entry(frame,font=(text_font,20),textvariable=name2).place(x=800,y=120)
      find_button=Button(frame,font=(text_font,20),text="Find",fg="black",command=find).place(x=625,y=120)
      frame.place(x=0,y=0)
main_page()
main.mainloop()
