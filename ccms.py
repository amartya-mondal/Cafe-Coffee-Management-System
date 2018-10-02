# -*- coding: utf-8 -*-
#CAFE COFFEE MANAGEMENT SYSTEM
#______________________________________________________________________________________________________________________________
#importing the required files
import Tkinter
from Tkinter import*
import random
import time
import datetime
import tkMessageBox
from tkSimpleDialog import askstring
import tkMessageBox

f=open("Database_of_my_Project.log","a+")
#______________________________________________________________________________________________________________________________
#creating the main screen
root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management Systems")
root.configure(background="black")  #background colour of main screen

#------------------------------------------------===============================================================================------
#Creating the main Frames
Tops=Frame(root, width=1350, height=100,bd=14, relief="raise")
Tops.pack(side=TOP)

f1=Frame(root, width=900, height=650,bd=8, relief="raise")
f1.pack(side=LEFT)

f2=Frame(root, width=440, height=650,bd=8, relief="raise")
f2.pack(side=RIGHT)
        #------------------------------------------------------------------------------------------------------------------------------------------

#Creating the sub frames(Creating small frames inside the left and right frames)
f1a=Frame(f1, width=900, height=330,bd=8, relief="groove")
f1a.pack(side=TOP)

f2a=Frame(f1, width=900, height=320,bd=6, relief="groove")
f2a.pack(side=BOTTOM)

ft2=Frame(f2, width=440, height=450,bd=12, relief="groove")
ft2.pack(side=TOP)

fb2=Frame(f2, width=440, height=250,bd=16, relief="groove")
fb2.pack(side=BOTTOM)

#Creating sub sub frame
f1aa=Frame(f1a, width=410, height=330,bd=16, relief="raise")
f1aa.pack(side=LEFT)

