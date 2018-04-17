import glob,sys
import time
import pandas as pd
import os
from tkinter import*
import tkinter
from tkinter import messagebox
class main:
    def __init__(self):
        self.model()
    def model(self):
        self.tk = tkinter.Tk()
        frame = tkinter.Frame(self.tk, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH,expand=1)
        
        self.tk.title("file copier")
        self.txt=Label(frame,text="past here your file location folder")
        self.txt.pack()
        self.ip_box_files_input=Entry(frame)
        self.ip_box_files_input.pack()
        self.txt=Label(frame,text="past here output folder Location")
        self.txt.pack()
        self.ip_box_files_out=Entry(frame)
        self.ip_box_files_out.pack()
        self.btn=Button(frame,text="start copy",command=self.copy_files)
        self.btn.pack()
        
        button = tkinter.Button(frame,text="Exit",command=self.tk.destroy)
        button.pack(side=BOTTOM)
        self.lebel=Label(frame,text="Developed by Ahmmed sabbir")
        self.lebel.pack(side="bottom")
        self.tk.mainloop()

    def copy_files(self):
        p=r"".join(self.ip_box_files_out.get())
        path =r"".join(self.ip_box_files_input.get())
        if path=='' or p=='':
            messagebox.showinfo("Error", "there is no location path \n or \n Location Path is Empty")
            self.tk.destroy()
            sys.exit()
        all_files = glob.glob(os.path.join(path, "*.csv")) #make list of paths
        list_=[]
        frame=pd.DataFrame()
        for file in all_files:
            # Getting the file name without extension
            file_name = os.path.splitext(os.path.basename(file))[0]
            # Reading the file content to create a DataFrame
            dfn = pd.read_csv(file,index_col=None,header=0)
            # Setting the file name (without extension) as the index name
            list_.append(dfn)
            frame=pd.concat(list_)
        frame.to_csv(os.path.join(p,'out_file.csv'))
        ##f=open("data.txt","wb")
        ##f.write(list)
        ##f.close()


m=main()
