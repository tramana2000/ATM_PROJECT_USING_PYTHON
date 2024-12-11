from tkinter import *
window=Tk()

window.config(background='black')
#************************************************frame declaration****************************************************#
def show_frame1(frame):
   frame.tkraise()
   frame.grid(row=0,rowspan=4,column=1,columnspan=2,sticky='nsew')
frame1=Frame(window,bg='black')

frame2=Frame(window,bg='yellow')
frame3=Frame(window,bg='pink')
frame4=Frame(window,bg='black')
frame5=Frame(window,bg='black')
frame6=Frame(window,bg='pink')
frame7=Frame(window,bg='black')
frame8=Frame(window,bg='black')
frame9=Frame(window,bg='black')
frame10=Frame(window,bg='black')
frame11=Frame(window,bg='black')
frame12=Frame(window,bg='black')
frame13=Frame(window,bg='black')
frame14=Frame(window,bg='black')
frame15=Frame(window,bg='black')
frame16=Frame(window,bg='black')
frame17=Frame(window,bg='black')
frame18=Frame(window,bg='black')
frame19=Frame(window,bg='black')
frame20=Frame(window,bg='black')
frame21=Frame(window,bg='black')
frame22=Frame(window,bg='black')
frame23=Frame(window,bg='black')
frame24=Frame(window,bg='black')
frame25=Frame(window,bg='black')
frame26=Frame(window,bg='black')
frame27=Frame(window,bg='black')
frame28=Frame(window,bg='black')
frame29=Frame(window,bg='black')
frame30=Frame(window,bg='black')
show_frame1(frame1)
#frame3=Frame(window)


#**********************************************************************************************************************#
amountdeposited=0
amounttransfered=0
names=['mahesh','ravi','kishore']
account_numbers=[202177,22356,31541]
ifsc_code=['sbin11545','sbin1145213','andb216453']
Type_of_account=['current','savings','salaried']
ATM_card_number=[12102001,12102002,12102003]
ATM_pin=[0000,1111,2222]
account_opened_date=['03-06-2002','02-03-2009','03-08-2015']
branch=['galivedu-516267','rayachoti-25364','chitoor-58951']
password=['1234','2211','3356']
balance=[1000,1500,2000]
#**********************************************************************************************************************#


def start():
    show_frame1(frame1)
    frame1.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
#***************************************************enter**************************************************************#
def show_frame():
    global password
    global userindex
    pin_no=frame1_entry.get()

    for i in password:
       if pin_no==i:
          show_frame1(frame2)
          frame2.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
          userindex=password.index(pin_no)
          break
       else:
         show_frame1(frame3)
         frame3.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
    else:
       show_frame1(frame4)
       frame4.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
#*****************************************************cancel**********************************************************#
def cancel():
    global operator
    operator = ""
    InputText.set("")
    show_frame1(frame1)
    frame1.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
    button_enter.config(command=show_frame)
#*******************************************************clear ********************************************************#

def clear():
    global operator
    operator = ""
    InputText.set("")
#****************************************************cash deposit functions********************************************#
def cash_deposit():
    global operator
    operator = ""
    InputText.set("")
    show_frame1(frame5)
    frame5.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')

    button_enter.config(command=deposited_amount)


def deposited_amount():
    global amountdeposited

    amountdeposited=frame5_entry.get()
    if len(amountdeposited)>0:
      if int(str(amountdeposited))>0:
        show_frame1(frame6)
        frame6.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
        frame6_info.config(text="you deposited "+str(amountdeposited)+" successfully")
        frame6_info.pack()
      else:
        show_frame1(frame14)
        frame14.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
        frame14_info.config(text="enter valid amount")
        frame14_info.pack()
    else:
      show_frame1(frame14)
      frame14.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
      frame14_info.config(text="enter valid amount")
      frame14_info.pack()

#**********************************************************transfer amount********************************************#
def transfer_account():
    global operator
    operator = ""
    InputText.set("")
    show_frame1(frame7)
    frame7.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
    button_enter.config(command=transfer_amount)
def transfer_amount():

    accountnumber=frame7_entry.get()
    global operator
    operator = ""
    InputText.set("")
    if len(accountnumber)==6:
      show_frame1(frame8)
      frame8.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
      button_enter.config(command=transfered_amount)
    else:
        show_frame1(frame29)
        frame29.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
def transfered_amount():

    global amounttransfered
    amounttransfered=frame8_entry.get()
    if int(str(amounttransfered))>0:
      show_frame1(frame9)
      frame9.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
      frame9_info.config(text="you transfered "+str(amounttransfered)+" successfully")
      frame9_info.pack()
    else:
        show_frame1(frame30)
        frame30.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
