#pip install tk  in your cmd
#use tab key to move side and down in the software

from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
import pymysql

root = Tk()
root.title('Billing Software')
root.geometry('250x200+250+200')
bg_color = '#33ACFF'

#================Database_connection=========
connect = pymysql.connect(host='localhost',user='root',passwd='',database='i_k_stores_sales')
cursor = connect.cursor()
        
#==============Top section=================
title = Label(root,text='Retail Invoice',bg=bg_color,fg='white',font=('Bookman Old Style',24,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#=============Shop Address & Details========
name = Label(root, text='I K STORES',font=('Bookman Old Style',22,'bold'),anchor='w')
building = Label(root, text='E.A COMPLEX',font=('Bookman Old Style',12,'bold'),anchor='w')
place = Label(root, text='MYSORE ROAD,MANANANTHAVADY',font=('Bookman Old Style',12,'bold'),anchor='w')
district = Label(root, text='WAYANAD(Dt)',font=('Bookman Old Style',12,'bold'),anchor='w')
mobile = Label(root, text='Mobile:9656570390',font=('Bookman Old Style',12,'bold'),anchor='w')
gstin = Label(root, text='GSTIN:32AZVPM3512D1ZJ',font=('Bookman Old Style',12,'bold'),anchor='w')
name.pack(fill='both')
building.pack(fill='both')
place.pack(fill='both')
district.pack(fill='both')
mobile.pack(fill='both')
gstin.pack(fill='both')

inv_no = Label(root,text='Inv No.',font=('Bookman Old Style',12,'bold'))
inv_no.place(x=1000, y=120, anchor="center")
inv_input = Entry(root,width=13,font=('Bookman Old Style',9,'bold'))
inv_input.place(x=970,y=135)
date = Label(root,text='Date:',font=('Bookman Old Style',12,'bold'))
date.place(x=967, y=160)
date_input=DateEntry(root,selectmode='day',width=10)
date_input.place(x=970,y=190)

#============Customer,product,price -details===
buyer = Label(root, text='BUYER',font=('Bookman Old Style',12,'bold','underline'),anchor='w')
buyer.pack(padx=1,pady=15)

Input_frame = Frame(root)
Input_frame.pack()
slno = Label(Input_frame,text="SlNo.",font=('Bookman Old Style',12,'bold'))
slno.grid(row=0,column=0)
desc_goods = Label(Input_frame,text="Description of goods",font=('Bookman Old Style',12,'bold'))
desc_goods.grid(row=0,column=1)
hsn_sac = Label(Input_frame,text="HSN/SAC",font=('Bookman Old Style',12,'bold'))
hsn_sac.grid(row=0,column=2)
quant = Label(Input_frame,text="Quantity",font=('Bookman Old Style',12,'bold'))
quant.grid(row=0,column=3)
unit_pri = Label(Input_frame,text="Unit price",font=('Bookman Old Style',12,'bold'))
unit_pri.grid(row=0,column=4)
gro_val = Label(Input_frame,text="Gross Value",font=('Bookman Old Style',12,'bold'))
gro_val.grid(row=0,column=5)

count=0
for i in range(10):
    slno_en = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
    count=count+1
    slno_en.insert(0,count)
    slno_en.grid(row=i+1,column=0)
    desc_goods_en = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
    desc_goods_en.grid(row=i+1,column=1)
    hsn_sac_en = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
    hsn_sac_en.grid(row=i+1,column=2)
    quant_en = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
    quant_en.grid(row=i+1,column=3)
    unit_pri_en = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
    unit_pri_en.grid(row=i+1,column=4)
    gro_val_en = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
    gro_val_en.grid(row=i+1,column=5)

gro_tot = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
gro_tot.insert(0,"Gross Total")
gro_tot.grid(row=11,column=5)
st_gst = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
st_gst.insert(0,"State Total")
st_gst.grid(row=12,column=5)
cen_gst = Entry(Input_frame,text="Central GST",font=('Bookman Old Style',12,'bold'))
cen_gst.insert(0,"Central GST")
cen_gst.grid(row=13,column=5)
rou_off = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
rou_off.insert(0,"Round off")
rou_off.grid(row=14,column=5)
total = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
total.insert(0,"Total")
total.grid(row=15,column=5)

amount = Entry(Input_frame,font=('Bookman Old Style',12,'bold'))
amount.insert(0,"Amount in words")
amount.grid(row=16,column=4)

dec = Label(root,text="We declare that this invoice shows the actual price of the goods described and that all products are true and correct.",font=('Bookman Old Style',12,'bold'))
dec.pack()



#==========Save_data_to_database=======
def save_data():
    Invoice_no = inv_input.get()
    Sl_no = slno_en .get()
    Date  = date_input.get()
    Description = desc_goods_en.get()
    HSN_SAC  = hsn_sac_en.get()
    Quantity = quant_en.get()
    Unit_price = unit_pri_en.get()
    Gross_value = gro_val_en.get()
    Gross_total = gro_tot.get()
    State_gst = st_gst.get()
    Central_gst = cen_gst.get()
    Round_off = rou_off.get()
    Total = total.get()
    Amount_in_words = amount.get()
    cursor.execute("insert into Retail_Invoice(Invoice_no,Sl_no,Date,Description,HSN_SAC,Quantity,Unit_price,Gross_value,Gross_total, "\
                   "State_gst,Central_gst,Round_off,Total,Amount_in_words) values ('"+Invoice_no+"','"+Sl_no+"','"+Date+"','"+Description+"','"+HSN_SAC+"','"+Quantity+"', "\
                   " '"+Unit_price+"','"+Gross_value+"','"+Gross_total+"','"+State_gst+"','"+Central_gst+"','"+Round_off+"','"+Total+"', "\
                   " '"+Amount_in_words+"')")
    connect.commit()                  

sign_bt = Button(root,text="Authorized Signatory",font=('Bookman Old Style',12,'bold','italic'),command=save_data)
sign_bt.pack(side='right')
       
root.mainloop()
