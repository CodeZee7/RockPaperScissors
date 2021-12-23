'''

This script was coded by, and belongs to:

        CodeZee - Zeeshan Ibrahim

'''

#import necessary modules
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
#pillow needs to be pip installed
from PIL import ImageTk, Image


#initilaise the scores
user_score=0
cpu_score=0

def show_frame(frame):
    frame.tkraise()
    
def exitApp():
    window.destroy()
    exit()
    
def restart():
    show_frame(startFrame)
    
def loss_message():
    l = messagebox.showinfo("You lost!", "CPU was the first to 3")
    global user_score, cpu_score
    user_score, cpu_score = 0,0
    scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
    bgFrame.config(image=i0)
    show_frame(endFrame)
        
def win_message():
    w = messagebox.showinfo("You won!", "You were the first to 3")
    global user_score, cpu_score
    user_score, cpu_score = 0,0
    scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
    bgFrame.config(image=i0)
    show_frame(endFrame)

def duel(user_option):
    global user_score, cpu_score

    #randomise cpu's choice
    cpu_number = random.randint(0,2)
    if cpu_number == 0:
        cpu_option = "rock"
        time.sleep(1)

        #display image
        bgFrame.config(image=i1)
    elif cpu_number == 1:
        cpu_option = "paper"
        time.sleep(1)
        bgFrame.config(image=i2)
    else:
        cpu_option = "scissors"
        time.sleep(1)
        bgFrame.config(image=i3)


    #check if draw
    if user_option == cpu_option:
        messagebox.showinfo("Draw!", "No one gets a point.")

#===================compares all combinations and outputs who wins====================
    elif user_option == "rock" and cpu_option == "paper":
        
        messagebox.showinfo("Paper beats rock.", "CPU gets a point.")
        cpu_score += 1
        scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
        if user_score==3:
            win_message()
        if cpu_score==3:
            loss_message()
        
    elif user_option == "rock" and cpu_option == "scissors":
        
        messagebox.showinfo("Rock beats scissors.", "You get a point.")
        user_score += 1
        scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
        if user_score==3:
            win_message()
        if cpu_score==3:
            loss_message()
        
    elif user_option == "paper" and cpu_option == "scissors":
        
        messagebox.showinfo("Scissors beats paper.", "CPU gets a point.")
        cpu_score += 1
        scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
        if user_score==3:
            win_message()
        if cpu_score==3:
            loss_message()
        
    elif user_option == "paper" and cpu_option == "rock":
        
        messagebox.showinfo("Paper beats rock.", "You get a point.")
        user_score += 1
        scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
        if user_score==3:
            win_message()
        if cpu_score==3:
            loss_message()
        
    elif user_option == "scissors" and cpu_option == "rock":
        
        messagebox.showinfo("Rock beats scissors.", "CPU gets a point.")
        cpu_score += 1
        scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
        if user_score==3:
            win_message()
        if cpu_score==3:
            loss_message()
        
    elif user_option == "scissors" and cpu_option == "paper":
        
        messagebox.showinfo("Scissors beats paper.", "You get a point.")
        user_score += 1
        scorelbl.config(text=f"YOU : {user_score} - {cpu_score} : CPU")
        if user_score==3:
            win_message()
        if cpu_score==3:
            loss_message()




    
#initialise window
window = Tk()
window.title("Rock, Paper, Scissors!")
window.geometry("700x700+100+50")
window.resizable(False, False)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


#===========================convert all images into photo images===================
img0 = Image.open("blank.png")
img0 = img0.resize((450,450))
i0 = ImageTk.PhotoImage(img0)

img1 = Image.open("rock.png")
img1 = img1.resize((450,450))
i1 = ImageTk.PhotoImage(img1)

img2 = Image.open("paper.png")
img2 = img2.resize((450,450))
i2 = ImageTk.PhotoImage(img2)

img3 = Image.open("scissors.png")
img3 = img3.resize((450,450))
i3 = ImageTk.PhotoImage(img3)


#==================================starting page=====================
startFrame = Frame(window, bg="white")

titlelbl = Label(startFrame, text="Rock, Paper, Scissors!\nFirst to 3", font=("arial",45,"bold"), bg="white", fg="black")
titlelbl.pack(pady=(10, 200))

startBtn = Button(startFrame, text="Start", font=("arial",20,"bold"), width=12, height=2, command=lambda : show_frame(gameFrame))
startBtn.pack()

instruction = Label(startFrame, bg="white", text="1)Choose your option.\n2)Wait for the CPU to make a choice.\n3)The first to 3 wins.", font=("arial",30))
instruction.pack(side=BOTTOM, pady=(0,20))

#===================================end page=========================
endFrame = Frame(window, bg="white")

playAgain = Button(endFrame, text="Play Again", font=("arial",20,"bold"), width=20, height=3, command=restart)
playAgain.pack(pady=(150,0))

exitbtn = Button(endFrame, text="Exit", font=("arial",20,"bold"), width=20, height=3, command=exitApp)
exitbtn.pack(pady=(0,150), side=BOTTOM)


#======================================main game page========================
gameFrame = Frame(window, bg="white")

scorelbl = Label(gameFrame, text=f"YOU : {user_score} - {cpu_score} : CPU", font=("arial",50,"bold"), bg="white", fg="black")
scorelbl.pack(pady=10)



bgFrame = Label(gameFrame, bg="white", image=i0)
bgFrame.pack()

btnFrame = Frame(gameFrame, bg="white")
btnFrame.pack(pady=10)

rockBtn = Button(btnFrame, text="Rock", font=("arial",20,"bold"), width=12, height=2, command = lambda : duel("rock"))
rockBtn.pack(side=LEFT, padx=5)

paperBtn = Button(btnFrame, text="Paper", font=("arial",20,"bold"), width=12, height=2, command = lambda : duel("paper"))
paperBtn.pack(side=LEFT, padx=5)

scissorsBtn = Button(btnFrame, text="Scissors", font=("arial",20,"bold"), width=12, height=2, command = lambda : duel("scissors"))
scissorsBtn.pack(side=LEFT, padx=5)

#grid all frames to window
for frame in (startFrame, gameFrame, endFrame):
    frame.grid(row=0, column=0, sticky="nsew")

#push the first frame to top
show_frame(startFrame)

window.mainloop()