#*********************************************check balance***********************************************************#
def checkbalance():
    global balance
    global userindex
    balanceshow=balance[userindex]
    show_frame1(frame10)
    frame1.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
    frame10_info.config(text="your   balance : "+str(balanceshow))
    frame10_info.pack()
#*************************************************aadhar link**********************************************************#
def account_no_to_link():
    global operator
    operator = ""
    InputText.set("")

    show_frame1(frame11)
    frame11.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')

    button_enter.config(command=aadharlink)
def aadharlink():
     global operator
     operator = ""
     InputText.set("")

     show_frame1(frame12)
     frame12.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
     button_enter.config(command=aadharlinked)
def aadharlinked():
     show_frame1(frame13)
     frame13.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
     frame13_info.config(text="your aadhar linked successfully")
     frame13_info.pack()
#*************************************************withdrawal*********************************************************#
def withdrawalamount():
    global operator
    operator = ""
    InputText.set("")
    show_frame1(frame15)
    frame15.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')

    button_enter.config(command=amountdebited)
def amountdebited():
    global debitedamount
    global balance
    global userindex
    debitedamount=frame15_entry.get()
    if len(debitedamount)>0 and int(str(debitedamount))>0:
      if int(str(debitedamount))<balance[userindex]:
        show_frame1(frame16)
        frame16.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
        frame16_info.config(text="you withdrawal amount "+str(debitedamount)+" is successful")
        frame16_info.pack()
      else:
        show_frame1(frame17)
        frame17.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
        frame17_info.config(text="you dont have sufficient balance to withdraw")
        frame17_info.pack()
    else:
      show_frame1(frame17)
      frame17.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
      frame17_info.config(text="enter valid amount")
      frame17_info.pack()
#******************************************account information********************************************************#
def account_information():
    global userindex
    global account_numbers
    global password
    global names
    global ifsc_code
    global Type_of_account
    global account_opened_date
    global branch
    global ATM_card_number
    global balance
    show_frame1(frame18)
    frame18.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
    frame18_info.config(text="username: "+str(names[userindex])+'\n''password: '+str(password[userindex])+'\n'
                        'ac_no: '+str(account_numbers[userindex])+'\n''ifsc code: '+str(ifsc_code[userindex])+'\n'
                        'account type: '+str(Type_of_account[userindex])+'\n'
                        'ac. opened date: '+str(account_opened_date[userindex])+'\n'
                        'branch: '+branch[userindex]+'\n''ATM number: '+str(ATM_card_number[userindex])+'\n'
                        'account balance: '+str(balance[userindex]))
    frame18_info.pack()
#*********************************************new pin generation******************************************************
def new_pin():
    global operator
    operator = ""
    InputText.set("")
    show_frame1(frame19)
    frame19.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')

    button_enter.config(command=pin_generation)
def pin_generation():
    global ATM_card_number
    global userindex
    global ATM_pin
    card_number=frame19_entry.get()
    if int(str(card_number))==ATM_card_number[userindex]:
        global operator
        operator = ""
        InputText.set("")
        show_frame1(frame20)
        frame20.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
        button_enter.config(command=sendotp)
    else:
        show_frame1(frame28)
        frame28.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')


def sendotp():
       otp=frame20_entry.get()
       if len(str(otp))==6:
         show_frame1(frame21)
         frame21.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
       else:
         show_frame1(frame22)
         frame22.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')

#*************************************************pin change**********************************************************#
def pin_change():
    global operator
    operator = ""
    InputText.set("")
    show_frame1(frame23)
    frame23.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')

    button_enter.config(command=new_pin_enter)
def new_pin_enter():
    global ATM_pin
    global userindex
    old_pin=frame23_entry.get()
    if int(str(old_pin))==ATM_pin[userindex]:

        global operator
        operator = ""
        InputText.set("")
        show_frame1(frame24)
        frame24.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
        button_enter.config(command=changedsuccessfully)
    else:
      show_frame1(frame25)
      frame25.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
def changedsuccessfully():
    newpin=frame24_entry.get()
    if len(newpin)==4:
        show_frame1(frame26)
        frame26.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
    else:
        show_frame1(frame27)
        frame27.grid(row=0, rowspan=4, column=1, columnspan=2, sticky='nsew')
#********************************************button function***********************************************************#
def ClickButton(char):
    global operator
    operator += str(char)
    InputText.set(operator)
