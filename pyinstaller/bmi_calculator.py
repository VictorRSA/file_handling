#!/usr/bin/env python3
print("#Created on:Date:13 October 2020")
print("#Creator:Author:Victor Nkuna")

print("#Email:victor.nkuna@yaoo.com")
print()


from tkinter import *
from tkinter import messagebox   #to take the message ,alterntivelly use a =Entry()



def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    #to make variables an float because by default the var_entry=Entry() by default is a string,

    return height  #return the hight of the entry input


def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight


def calculate_bmi(a=""):
    # "a" is there because the bind function gives an argument to the function....
    print(a)
    '''
      This function calculates the result
    '''

    #to capture erros,the code will run even if user makes worng input

    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        """CHecking our condition """

        """If your BMI is less than 18.5, it falls within the underweight range. 
        If your BMI is 18.5 to 24.9, it falls within the normal or Healthy Weight range.
         If your BMI is 25.0 to 29.9, it falls within the overweight range. 
         If your BMI is 30.0 or higher, it falls within the obese range."""

        print()



        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Super obese!!"
            messagebox.showinfo("Result", res)

#8-2fermENt2020
if __name__ == '__main__':   #run the the main function,in this exaple name
    TOP = Tk()
    TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("400x400")
    TOP.configure(background="steelblue")   #use google color :#307678picker to customize your coors
    TOP.title("GUI BMI Calculator Application")
    TOP.resizable(width=True, height=True)
    LABLE = Label(TOP, bg="#307678", text="Welcome to BMI Calculator", font=("Helvetica", 15, "bold"), pady=10)
    #use color picker to adjust colors to your specifications

    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Height (in cm):", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    BUTTON = Button(bg="green", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()
