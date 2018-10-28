import glob
import time
from tkinter.filedialog import askdirectory
from tkinter.ttk import Progressbar
from tkinter import messagebox
import pandas as pd
from tkinter import*
import tkinter as tk
import os


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.window_config()
        self.createWidgets()
    def createWidgets(self):
        self.result_label()
        self.Out_File_name()
        self.select_option_bar()
        self.InPut_file_Button()
        self.OutPut_file_Button()
        self.START_Button()
        self.Exit_Button()
    def window_config(self):
        self.master.title("Excel File Marger")
        self.master.minsize(400, 400)
        self.master.maxsize(1000, 400)
    def InPut_file_Button(self):
        self.input_Folder_Location = Button(self,text="Select INPUT File Location")
        self.input_Folder_Location["fg"]   = "black"
        self.input_Folder_Location["command"] = self.in_folder_loc
        self.input_Folder_Location.pack({"side": "left"})
    def OutPut_file_Button(self):
        self.input_Folder_Location = Button(self,text="Select OUTPUT File Location")
        self.input_Folder_Location["fg"]   = "black"
        self.input_Folder_Location["command"] = self.out_folder_loc
        self.input_Folder_Location.pack({"side": "left"})
    def result_label(self):
        self.r_label = Label(self)
        self.r_label.pack(side=BOTTOM)
    def option_manu_check(self,selection):
        self.item = selection
        options = [
            'csv',
            'xlxs'
        ]

        if selection.lower() in options:
            if(selection.lower()=='csv'):
                self.start["command"] =  self.csv_start
                self.r_label["text"]="CSV selected"
        if(selection.lower()=='xlxs'):
            self.start["command"] =  self.excel_start
            self.r_label["text"]="XLXS selected"
        else:
            pass
        #print(items)

        # remove old elements


    def select_option_bar(self):
        self.variable = tk.StringVar(self)
        options= ["CSV", "XLXS"]
        self.variable.set("select type")
        self.w = OptionMenu(self, self.variable,*options,command=self.option_manu_check )
        self.w.pack(side="left")

    def START_Button(self):
        self.start = Button(self)
        self.start["text"] = "START"
        self.start["fg"]   = "red"
        self.start.pack({"side": "left"})
        
    def Exit_Button(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})
    def Out_File_name(self):
        self.label = Label(self,text="OUTPUT File Name")
        self.label.pack()
        self.File_name = Entry(self)
        self.File_name.pack()
####################################################################
# ****************** END OF WINDOW DESIGN SECTION *********************
#####################################################################
    def in_folder_loc(self):
        self.in_folder_location = askdirectory()
    def out_folder_loc(self):
        self.out_folder_location = askdirectory()
    def csv_start(self):
        try:
            input_folder_location = self.in_folder_location
            output_folder_location = self.out_folder_location
            OUTPUT_FILE_NAME = self.File_name.get()
            if(OUTPUT_FILE_NAME==''):
                messagebox.showwarning("Warning","Please Define output file name")
            else:
                self.r_label["text"]="proccess running please wait"
                self.Read_CSV(input_folder_location,output_folder_location,OUTPUT_FILE_NAME)
                self.r_label["text"]="Comleted !!"
        except:
            tk.messagebox.showwarning("Warning","Please select files location first")

    def excel_start(self):
        try:
            input_folder_location = self.in_folder_location
            output_folder_location = self.out_folder_location
            OUTPUT_FILE_NAME = self.File_name.get()
            if(OUTPUT_FILE_NAME==''):
                messagebox.showwarning("Warning","Please Define output file name")
            else:
                self.r_label["text"]="proccess running please wait"
                self.Read_EXCEL(input_folder_location,output_folder_location,OUTPUT_FILE_NAME)
                self.r_label["text"]="Comleted !!"
        except:
            tk.messagebox.showwarning("Warning","Please select files location first")


#############################################################################################
#******************** start methode for Excel (xlsx) Read and Add ****************************
#############################################################################################
    def Read_EXCEL(self,
        input_file_loc,
        output_file_loc,
        file_name):
        OutPut_path=r""+str(output_file_loc) #output folder
        path =r""+str(input_file_loc)  #input folder
        all_files = glob.glob(os.path.join(path, "*.xlsx")) #make list of paths
        list_=[]
        frame=pd.DataFrame()
        for file in all_files:
            dfn = pd.read_excel(file,index_col=None,header=0)
            list_.append(dfn)
        frame=pd.concat(list_)
        writer = pd.ExcelWriter(os.path.join(OutPut_path,str(file_name)+'.xlsx'), engine='xlsxwriter')
        ##    print(dataframe)
        frame.to_excel(writer)
        writer.save()
#################################################################################################
#*************** start method for csv read and ADD ****************************************
###############################################################################################
    def Read_CSV(self,input_file_loc,output_file_loc,file_name):

        OutPut_path=r""+str(output_file_loc) #output folder
        path =r""+str(input_file_loc)  #input folder
        all_files = glob.glob(os.path.join(path, "*.csv")) #make list of paths
        list_=[]
        frame=pd.DataFrame()
        for file in all_files:
            dfn = pd.read_csv(file,index_col=None,header=0)
            list_.append(dfn)
        frame=pd.concat(list_)
        frame.to_csv(os.path.join(OutPut_path,str(file_name)+'.csv'))

root = Tk()
# create the application
app = Application(master=root)
app.mainloop()



