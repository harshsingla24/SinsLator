from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob




window1=Tk()
window1.title('Sins Lator')
window1.geometry('1280x435+150+250')


def label_change():
    c=combo1.get()
    c1=combo2.get()
    y=("From:-",c)
    z=("To:-",c1)
    label1.configure(text=y)
    label2.configure(text=z)
    window1.after(1000,label_change)

def translate_function():
    global language
    try:
        text_=text1.get(1.0,END)
        c2=combo1.get()
        c3=combo2.get()
        if(text_):
            words=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=i
            words=words.translate(from_lang=lan,to=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","Try Later\n\nThank You!!!")
        

#icon
#image_icon=PhotoImage(file="iconphoto.png") 
image_icon=PhotoImage(file="13.png") 

window1.iconphoto(False,image_icon)

#arrow
arrow_image=PhotoImage(file="singlearrowpicture.png")
image_label=Label(window1,image=arrow_image,width=260)
image_label.place(x=500,y=165)





'''

Fonts:-

Playbill    #Size unadaptive
Symbol      #not readable
Sylfaen
Impact
Jokerman
segoe
Roboto
Elephant
RobotoV
'''

#Version Label
label_version=Label(window1,text='Version:-0.1.0.1',font='Impact 13 ',fg='black',bg='white',width=15,height=1,bd=4,relief=GROOVE)
label_version.place(x=1130,y=0)


#Title Label
label0=Label(window1,text='Language Translator ',font='Elephant 30 bold',fg='salmon',bg='ivory',width=18,bd=2,relief=GROOVE)
label0.place(x=400,y=5)

#Beta Label
label_beta=Label(window1,text='beta',font='Impact 13 ',fg='springgreen',bg='ivory',width=5,height=1,bd=0,relief=GROOVE)
label_beta.place(x=880,y=36)







language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()


combo1=ttk.Combobox(window1,values=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=60)
combo1.set("english")

label1=Label(window1,text='ENGLISH',font='Sylfaen 30 bold',bg='teal',width=18,bd=5,
             relief=GROOVE)
label1.place(x=10,y=90)


f=Frame(window1,bg='black',bd=5)
f.place(x=10,y=158,width=440,height=210)


text1=Text(f,font='Roboto 20',bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)


scrollbar1=Scrollbar(f)
scrollbar1.pack(side='right',fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)









combo2=ttk.Combobox(window1,values=languageV,font='RobotoV 14',state='r')
combo2.place(x=930,y=60)
combo2.set("hindi")


label2=Label(window1,text='ENGLISH',font='Sylfaen 30 bold',bg='teal',width=18,bd=5,
             relief=GROOVE)
label2.place(x=820,y=90)


f1=Frame(window1,bg='black',bd=5)
f1.place(x=820,y=158,width=440,height=210)

text2=Text(f1,font='Roboto 20',bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)


scrollbar2=Scrollbar(f1)
scrollbar2.pack(side='right',fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#Translate Button

b1=Button(window1,text='Translate',font='Roboto 15 bold',
          activebackground='gray',activeforeground='wheat',
          bg='gray',fg='black',cursor='hand2',bd=5,
          command=translate_function)
b1.place(x=570,y=320)




label_name=Label(window1,text='Made By:-\nHarsh Singla',font='Jokerman 15 bold',bg='salmon',fg='black',width=12,bd=3,relief=GROOVE)
label_name.place(x=1085,y=370)


'''
Colors
1. springgreen
2. ivory
3. salmon
4. gray
5. pink
6. wheat

'''


label_change()


window1.configure(bg="wheat")

window1.mainloop()