operator=""
InputText = StringVar()
#**************************************************frame1*************************************************************#
frame1_info=Label(frame1,height=16,width=36,text='WELCOME\nTO\nATM\n\n\nenter your password:',bd=10,bg='black',fg='red',relief=RIDGE)
frame1_info.pack(side=TOP)
frame1_entry=Entry(frame1,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame1_entry.pack(side=BOTTOM)
#**************************************************frame2**************************************************************#
frame2_text=Label(frame2,height=19,
                  text='\ncash deposit\t\t              withdrawal' + '\n\n'
                       ' \n\n\ntransfer funds\t\taccount information' + '\n\n'
                       '\n\n\nBalance enquiry\t\tNew pin generation' + '\n\n'
                       '\n\n\nlink aadhar \t\t             PIN change' + '\n\n',
                                bd=10,bg='black',fg='red',relief=RIDGE)
frame2_text.pack()
#*******************************************************frame3*********************************************************#
frame3_text=Label(frame3,text='\n\nyou entered wrong password',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame3_text.place(x=0,y=0)
#**********************************************************************************************************************#
frame4_text=Label(frame4,text='\n\nplease enter valid password',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame4_text.place(x=0,y=0)
#****************************************************frame5************************************************************#
frame5_info=Label(frame5,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter amount to deposit:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame5_info.pack(side=TOP)
frame5_entry=Entry(frame5,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame5_entry.pack(side=BOTTOM)
#*****************************************************frame6**********************************************************#
frame6_info=Label(frame6,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#frame6_info.pack()
frame14_info=Label(frame14,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#**************************************************transfer amount*****************************************************#
frame7_info=Label(frame7,height=16,width=36,
                  text='\n\n\n\n\n\n\n\n\n\nEnter account number to which account \nyou want to transfer:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame7_info.pack(side=TOP)
frame7_entry=Entry(frame7,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame7_entry.pack(side=BOTTOM)
frame8_info=Label(frame8,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter amount to transfer:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame8_info.pack(side=TOP)
frame8_entry=Entry(frame8,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame8_entry.pack(side=BOTTOM)
frame29_text=Label(frame29,text='\n\nplease enter valid account number',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame29_text.place(x=0,y=0)
frame30_text=Label(frame30,text='\n\nplease enter valid amount',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame30_text.place(x=0,y=0)
#*******************************************************frame9******************************************************#
frame9_info=Label(frame9,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#***************************************************check balance frames***********************************************#
frame10_info=Label(frame10,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#*********************************************************frame11*****************************************************#
frame11_info=Label(frame11,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter account number to link aadhar:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame11_info.pack(side=TOP)
frame11_entry=Entry(frame11,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame11_entry.pack(side=BOTTOM)
#********************************************************frame12******************************************************#
frame12_info=Label(frame12,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter aadhar number to link:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame12_info.pack(side=TOP)
frame12_entry=Entry(frame12,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame12_entry.pack(side=BOTTOM)
#********************************************************aadhar link******************************************************#
frame13_info=Label(frame13,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#***************************************************cash withdrawal****************************************************#
frame15_info=Label(frame15,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter amount to withdrawal:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame15_info.pack(side=TOP)
frame15_entry=Entry(frame15,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame15_entry.pack(side=BOTTOM)
frame16_info=Label(frame16,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#frame6_info.pack()
frame17_info=Label(frame17,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#******************************************account information*******************************************************#
frame18_info=Label(frame18,height=19,width=36,bg='black',fg='red',bd=10,relief=RIDGE)
#***********************************************new pin generation****************************************************#
frame19_info=Label(frame19,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter ATM card number:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame19_info.pack(side=TOP)
frame19_entry=Entry(frame19,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame19_entry.pack(side=BOTTOM)
frame20_info=Label(frame20,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter OTP send to mobile number:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame20_info.pack(side=TOP)
frame20_entry=Entry(frame20,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame20_entry.pack(side=BOTTOM)
frame21_text=Label(frame21,text='\n\nyour password sent to your\n registred mobile number',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame21_text.place(x=0,y=0)
frame22_text=Label(frame22,text='\n\nenter valid OTP',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame22_text.place(x=0,y=0)

#***********************************************PIN change*************************************************#
frame23_info=Label(frame23,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter old pin:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame23_info.pack(side=TOP)
frame23_entry=Entry(frame23,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame23_entry.pack(side=BOTTOM)
frame24_info=Label(frame24,height=16,width=36,text='\n\n\n\n\n\n\n\n\n\nEnter new password what you want:',
                  bd=10,bg='black',fg='red',relief=RIDGE)
frame24_info.pack(side=TOP)
frame24_entry=Entry(frame24,bg='blue',width=36,bd=10,textvariable=InputText,fg='red',font=('arial',9,'bold'))
frame24_entry.pack(side=BOTTOM)
frame25_text=Label(frame25,text='\n\nyou entered wrong password',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame25_text.place(x=0,y=0)
frame26_text=Label(frame26,text='\n\nyour pin changed successfully',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame26_text.place(x=0,y=0)
frame27_text=Label(frame27,text='\n\nEnter valid pin',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame27_text.place(x=0,y=0)
frame28_text=Label(frame28,text='\n\nEnter valid ATM card number',
                  height=19,width=36,bg='black',bd=10,fg='red',relief=RIDGE)
frame28_text.place(x=0,y=0)
 #***********************************************************buttons***************************************************#
image1=PhotoImage(file='one.png')
image2=PhotoImage(file='two.png')
image3=PhotoImage(file='three.png')
image4=PhotoImage(file='four.png')
image5=PhotoImage(file='five.png')
image6=PhotoImage(file='six.png')
image7=PhotoImage(file='seven.png')
image8=PhotoImage(file='eight.png')
image9=PhotoImage(file='nine.png')
image10=PhotoImage(file='zero.png')
image11=PhotoImage(file='lArrow.png')
image12=PhotoImage(file='rArrow.png')
image13=PhotoImage(file='enter.png')
image14=PhotoImage(file='clear.png')
image15=PhotoImage(file='cancel.png')
image16=PhotoImage(file='empty.png')
#*********************************************************************************************************************#
button1=Button(window,command=lambda:ClickButton('1'),image=image1)
button1.grid(row=4, column=0, sticky="nsew")
button2=Button(window,image=image2,command=lambda:ClickButton('2'))
button2.grid(row=4, column=1, sticky="nsew")
button3=Button(window,image=image3,command=lambda:ClickButton('3'))
button3.grid(row=4, column=2, sticky="nsew")
button4=Button(window,image=image4,command=lambda:ClickButton('4'))
button4.grid(row=5, column=0, sticky="nsew")
button5=Button(window,image=image5,command=lambda:ClickButton('5'))
button5.grid(row=5, column=1, sticky="nsew")
button6=Button(window,image=image6,command=lambda:ClickButton('6'))
button6.grid(row=5, column=2, sticky="nsew")
button7=Button(window,image=image7,command=lambda:ClickButton('7'))
button7.grid(row=6, column=0, sticky="nsew")
button8=Button(window,image=image8,command=lambda:ClickButton('8'))
button8.grid(row=6, column=1, sticky="nsew")
button9=Button(window,image=image9,command=lambda:ClickButton('9'))
button9.grid(row=6, column=2, sticky="nsew")
button0=Button(window,image=image10,command=lambda:ClickButton('0'))
button0.grid(row=7, column=1, sticky="nsew")

button11=Button(window,image=image16,command=lambda:ClickButton('*'))
button11.grid(row=7, column=0, sticky="nsew")
button12=Button(window,image=image16,command=lambda:ClickButton('#'))
button12.grid(row=7, column=2, sticky="nsew")
#***********************************************>>>>>>>>>>>>>>>>***********************************************
button17=Button(window,image=image11,command=cash_deposit)
button17.grid(row=0, column=0, sticky="nsew")
button18=Button(window,image=image11,command=transfer_account)
button18.grid(row=1, column=0, sticky="nsew")
button19=Button(window,image=image11,command=checkbalance)
button19.grid(row=2, column=0, sticky="nsew")
button20=Button(window,image=image11,command=account_no_to_link)
button20.grid(row=3, column=0, sticky="nsew")
#*************************************************<<<<<<<<<<<**********************************************************#
button21=Button(window,image=image12,command=withdrawalamount)
button21.grid(row=0, column=3, sticky="nsew")
button22=Button(window,image=image12,command=account_information)
button22.grid(row=1, column=3, sticky="nsew")
button23=Button(window,image=image12,command=new_pin)
button23.grid(row=2, column=3, sticky="nsew")
button24=Button(window,image=image12,command=pin_change)
button24.grid(row=3, column=3, sticky="nsew")
#**********************************************************************************************************************#
button_cancel=Button(window,image=image15,command=cancel)
button_cancel.grid(row=4, column=3, sticky="nsew")
button_clear=Button(window,image=image14,command=clear)
button_clear.grid(row=5, column=3, sticky="nsew")
button_enter=Button(window,image=image13,command=show_frame)
button_enter.grid(row=6, column=3, sticky="nsew")
button_start=Button(window,image=image16)
button_start.grid(row=7, column=3, sticky="nsew")

#*****************************************************************grid lines*******************************************#

#*********************************************************************************************************************#
window.mainloop()
