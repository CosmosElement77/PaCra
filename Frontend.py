from tkinter import *
from Backend import *
from tkinter.ttk import Progressbar

base=Tk()
base.title("PaCra-The Password Cracker")
base.geometry("400x600")
base.resizable(False,False)

base_buttons=Frame(base)
base_buttons.pack(pady=20)
###
zip_file=StringVar()
word_file=StringVar()
result=StringVar()
def show_progress():
    progress.start()
    PassCrack(zip_file.get(), word_file.get(),result)
    progress.stop()

###

Zip=Button(base_buttons,text="Select Zip File",fg="black",bg="white",height=2,width=15,command=lambda: getZip(zip_file))
# Zip.grid(row=0,column=0,padx=10,pady=40)
Zip.pack(padx=10,side=LEFT)

PassFile=Button(base_buttons,text="Select the Text File",fg="black",bg="white",height=2,width=15,command=lambda: getWord(word_file))
# PassFile.grid(row=0,column=1,padx=10,pady=40)
PassFile.pack(padx=10,side=LEFT)

progress = Progressbar(base, orient=HORIZONTAL, length=300, mode='indeterminate')
progress.pack(pady=30)

Start=Button(base,text="Start BruteForce",fg="white",bg="black",height=2,width=15,command=show_progress)
# Start.grid(row=1,column=0,padx=10,pady=50)
Start.pack(pady=20)

label_end=Label(base,textvariable=result,font=("Times New Roman",14))
# label_end.grid(row=2,column=0,padx=10,pady=70)
label_end.pack(pady=40)
####################
base.mainloop()
####################