import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import messagebox
from tkinter import ttk
import ctypes
from tkinter import BOTH, RAISED, X, Y, END
import Checker as check
import time
import webbrowser
import sender

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class supplier:
	def __init__(self,name):
		self.name = name
		self.articles = []
		self.messages = []
		self.Separator = ''
		self.article_label = ''
		self.warning_label = ''
		self.name_label = ''
		self.drop_button = ''
		self.clicked = False
		self.index = 0
		self.links = []
		self.labels = []
		self.highest_warning = 0
		self.user = ''

class checkerGui:

	def __init__(self):


		self.window = tk.Tk()
		self.window.title("CASM")
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
		self.user = self.login_entry.get()
		self.background_label.destroy()
		self.login_entry.destroy()
		self.pass_entry.destroy()
		self.login_button.destroy()
		self.loading()
		self.tool_screen()
	def loading(self):
		
		self.window.config(bg='white')
		self.cover_pic = tk.PhotoImage(file='images/cover1.png')
		self.cover_pich = tk.PhotoImage(file='images/coverh.png')
		self.frames = [tk.PhotoImage(file='images/loading.gif',format = 'gif -index %i' %(i)) for i in range(24)]
		self.cisco_photo = tk.PhotoImage(file='images/cisco-513.png')
		self.cisco_logo = tk.Label(self.window, image=self.cisco_photo, bg = 'white')
		self.label = tk.Label(self.window, image=self.frames[0])
		self.cover_label = tk.Label(self.window, image=self.cover_pic, bg= 'white')
		self.cover_label2 = tk.Label(self.window, image=self.cover_pic, bg= 'white')
		self.cover_label3 = tk.Label(self.window, image=self.cover_pich, bg= 'white')
		self.cover_label4 = tk.Label(self.window, image=self.cover_pich, bg= 'white')

		self.cover_label4.place(y=530, x=288)
		self.cover_label3.place(y=393,x=288)
		self.cover_label2.place(x=418,y=395)
		self.cover_label.place(x=283,y=395)
		self.cisco_logo.place(x=250, y=210)
		self.label.place(x = 290,y = 400)
		
		
		i = 1
		j = 0
		while(j < 2):
			self.label.config(image=self.frames[i])
			i += 1
			if(i == 24):
				i=0
				j+=1
			self.window.update()
			time.sleep(.1)

		self.label.destroy()
		self.cisco_logo.destroy()
		self.cover_label.destroy()
		self.cover_label2.destroy()
		self.cover_label3.destroy()
		self.cover_label4.destroy()
		self.window.update()
		
	def tool_screen(self):

		self.suppliers = []
		self.menu_offset = 30
		self.scroller_items = []
		self.window.geometry("1000x800")
		self.window.configure(background='#0c4361')

		self.arrow_photo = tk.PhotoImage(file='./images/arrow2.png')
		self.gear_photo = tk.PhotoImage(file = './images/gear2.png')
		self.plus_photo = tk.PhotoImage(file = './images/add3.png')
		self.lwarning_photo = tk.PhotoImage(file = './images/low_warning3.png')
		self.hwarning_photo = tk.PhotoImage(file = './images/high_warning.png')
		self.plane_photo = tk.PhotoImage(file = './images/planec.png')
		self.refresh_photo = tk.PhotoImage(file = './images/refresh.png')

		self.add_button = tk.Button(self.window, command = self.__pop_up)
		self.add_button.config(image=self.plus_photo, width = '39', height = '38', relief=tk.FLAT,background='#0c4361')
		self.add_button.grid(row=0,column=0)

		self.settings_button = tk.Button(self.window, command=self.settings)
		self.settings_button.config(image=self.gear_photo, width = '39', height = '38', relief=tk.FLAT,background='#0c4361')
		self.settings_button.grid(row=0,column=1)
		
		self.database_button = tk.Button(self.window, image=self.plane_photo, width = '39', height = '38', relief=tk.FLAT, background='#0c4361')
		self.database_button.grid(row=0,column = 2)
		self.database_button.config(command=self.add_article)

		self.place_holder = tk.Label(self.window, width = '81', bg='#0c4361')
		self.place_holder.grid(row=0, column=3)
		self.refresh_button = tk.Button(self.window, image=self.refresh_photo, width = 39, height = 39, relief = tk.FLAT, background='#0c4361')
		self.refresh_button.grid(row=0, column=4)
		self.refresh_button.config(command=self.refresh)


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

		levels = ["No", 'Medium', 'High']
	
		self.warning_dropd = ttk.Combobox(self.popup_window, values=levels,width=10,state="readonly")
		self.warning_dropd.grid(row=0, column=4,padx=5,pady=5)

		self.send_button = tk.Button(self.popup_window, text='Send', bg='white', command=self.send_database)
		self.send_button.grid(row=2, column=4)

		self.supplier_label = tk.Label(self.popup_window, text='Supplier:', bg='white')
		self.supplier_label.grid(row=2,column=0)

		self.supplier_text = tk.Entry(self.popup_window, width='25')
		self.supplier_text.grid(row=2,column=1)
		

	def send_database(self):
		database = open("database.txt", 'a')
		supplier = self.supplier_text.get()
		message = self.mess_entry.get("1.0",END)
		warning = self.warning_dropd.get()
		title = self.title_entry.get()
		author = self.user

		while(message.endswith('\n')):
			message = message[:-1]

		database.write(supplier + '\n' + title + '\n' + warning + '\n' + message + '\n' + author + '\n')

		database.close()
		self.popup_window.destroy()


	def __slide(self, index):

		temp_supplier = self.suppliers[index]
		num_articles = len(temp_supplier.articles) + len(temp_supplier.messages)
		padding = 44 * num_articles

		if not temp_supplier.clicked:

			i = 0
			while (i < padding):

				temp_supplier.Separator.place(y=((index+1)*50)+40 + i, x = 0,relwidth=1)
				for j in range(index + 1,len(self.suppliers)):
					
					temp_supplier2 = self.suppliers[j]
			 		
					temp_supplier2.drop_button.place(y = ((j+1) * 50) - 8 + i, x = 950)
					
					temp_supplier2.article_label.place(y = ((j+1) * 50) + i, x = 890)
					temp_supplier2.name_label.place(y = ((j+1) * 50)+i, x = 0)
					temp_supplier2.Separator.place(y= ((j+1) *50)+40 + i, x = 0,relwidth=1)

					if(temp_supplier2.warning_label != ''):
						temp_supplier2.warning_label.place(y = ((j+1) * 50)-5 + i, x = 910)

				self.window.update()
				
				i += 2
			temp_supplier.clicked = True

			for k in range(0,len(temp_supplier.articles)):
				
				
				self.add_url(k,temp_supplier,index)

			for k in range(0,len(temp_supplier.messages)):
				self.add_message(k,temp_supplier,index)


		else:
			i = padding
			
			for k in range(0,num_articles):
				temp_supplier.links[k].destroy()
				temp_supplier.labels[k].destroy()
			del temp_supplier.links[:]
			del temp_supplier.labels[:]

			while (i > 0):

				temp_supplier.Separator.place(y=((index+1)*50)+40 + i, x = 0,relwidth=1)
				for j in range(len(self.suppliers)-1, index , -1):
					
					temp_supplier2 = self.suppliers[j]
					temp_supplier2.drop_button.place(y = ((j+1) * 50) - 8 + i, x = 950)
					temp_supplier2.article_label.place(y = ((j+1) * 50) + i, x = 890)
					temp_supplier2.name_label.place(y = ((j+1) * 50) + i, x = 0)
					temp_supplier2.Separator.place(y= ((j+1) *50)+40 + i, x = 0,relwidth=1)
					if(temp_supplier2.warning_label != ''):
						temp_supplier2.warning_label.place(y = ((j+1) * 50)-5 + i, x = 910)
				self.window.update()

				i -= 2
			temp_supplier.clicked = False
	
	def hover_on(self,event, placement, words):

		text_displayed = ''

		for word in words:
			text_displayed = text_displayed + word +', '
		
		text_displayed = text_displayed[:-2]

		self.hover_label = tk.Label(self.window, text=text_displayed)
		self.hover_label.place(x=415, y=placement - 10)

	def hover_off(self,event):
		self.hover_label.destroy()

	def callback(self,url):

		 webbrowser.open_new(url)

	
	def settings(self):

		self.popup_window = tk.Toplevel()
		self.popup_window.title('Settings')
		self.popup_window.config( bg='white')
		#self.popup_window.geometry("600x400")

		self.hwarning_label = tk.Label(self.popup_window, text='High Warning Triggers:', bg='white')
		self.mwarning_label = tk.Label(self.popup_window, text='Medium Warning Triggers:', bg='white')

		self.hwarning_entries = tk.Text(self.popup_window, width = 30, height = 8)
		self.mwarning_entries = tk.Text(self.popup_window, width = 30, height = 8)

		self.int_var = tk.IntVar(value=3)
		self.email_radio = tk.Radiobutton(self.popup_window,text = 'Email', bg='white',variable = self.int_var, value = 3)
		self.webex_radio = tk.Radiobutton(self.popup_window,text = 'Webex Teams', bg='white', variable = self.int_var, value = 4)
		self.mobile_radio = tk.Radiobutton(self.popup_window,text = 'Mobile', bg='white',variable = self.int_var, value = 5)

		self.save_button = tk.Button(self.popup_window, text='Save', command=self.save, bg='white')
		self.notification_label = tk.Label(self.popup_window, text='Notifications', bg='white')

		self.hwarning_label.grid(row=0, column = 0)
		self.mwarning_label.grid(row=1, column=0, padx=5)

		self.hwarning_entries.grid(row=0,column = 1, padx = 10, pady = 10)
		self.mwarning_entries.grid(row=1,column = 1, padx = 10, pady = 10)

		self.notification_label.grid(row=5, column=0)
		self.email_radio.grid(row=4, column=1)
		self.webex_radio.grid(row=5, column=1)
		self.mobile_radio.grid(row=6, column=1)
		self.save_button.grid(row=7,column=0, columnspan=2, pady=10)

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

		hwords = self.hwarning_entries.get("1.0",END).rstrip('\n')
		mwords = self.mwarning_entries.get("1.0",END).rstrip('\n')
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

		number_of_articles = len(temp_supplier.articles) + len(temp_supplier.messages)
		temp_supplier.name_label = tk.Label(self.window, text=self.text,background='#0c4361',fg='white')
		temp_supplier.name_label.place(y = (len(self.suppliers) * 50), x = 0)
		self.window.update()
		
		if(temp_supplier.highest_warning == 2):
			temp_supplier.warning_label = tk.Label(self.window,image = self.hwarning_photo,background='#0c4361')
			temp_supplier.warning_label.place(y = (len(self.suppliers) * 50)-5, x = 910)

		elif(temp_supplier.highest_warning == 1):
			temp_supplier.warning_label = tk.Label(self.window,image = self.lwarning_photo,background='#0c4361')
			temp_supplier.warning_label.place(y = (len(self.suppliers) * 50)-5, x = 910)

		temp_supplier.article_label = tk.Label(self.window, text=number_of_articles,background='#0c4361', fg='white')
		temp_supplier.article_label.place(y = (len(self.suppliers) * 50), x = 890)

		temp_supplier.Separator = ttk.Separator(self.window, orient='horizontal')
		temp_supplier.Separator.place(y=(len(self.suppliers)*50)+40, x = 0,relwidth=1)

		temp_supplier.drop_button = tk.Button(self.window, command = lambda: self.__slide(temp_supplier.index))
		temp_supplier.drop_button.config(image=self.arrow_photo, width='43', height='42',relief=tk.FLAT,background='#0c4361')
		temp_supplier.drop_button.place(y = (len(self.suppliers) * 50) - 8, x = 950)
		self.window.update()
		return temp_supplier

	def destroy_all(self):

		for supplier in self.suppliers:
			supplier.drop_button.destroy()
			supplier.Separator.destroy()
			supplier.article_label.destroy()
			if(supplier.highest_warning > 0):
				supplier.warning_label.destroy()
			supplier.name_label.destroy()

	def add_url(self,k,temp_supplier,index):

		url = temp_supplier.articles[k].url
		display = ''
		max = 36

		if(len(temp_supplier.articles[k].title) > max):
			display = temp_supplier.articles[k].title[:max] + '...'
		else:
			display = temp_supplier.articles[k].title

		temp = tk.Button(self.window, text=display, fg="black", cursor="hand2", relief = tk.FLAT, anchor = 'w')
		temp_supplier.links.append(temp)
		temp.config(command = lambda: self.callback(url), width = 33, height = 1, bg='#0c4361', fg='white', font="Verdana 10 underline")

		war_label = tk.Button(self.window, relief = tk.FLAT, bg='#0c4361')
		temp_supplier.labels.append(war_label)

		placement = ((index+1)*50)+35 + (k*40)
		words = temp_supplier.articles[k].words
		if(temp_supplier.articles[k].warning == 1):
			war_label.config(image=self.lwarning_photo, width=40, height=40)
			war_label.place(y=placement, x = 410)
			war_label.bind('<Enter>', lambda a, b = placement, c = words :self.hover_on(a, b, c))
			war_label.bind('<Leave>', lambda a: self.hover_off(a))


		elif(temp_supplier.articles[k].warning == 2):
			war_label.config(image=self.hwarning_photo, width=40, height=40)
			war_label.place(y=placement, x = 410)
			war_label.bind('<Enter>', lambda a, b = placement, c = words :self.hover_on(a, b, c))
			war_label.bind('<Leave>', lambda a: self.hover_off(a))

		temp.place(y=((index+1)*50)+40 + (k*40), x = 0)

	def add_message(self,k,temp_supplier,index):
		message = temp_supplier.messages[k]
		j = k + len(temp_supplier.articles)

		temp = tk.Button(self.window, text=message.title, fg="black", cursor="hand2", relief = tk.FLAT, anchor = 'w')
		temp_supplier.links.append(temp)
		#temp.config(command = lambda: self.open_message(message), width = 33, height = 1, bg='#0c4361', fg='white', font="Verdana 10 underline")
		temp.config( width = 33, height = 1, bg='#0c4361', fg='white', font="Verdana 10 underline")

		war_label = tk.Button(self.window, relief = tk.FLAT, bg='#0c4361')
		temp_supplier.labels.append(war_label)

		placement = ((index+1)*50)+35 + (j*40)
		words = temp_supplier.messages[k].words
		if(temp_supplier.articles[k].warning == 1):
			war_label.config(image=self.lwarning_photo, width=40, height=40)
			war_label.place(y=placement, x = 410)
			war_label.bind('<Enter>', lambda a, b = placement, c = words :self.hover_on(a, b, c))
			war_label.bind('<Leave>', lambda a: self.hover_off(a))


		elif(temp_supplier.messages[k].warning == 2):
			war_label.config(image=self.hwarning_photo, width=40, height=40)
			war_label.place(y=placement, x = 410)
			war_label.bind('<Enter>', lambda a, b = placement, c = words :self.hover_on(a, b, c))
			war_label.bind('<Leave>', lambda a: self.hover_off(a))

		temp.place(y=placement, x = 0)

	def browse_button_func(self):
		suppliers = []
		self.directory = filedialog.askopenfile(parent=self.popup_window,mode='rb',title='Choose a file').name
		self.popup_window.destroy()
		with open(self.directory,'r') as file_object:	

			for line in file_object:
				
				self.text = line.rstrip('\n')
				supp = self.add_supplier()
				if(supp.highest_warning == 2):
					suppliers.append(supp.name)
		if(suppliers != []):
			sender.send_email(self.user, suppliers)

	def refresh(self):
		email_suppliers = []
		temp = self.suppliers
		self.destroy_all()
		self.suppliers = []

		for supplier in temp:
			self.text = supplier.name
			supp = self.add_supplier()
			if(supp.highest_warning == 2):
				email_suppliers.append(supp.name)
		if(email_suppliers != []):
			sender.send_email(self.user, email_suppliers)

test = checkerGui()
