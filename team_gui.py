# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:36:36 2016

@author: adamwarner
"""

import Tkinter as tk
import pandas as pd 
import numpy as np

LARGE_FONT = ("Verdana",12)

class Adam(tk.Tk):
    def __init__(self,*args,**kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        
        container.pack(side = "top",fill ="both", expand = True)
        
        container.grid_rowconfigure(0,weight =1)
        container.grid_columnconfigure(0,weight =1)
        
        # Create a dictionary
        self.frames = {}
        frame = StartPage(container,self)
        self.frames[StartPage] = frame
        
        frame.grid(row =0, column = 0, sticky = "nsew")
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text ="Start Page",font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
app = Adam()
app.mainloop()
        
#root = tk.Tk()
#root.title("Simple GUI")
#root.geometry("200x100")
#root.mainloop()