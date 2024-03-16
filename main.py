from tkinter import*
from tkinter import messagebox
import random
import os
##############################################
#functions
####################

if not os.path.exists('bills'):
    os.mkdir('bills')

def searchbill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnoentry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
        else:
            messagebox.showerror('Error', 'invalid bill no')

def cleararea():
    textarea.delete(1.0,END)
def savebill():
    res=messagebox.askyesno('Confirm','do you want to save the bill')
    if res:
        billcontent=textarea.get(1.0,END)
        file=open(f'bills/{billno}.txt','w')
        file.write(billcontent)
        file.close()
        messagebox.showinfo('Success','bill saved successfully')
def billarea():
    if nameentry.get()=='' or phoneentry.get()=='':
        messagebox.showerror('Error','Customer details required')
    elif cosmeticpriceentry.get()=='' and grocerypriceentry.get()=='' and colddrinkpriceentry.get()=='':
        messagebox.showerror('Error','no product selected')
    elif cosmeticpriceentry.get()=='0Rs' and grocerypriceentry.get()=='0Rs' and colddrinkpriceentry.get()=='0Rs':
        messagebox.showerror('Error', 'no product selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**WELCOME**')
        textarea.insert(END,'\n\nbill number :- '+str(billno))
        textarea.insert(END,'\n\ncutomer name :- '+str(nameentry.get()))
        textarea.insert(END,'\n\nphone no :- '+str(phoneentry.get()))
        textarea.insert(END,'\n\n=============================================')
        textarea.insert(END,'\nproduct\t\tquantity\t\tprice')
        textarea.insert(END, '\n==============================================')
        if bathentry.get()!='0':
            textarea.insert(END,'\nbath soap\t\t'+str(bathentry.get())+'\t\t'+str(soapvalue))

        textarea.insert(END, '\n----------------------------------------------')
        textarea.insert(END,'\ntotal bill :- '+str(totalp))
        textarea.insert(END, '\n----------------------------------------------')
        savebill()
def total():
    #cosmetic
    global billno
    billno = random.randint(1, 100)
    global soapvalue,totalp
    soapvalue=int(bathentry.get())*10
    facecreamvalue=int(facecreamentry.get())*20
    facewashvalue=int(fasewashentry.get())*30
    hairsprayvalue=int(hairsprayentry.get())*40
    hairgelvalue=int(hairgelentry.get())*50
    bodylotionvalue=int(bodylotionentry.get())*60
    totalpricecos=soapvalue+facecreamvalue+facewashvalue+hairsprayvalue+hairgelvalue+bodylotionvalue
    costax=totalpricecos*0.12
    cosmeticpriceentry.delete(0,END)
    cosmeticpriceentry.insert(0,str(totalpricecos)+'Rs')
    cosmetictaxpriceentry.delete(0,END)
    cosmetictaxpriceentry.insert(0,str(costax)+'Rs')

    ####grocery
    ricevalue=int(riceentry.get())*10
    dalvalue=int(dalentry.get())*20
    beanvalue=int(beansentry.get())*30
    breadvalue=int(breadentry.get())*40
    spicevalue=int(spicesentry.get())*50
    saltvalue=int(saltentry.get())*60
    totalpricegro=ricevalue+dalvalue+beanvalue+breadvalue+spicevalue+saltvalue
    grotax=totalpricegro*0.12
    grocerypriceentry.delete(0,END)
    grocerypriceentry.insert(0,str(totalpricegro)+'Rs')
    grocerytaxpriceentry.delete(0,END)
    grocerytaxpriceentry.insert(0,str(grotax)+'Rs')

    ####drinks
    cocovalue=int(cocoentry.get())*10
    mazavalue=int(mazaentry.get())*20
    slicevalue=int(sliceentry.get())*30
    appyvalue=int(appyentry.get())*40
    mrindavalue=int(mrindaentry.get())*50
    limcavalue=int(limcaentry.get())*60
    totalpricedrink=cocovalue+mazavalue+slicevalue+appyvalue+mrindavalue+limcavalue
    coldtax=totalpricedrink*0.12
    colddrinkpriceentry.delete(0,END)
    colddrinkpriceentry.insert(0,str(totalpricedrink)+'Rs')
    colddrinktaxpriceentry.delete(0,END)
    colddrinktaxpriceentry.insert(0,str(coldtax)+'Rs')
    totalp=totalpricedrink+totalpricegro+totalpricecos+costax+grotax+coldtax
