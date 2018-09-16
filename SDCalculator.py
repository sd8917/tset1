from tkinter import *
root=Tk()


#use to input the data in entry field

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

# use to clear the entry field 

def button_clear():
    global operator
    operator= ""
    text_Input.set("")

#use to calculate the opertion and give the result

def btn_equal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""



root.title("SDCalculator")
operator= ""
text_Input=StringVar()


##########################################################################################################################################

text_entry=Entry(root,font=('arial',20,'bold'),bd=3,fg="black",bg="cyan",textvariable=text_Input ,insertwidth=5,justify="right")
text_entry.grid(columnspan=4)


#####################################################################################################################################

button_7 = Button(root,text="7",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(7))
button_7.grid(column=0)
button_8 = Button(root,text="8",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(8))
button_8.grid(column=1,row=1)
button_9 = Button(root,text="9",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(9))
button_9.grid(column=2,row=1)
button_add = Button(root,text="+",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick("+"))
button_add.grid(column=3,row=1)



###################################################################################################################################
button_6 = Button(root,text="6",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(6))
button_6.grid(column=0)
button_5 = Button(root,text="5",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(5))
button_5.grid(column=1,row=2)
button_4 = Button(root,text="4",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(4))
button_4.grid(column=2,row=2)
button_sub = Button(root,text="-",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick("-"))
button_sub.grid(column=3,row=2)



###########################################################################################################################
'''this is for 4th row key we use it !!! btnclick  declared above which are use in it and  padx-to pad in x direction ,
calculation'''

button_1 = Button(root,text="1",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(1))
button_1.grid(column=0)
button_2 = Button(root,text="2",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(2))
button_2.grid(column=1,row=3)
button_3 = Button(root,text="3",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(3))
button_3.grid(column=2,row=3)
button_mult = Button(root,text="*",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick("*"))
button_mult.grid(column=3,row=3)



############################################################################################################################
'''this is for 4th row key we use it !!! btnclear function declared above which are use in it and btn_equal is use to find the 
calculation'''

button_0 = Button(root,text="0",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick(0))
button_0.grid(column=0)
button_clear = Button(root,text="C",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=button_clear)
button_clear.grid(column=1,row=4)
button_equal = Button(root,text="=",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=btn_equal)
button_equal.grid(column=2,row=4)
button_div = Button(root,text="/",padx=18,pady=18,fg="black",font=('arial',20,'bold'),bd=3,command=lambda:btnClick("/"))
button_div.grid(column=3,row=4)


root.mainloop()