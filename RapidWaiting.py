
import random
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *
import tkinter as tk



def system():
    root = tk.Tk()
    root.geometry("1680x800")
    root.title("Rapid Waiting System")


    def Database():
        global connectn, cursor
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS Restaurantrecords(ordno text,sh text,shf text,w text, fpf text, fc text, mcb text, cb text, c text, mc text, s text, fj text, ct text, mo text, mi text, ctl text,sb text,tax text,tot text)")

    # variable datatype assignment
    orderno = StringVar()
    Shawarma = StringVar()
    ShawarmaFries = StringVar()
    FivePcsWings = StringVar()
    FivePcswithFries = StringVar()
    FriedChicken = StringVar()
    MarylandChickenBiryani = StringVar()
    ChickenBiryani = StringVar()
    Choma = StringVar()
    MasalaChips = StringVar()
    Soda = StringVar()
    FreshJuice = StringVar()
    Cocktails = StringVar()
    Mocktails = StringVar()
    Milkshake = StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    total = StringVar()

    # defining total function
    def tottal():
        # fetching the values from entry box
        order = (orderno.get())
        sh = float(Shawarma.get())
        shf = float(ShawarmaFries.get())
        w = float(FivePcsWings.get())
        fpf = float(FivePcswithFries.get())
        fc = float(FriedChicken.get())
        mcb = float(MarylandChickenBiryani.get())
        cb = float(ChickenBiryani.get())
        c = float(Choma.get())
        mc = float(MasalaChips.get())
        s = float(Soda.get())
        fj = float(FreshJuice.get())
        ctl = float(Cocktails.get())
        mo = float(Mocktails.get())
        mi = float(Milkshake.get())

        # computing the cost of items

        costsh = sh* 250
        costshf = shf * 350
        costw = w * 250
        costfpf = fpf * 350
        costfc = fc * 250
        costmcb = mcb * 350
        costcb = cb * 450
        costc = c * 320
        costmc = mc * 200
        costs = s * 50
        costfj = fj * 100
        costctl = ctl * 120
        costmo = mo * 150
        costmi = mi * 350

        # computing the charges
        costofmeal = (costsh+ costshf+ costw + costfpf + costfc + costmcb + costcb + costc + costmc + costs + costfj + costctl + costmo + costmi)
        ptax = ((costsh+ costshf+ costw + costfpf + costfc + costmcb + costcb + costc + costmc + costs + costfj + costctl + costmo + costmi) * 0.18)
        sub = (costsh+ costshf+ costw + costfpf + costfc + costmcb + costcb + costc + costmc + costs + costfj + costctl + costmo + costmi)
        paidtax = str(ptax)
        overall = str(ptax + sub)

        # Displaying the values
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        total.set(overall)

    # defining reset function
    def reset():
        orderno.set("")
        Shawarma.set("")
        ShawarmaFries.set("")
        FivePcsWings.set("")
        FivePcswithFries.set("")
        FriedChicken.set("")
        MarylandChickenBiryani.set("")
        ChickenBiryani.set("")
        Choma.set("")
        MasalaChips.set("")
        Soda.set("")
        FreshJuice.set("")
        Cocktails.set("")
        Mocktails.set("")
        Milkshake.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        total.set("")

    # defining exit function
    def exit():
        root.destroy()

    # Topframe
    topframe = Frame(root, bg="white", width=1200, height=50)
    topframe.pack(side=TOP)

    # Leftframe
    leftframe = Frame(root, width=900, height=680)
    leftframe.pack(side=LEFT)

    # rightframe
    rightframe = Frame(root, width=400, height=680)
    rightframe.pack(side=RIGHT)

    # Data display
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    style = ttk.Style()
    style.configure("Treeview",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', 'light#15191c')])

    # Table Top
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "sh", "shf", "w", "fpf", "fc", "mcb", "cb", "c", "mc", "s", "fj", "ctl", "mo", "mi", "ct", "sb", "tax", "tot")

    # Table Creation
    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("sh", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("shf", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("w", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("fpf", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("fc", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("mcb", anchor=CENTER, width=150, minwidth=25)
    my_tree.column("cb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("c", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("mc", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("s", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("fj", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("ctl", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("mo", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("mi", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=100, minwidth=25)

    # defining  headings for table
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("sh", text="Shawarma", anchor=CENTER)
    my_tree.heading("shf", text="ShawarmaFries", anchor=CENTER)
    my_tree.heading("w", text="FivePcsWings", anchor=CENTER)
    my_tree.heading("fpf", text="FivePcswithFries", anchor=CENTER)
    my_tree.heading("fc", text="FriedChicken", anchor=CENTER)
    my_tree.heading("mcb", text="MarylandChickenBiryani", anchor=CENTER)
    my_tree.heading("cb", text="ChickenBiryani", anchor=CENTER)
    my_tree.heading("c", text="Choma", anchor=CENTER)
    my_tree.heading("mc", text="MasalaChips", anchor=CENTER)
    my_tree.heading("s", text="Soda", anchor=CENTER)
    my_tree.heading("fj", text="FreshJuice", anchor=CENTER)
    my_tree.heading("ctl", text="Cocktails", anchor=CENTER)
    my_tree.heading("mo", text="Mocktails", anchor=CENTER)
    my_tree.heading("mi", text="Milkshake", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    # defining add function to add record
    def add():
        Database()
        orders = orderno.get()
        sh = Shawarma.get()
        shf = ShawarmaFries.get()
        w = FivePcsWings.get()
        fpf = FivePcswithFries.get()
        fc = FriedChicken.get()
        mcb = MarylandChickenBiryani.get()
        cb = ChickenBiryani.get()
        c = Choma.get()
        mc = MasalaChips.get()
        s = Soda.get()
        fj = FreshJuice.get()
        ctl = Cocktails.get()
        mo = Mocktails.get()
        mi = Milkshake.get()
        costs = cost.get()
        subtotals = subtotal.get()
        taxs = tax.get()
        totals = total.get()
        if orders == "" or sh == "" or shf == "" or w == "" or fpf == "" or fc == "" or mcb == "" or cb == "" or c == "" or mc == "" or s == "" or fj == "" or ctl == "" or mo == "" or mi == "" or costs == "" or subtotals == "" or taxs == "" or totals == "":
            messagebox.showinfo("Warning", "Please fill the empty field!!!")
        else:
            connectn.execute(
                'INSERT INTO Restaurantrecords (ordno, sh, shf , w ,fpf , fc, mcb, cb, c, mc, s, fj, ctl, mo, mi, ct ,sb ,tax, tot) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                (orders, sh, shf, w, fpf, fc, mcb, cb, c, mc, s, fj, ctl, mo, mi, costs, subtotals, taxs, totals))
            connectn.commit()
            messagebox.showinfo("Message", "Stored successfully")
        # refresh table data
        DisplayData()
        connectn.close()

    # defining function to access data from sqlite datrabase
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_chilfpfen())
        cursor = connectn.execute("SELECT * FROM Restaurantrecords")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor = connectn.execute("DELETE FROM Restaurantrecords WHERE ordno= %d" % selecteditem[0])
            connectn.commit()
            cursor.close()
            connectn.close()

    # Time
    localtime = time.asctime(time.localtime(time.time()))
    # Top part
    main_lbl = Label(topframe, font=('Poppins', 25, 'bold'), text="Msosi.com", fg="#020203",
                   anchor=W)
    main_lbl.grid(row=0, column=0)
    main_lbl = Label(topframe, font=('Poppins', 15,), text=localtime, fg="black", anchor=W)
    main_lbl.grid(row=1, column=0)

    ### Labels
    # items
    ordlbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Order No.", fg="black", bd=5, anchor=W).grid(row=1,
                                                                                                             column=0)
    ordtxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                   textvariable=orderno).grid(row=2, column=0)
    # Shawarma
    shlbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Shawarma", fg="black", bd=5, anchor=W).grid(row=3,
                                                                                                         column=0)
    shtxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                   textvariable=Shawarma).grid(row=4, column=0)
    # ShawarmaFries
    shflbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="ShawarmaFries", fg="black", bd=5, anchor=W).grid(row=3,
                                                                                                          column=1)
    shftxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                   textvariable=ShawarmaFries).grid(row=4, column=1)
    # FivePcsWings
    wlbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="FivePcsWings", fg="black", bd=5, anchor=W).grid(row=5,
                                                                                                          column=0)
    wtxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                   textvariable=FivePcsWings).grid(row=6, column=0)
    # FivePcswithFries
    fpfinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="FivePcswithFries", fg="black", bd=5, anchor=W).grid(row=5,
                                                                                                            column=1)
    fpfinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=FivePcswithFries).grid(row=6, column=1)
    # FriedChicken
    fcinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="FriedChicken", fg="black", bd=5, anchor=W).grid(row=7,
                                                                                                            column=0)
    fcfinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=FriedChicken).grid(row=8, column=0)
    # MarylandChikenBiryani
    mcbinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="MarylandChickenBiryani", fg="black", bd=5, anchor=W).grid(row=7,
                                                                                                            column=1)
    mcbinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=MarylandChickenBiryani).grid(row=8, column=1)
    # ChickenBiryani
    cbinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="ChickenBiryani", fg="black", bd=5, anchor=W).grid(row=9,
                                                                                                            column=0)
    cbinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=ChickenBiryani).grid(row=10, column=0)
    # Choma
    cinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Choma", fg="black", bd=5, anchor=W).grid(row=9,
                                                                                                            column=1)
    cinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=Choma).grid(row=10, column=1)
    # MasalaChips
    mcinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="MasalaChips", fg="black", bd=5, anchor=W).grid(row=11,
                                                                                                            column=0)
    mcinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=MasalaChips).grid(row=12, column=0)
    # Soda
    sinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Soda", fg="black", bd=5, anchor=W).grid(row=3,
                                                                                                            column=2)
    sinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=Soda).grid(row=4, column=2)
    # FreshJuice
    fjinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="FreshJuice", fg="black", bd=5, anchor=W).grid(row=5,
                                                                                                            column=2)
    fjinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=FreshJuice).grid(row=6, column=2)
    # Cocktails
    ctlinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Cocktails", fg="black", bd=5, anchor=W).grid(row=7,
                                                                                                            column=2)
    ctlinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=Cocktails).grid(row=8, column=2)
    # Mocktails
    moinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Mocktails", fg="black", bd=5, anchor=W).grid(row=9,
                                                                                                            column=2)
    moinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=Mocktails).grid(row=10, column=2)
    # Milkshake
    miinklbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Milkshake", fg="black", bd=5, anchor=W).grid(row=11,
                                                                                                            column=1)
    miinktxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right',
                     textvariable=Milkshake).grid(row=12, column=1)
    # cost
    costlbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Cost", bd=5, anchor=W).grid(row=14, column=0)
    costtxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right', bg="lightgrey",
                   textvariable=cost).grid(row=14, column=1)
    # subtotal
    sublbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Subtotal", bd=5, anchor=W).grid(row=15, column=0)
    subtxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right', bg="lightgrey",
                   textvariable=subtotal).grid(row=15, column=1)
    # tax
    taxlbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Tax", bd=5, anchor=W).grid(row=16, column=0)
    taxtxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right', bg="lightgrey",
                   textvariable=tax).grid(row=16, column=1)
    # total
    totallbl = Label(leftframe, font=('Poppins', 12, 'bold'), text="Total", bd=5, anchor=W).grid(row=17,column=0)
    totaltxt = Entry(leftframe, font=('Poppins', 12, 'bold'), bd=2, insertwidth=4, justify='right', bg="lightgrey",
                     textvariable=total).grid(row=17, column=1)
    # buttons


    totbtn = Button(leftframe, font=('Poppins', 12, 'bold'), text="Total", bg="Lightgrey", fg="#048449", bd=4, padx=2, pady=2,
                    width=8, command=tottal).grid(row=18, column=0)

    resetbtn = Button(leftframe, font=('Poppins', 12, 'bold'), text="Reset", bg="lightgrey", fg="black", bd=4, padx=2,
                      pady=2, width=8, command=reset).grid(row=13, column=2)

    exitbtn = Button(leftframe, font=('Poppins', 12, 'bold'), text="Exit RapidWaiting", bg="lightgrey", fg="#c4112f", bd=4, padx=2,
                     pady=2, width=12, command=exit).grid(row=18, column=2)

    addbtn = Button(leftframe, font=('Poppins', 12, 'bold'), text="Add", bg="lightgrey", fg="black", bd=4, padx=2, pady=2,
                    width=8, command=add).grid(row=18, column=1)

    deletebtn = Button(leftframe, font=('Poppins', 12, 'bold'), text="Delete Record", bg="#c4112f", fg="white", bd=4,
                       padx=2, pady=2, width=12, command=Delete).grid(row=15, column=2)

    # Feedback form

    def feedbackk():
        feed = Tk()
        feed.geometry("900x900")
        feed.title("Submit Feedback form")
        # database #
        connectn = sqlite3.connect("Restaurant.db")
        cursor = connectn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS FEEDBACK(n text,eid text,feedback5 text,com text)")
        # variable datatype asssignment 
        name = StringVar()
        email = StringVar()
        comments = StringVar()

        # defiing submit function
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END)
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Excellent"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
            conn = sqlite3.connect("Restaurant.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO FEEDBACK VALUES ('" + n + "','" + eid + "','" + com + "','" + feedback5 + "')")
            messagebox.showinfo("message", "data inserted !")
            feed.destroy()

        # defining cancel button
        def cancel():
            feed.destroy()

        # label#
        lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", fg="black").pack(side=TOP)
        lbl2 = Label(feed, font=("calisto MT", 15), text="We're glad you chose us ! Please tell us how it was!",
                     fg="black").pack(side=TOP)
        # name
        namelbl = Label(feed, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(feed, font=('vardana', 15), bd=2, insertwidth=2, bg="white", justify='right',
                        textvariable=name).place(x=15, y=185)
        # email
        emaillbl = Label(feed, font=('vardana', 15), text="Email:-", fg="black", bd=10, anchor=W).place(x=260, y=150)
        emailtxt = Entry(feed, font=('vardana', 15), bd=2, insertwidth=2, bg="white", justify='right',
                         textvariable=email).place(x=285, y=185)
        #checkbutton
        ratelbl = Label(feed, font=('vardana', 15), text="How would you rate us?", fg="black", bd=10, anchor=W).place(
            x=10, y=215)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('Poppins', 10, "bold"), text="Excellent", bg="white", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=260)
        c2 = Checkbutton(feed, font=('Poppins', 10, "bold"), text="Good", bg="white", variable=checkvar2, )
        c2.deselect()
        c2.place(x=120, y=260)
        c3 = Checkbutton(feed, font=('Poppins', 10, "bold"), text=" Average", bg="white", variable=checkvar3, )
        c3.deselect()
        c3.place(x=220, y=260)
        c4 = Checkbutton(feed, font=('Poppins', 10, "bold"), text="   Poor  ", bg="white", variable=checkvar4, )
        c4.deselect()
        c4.place(x=320, y=260)
        # comments
        commentslbl = Label(feed, font=('Poppins', 15), text="Comments", fg="black", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=100, height=20)
        txt.place(x=15, y=335)
        # button
        submit = Button(feed, font=("Poppins", 15), text="Submit", fg="#048449", bg="lightgrey", bd=2, command=submit).place(
            x=145, y=680)
        cancel = Button(feed, font=("Poppins", 15), text="Cancel", fg="#c4112f", bg="lightgrey", bd=2, command=cancel).place(
            x=245, y=680)
        feed.mainloop()

    # Feedbackbutton
    feedbtn = Button(leftframe, font=('Poppins', 12, 'bold'), text="Feedback Form", fg="white", bg="#e3503b", bd=3, padx=2,
                     pady=2, width=12, command=feedbackk).grid(row=1, column=2, columnspan=1)

    # Menu Card
    def menu():
        roott = Tk()
        roott.title("Msosi.com Menu")
        roott.geometry("900x900")
        lblinfo = Label(roott, font=("Poppins", 20, "bold"), text="ITEM LIST", fg="#084281", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(roott, font=("Poppins", 20, "bold"), text="Prices", fg="#084281", bd=10)
        lblprice.grid(row=0, column=3)
        lblShawarma = Label(roott, font=("Poppins", 20, "bold"), text="Shawarma", fg="#15191c", bd=10)
        lblShawarma.grid(row=1, column=0)
        lblpricesh = Label(roott, font=("Poppins", 20, "bold"), text="260/-", fg="#15191c", bd=10)
        lblpricesh.grid(row=1, column=3)
        lblShawarmaFries = Label(roott, font=("Poppins", 20, "bold"), text="ShawarmaFries", fg="#15191c", bd=10)
        lblShawarmaFries.grid(row=3, column=0)
        lblpriceshf = Label(roott, font=("Poppins", 20, "bold"), text="350/-", fg="#15191c", bd=10)
        lblpriceshf.grid(row=3, column=3)
        lblFivePcsWings = Label(roott, font=("Poppins", 20, "bold"), text="FivePcsWings", fg="#15191c", bd=10)
        lblFivePcsWings.grid(row=4, column=0)
        lblpricew = Label(roott, font=("Poppins", 20, "bold"), text="250/-", fg="#15191c", bd=10)
        lblpricew.grid(row=4, column=3)
        lblFivePcswithFries = Label(roott, font=("Poppins", 20, "bold"), text="FivePcswithFries", fg="#15191c", bd=10)
        lblFivePcswithFries.grid(row=5, column=0)
        lblpricefpf = Label(roott, font=("Poppins", 20, "bold"), text="350/-", fg="#15191c", bd=10)
        lblpricefpf.grid(row=5, column=3)
        lblFriedChicken = Label(roott, font=("Poppins", 20, "bold"), text="FriedChicken", fg="#15191c", bd=10)
        lblFriedChicken.grid(row=6, column=0)
        lblpricefc = Label(roott, font=("Poppins", 20, "bold"), text="250/-", fg="#15191c", bd=10)
        lblpricefc.grid(row=6, column=3)
        lblMarylandChickenBiryani = Label(roott, font=("Poppins", 20, "bold"), text="MarylandChickenBiryani", fg="#15191c", bd=10)
        lblMarylandChickenBiryani.grid(row=7, column=0)
        lblpricemcb = Label(roott, font=("Poppins", 20, "bold"), text="350/-", fg="#15191c", bd=10)
        lblpricemcb.grid(row=7, column=3)
        lblChickenBiryani = Label(roott, font=("Poppins", 20, "bold"), text="ChickenBiryani", fg="#15191c", bd=10)
        lblChickenBiryani.grid(row=8, column=0)
        lblpricecb = Label(roott, font=("Poppins", 20, "bold"), text="450/-", fg="#15191c", bd=10)
        lblpricecb.grid(row=8, column=3)
        lblChoma = Label(roott, font=("Poppins", 20, "bold"), text="Choma", fg="#15191c", bd=10)
        lblChoma.grid(row=9, column=0)
        lblpricec = Label(roott, font=("Poppins", 20, "bold"), text="320/-", fg="#15191c", bd=10)
        lblpricec.grid(row=9, column=3)
        lblMasalaChips = Label(roott, font=("Poppins", 20, "bold"), text="MasalaChips", fg="#15191c", bd=10)
        lblMasalaChips.grid(row=10, column=0)
        lblpricemc = Label(roott, font=("Poppins", 20, "bold"), text="200/-", fg="#15191c", bd=10)
        lblpricemc.grid(row=10, column=3)
        lblSoda = Label(roott, font=("Poppins", 20, "bold"), text="Soda", fg="#15191c", bd=10)
        lblSoda.grid(row=11, column=0)
        lblprices = Label(roott, font=("Poppins", 20, "bold"), text="50/-", fg="#15191c", bd=10)
        lblprices.grid(row=11, column=3)
        lblFreshJuice = Label(roott, font=("Poppins", 20, "bold"), text="FreshJuice", fg="#15191c", bd=10)
        lblFreshJuice.grid(row=12, column=0)
        lblpricefj = Label(roott, font=("Poppins", 20, "bold"), text="100/-", fg="#15191c", bd=10)
        lblpricefj.grid(row=12, column=3)
        lblCocktails = Label(roott, font=("Poppins", 20, "bold"), text="Cocktails", fg="#15191c", bd=10)
        lblCocktails.grid(row=13, column=0)
        lblpricectl = Label(roott, font=("Poppins", 20, "bold"), text="120/-", fg="#15191c", bd=10)
        lblpricectl.grid(row=13, column=3)
        lblMocktails = Label(roott, font=("Poppins", 20, "bold"), text="Mocktails", fg="#15191c", bd=10)
        lblMocktails.grid(row=14, column=0)
        lblpricemo = Label(roott, font=("Poppins", 20, "bold"), text="150/-", fg="#15191c", bd=10)
        lblpricemo.grid(row=14, column=3)
        lblMilkshake = Label(roott, font=("Poppins", 20, "bold"), text="Milkshake", fg="#15191c", bd=10)
        lblMilkshake.grid(row=15, column=0)
        lblpricemi = Label(roott, font=("Poppins", 20, "bold"), text="350/-", fg="#15191c", bd=10)
        lblpricemi.grid(row=15, column=3)
        roott.mainloop()

    # menubutton
    menubtn = Button(leftframe, font=('Poppins', 12, 'bold'), text="Menu Card", bg="#084281", fg="white", bd=3, padx=2,
                     pady=2, width=12, command=menu).grid(row=1, column=1)

    root.mainloop()


system()