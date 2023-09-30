from tkinter import *
from tkinter import messagebox
import random

words=['cinnamon','ferocious',"ineffable","sycophant","obfuscate","cacophony","perseverance",
"perseverance", "ubiquitous", "conundrum", "serenity", "meticulous", "eloquent", "confluence",
"resilience", "exuberant", "innovative","star", "ocean", "mountain", "pizza", "wobble", "whippersnapper",
"dog", "cat", "tree", "ball", "sun", "book", "house", "blue", "rain", "run","python", "java", "c++", "ruby",
"javascript","alice", "bob", "emily", "david", "developer", "engineer", "designer", "manager", "analyst",
"teacher", "doctor", "nurse", "chef", "artist", "lawyer", "student", "professor", "associate professor",
"assistant professor", "lecturer", "ph.d.", "mba", "software", "hardware", "database", "network", "security", "ai",
"machine learning", "data science", "web development", "frontend", "backend", "cybersecurity", "devops", "blockchain",
"scrum master", "product manager", "ux designer", "ui developer", "data analyst", "computer science", "project manager",
"new delhi", "mumbai", "bangalore", "kolkata", "chennai", "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow",
"chandigarh", "bhopal", "indore", "kochi", "surat", "varanasi", "goa", "nagpur", "coimbatore", "amritsar"]

sliderwords = ''
count = 0

def labelSlider():
    global count,sliderwords
    text='Test Your Typing Speed'
    if(count>=len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    fontlabel.config(text=sliderwords)
    fontlabel.after(250,labelSlider)

def game_timer():
    global timeleft,i
    if timeleft<11:
        timelabelcount.config(fg='red')
    if timeleft>0:
        timeleft-=1
        timelabelcount.config(text=timeleft)
        timelabelcount.after(1000, game_timer)
    else:
        global score,miss,poorLabel,poor1Label
        wordEntry.config(state=DISABLED)
        result=score-miss
        gameplay_detaillabel.config(text=f'Correct Words= {score} \nWrong Words= {miss}\nFinal Score= {result}')
        if result<=0:
            accuracy_label.config(text='accuracy = 0')
        else:
            accuracy_label.config(text=f'accuracy = {result*100/(score+miss)}')

        if result<=10:
            poorLabel.config(image=poorpic)
            poor1Label.config(image=poorpic)


        elif 17<result>10:
            poorLabel.config(image=goodpic)
            poor1Label.config(image=goodpic)

        elif result>=17:
            poorLabel.config(image=propic)
            poor1Label.config(image=propic)


        res=messagebox.askyesno("Speed Game",'Do You Want To Play Again?')
        if res:
            score=0
            timeleft=60
            miss=0
            i=0
            timelabelcount.config(fg='black')
            wordEntry.config(state=NORMAL)
            poorLabel.place_forget()
            poor1Label.place_forget()
            timelabelcount.config(text=timeleft)
            scorelabelcount.config(text=i)
            wordlabel.config(text=words[0])
            gameplay_detaillabel.config(text='Type Word And Hit Enter')

        else:
            root.destroy()



score=0
miss=0
i=0
def play_game(event):


    global timeleft,score,miss,i
    i += 1
    scorelabelcount.config(text=i)
    if timeleft==60:
        game_timer()
    gameplay_detaillabel.config(text='')
    if wordEntry.get()==wordlabel['text']:

        score+=1

    else:
        miss+=1

    random.shuffle(words)
    wordlabel.config(text=words[0])
    wordEntry.delete(0,END)





root=Tk()
root.geometry('700x700+250+30')
root.configure(bg='seashell2')
root.title("Typing Speed Tester")
root.iconbitmap('icon.ico')

#variables
timeleft=60

logopic=PhotoImage(file='logo.png')
piclabel=Label(root,image=logopic,bg='seashell2')
piclabel.place(x=220,y=50)

fontlabel=Label(root,text="",font=('arial',25,'italic bold'),
                bg='seashell2',fg='indianred',width=35)
fontlabel.place(x=0,y=10)
labelSlider()
random.shuffle(words)
wordlabel=Label(root,text=words[0],font=('cooper black',28,'italic bold'),bg='seashell2')
wordlabel.place(x=350,y=350,anchor=CENTER )

scorelabel=Label(root,text='Words',font=('castellar',28,' bold'),bg='seashell2')
scorelabel.place(x=30,y=100)

scorelabelcount=Label(root,text=i,font=('castellar',28,'italic bold'),bg='seashell2')
scorelabelcount.place(x=80,y=180)

timelabel=Label(root,text='Timer',font=('castellar',28,'bold'),bg='seashell2')
timelabel.place(x=510,y=100)

timelabelcount=Label(root,text=timeleft,font=('castellar',28,'italic bold'),bg='seashell2')
timelabelcount.place(x=550,y=180)

gameplay_detaillabel=Label(root,text='Type Word And Hit Enter',font=('chiller',30,'italic bold'),
                           bg='seashell2',fg='IndianRed')
gameplay_detaillabel.place(x=210,y=460)

accuracy_label=Label(root,text='',font=('chiller',30,'italic bold'),
                           bg='seashell2',fg='IndianRed')
accuracy_label.place(x=210,y=600)

wordEntry=Entry(root,font=('arial',25,'italic bold'),bd='10',justify=CENTER)
wordEntry.place(x=160,y=390)
wordEntry.focus_set()

poorpic = PhotoImage(file='poor.png')

goodpic = PhotoImage(file='good.png')

propic = PhotoImage(file='pro.png')

poorLabel = Label(root,bg='seashell2')
poorLabel.place(x=80, y=490)


poor1Label = Label(root,bg='seashell2')
poor1Label.place(x=540, y=490)

root.bind('<Return>',play_game)
root.mainloop()