##############################################
#gui
#############
root=Tk()
#to add title
root.title('Billing System')
#it is used to specify the size
root.geometry("1270x685")
#it is used to add icon
root.iconbitmap("icon.ico")
#we are creating label for heading
headinglabel=Label(root,text='Billing System',font=('calibri',30,'bold'),bg='gray',fg='white',bd=8,relief=SOLID)
headinglabel.pack(fill=X)
#
cusdetframe=LabelFrame(root,text='Customer Details',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
cusdetframe.pack(fill=X)

namelabel=Label(cusdetframe,text='Name',font=('calibri',15,'bold'),bg='gray',fg='white')
namelabel.grid(row=0,column=0,padx=20)

nameentry=Entry(cusdetframe,font=('arial',15),bd=7,width=18)
nameentry.grid(row=0,column=1,padx=8)

phonelabel=Label(cusdetframe,text='Phone Number',font=('calibri',15,'bold'),bg='gray',fg='white')
phonelabel.grid(row=0,column=2,padx=20,pady=2)

phoneentry=Entry(cusdetframe,font=('arial',15),bd=7,width=18)
phoneentry.grid(row=0,column=3,padx=8)

billnolabel=Label(cusdetframe,text='Bill No',font=('calibri',15,'bold'),bg='gray',fg='white')
billnolabel.grid(row=0,column=4,padx=20,pady=2)

billnoentry=Entry(cusdetframe,font=('arial',15),bd=7,width=18)
billnoentry.grid(row=0,column=5,padx=8)

searchbutton=Button(cusdetframe,text='Search',font=('arial',12,'bold'),bd=7,command=searchbill)
searchbutton.grid(row=0,column=6,padx=20,pady=8)


productsframe=Frame(root)
productsframe.pack()


cosmetframe=LabelFrame(productsframe,text='Cosmetics',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
cosmetframe.grid(row=0,column=0)

bathlabel=Label(cosmetframe,text='Bath Soap',font=('calibri',15,'bold'),bg='gray',fg='white')
bathlabel.grid(row=0,column=0,padx=10,pady=9,sticky='w')
bathentry=Entry(cosmetframe,font=('arial',15),bd=5,width=10)
bathentry.insert(0,0)
bathentry.grid(row=0,column=1,pady=9,padx=10)

facecreamlabel=Label(cosmetframe,text='face cream',font=('calibri',15,'bold'),bg='gray',fg='white')
facecreamlabel.grid(row=1,column=0,padx=10,pady=9,sticky='w')
facecreamentry=Entry(cosmetframe,font=('arial',15),bd=5,width=10)
facecreamentry.insert(0,0)
facecreamentry.grid(row=1,column=1,pady=9,padx=10)

fasewashlabel=Label(cosmetframe,text='fase wash',font=('calibri',15,'bold'),bg='gray',fg='white')
fasewashlabel.grid(row=2,column=0,padx=10,pady=9,sticky='w')
fasewashentry=Entry(cosmetframe,font=('arial',15),bd=5,width=10)
fasewashentry.insert(0,0)
fasewashentry.grid(row=2,column=1,pady=9,padx=10)

hairspraylabel=Label(cosmetframe,text='hair spray',font=('calibri',15,'bold'),bg='gray',fg='white')
hairspraylabel.grid(row=3,column=0,padx=10,pady=9,sticky='w')
hairsprayentry=Entry(cosmetframe,font=('arial',15),bd=5,width=10)
hairsprayentry.insert(0,0)
hairsprayentry.grid(row=3,column=1,pady=9,padx=10)

hairgellabel=Label(cosmetframe,text='hair gel',font=('calibri',15,'bold'),bg='gray',fg='white')
hairgellabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
hairgelentry=Entry(cosmetframe,font=('arial',15),bd=5,width=10)
hairgelentry.insert(0,0)
hairgelentry.grid(row=4,column=1,pady=9,padx=10)

bodylotionlabel=Label(cosmetframe,text='body lotion',font=('calibri',15,'bold'),bg='gray',fg='white')
bodylotionlabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
bodylotionentry=Entry(cosmetframe,font=('arial',15),bd=5,width=10)
bodylotionentry.insert(0,0)
bodylotionentry.grid(row=4,column=1,pady=9,padx=10)

##################
groceryframe=LabelFrame(productsframe,text='Grocery',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
groceryframe.grid(row=0,column=1)

dallabel=Label(groceryframe,text='Dal',font=('calibri',15,'bold'),bg='gray',fg='white')
dallabel.grid(row=0,column=0,padx=10,pady=9,sticky='w')
dalentry=Entry(groceryframe,font=('arial',15),bd=5,width=10)
dalentry.insert(0,0)
dalentry.grid(row=0,column=1,pady=9,padx=10)

ricelabel=Label(groceryframe,text='Rice',font=('calibri',15,'bold'),bg='gray',fg='white')
ricelabel.grid(row=1,column=0,padx=10,pady=9,sticky='w')
riceentry=Entry(groceryframe,font=('arial',15),bd=5,width=10)
riceentry.insert(0,0)
riceentry.grid(row=1,column=1,pady=9,padx=10)

beanslabel=Label(groceryframe,text='Beans',font=('calibri',15,'bold'),bg='gray',fg='white')
beanslabel.grid(row=2,column=0,padx=10,pady=9,sticky='w')
beansentry=Entry(groceryframe,font=('arial',15),bd=5,width=10)
beansentry.insert(0,0)
beansentry.grid(row=2,column=1,pady=9,padx=10)

breadlabel=Label(groceryframe,text='Bread',font=('calibri',15,'bold'),bg='gray',fg='white')
breadlabel.grid(row=3,column=0,padx=10,pady=9,sticky='w')
breadentry=Entry(groceryframe,font=('arial',15),bd=5,width=10)
breadentry.insert(0,0)
breadentry.grid(row=3,column=1,pady=9,padx=10)

spiceslabel=Label(groceryframe,text='Spices',font=('calibri',15,'bold'),bg='gray',fg='white')
spiceslabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
spicesentry=Entry(groceryframe,font=('arial',15),bd=5,width=10)
spicesentry.insert(0,0)
spicesentry.grid(row=4,column=1,pady=9,padx=10)

saltlabel=Label(groceryframe,text='Salt',font=('calibri',15,'bold'),bg='gray',fg='white')
saltlabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
saltentry=Entry(groceryframe,font=('arial',15),bd=5,width=10)
saltentry.insert(0,0)
saltentry.grid(row=4,column=1,pady=9,padx=10)



#########################
Colddrinkframe=LabelFrame(productsframe,text='Cold Drinks',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
Colddrinkframe.grid(row=0,column=2)

cocolabel=Label(Colddrinkframe,text='Coco cola',font=('calibri',15,'bold'),bg='gray',fg='white')
cocolabel.grid(row=0,column=0,padx=10,pady=9,sticky='w')
cocoentry=Entry(Colddrinkframe,font=('arial',15),bd=5,width=10)
cocoentry.insert(0,0)
cocoentry.grid(row=0,column=1,pady=9,padx=10)

mazalabel=Label(Colddrinkframe,text='Maza',font=('calibri',15,'bold'),bg='gray',fg='white')
mazalabel.grid(row=1,column=0,padx=10,pady=9,sticky='w')
mazaentry=Entry(Colddrinkframe,font=('arial',15),bd=5,width=10)
mazaentry.insert(0,0)
mazaentry.grid(row=1,column=1,pady=9,padx=10)

slicelabel=Label(Colddrinkframe,text='Slice',font=('calibri',15,'bold'),bg='gray',fg='white')
slicelabel.grid(row=2,column=0,padx=10,pady=9,sticky='w')
sliceentry=Entry(Colddrinkframe,font=('arial',15),bd=5,width=10)
sliceentry.insert(0,0)
sliceentry.grid(row=2,column=1,pady=9,padx=10)

appylabel=Label(Colddrinkframe,text='Appy',font=('calibri',15,'bold'),bg='gray',fg='white')
appylabel.grid(row=3,column=0,padx=10,pady=9,sticky='w')
appyentry=Entry(Colddrinkframe,font=('arial',15),bd=5,width=10)
appyentry.insert(0,0)
appyentry.grid(row=3,column=1,pady=9,padx=10)

mrindalabel=Label(Colddrinkframe,text='Mrinda',font=('calibri',15,'bold'),bg='gray',fg='white')
mrindalabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
mrindaentry=Entry(Colddrinkframe,font=('arial',15),bd=5,width=10)
mrindaentry.insert(0,0)
mrindaentry.grid(row=4,column=1,pady=9,padx=10)

limcalabel=Label(Colddrinkframe,text='Limca',font=('calibri',15,'bold'),bg='gray',fg='white')
limcalabel.grid(row=4,column=0,padx=10,pady=9,sticky='w')
limcaentry=Entry(Colddrinkframe,font=('arial',15),bd=5,width=10)
limcaentry.insert(0,0)
limcaentry.grid(row=4,column=1,pady=9,padx=10)


######
billframe=Frame(productsframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)
billarealabel=Label(billframe,text='Label Area',font=('arial',15),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=16,width=50,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview())

################################
billmenuframe=LabelFrame(root,text='Bill Menu',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
billmenuframe.pack(fill=X)

cosmetpricelabel=Label(billmenuframe,text='Cosmetics price',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
cosmetpricelabel.grid(row=0,column=0)
cosmeticpriceentry=Entry(billmenuframe,font=('arial',15),bd=5,width=10)
cosmeticpriceentry.grid(row=0,column=1,pady=6,padx=10)

grocerypricelabel=Label(billmenuframe,text='Grocery price',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
grocerypricelabel.grid(row=1,column=0)
grocerypriceentry=Entry(billmenuframe,font=('arial',15),bd=5,width=10)
grocerypriceentry.grid(row=1,column=1,pady=6,padx=10)

colddrinkpricelabel=Label(billmenuframe,text='cold drinks price price',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
colddrinkpricelabel.grid(row=2,column=0)
colddrinkpriceentry=Entry(billmenuframe,font=('arial',15),bd=5,width=10)
colddrinkpriceentry.grid(row=2,column=1,pady=6,padx=10)


cosmettaxpricelabel=Label(billmenuframe,text='Cosmetics tax price',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
cosmettaxpricelabel.grid(row=0,column=2)
cosmetictaxpriceentry=Entry(billmenuframe,font=('arial',15),bd=5,width=10)
cosmetictaxpriceentry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxpricelabel=Label(billmenuframe,text='Grocery tax price',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
grocerytaxpricelabel.grid(row=1,column=2)
grocerytaxpriceentry=Entry(billmenuframe,font=('arial',15),bd=5,width=10)
grocerytaxpriceentry.grid(row=1,column=3,pady=6,padx=10)

colddrinktaxpricelabel=Label(billmenuframe,text='cold drinks tax price',font=('calibri',15,'bold'),bg='gray',fg='yellow',bd=8,relief=GROOVE)
colddrinktaxpricelabel.grid(row=2,column=2)
colddrinktaxpriceentry=Entry(billmenuframe,font=('arial',15),bd=5,width=10)
colddrinktaxpriceentry.grid(row=2,column=3,pady=6,padx=10)



buttonFrame=Frame(billmenuframe,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=4,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=2,padx=30)

billButton=Button(buttonFrame,text='BILL',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=4,pady=10,command=billarea)
billButton.grid(row=0,column=1,pady=2,padx=30)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=4,pady=10,command=cleararea)
clearButton.grid(row=0,column=4,pady=2,padx=30)



root.mainloop()