f1ab=Frame(f1a, width=410, height=330,bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a, width=450, height=330,bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab=Frame(f2a, width=450, height=330,bd=14, relief="raise")
f2ab.pack(side=RIGHT)

#Configuring the main frames
Tops.configure(background="black")
f1.configure(background="black")
f2.configure(background="black")

#Filling the top most frame
lblInfo = Label(Tops, font=("arial",63,"bold"), text="Cafe Coffee Management System",bd=10)
lblInfo.grid(row=0,column=0)

#________________________________________________________________Declaring The Commands of the Buttons______________________________________________________
#Exit Button
def qExit():
    qExit=tkMessageBox.askyesno("Quit System","Do you want to exit?")
    if qExit>0:
        root.destroy()
        f.close()
        return
          #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

#Reset Button
def Reset():
    PaidTax.set("0")
    SubTotal.set("0")
    TotalCost.set("0")
    CostofDrinks.set("0")
    CostofCakes.set("0")
    ServiceCharge.set("0")
    txtReceipt.delete("1.0",END)

    E_Latta.set("0")
    E_Espresso.set("0")
    E_Iced_Latte.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")

    E_Coffee_Cake.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    txtLatta.configure(state=DISABLED)
    txtEspresso.configure(state=DISABLED)
    txtIced_Latte.configure(state=DISABLED)
    txtVale_Coffee.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtAfrican_Coffee.configure(state=DISABLED)
    txtAmerican_Coffee.configure(state=DISABLED)
    txtIced_Cappuccino.configure(state=DISABLED)
    txtCoffee_Cake.configure(state=DISABLED)
    txtRed_Velvet_Cake.configure(state=DISABLED)
    txtBlack_Forest_Cake.configure(state=DISABLED)
    txtBoston_Cream_Cake.configure(state=DISABLED)
    txtLagos_Chocolate_Cake.configure(state=DISABLED)
    txtKilburn_Chocolate_Cake.configure(state=DISABLED)
    txtCarlton_Hill_Chocolate_Cake.configure(state=DISABLED)
    txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#CheckButtons
    
def chkbutton_value():
    if (var1.get()==1):
        txtLatta.configure(state= NORMAL)
    elif var1.get()==0:
        txtLatta.configure(state=DISABLED)
        E_Latta.set("0")

    if (var2.get()==1):
        txtEspresso.configure(state= NORMAL)
    elif var2.get()==0:
        txtEspresso.configure(state=DISABLED)
        E_Espresso.set("0")

    if (var3.get()==1):
        txtIced_Latte.configure(state= NORMAL)
    elif var3.get()==0:
        txtIced_Latte.configure(state=DISABLED)
        E_Iced_Latte.set("0")

    if (var4.get()==1):
        txtVale_Coffee.configure(state= NORMAL)
    elif var4.get()==0:
        txtVale_Coffee.configure(state=DISABLED)
        E_Vale_Coffee.set("0")

    if (var5.get()==1):
        txtCappuccino.configure(state= NORMAL)
    elif var5.get()==0:
        txtCappuccino.configure(state=DISABLED)
        E_Cappuccino.set("0")

    if (var6.get()==1):
        txtAfrican_Coffee.configure(state= NORMAL)
    elif var6.get()==0:
        txtAfrican_Coffee.configure(state=DISABLED)
        E_African_Coffee.set("0")

    if (var7.get()==1):
        txtAmerican_Coffee.configure(state= NORMAL)
    elif var7.get()==0:
        txtAmerican_Coffee.configure(state=DISABLED)
        E_American_Coffee.set("0")

    if (var8.get()==1):
        txtIced_Cappuccino.configure(state= NORMAL)
    elif var8.get()==0:
        txtIced_Cappuccino.configure(state=DISABLED)
        E_Iced_Cappuccino.set("0")

    if (var9.get()==1):
        txtCoffee_Cake.configure(state= NORMAL)
    elif var9.get()==0:
        txtCoffee_Cake.configure(state=DISABLED)
        E_Coffee_Cake.set("0")

    if (var10.get()==1):
        txtRed_Velvet_Cake.configure(state= NORMAL)
    elif var10.get()==0:
        txtRed_Velvet_Cake.configure(state=DISABLED)
        E_Red_Velvet_Cake.set("0")

    if (var11.get()==1):
        txtBlack_Forest_Cake.configure(state= NORMAL)
    elif var11.get()==0:
        txtBlack_Forest_Cake.configure(state=DISABLED)
        E_Black_Forest_Cake.set("0")

    if (var12.get()==1):
        txtBoston_Cream_Cake.configure(state= NORMAL)
    elif var12.get()==0:
        txtBoston_Cream_Cake.configure(state=DISABLED)
        E_Boston_Cream_Cake.set("0")

    if (var13.get()==1):
        txtLagos_Chocolate_Cake.configure(state= NORMAL)
    elif var13.get()==0:
        txtLagos_Chocolate_Cake.configure(state=DISABLED)
        E_Lagos_Chocolate_Cake.set("0")

    if (var14.get()==1):
        txtKilburn_Chocolate_Cake.configure(state= NORMAL)
    elif var14.get()==0:
        txtKilburn_Chocolate_Cake.configure(state=DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")

    if (var15.get()==1):
        txtCarlton_Hill_Chocolate_Cake.configure(state= NORMAL)
    elif var15.get()==0:
        txtCarlton_Hill_Chocolate_Cake.configure(state=DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")

    if (var16.get()==1):
        txtQueen_Park_Chocolate_Cake.configure(state= NORMAL)
    elif var16.get==0:
        txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")


#==========================================================================================================================================
#Cost of Items
        
def CostofItem(flagcheck=0):
    todo=flagcheck
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Iced_Latte.get())
    Item4=float(E_Vale_Coffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Coffee.get())
    Item7=float(E_American_Coffee.get())
    Item8=float(E_Iced_Cappuccino.get())
    
    Item9=float(E_Coffee_Cake.get())
    Item10=float(E_Red_Velvet_Cake.get())
    Item11=float(E_Black_Forest_Cake.get())
    Item12=float(E_Boston_Cream_Cake.get())
    Item13=float(E_Lagos_Chocolate_Cake.get())
    Item14=float(E_Kilburn_Chocolate_Cake.get())
    Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16=float(E_Queen_Park_Chocolate_Cake.get())

    PriceofDrinks=(Item1 * 80) + (Item2 * 130) +(Item3 * 140) +(Item4 * 120) +(Item5 * 130) + (Item6 * 200) +(Item7 * 150) +(Item8 * 80)

    PriceofCakes=(Item9 * 90) + (Item10 * 140) +(Item11 * 130) +(Item12 * 100) +(Item13 * 110)+ (Item14 * 150) +(Item15 * 200) +(Item16 * 100)

    DrinksPrice=unicode(u"\u20B9") + str('%.2f'%(PriceofDrinks))
    CakesPrice=unicode(u"\u20B9")+ str('%.2f'%(PriceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC=unicode(u"\u20B9")+ str('%.2f'%(100))
    ServiceCharge.set(SC)

    SubTotalofITEMS=unicode(u"\u20B9")+ str('%.2f'%(PriceofCakes + PriceofDrinks+100))
    SubTotal.set(SubTotalofITEMS)

    Tax=unicode(u"\u20B9")+ str('%.2f'%((PriceofCakes + PriceofDrinks+100)*0.15))
    PaidTax.set(Tax)
    TT=((PriceofCakes + PriceofDrinks+100)*0.15)
    TC=unicode(u"\u20B9")+ str('%.2f'%(PriceofDrinks + PriceofCakes+100+ TT ))
    TotalCost.set(TC)
    #+++++++++++++++++++++++++++++++++
    #Calling the Receipt
    Receipt(todo)


#==========================================================DISPLAY RECEIPT================================================================================
#Receipt
def Receipt(flags=0):
    todo=flags
    if todo==0:
        f.seek(0)
        list_data=f.readlines()
        n=len(list_data)
        if n==0:
            Reference_No=1000
        else:
            lastline=list_data[n-1]
            t=lastline.split(",")
            Reference_No=int(t[0])
            Reference_No+=1
        
        ref=str(Reference_No)
        Receipt_Ref.set(ref)
    else:
        pass

    
    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ Receipt_Ref.get()+'\t\t' +DateofOrder.get()+'\n')
    
    txtReceipt.insert(END,'Items\t\t\t\t\t' + "No of Items \n\n")
                      
    txtReceipt.insert(END,"Latte: \t\t\t\t\t"+ str(E_Latta.get())+ "\n")
    txtReceipt.insert(END,"Espresso: \t\t\t\t\t"+str(E_Espresso.get())+ "\n")
    txtReceipt.insert(END,"Iced Latte: \t\t\t\t\t"+str(E_Iced_Latte.get())+ "\n")
    txtReceipt.insert(END,"Vale Coffee: \t\t\t\t\t"+str(E_Vale_Coffee.get())+ "\n")
    txtReceipt.insert(END,"Cappuccino: \t\t\t\t\t"+str(E_Cappuccino.get())+ "\n")
    txtReceipt.insert(END,"African Coffee: \t\t\t\t\t"+ str(E_African_Coffee.get()) + "\n")
    txtReceipt.insert(END,"American Coffee: \t\t\t\t\t"+str(E_American_Coffee.get())+ "\n")
    txtReceipt.insert(END,"Iced Cappuccino:\t\t\t\t\t"+str(E_Iced_Cappuccino.get())+ "\n")
    txtReceipt.insert(END,"Coffee Cake: \t\t\t\t\t"+str(E_Coffee_Cake.get())+ "\n")
    txtReceipt.insert(END,"Red Velvet Cake: \t\t\t\t\t"+str(E_Red_Velvet_Cake.get())+ "\n")
    txtReceipt.insert(END,"Black Forest Cake: \t\t\t\t\t"+str(E_Black_Forest_Cake.get())+ "\n")
    txtReceipt.insert(END,"Boston Cream Cake: \t\t\t\t\t"+str(E_Boston_Cream_Cake.get())+ "\n")
    txtReceipt.insert(END,"Lagos Chocolate Cake: \t\t\t\t\t"+ str(E_Lagos_Chocolate_Cake.get())+ "\n")
    txtReceipt.insert(END,"Kilburn Chocolate Cake: \t\t\t\t\t"+str(E_Kilburn_Chocolate_Cake.get())+ "\n")
    txtReceipt.insert(END,"Carlton Hill Chocolate Cake: \t\t\t\t\t"+str(E_Carlton_Hill_Chocolate_Cake.get())+ "\n")
    txtReceipt.insert(END,"Queen Park Chocolate Cake: \t\t\t\t\t"+str(E_Queen_Park_Chocolate_Cake.get())+ "\n")
    txtReceipt.insert(END,u"Cost of Drinks: \t\t"+CostofDrinks.get()+ u"\tTax Paid:\t\t"+ PaidTax.get() +"\n")
    txtReceipt.insert(END,"Cost of Cakes:\t\t"+CostofCakes.get()+"\tSubTotal:\t\t" + SubTotal.get()+"\n")
    txtReceipt.insert(END,"Service Charge:\t\t"+ ServiceCharge.get() +"\tTotal Cost:\t\t"+TotalCost.get()+ "\n")

    if todo==0: 
        DataEntry()
    else:
        pass
    
#____________________________________________________________________________________________________________________________
#Keeping records of Receipt
def DataEntry():
    f.seek(0,2)
    Item1=float(E_Latta.get())
    Item2=float(E_Espresso.get())
    Item3=float(E_Iced_Latte.get())
    Item4=float(E_Vale_Coffee.get())
    Item5=float(E_Cappuccino.get())
    Item6=float(E_African_Coffee.get())
    Item7=float(E_American_Coffee.get())
    Item8=float(E_Iced_Cappuccino.get())
    
    Item9=float(E_Coffee_Cake.get())
    Item10=float(E_Red_Velvet_Cake.get())
    Item11=float(E_Black_Forest_Cake.get())
    Item12=float(E_Boston_Cream_Cake.get())
    Item13=float(E_Lagos_Chocolate_Cake.get())
    Item14=float(E_Kilburn_Chocolate_Cake.get())
    Item15=float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16=float(E_Queen_Park_Chocolate_Cake.get())

    rec=str(Receipt_Ref.get())+","+ DateofOrder.get()+","+ str(Item1) +","+ str(Item2)+","+ str(Item3)+ ","+str(Item4)+ ","+str(Item5)+ ","+str(Item5)+","+ str(Item6)+","+ str(Item7)\
         +","+ str(Item8)+","+ str(Item9)+","+ str(Item10)+","+ str(Item11)+ ","+str(Item12)+ ","+str(Item13)+ ","+str(Item14)+","+ str(Item15)+","+ str(Item16)+ "\n"
        
    f.write(rec)     
    f.flush()    
    
#____________________________________________________________________________________________________________________________
#Searching old data by reference no

def SearchOperation():
    
    Reset()
    f.seek(0,0)
    finding= askstring('Cafe Coffee Management System', 'Enter Reference NO to Search For??')
    list_data=f.readlines()
    n=len(list_data)
    flag=0
    for i in range(n):
        line=list_data[i]
        t=line.split(",")
        Ref=t[0]
        if Ref==finding:
            flag=1
            break
        else:
            flag=0

    if flag==0:
        tkMessageBox.showinfo(title="Cafe Coffee Management System", message="!!!!Data Not Found!!!!")
    else:
        Reset()
        
        doO=t[1]
        Item1=float(t[2])
        Item2=float(t[3])
        Item3=float(t[4])
        Item4=float(t[5])
        Item5=float(t[6])
        Item6=float(t[7])
        Item7=float(t[8])
        Item8=float(t[9])

        Item9=float(t[10])
        Item10=float(t[11])
        Item11=float(t[12])
        Item12=float(t[13])
        Item13=float(t[14])
        Item14=float(t[15])
        Item15=float(t[16])
        Item16=float(t[17])
        
        #---------------------------------------------------------------------------
        #Activating the checkbuttons which contains some values
        if (Item1!=0.0):
            txtLatta.configure(state= NORMAL)
        else:
            txtLatta.configure(state=DISABLED)
            E_Latta.set("0.0")

        if (Item2!=0.0):
            txtEspresso.configure(state= NORMAL)
        else :
            txtEspresso.configure(state=DISABLED)
            E_Espresso.set("0.0")

        if (Item3!=0.0):
            txtIced_Latte.configure(state= NORMAL)
        else:
            txtIced_Latte.configure(state=DISABLED)
            E_Iced_Latte.set("0.0")

        if (Item4!=0.0):
            txtVale_Coffee.configure(state= NORMAL)
        else :
            txtVale_Coffee.configure(state=DISABLED)
            E_Vale_Coffee.set("0.0")

        if (Item5!=0.0):
            txtCappuccino.configure(state= NORMAL)
        else :
            txtCappuccino.configure(state=DISABLED)
            E_Cappuccino.set("0")

        if (Item6!=0.0):
            txtAfrican_Coffee.configure(state= NORMAL)
        else :
            txtAfrican_Coffee.configure(state=DISABLED)
            E_African_Coffee.set("0")

        if Item7!=0.0:
            txtAmerican_Coffee.configure(state= NORMAL)
        else :
            txtAmerican_Coffee.configure(state=DISABLED)
            E_American_Coffee.set("0")

        if (Item8!=0.0):
            txtIced_Cappuccino.configure(state= NORMAL)
        else :
            txtIced_Cappuccino.configure(state=DISABLED)
            E_Iced_Cappuccino.set("0")

        if (Item9!=0.0):
            txtCoffee_Cake.configure(state= NORMAL)
        else :
            txtCoffee_Cake.configure(state=DISABLED)
            E_Coffee_Cake.set("0.0")

        if (Item10!=0.0):
            txtRed_Velvet_Cake.configure(state= NORMAL)
        else :
            txtRed_Velvet_Cake.configure(state=DISABLED)
            E_Red_Velvet_Cake.set("0")

        if (Item11!=0.0):
            txtBlack_Forest_Cake.configure(state= NORMAL)
        else :
            txtBlack_Forest_Cake.configure(state=DISABLED)
            E_Black_Forest_Cake.set("0")

        if (Item12!=0.0):
            txtBoston_Cream_Cake.configure(state= NORMAL)
        else :
            txtBoston_Cream_Cake.configure(state=DISABLED)
            E_Boston_Cream_Cake.set("0")

        if (Item13!=0.0):
            txtLagos_Chocolate_Cake.configure(state= NORMAL)
        else :
            txtLagos_Chocolate_Cake.configure(state=DISABLED)
            E_Lagos_Chocolate_Cake.set("0")

        if (Item14!=0.0):
            txtKilburn_Chocolate_Cake.configure(state= NORMAL)
        else :
            txtKilburn_Chocolate_Cake.configure(state=DISABLED)
            E_Kilburn_Chocolate_Cake.set("0")

        if (Item15!=0.0):
            txtCarlton_Hill_Chocolate_Cake.configure(state= NORMAL)
        else :
            txtCarlton_Hill_Chocolate_Cake.configure(state=DISABLED)
            E_Carlton_Hill_Chocolate_Cake.set("0")

        if (Item16!=0.0):
            txtQueen_Park_Chocolate_Cake.configure(state= NORMAL)
        else :
            txtQueen_Park_Chocolate_Cake.configure(state=DISABLED)
            E_Queen_Park_Chocolate_Cake.set("0")

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        E_Latta.set(Item1)
        E_Espresso.set(Item2)
        E_Iced_Latte.set(Item3)
        E_Vale_Coffee.set(Item4)
        E_Cappuccino.set(Item5)
        E_African_Coffee.set(Item6)
        E_American_Coffee.set(Item7)
        E_Iced_Cappuccino.set(Item8)

        E_Coffee_Cake.set(Item9)
        E_Red_Velvet_Cake.set(Item10)
        E_Black_Forest_Cake.set(Item11)
        E_Boston_Cream_Cake.set(Item12)
        E_Lagos_Chocolate_Cake.set(Item13)
        E_Kilburn_Chocolate_Cake.set(Item14)
        E_Carlton_Hill_Chocolate_Cake.set(Item15)
        E_Queen_Park_Chocolate_Cake.set(Item16)
        Receipt_Ref.set(finding)
        DateofOrder.set(doO)
        

        CostofItem(1)

    
    
#__________________________________________________________________DECLARING THE VARIABLES___________________________________________________________________

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var15=IntVar()
var16=IntVar()

PaidTax=IntVar()
SubTotal=IntVar()
TotalCost=IntVar()
CostofDrinks=IntVar()
CostofCakes=IntVar()
ServiceCharge=IntVar()
txtReceipt=IntVar()

DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofCakes=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()

E_Latta=IntVar()
E_Espresso=IntVar()
E_Iced_Latte=IntVar()
E_Vale_Coffee=IntVar()
E_Cappuccino=IntVar()
E_African_Coffee=IntVar()
E_American_Coffee=IntVar()
E_Iced_Cappuccino=IntVar()

E_Coffee_Cake=IntVar()
E_Red_Velvet_Cake=IntVar()
E_Black_Forest_Cake=IntVar()
E_Boston_Cream_Cake=IntVar()
E_Lagos_Chocolate_Cake=IntVar()
E_Kilburn_Chocolate_Cake=IntVar()
E_Carlton_Hill_Chocolate_Cake=IntVar()
E_Queen_Park_Chocolate_Cake=IntVar()

E_Latta.set("0")
E_Espresso.set("0")
E_Iced_Latte.set("0")
E_Vale_Coffee.set("0")
E_Cappuccino.set("0")
E_African_Coffee.set("0")
E_American_Coffee.set("0")
E_Iced_Cappuccino.set("0")

E_Coffee_Cake.set("0")
E_Red_Velvet_Cake.set("0")
E_Black_Forest_Cake.set("0")
E_Boston_Cream_Cake.set("0")
E_Lagos_Chocolate_Cake.set("0")
E_Kilburn_Chocolate_Cake.set("0")
E_Carlton_Hill_Chocolate_Cake.set("0")
E_Queen_Park_Chocolate_Cake.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

#______________________________________________________________________LIST OF COFFEES_____________________________________________________________

Latta=Checkbutton(f1aa, text="Latte \t", variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Latta.grid(row=0, sticky=W)

Espresso=Checkbutton(f1aa, text="Espresso \t", variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Espresso.grid(row=1, sticky=W)

Iced_Latte=Checkbutton(f1aa, text="Iced Latte \t", variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Iced_Latte.grid(row=2, sticky=W)

Vale_Coffee=Checkbutton(f1aa, text="Vale Coffee \t", variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Vale_Coffee.grid(row=3, sticky=W)

Cappuccino=Checkbutton(f1aa, text="Cappuccino \t", variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Cappuccino.grid(row=4, sticky=W)

African_Coffee=Checkbutton(f1aa, text="African Coffee \t", variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
African_Coffee.grid(row=5, sticky=W)

American_Coffee=Checkbutton(f1aa, text="American Coffee \t", variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
American_Coffee.grid(row=6, sticky=W)

Iced_Cappuccino=Checkbutton(f1aa, text="Iced Cappuccino \t", variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Iced_Cappuccino.grid(row=7, sticky=W)

#_______________________________________________________________________LIST OF CAKES_____________________________________________________________

CoffeeCake=Checkbutton(f1ab, text="Coffee Cake \t", variable=var9, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
CoffeeCake.grid(row=0, sticky=W)

Red_Velvet_Cake=Checkbutton(f1ab, text="Red Velvet Cake \t", variable=var10, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Red_Velvet_Cake.grid(row=1, sticky=W)

Black_Forest_Cake=Checkbutton(f1ab, text="Black Forest Cake \t", variable=var11, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Black_Forest_Cake.grid(row=2, sticky=W)

Boston_Cream_Cake=Checkbutton(f1ab, text="Boston Cream Cake \t", variable=var12, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Boston_Cream_Cake.grid(row=3, sticky=W)

Lagos_Chocolate_Cake=Checkbutton(f1ab, text="Lagos Chocolate Cake \t", variable=var13, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Lagos_Chocolate_Cake.grid(row=4, sticky=W)

Kilburn_Chocolate_Cake=Checkbutton(f1ab, text="Kilburn Chocolate Cake \t", variable=var14, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Kilburn_Chocolate_Cake.grid(row=5, sticky=W)

Carlton_Hill_Chocolate_Cake=Checkbutton(f1ab, text="Carlton Hill Chocolate Cake \t", variable=var15, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Carlton_Hill_Chocolate_Cake.grid(row=6, sticky=W)

Queen_Park_Chocolate_Cake=Checkbutton(f1ab, text="Queen Park Chocolate Cake \t", variable=var16, onvalue=1, offvalue=0, font=('arial',18,'bold'),command=chkbutton_value)
Queen_Park_Chocolate_Cake.grid(row=7, sticky=W)

#________________________________________________________Enter WIdeget For Drinks__________________________________________________________________

txtLatta=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Latta,state=DISABLED)
txtLatta.grid(row=0, column=1)

txtEspresso=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Espresso,state=DISABLED)
txtEspresso.grid(row=1, column=1)

txtIced_Latte=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Iced_Latte,state=DISABLED)
txtIced_Latte.grid(row=2, column=1)

txtVale_Coffee=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Vale_Coffee,state=DISABLED)
txtVale_Coffee.grid(row=3, column=1)

txtCappuccino=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Cappuccino,state=DISABLED)
txtCappuccino.grid(row=4, column=1)

txtAfrican_Coffee=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_African_Coffee,state=DISABLED)
txtAfrican_Coffee.grid(row=5, column=1)

txtAmerican_Coffee=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_American_Coffee,state=DISABLED)
txtAmerican_Coffee.grid(row=6, column=1)

txtIced_Cappuccino=Entry(f1aa,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Iced_Cappuccino,state=DISABLED)
txtIced_Cappuccino.grid(row=7, column=1)

#__________________________________________________Enter WIdeget For Cakes_______________________________________________________________
txtCoffee_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Coffee_Cake,state=DISABLED)
txtCoffee_Cake.grid(row=0, column=1)

txtRed_Velvet_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Red_Velvet_Cake,state=DISABLED)
txtRed_Velvet_Cake.grid(row=1, column=1)

txtBlack_Forest_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Black_Forest_Cake,state=DISABLED)
txtBlack_Forest_Cake.grid(row=2, column=1)

txtBoston_Cream_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Boston_Cream_Cake,state=DISABLED)
txtBoston_Cream_Cake.grid(row=3, column=1)

txtLagos_Chocolate_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Lagos_Chocolate_Cake,state=DISABLED)
txtLagos_Chocolate_Cake.grid(row=4, column=1)

txtKilburn_Chocolate_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Kilburn_Chocolate_Cake,state=DISABLED)
txtKilburn_Chocolate_Cake.grid(row=5, column=1)

txtCarlton_Hill_Chocolate_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Carlton_Hill_Chocolate_Cake,state=DISABLED)
txtCarlton_Hill_Chocolate_Cake.grid(row=6, column=1)

txtQueen_Park_Chocolate_Cake=Entry(f1ab,font=("arial",16,'bold'),bd=8,width=6,justify='left',textvariable=E_Queen_Park_Chocolate_Cake,state=DISABLED)
txtQueen_Park_Chocolate_Cake.grid(row=7, column=1)

#_________________________________________________________RECEIPT NAMESPACE______________________________________________________________________________
lblReceipt=Label(ft2,font=('arial',12,'bold'), text="Receipt:",bd=2,anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt=Text(ft2, width=59, height=22,bg="white",bd=8, font=("arial",11,"bold"))
txtReceipt.grid(row=1, column=0)

#____________________________________________________________Cost of Items________________________________________________________________________
lblCostofDrinks=Label(f2aa,font=('arial',16,'bold'), text="Cost of Drinks", bd=8)
lblCostofDrinks.grid(row=0, column=0, sticky=W)
txtCostofDrinks=Entry(f2aa,font=('arial',16,'bold'), insertwidth=2,bd=8,textvariable=CostofDrinks, justify='left')
txtCostofDrinks.grid(row=0, column=1)

lblCostofCakes=Label(f2aa,font=('arial',16,'bold'), text="Cost of Cakes", bd=8)
lblCostofCakes.grid(row=3, column=0, sticky=W)
txtCostofCakes=Entry(f2aa,font=('arial',16,'bold'), bd=8,insertwidth=2,textvariable=CostofCakes, justify='left')
txtCostofCakes.grid(row=3, column=1)

lblServiceCharge=Label(f2aa,font=('arial',16,'bold'), text="Service Tax", bd=8)
lblServiceCharge.grid(row=4, column=0, sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',16,'bold'), bd=8,insertwidth=2,textvariable=ServiceCharge ,justify='left')
txtServiceCharge.grid(row=4, column=1)

#___________________________________________Payment Information____________________________________________________________
lblPaidTax=Label(f2ab,font=('arial',16,'bold'), text="GST", bd=8)
lblPaidTax.grid(row=2, column=0, sticky=W)
txtPaidTax=Entry(f2ab,font=('arial',16,'bold'), bd=8,insertwidth=2,textvariable=PaidTax ,justify='left')
txtPaidTax.grid(row=2, column=1)

lblSubTotal=Label(f2ab,font=('arial',16,'bold'), text="Sub Total", bd=8)
lblSubTotal.grid(row=3, column=0, sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',16,'bold'), bd=8,insertwidth=2,textvariable=SubTotal , justify='left')
txtSubTotal.grid(row=3, column=1)

lblTotalCost=Label(f2ab,font=('arial',16,'bold'), text="Total", bd=8)
lblTotalCost.grid(row=4, column=0, sticky=W)
txtTotalCost=Entry(f2ab,font=('arial',16,'bold'), bd=8,insertwidth=2,textvariable=TotalCost , justify='left')
txtTotalCost.grid(row=4, column=1)
  
#________________________________________________________Buttons___________________________________________________________________________

btnTotal=Button(fb2,padx=16,pady=1,bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Receipt", command=CostofItem)
btnTotal.grid(row=0,column=0)

btnReceipt=Button(fb2,padx=16,pady=1,bd=4, fg="black", font=('arial',16,'bold'), width=5,command=SearchOperation, text="Search")
btnReceipt.grid(row=0,column=1)

btnReset=Button(fb2,padx=16,pady=1,bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Reset",command=Reset)
btnReset.grid(row=0,column=2)

btnExit=Button(fb2,padx=16,pady=1,bd=4, fg="black", font=('arial',16,'bold'), width=5, text="Exit", command=qExit)
btnExit.grid(row=0,column=3)

#________________________________________________________________________________________________________________________________________________
root.mainloop()
