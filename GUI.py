import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import messagebox
from tkinter import ttk
import ctypes
from tkinter import BOTH, RAISED, X, Y, END
import Checker as check
import time
import webbrowser
ctypes.windll.shcore.SetProcessDpiAwareness(1)

class supplier:
	def __init__(self,name):
		self.name = name
		self.articles = []
		self.Separator = ''
		self.article_label = ''
		self.warning_label = ''
		self.name_label = ''
		self.drop_button = ''
		self.clicked = False
		self.index = 0
		self.links=[]

class checkerGui:

	def __init__(self):


		self.window = tk.Tk()
		self.window.title("Checker")
		self.window.geometry("700x800")
		self.window.resizable(0, 0)

		filename = tk.PhotoImage(file = "images/login.png")
		button_pic = tk.PhotoImage(file = "images/login_button.png")

		self.background_label = tk.Label(self.window, image=filename)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

		self.login_entry = tk.Entry(self.window, width = 30, relief = 'flat', font=("Helvetica", 15), fg='gray',justify='center', bg='#F9FAFC')
		self.login_entry.place(x=100,y=360)

		self.pass_entry = tk.Entry(self.window, width = 30, relief = 'flat', font=("Helvetica", 15), fg='gray', show="*",justify='center', bg = "#F9FAFC")
		self.pass_entry.place(x=100,y=500)

		self.login_button = tk.Button(self.window, width=370, height = 60,command=self.login, image = button_pic, relief = 'flat')
		self.login_button.place(x=145,y=690)
		


		self.window.mainloop()

	def login(self):
		self.background_label.destroy()
		self.login_entry.destroy()
		self.pass_entry.destroy()
		self.login_button.destroy()
		#self.loading()
		self.tool_screen()
	def loading(self):
		gif = tk.PhotoImage(file ='images/arrow2.png')
		self.label = tk.Label(self.window, image=gif)
		self.label.place(x=0,y=0, relwidth=1, relheight=1)
	def tool_screen(self):


		self.suppliers = []
		self.menu_offset = 30
		self.scroller_items = []

		self.window.configure(background='#009EDC')

		self.arrow_photo = tk.PhotoImage(file='./images/arrow2.png')
		self.gear_photo = tk.PhotoImage(file = './images/gear.png')
		self.plus_photo = tk.PhotoImage(file = './images/add3.png')
		self.lwarning_photo = tk.PhotoImage(file = './images/low_warning22.png')
		self.plane_photo = tk.PhotoImage(file = './images/planeb.png')

		self.add_button = tk.Button(self.window, command = self.__pop_up)
		self.add_button.config(image=self.plus_photo, width = '30', height = '30', relief=tk.FLAT,background='#009EDC')
		self.add_button.grid(row=0,column=0)

		self.settings_button = tk.Button(self.window, command=self.settings)
		self.settings_button.config(image=self.gear_photo, width = '30', height = '30', relief=tk.FLAT,background='#009EDC')
		self.settings_button.grid(row=0,column=1)
		
		self.database_button = tk.Button(self.window, image=self.plane_photo, width = '30', height = '30', relief=tk.FLAT, background='#009EDC')
		self.database_button.grid(row=0,column = 2)
		self.database_button.config(command=self.add_article)
		self.line = ttk.Separator(self.window, orient='horizontal')
		self.line.place(x=0, y=35, relwidth=1)
	def add_article(self):
		self.popup_window = tk.Toplevel()
		self.popup_window.title('Cisco Database')
		self.popup_window.configure(background='white')

		self.title_label = tk.Label(self.popup_window, text='Title:', bg='white')
		self.title_label.grid(row=0, column=0, padx=10, pady=10)

		self.title_entry = tk.Entry(self.popup_window, width=25)
		self.title_entry.grid(row=0,column=1)

		self.mess_label = tk.Label(self.popup_window, text='Message:', bg='white')
		self.mess_label.grid(row=1, column=0, padx=10, pady=10)

		self.mess_entry = tk.Text(self.popup_window, width=45, height=10)
		self.mess_entry.config(font=("Times New Roman",13))
		self.mess_entry.grid(row=1,column=1,pady=10,padx=10, columnspan=4)

		self.warning_option = tk.Label(self.popup_window, text='Warning:', bg='white')
		self.warning_option.grid(row=0,column=3,padx=5,pady=5)

		levels = ['low', 'medium', 'high']
	
		self.warning_dropd = ttk.Combobox(self.popup_window, values=levels,width=10,state="readonly")
		self.warning_dropd.grid(row=0, column=4,padx=5,pady=5)

		self.send_button = tk.Button(self.popup_window, text='Send', bg='white')
		self.send_button.grid(row=2, column=4)

		self.supplier_label = tk.Label(self.popup_window, text='Supplier:', bg='white')
		self.supplier_label.grid(row=2,column=0)

		self.supplier_text = tk.Entry(self.popup_window, width='25')
		self.supplier_text.grid(row=2,column=1)
		#database = open("database.txt",'a')

	def __slide(self, index):

		temp_supplier = self.suppliers[index]
		num_articles = len(temp_supplier.articles)
		padding = 40 * num_articles

		if not temp_supplier.clicked:

			i = 0
			while (i < padding):

				temp_supplier.Separator.place(y=((index+1)*50)+40 + i, x = 0,relwidth=1)
				for j in range(index + 1,len(self.suppliers)):
					
					temp_supplier2 = self.suppliers[j]
			 		
					temp_supplier2.drop_button.place(y = ((j+1) * 50) + i, x = 650)
					temp_supplier2.warning_label.place(y = ((j+1) * 50)-5 + i, x = 610)
					temp_supplier2.article_label.place(y = ((j+1) * 50) + i, x = 590)
					temp_supplier2.name_label.place(y = ((j+1) * 50)+i, x = 0)
					temp_supplier2.Separator.place(y= ((j+1) *50)+40 + i, x = 0,relwidth=1)
				self.window.update()
				
				i += 2
			temp_supplier.clicked = True

			for k in range(0,num_articles):
				
				url = temp_supplier.articles[k].url
				self.add_url(k,url,temp_supplier,index)


		else:
			i = padding
			
			for k in range(0,num_articles):
				
				temp_supplier.links[k].destroy()
			del temp_supplier.links[:]

			while (i > 0):

				temp_supplier.Separator.place(y=((index+1)*50)+40 + i, x = 0,relwidth=1)
				for j in range(len(self.suppliers)-1, index , -1):
					
					temp_supplier2 = self.suppliers[j]
					temp_supplier2.drop_button.place(y = ((j+1) * 50) + i, x = 650)
					temp_supplier2.warning_label.place(y = ((j+1) * 50)-5 + i, x = 610)
					temp_supplier2.article_label.place(y = ((j+1) * 50) + i, x = 590)
					temp_supplier2.name_label.place(y = ((j+1) * 50) + i, x = 0)
					temp_supplier2.Separator.place(y= ((j+1) *50)+40 + i, x = 0,relwidth=1)
				self.window.update()

				i -= 2
			temp_supplier.clicked = False
			

	def callback(self,url):

		 webbrowser.open_new(url)
	def settings(self):

		self.popup_window = tk.Toplevel()
		self.popup_window.title('Settings')
		#self.popup_window.geometry("600x400")

		self.hwarning_label = tk.Label(self.popup_window, text='High Warning Triggers:')
		self.mwarning_label = tk.Label(self.popup_window, text='Medium Warning Triggers:')

		self.hwarning_entries = tk.Text(self.popup_window, width = 25, height = 10)
		self.mwarning_entries = tk.Text(self.popup_window, width = 25, height = 10)

		self.save_button = tk.Button(self.popup_window, text='Save', command=self.save)

		self.hwarning_label.grid(row=0, column = 0)
		self.mwarning_label.grid(row=1, column=0)

		self.hwarning_entries.grid(row=0,column = 1, padx = 10, pady = 10)
		self.mwarning_entries.grid(row=1,column = 1, padx = 10, pady = 10)

		self.save_button.grid(row=2,column=1)

		high_file = open('high_warning.txt', 'r')
		med_file = open('med_warning.txt','r')
		hwords = high_file.read()
		mwords = med_file.read()
		self.hwarning_entries.insert(END,hwords)
		self.mwarning_entries.insert(END,mwords)
		high_file.close()
		med_file.close()

		self.settings_button["state"] = "disabled" 
		self.add_button["state"] = "disabled" 
		self.window.wait_window(self.popup_window)
		self.add_button["state"] = "normal" 
		self.settings_button["state"] = "normal"

	def save(self):
		high_file = open('high_warning.txt', 'w')
		med_file = open('med_warning.txt','w')

		hwords = self.hwarning_entries.get("1.0",END)
		mwords = self.mwarning_entries.get("1.0",END)
		high_file.write(hwords)
		med_file.write(mwords)

		high_file.close()
		med_file.close()
		self.popup_window.destroy()
	def __pop_up(self):


		self.popup_window = tk.Toplevel()
		self.popup_window.title('New Suppliers')
		self.popup_window.geometry("400x150")
		self.text_label = tk.Label(self.popup_window, text='Enter Supplier name or Path:')
		self.supplier_entry = tk.Entry(self.popup_window, width = 25)
		self.text_label.pack(pady=10,padx=10)
		self.supplier_entry.pack()


		buttons_panel = tk.Frame(self.popup_window)

		ok_button = tk.Button(buttons_panel,text='Ok', command=self.__get_entry)
		browse_button = tk.Button(buttons_panel, text='Browse...', command=self.browse_button_func)

		browse_button.pack(side='left',pady=10,padx=10)
		ok_button.pack(side='left',pady=10,padx=10)
		buttons_panel.pack()

		self.add_button["state"] = "disabled" 
		self.settings_button["state"] = "disabled"
		self.window.wait_window(self.popup_window)
		self.settings_button["state"] = "normal"
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
		check.search_supplier(temp_supplier)
		temp_supplier.index = len(self.suppliers)
		self.suppliers.append(temp_supplier)

		number_of_articles = len(temp_supplier.articles)
		temp_supplier.name_label = tk.Label(self.window, text=self.text,background='#009EDC',fg='white')
		temp_supplier.name_label.place(y = (len(self.suppliers) * 50), x = 0)

		
		temp_supplier.warning_label = tk.Label(self.window,image = self.lwarning_photo,background='#009EDC')
		temp_supplier.warning_label.place(y = (len(self.suppliers) * 50)-5, x = 610)

		temp_supplier.article_label = tk.Label(self.window, text=number_of_articles,background='#009EDC')
		temp_supplier.article_label.place(y = (len(self.suppliers) * 50), x = 590)

		temp_supplier.Separator = ttk.Separator(self.window, orient='horizontal')
		temp_supplier.Separator.place(y=(len(self.suppliers)*50)+40, x = 0,relwidth=1)

		temp_supplier.drop_button = tk.Button(self.window, command = lambda: self.__slide(temp_supplier.index))
		temp_supplier.drop_button.config(image=self.arrow_photo, width='39', height='32',relief=tk.FLAT,background='#009EDC')
		temp_supplier.drop_button.place(y = (len(self.suppliers) * 50), x = 650)


	def add_url(self,k,url,temp_supplier,index):

		temp = tk.Button(self.window, text=temp_supplier.articles[k].title, fg="black", cursor="hand2", relief = tk.FLAT, anchor = 'w')

		temp_supplier.links.append(temp)
	
		temp.config(command = lambda: self.callback(url))
		temp.place(y=((index+1)*50)+40 + (k*40), x = 0,relwidth=1)


	def browse_button_func(self):
		suppliers = []
		self.directory = filedialog.askopenfile(parent=self.popup_window,mode='rb',title='Choose a file').name
		self.popup_window.destroy()
		with open(self.directory,'r') as file_object:	

			for line in file_object:
				self.text = line
				self.add_supplier()
			
test = checkerGui()

