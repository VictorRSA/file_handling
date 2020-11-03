from tkinter import *
import tkinter

from tkinter import simpledialog, messagebox, filedialog, Text

root = Tk()
root.geometry("600x600")
root.title("********Text Files Creation System:********")


def clear():
    txt.delete(1.0, END)


def kill_gui():
    root.destroy()


def get_txt():
    user_txt = txt.get('1.0', END+'-1c')
    # types =[("Text files",".txt"),("Document files",".doc")]
    # dialog = filedialog.askopenfiles(filetypes=types)
    # file_show = dialog.show()
    # if file_show !='':
    input =txt.insert(END,user_txt)



def append_txt_in_file():
    do_you_want_to_save = messagebox.askyesno(title=None,
                                              message="Do you want append the texts you just typed in the text input box:\n")
    if do_you_want_to_save==True:  # if do yo want to save ==True
        prompt = simpledialog.askstring(title="Text", prompt="Enter the filename and extension to save your "
                                                             "activities:\n")
        if prompt == True:
            with open(prompt, "a+") as file:
                file.writelines(txt.get('1.0',END))
                file.close()



    else:
        messagebox.showinfo("Return", "You will now return to the application main screen")


def display():

    ask = messagebox.askyesno(Title=None,message="Do yo want to open esisting text files:")
    if ask ==True:
        def call():
            name = filedialog.askopenfilename()
            messagebox.showinfo(name)
            btn = Button(root,text="Open exising text file to display:",command=call)
            btn.grid(row=2,column=7,padx=25,pady=25)

    else:
        msg = txt.get()
        txt.insert("end",u"\n{}".format(msg))



label = Label(root, text="My weekend activities", fg="blue", font=("Helvetica",16))
label.grid(row=0, column=0, padx=25, pady=25)

txt: Text = Text(root,bd=1,font=("Arial",14))
txt.grid(row=5, column=1, columnspan=4, padx=25, pady=25,sticky=W+E+N+S)
create_btn = Button(root, text="Create textile", fg="gray",command=append_txt_in_file)
create_btn.grid(row=2, column=2, padx=25, pady=25)

display_created_txt = Button(root, text="Display", fg="green2", command=get_txt)
display_created_txt.grid(row=2, column=3, padx=25, pady=25)

append_created_txt = Button(root, text="Append Data", fg="orange", command=append_txt_in_file)
append_created_txt.grid(row=2, column=4, padx=25, pady=25)

clear_create_txt = Button(root, text="Clear", fg="red", command=clear)
clear_create_txt.grid(row=2, column=5, padx=25, pady=25)

exit_btn = Button(root, text="Exit", fg="red2", command=kill_gui)
exit_btn.grid(row=2, column=6, padx=25, pady=25)

root.mainloop()
