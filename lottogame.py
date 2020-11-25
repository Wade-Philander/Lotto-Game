# Wade Philander
# EOM task, Lottery 
# Due date 30 Nov 2020

import random
from random import sample
import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import *


window = Tk()
window.title("Lottery App")
window.geometry('550x350')

time=datetime.now()

time_lb= Label(window, text=time.strftime("%d/%m/%y %H:%M"))
time_lb.place(x=220, y=250)

def getting_user_input():

    root = Tk()
    root.title("Enter your lottery Numbers")
    root.geometry('700x250')

    user_nums = []

    user_nums_en = Entry(root)
    user_nums_en.place(x=280 ,y=70)
    user_nums_lb = Label(root, text="PLEASE ENTER YOUR LUCKY 6 LOTTERY NUMBERS USING SPACES BETWEEN ")
    user_nums_lb.place(x=100, y=5)

    def chec():
        
        try:
            y = user_nums_en.get().split(" ")
            for i in range(6):
                #x = int(input=("enter user lottery number"))
                x = y[i]
                user_nums.append(int(x))
            print(user_nums)

        except:
            messagebox.showerror("ERROR","PLEASE FOLLOW ABOVE INSTRUCTION")

        count=0
        for i in user_nums:
            if i in lot_num:
                count+=1
                print(count)

        lb1 = Label(root)
        lb1.place( x=185 , y=180)
        
        lb2 = Label(root)
        
        if count ==0:
            lb1.config(text="Your numbers are, " + str(sorted(user_nums)) + "\n You have won got 0 correct, \n" + "lotto number are: " + str(sorted(lot_num)) + "\n You won nothing!"+ "\n" + time.strftime("%d/%m/%y %H:%M"))

        elif count ==1:
            lb1.config(text="Your numbers are, " + str(sorted(user_nums)) + "\n You have won got 1 correct, \n" + "lotto number are: " + str(sorted(lot_num))  + "\n You won nothing!"+ "\n" + time.strftime("%d/%m/%y %H:%M"))
        elif count ==2:
            lb1.config(text="Your numbers are, " + str(sorted(user_nums)) + "\n You have won got 2 correct, \n" + "lotto number are: " + str(sorted(lot_num))  + "\n Well done, you won a prize of R20.00" + "\n" + time.strftime("%d/%m/%y %H:%M"))
            
        elif count ==3:
            lb1.config(text="Your numbers are, " + str(sorted(user_nums)) + "\n You have won got 3 correct, \n" + "lotto number are: " + str(sorted(lot_num))  + "\n Well done, you  won, R100.50!" + "\n" + time.strftime("%d/%m/%y %H:%M"))
            
        elif count ==4:
            lb1.config(text="Your numbers are, " + str(sorted(user_nums)) + "\n You have won got 4 correct, \n" + "lotto number are: " + str(sorted(lot_num))  + "\n Siesa! you won R2,384.00!" + "\n" + time.strftime("%d/%m/%y %H:%M"))
            
        elif count == 5:
            lb1.config(text="Your numbers are, " + str(sorted(user_nums)) + "\n You have won got 5 correct, \n" + "lotto number are: " + str(sorted(lot_num))  + "\n Wow! so close, but you have won a huge amount of 8,584.00!" + "\n" + time.strftime("%d/%m/%y %H:%M"))
            
        elif count == 6:
            lb1.config(text="Your numbers are, " + str(sorted(user_nums)) + "\n You have won got 6 correct, \n" + "lotto number are: " + str(sorted(lot_num))  + "\n you have won a whopping amount of 10 000 000!" + "\n" + time.strftime("%d/%m/%y %H:%M"))
            messagebox.showinfo("WINNER,WINNER, CHICKEN DINNER.", "You got all Correct and won 10 Million Rand")

        f = open("result.txt", "w+")
        f.write(lb1.cget("text"))
        f.close()

        f=open("result.txt", "a+")
        f.write(lb1.cget("text"))
        f.close()

    btn = Button(root, text="CHECK LOTTERY RESULT", command=chec)
    btn.place(x=270, y=120)


    root.mainloop()

# ************************************** checks if player is over 18 yrs old ***************************

lot_num = sample(range(1,50),6)   # Generate random 6 numbers 
print(lot_num)



def age():
    player = player_entry.get()
    
    try:
        age = int(age_en.get())
        if age >= 18:                                               
            #print("Welcome to the loto draw", player)
            getting_user_input()

        else:
            messagebox.showerror("Error","You are underage, go play housie")


    except ValueError:
        messagebox.showerror("Error","Only use numbers for age")


#************************************************************ TKINTER *********************************************************

player_entry = Entry(window)
player_entry.place(x=250, y=100)
player_lb = Label(window, text="Enter your full name")
player_lb.place(x=100, y=100)

age_en = Entry(window)
age_en.place( x=250, y=150)
age_lb = Label(window, text="Please enter your age")
age_lb.place( x=100, y=150)

check_btn = Button(window, text="Check credentials", command=age)
check_btn.place( x=200, y=200)




window.mainloop()
