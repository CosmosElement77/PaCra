from tkinter import *
from Backend import *
from tkinter.ttk import Progressbar

base=Tk()
base.title("PaCra-The Password Cracker")
base.iconbitmap("Logo.ico")
base.geometry("400x600")
base.resizable(False,False)
base_buttons=Frame(base)
base_buttons.pack(pady=20)

###
zip_file_path=StringVar()
word_file_path=StringVar()
result=StringVar()
def show_progress():
    progress.start()
    PassCrack(zip_file_path.get(), word_file_path.get(),result)
    progress.stop()
###

Zip=Button(base_buttons,text="Select Zip File",fg="black",bg="white",height=2,width=15,command=lambda: getZip(zip_file_path))
Zip.pack(padx=10,side=LEFT)
zipf_name=Label(base,textvariable=zip_file_path)
zipf_name.pack(pady=15)

PassFile=Button(base_buttons,text="Select the Text File",fg="black",bg="white",height=2,width=15,command=lambda: getWord(word_file_path))
PassFile.pack(padx=10,side=LEFT)
txt_name=Label(base,textvariable=word_file_path)
txt_name.pack(pady=15)

progress = Progressbar(base, orient=HORIZONTAL, length=300, mode='indeterminate')
progress.pack(pady=20)

Start=Button(base,text="Start BruteForce",fg="white",bg="black",height=2,width=15,command=show_progress)
Start.pack(pady=30)

label_end=Label(base,textvariable=result,font=("Times New Roman",14),wraplength=300)
label_end.pack(pady=40)
####################
base.mainloop()
####################