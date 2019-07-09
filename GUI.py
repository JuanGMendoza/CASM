import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import messagebox
from tkinter import ttk
import ctypes
from tkinter import BOTH, RAISED, X, Y
from Checker import *

# ctypes.windll.shcore.SetProcessDpiAwareness(1)

class supplier:
	def __init__(self,name):
		self.name = name
		self.articles = []

class checkerGui:

	def __init__(self):

		self.suppliers = []
		self.menu_offset = 30

		self.window = tk.Tk()
		self.window.title("Checker")
		self.window.geometry("700x900")
		self.window.resizable(0, 0)
		self.window.configure(background='white')

		self.arrow_photo = tk.PhotoImage(file='images/arrow.png')
		self.gear_photo = tk.PhotoImage(file = 'images/gear.png')
		self.plus_photo = tk.PhotoImage(file = 'images/add2.png')
		self.lwarning_photo = tk.PhotoImage(file = 'images/low_warning2.png')

		self.add_button = tk.Button(self.window, command = self.__pop_up)
		self.add_button.config(image=self.plus_photo, width = '30', height = '30', relief=tk.FLAT,background='white')
		self.add_button.grid(row=0,column=0)

		self.settings_button = tk.Button(self.window)
		self.settings_button.config(image=self.gear_photo, width = '30', height = '30', relief=tk.FLAT,background='white')
		self.settings_button.grid(row=0,column=1)
		

		self.line = ttk.Separator(self.window, orient='horizontal')
		self.line.place(x=0, y=35, relwidth=1)
	
		
		self.window.mainloop()

	def __pop_up(self):


		self.popup_window = tk.Toplevel()
		self.popup_window.title('New Suppliers')
		self.popup_window.geometry("400x150")
		tk.Label(self.popup_window, text='Enter Supplier name or Path:').pack(pady=10,padx=10)
		self.supplier_entry = tk.Entry(self.popup_window, width = 25)
		self.supplier_entry.pack()

		buttons_panel = tk.Frame(self.popup_window)

		ok_button = tk.Button(buttons_panel,text='Ok', command=self.__get_entry)
		browse_button = tk.Button(buttons_panel, text='Browse...', command=self.browse_button_func)

		browse_button.pack(side='left',pady=10,padx=10)
		ok_button.pack(side='left',pady=10,padx=10)
		buttons_panel.pack()

		self.add_button["state"] = "disabled" 
		self.window.wait_window(self.popup_window)
		self.add_button["state"] = "normal"
		

		

	def __get_entry(self):
		self.text = self.supplier_entry.get()
		if(self.text != ''):
			
			self.popup_window.destroy()
			self.add_supplier()

		elif(self.text == ''):
			pass
		
	def add_supplier(self):

		temp_supplier = supplier(self.text)
		search_supplier(temp_supplier)
		self.suppliers.append(temp_supplier)
		number = len(temp_supplier.articles)
		self.supplier_label = tk.Label(self.window, text=self.text,background='white').place(y = (len(self.suppliers) * 50), x = 0)

		if number > 0:
			tk.Label(self.window,image = self.lwarning_photo,background='white').place(y = (len(self.suppliers) * 50)-5, x = 610)
		self.article_label = tk.Label(self.window, text=number,background='white').place(y = (len(self.suppliers) * 50), x = 590)

		self.line = ttk.Separator(self.window, orient='horizontal').place(y=(len(self.suppliers)*50)+40, x = 0,relwidth=1)
		self.drop_button = tk.Button(self.window)
		self.drop_button.config(image=self.arrow_photo, width='39', height='32',relief=tk.FLAT,background='white')
		self.drop_button.place(y = (len(self.suppliers) * 50), x = 650)

		#save = open('Suppliers.txt', 'a')
		#save.write()



	def browse_button_func(self):
		try:
			suppliers = []
			self.directory = filedialog.askopenfile(parent=self.popup_window,mode='rb',title='Choose a file').name
			self.popup_window.destroy()
			with open(self.directory,'r') as file_object:	

				for line in file_object:
					self.text = line
					self.add_supplier()
			

		except:
			print('Error importing file')


test = checkerGui()

