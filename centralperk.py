from centralperk_gui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from mysql.connector import connect
import datetime
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
from numberexception import NumberError

class Centralperk(QMainWindow,Ui_MainWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.init_lgnbtn()
		self.init_regbtn()
		self.init_nadmsubbtn()
		self.init_nadmbckbtn()
		self.init_ncsbtn()
		self.init_ncssubbtn()
		self.init_ncsbckbtn()
		self.init_uptcsidsubbtn()
		self.init_uptcsbtn()
		self.init_uptfbtn()
		self.init_nfoodsubbtn()
		self.init_nbevsubbtn()
		self.init_nfbbckbtn()
		self.init_foodaddbtn()
		self.init_bevaddbtn()
		self.init_delcsbtn()
		self.init_delcsidbtn()
		self.init_fbbckbtn()
		self.init_prcrbtn()
		self.init_dispallcsbtn()
		self.init_dispcsbtn()
		self.init_delbckbtn()
		self.init_dispallcsbckbtn()
		self.init_delfoodbtn()
		self.init_delbevbtn()
		self.init_foodpriceuptbtn()
		self.init_bevpriceuptbtn()
		self.init_uptf1btn()
		self.init_delfoodbevbckbtn()
		self.init_uptcsidbckbtn()
		self.init_csgraphbtn()
		self.init_foodgraphbtn()
		self.init_bevgraphbtn()
		self.init_extbtn()

	def init_lgnbtn(self):
		self.lgn_btn.clicked.connect(self.admlgn_details)


	def init_regbtn(self):
		self.reg_btn.clicked.connect(self.on_move_regadm)		


	def init_nadmsubbtn(self):
		self.nadmsub_btn.clicked.connect(self.admreg_details)

	def init_nadmbckbtn(self):
		self.nadmbck_btn.clicked.connect(self.on_move_logadm)

	def init_ncsbtn(self):
		self.newcs_btn.clicked.connect(self.on_move_newcs)

	def init_ncssubbtn(self):
		self.ncssub_btn.clicked.connect(self.ncs_details)

	def init_ncsbckbtn(self):
		self.ncsbck_btn.clicked.connect(self.on_move_cs)	

	def init_uptcsidsubbtn(self):
		self.uptcsidsub_btn.clicked.connect(self.uptcheckcs_details)

	def init_uptcsbtn(self):
		self.uptcs_btn.clicked.connect(self.on_move_csid)

	def init_uptfbtn(self):
		self.uptf_btn.clicked.connect(self.on_move_uptfoodbev)

	def init_nfoodsubbtn(self):
		self.nfoodsub_btn.clicked.connect(self.foodupt_details)

	def init_nbevsubbtn(self):
		self.nbevsub_btn.clicked.connect(self.bevupt_details)

	def init_nfbbckbtn(self):
		self.nfbbck_btn.clicked.connect(self.on_move_cs)

	def init_foodaddbtn(self):
		self.foodadd_btn.clicked.connect(self.csaddfood_details)

	def init_bevaddbtn(self):
		self.bevadd_btn.clicked.connect(self.csaddbev_details)

	def init_delcsbtn(self):
		self.delcs_btn.clicked.connect(self.on_move_delcsid)

	def init_delcsidbtn(self):
		self.delcsid_btn.clicked.connect(self.delcheckcs_details)

	def init_fbbckbtn(self):
		self.dispallcs_edt.setText('')
		self.fbbck_btn.clicked.connect(self.on_move_cs)

	def init_prcrbtn(self):
		self.prcr_btn.clicked.connect(self.printcs_details)

	def init_dispallcsbtn(self):
		self.dispallcs_btn.clicked.connect(self.printallcs)

	def init_dispcsbtn(self):
		self.dispcs_btn.clicked.connect(self.on_move_dispallcs)

	def init_delbckbtn(self):
		self.delbck_btn.clicked.connect(self.on_move_cs)
	def init_dispallcsbckbtn(self):
		self.dispallcsbck_btn.clicked.connect(self.on_move_cs)

	def init_delfoodbtn(self):
		self.delfood_btn.clicked.connect(self.delfood)

	def init_delbevbtn(self):
		self.delbev_btn.clicked.connect(self.delbev)

	def init_foodpriceuptbtn(self):
		self.foodpriceupt_btn.clicked.connect(self.updatefood)

	def init_bevpriceuptbtn(self):
		self.bevpriceupt_btn.clicked.connect(self.updatebev)

	def init_uptf1btn(self):
		self.uptf1_btn.clicked.connect(self.on_move_delupt)

	def init_delfoodbevbckbtn(self):
		self.delfoodbevbck_btn.clicked.connect(self.on_move_cs)

	def init_uptcsidbckbtn(self):
		self.uptcsidbck_btn.clicked.connect(self.on_move_cs)

	def init_csgraphbtn(self):
		self.csgraph_btn.clicked.connect(self.display_customergraph)

	def init_foodgraphbtn(self):
		self.foodgraph_btn.clicked.connect(self.display_foodgraph)

	def init_bevgraphbtn(self):
		self.bevgraph_btn.clicked.connect(self.display_bevgraph)

	def init_extbtn(self):
		self.ext_btn.clicked.connect(self.exit_code)						

	def on_move_regadm(self):
		self.stackedWidget.setCurrentIndex(1)		
	
	def on_move_logadm(self):
		self.stackedWidget.setCurrentIndex(0)

	def on_move_newcs(self):
		self.stackedWidget.setCurrentIndex(3)

	def on_move_cs(self):
		self.dispallcs_edt.clear()
		self.billdisp_edt.clear()
		self.nbevname_edt.clear()
		self.nfoodname_edt.clear()
		self.nbevprice_edt.clear()
		self.nfoodprice_edt.clear()
		self.food1price_edt.clear()
		self.bev1price_edt.clear()
		self.stackedWidget.setCurrentIndex(2)

	def on_move_csid(self):
		self.stackedWidget.setCurrentIndex(4)

	def on_move_uptfoodbev(self):
		self.stackedWidget.setCurrentIndex(6)

	def on_move_uptcs(self):
		self.stackedWidget.setCurrentIndex(5)						

	def on_move_delcsid(self):
		self.stackedWidget.setCurrentIndex(7)

	def on_move_dispallcs(self):
		self.stackedWidget.setCurrentIndex(8)

	def on_move_delupt(self):
		self.uptfbcmb_details()
		self.stackedWidget.setCurrentIndex(9)		
	def admlgn_details(self):	

		usr = self.usr_edt.text()
		passw = self.pass_edt.text()

		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select password from admins where username = %s'
		cursor = conn.cursor()
		cursor.execute(query,(usr,))
		row = cursor.fetchone()
		try:
			p=row[0]
			if p == passw:
				self.on_move_cs()
			else:
			#print('Enter username and password properly')
				self.showmessagebox('Error','Enter username and password properly')	
		except:
			self.showmessagebox('Error','Enter username and password properly')	
	
	def admreg_details(self):

		usr = self.nadmusr_edt.text()
		passw = self.nadmpass_edt.text()
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'insert into admins(username,password) values(%s,%s)'
		cursor = conn.cursor()
		cursor.execute(query,(usr,passw))
		conn.commit()
		cursor.close()	
		#print('Registered successfully')
		self.showmessagebox('Admin entry','Registered successfully')
		self.nadmusr_edt.clear()
		self.nadmpass_edt.clear()
		
	def ncs_details(self):

		name = self.ncsname_edt.text()
		try:
			mbn = self.ncsmbn_edt.text()
			mbnl = len(mbn)
			mbn = int(mbn)
			try:
				if mbnl !=10:
					raise NumberError()
				add = self.ncsadd_edt.toPlainText()
			#date = str(self.calendar.selectedDate().toPyDate().strftime('%d/%m/%Y'))
				date = self.calendar.selectedDate().toPyDate()
				month = str(date.month)
				date = str(date.strftime('%d/%m/%Y'))
				print(date)
				print(month)
				time = str(datetime.datetime.today().time())
				print(time)
		

				conn = connect(host='localhost',database='prototype',user='root',password='')
				query1 = 'insert into customers(name,mobileno,address,checkindate,checkintime) values(%s,%s,%s,%s,%s)'
				cursor = conn.cursor()
				cursor.execute(query1,(name,mbn,add,date,time))
				conn.commit()
				cursor.close()
			#print('New customer added successfully')
				self.showmessagebox('Customer Entry','New customer added successfully')

				query2 = 'select * from customer_record where month_id = %s'
				cursor = conn.cursor()
				cursor.execute(query2,(month,))
				row = cursor.fetchone()
				count = row[2]
				count += 1

				query3 = 'update customer_record set customer_count = %s where month_id = %s'

				cursor = conn.cursor()
				cursor.execute(query3,(count,month))
				conn.commit()
				cursor.close()
				self.ncsname_edt.clear()
				self.ncsadd_edt.clear()
				self.ncsmbn_edt.clear()
			except NumberError:
				
				self.showmessagebox('Customer Entry','Mobile Number must be of 10 characters only')
		except ValueError:
			self.showmessagebox('Customer Entry','Enter mobile number properly')				



	def uptcheckcs_details(self):
		try:
			id = int(self.uptcsid_edt.text())
			conn = connect(host='localhost',database='prototype',user='root',password='')
			query = 'select id from customers where id = %s'
			cursor = conn.cursor()
			cursor.execute(query,(id,))
			row = cursor.fetchone()
			try:
				p=row[0]
				if p == id:
					self.uptcs_lbl.setText('{}'.format(p))
					self.on_move_uptcs()
					self.food_cmb.clear()
					self.food1_cmb.clear()
					self.bev_cmb.clear()
					self.bev1_cmb.clear()
					self.uptfbcmb_details()
			except Exception:
			#print('Customer not found')
				self.showmessagebox('Error','Customer not found')
		except:
			self.showmessagebox('Error','Enter customer id properly')		


	def foodupt_details(self):

		food_name = self.nfoodname_edt.text()
		try:	
			food_price = float(self.nfoodprice_edt.text())
			conn = connect(host='localhost',database='prototype',user='root',password='')
			query = 'insert into foods(foodname,price) values(%s,%s)'
			cursor = conn.cursor()
			cursor.execute(query,(food_name,food_price))
			conn.commit()
			cursor.close()
			#print('Food data added successfully')
			self.showmessagebox('Food Entry','Food data added successfully')
		except Exception:
			self.showmessagebox('Food Entry','Enter food price properly')

	def bevupt_details(self):

		bev_name = self.nbevname_edt.text()
		try:
			bev_price = float(self.nbevprice_edt.text())
			conn = connect(host='localhost',database='prototype',user='root',password='')
			query = 'insert into bevs(bevname,price) values(%s,%s)'
			cursor = conn.cursor()
			cursor.execute(query,(bev_name,bev_price))
			conn.commit()
			cursor.close()
			#print('Beverage data added successfully')
			self.showmessagebox('Beverage Entry','Beverage data added successfully')
		except Exception:
			self.showmessagebox('Beverage Entry','Enter beverage price properly')	

	def addfitemscmb(self):
		l=[]
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from foods'
		cursor=conn.cursor()
		cursor.execute(query)
		row=cursor.fetchone()
		while row is not None:
			l.append(row[1])
			row=cursor.fetchone()
		self.food_cmb.clear()
		self.food1_cmb.clear()
		self.food_cmb.addItems(l)
		self.food1_cmb.addItems(l)


	def addbitemscmb(self):
		l=[]
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query='select * from bevs'
		cursor = conn.cursor()
		cursor.execute(query)
		row = cursor.fetchone()
		while row is not None:
			l.append(row[1])
			row=cursor.fetchone()
		self.bev_cmb.clear()
		self.bev1_cmb.clear()
		self.bev_cmb.addItems(l)
		self.bev1_cmb.addItems(l)	

	def uptfbcmb_details(self):
		self.addfitemscmb()
		self.addbitemscmb()


	def csaddfood_details(self):
		self.billdisp_edt.clear()
		x=int(self.uptcs_lbl.text())
		food_name = self.food_cmb.currentText()	
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from foods where foodname = %s'
		cursor=conn.cursor()
		cursor.execute(query,(food_name,))
		row=cursor.fetchone()
		price=row[2]
		food_count=row[3]
		food_count += 1
		cursor.close()

		query1 = 'select tbill from customers where id = %s'
		cursor = conn.cursor()
		cursor.execute(query1,(x,))
		row = cursor.fetchone()
		tb = row[0]
		tb += price

		query2  = 'select foods from customers where id = %s'
		cursor = conn.cursor()
		cursor.execute(query2,(x,))
		row = cursor.fetchone()
		fi = row[0]
		fi += food_name +','

		query3 = 'update customers set foods = %s,tbill=%s where id = %s'

		cursor = conn.cursor()
		cursor.execute(query3,(fi,tb,x))
		conn.commit()
		cursor.close()
		#print('{} is ordered'.format(food_name))
		self.showmessagebox('Order status','{} is ordered'.format(food_name))

		query4 = 'update foods set foodcount = %s where foodname = %s'

		cursor = conn.cursor()
		cursor.execute(query4,(food_count,food_name))
		conn.commit()
		cursor.close()
		



	def csaddbev_details(self):
		self.billdisp_edt.clear()
		x=int(self.uptcs_lbl.text())
		bev_name = self.bev_cmb.currentText()	
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from bevs where bevname = %s'
		cursor=conn.cursor()
		cursor.execute(query,(bev_name,))
		row=cursor.fetchone()
		price=row[2]
		bev_count = row[3]
		bev_count += 1

		cursor.close()

		query1 = 'select tbill from customers where id = %s'
		cursor = conn.cursor()
		cursor.execute(query1,(x,))
		row = cursor.fetchone()
		tb = row[0]
		tb += price

		query2  = 'select bevs from customers where id = %s'
		cursor = conn.cursor()
		cursor.execute(query2,(x,))
		row = cursor.fetchone()
		fi = row[0]
		fi += bev_name +','

		query3 = 'update customers set bevs = %s,tbill=%s where id = %s'

		cursor = conn.cursor()
		cursor.execute(query3,(fi,tb,x))
		conn.commit()
		cursor.close()
		#print('{} is ordered'.format(bev_name))
		self.showmessagebox('Order status','{} is ordered'.format(bev_name))

		query4 = 'update bevs set bevcount = %s where bevname = %s'

		cursor = conn.cursor()
		cursor.execute(query4,(bev_count,bev_name))
		conn.commit()
		cursor.close()
		


	def delcheckcs_details(self):
		
		conn = connect(host='localhost',database='prototype',user='root',password='')
		try:
			id = int(self.delcs_edt.text())
			query = 'select * from customers where id = %s'
			cursor = conn.cursor()
			cursor.execute(query,(id,))
			row = cursor.fetchone()
			try:
				p= row[0]
				query = 'delete from customers where id = %s'
				cursor = conn.cursor()
				cursor.execute(query,(id,))
				conn.commit()
				self.showmessagebox('Customer Deletion','Customer deleted successfully')
				cursor.close()

			except Exception:
				
				self.showmessagebox('Customer Deletion','Customer not found')		
			
		except Exception:
				
			self.showmessagebox('Customer Deletion','Invalid customer id')		
	

	def printcs_details(self):
		id = int(self.uptcs_lbl.text())	
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from customers where id =%s'
		cursor = conn.cursor()
		cursor.execute(query,(id,))
		row = cursor.fetchone()
		id1 = row[0]
		name = row[1]
		mobile = row[2]
		address = row[3]
		food_data = row[4]
		food_data = food_data[:len(food_data)-1]
		
		bev_data = row[5]
		bev_data = bev_data[:len(bev_data)-1]
		
		tbill = row[6]
		date=row[7]
		time=row[8]
		j=1
		#str1 = 'Customer id:-\t{0}\nName:-\t{1}\nMobile number:-\t{2}\nAddress:-\t{3}\n==============BILL=================\n\nFood items\tPrice\n{4}\t{5}'.format(row[0],row[1],row[2],row[3],row[4],row[5])
		str1 = '*************************CENTRAL PERK****************************\n\n  C-4,Avenue Street,Manhattan\n\nCustomer id:-\t{0}\nName:-\t{1}\nMobile number:-\t{2}\nAddress:-\t{3}\nCheckin date:-\t{4}\nCheckin time:-\t{5}\n\n==============BILL=================\n\nFood items\tPrice\n'.format(id1,name,mobile,address,date,time)
		str2 = ''
		if len(food_data) !=0:
			l1=food_data.split(',')
			for i in range(len(l1)):
				x=self.checkfoodprice(l1[i])
				str2 +='{0}.{1}\tRs.{2}\n'.format(j,l1[i],x)
				j+=1
		if len(bev_data) !=0:
			l2=bev_data.split(',')
			for i in range(len(l2)):
				x=self.checkbevprice(l2[i])
				str2 +='{0}.{1}\tRs.{2}\n'.format(j,l2[i],x)
				j+=1
		str3 ='\n==================================\n\tTotal bill:-{0}\n==================================='.format(tbill)
		str2+=str3		
		str1 +=str2		

		self.billdisp_edt.setText(str1)


	def printallcs(self):
		l=[]
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from customers'
		cursor=conn.cursor()
		cursor.execute(query)		
		row = cursor.fetchone()
		while row is not None:
			l.append((row[0],row[1],row[7],row[8]))
			row = cursor.fetchone()
		

		str1 = 'Customer id\tName\tDate\tTime\n\n'
		str2 = ''
		for i in range(len(l)):
			str2 += '{0}\t{1}\t{2}\t{3}\n'.format(l[i][0],l[i][1],l[i][2],l[i][3])

		str1 += str2
		self.dispallcs_edt.setText(str1)


	def showmessagebox(self,title,message):
		msgbox = QMessageBox()
		msgbox.resize(200,100)
		msgbox.setIcon(QMessageBox.Information)
		msgbox.setWindowTitle(title)
		msgbox.setText(message)
		msgbox.setStandardButtons(QMessageBox.Ok)
		msgbox.exec_()



	def checkfoodprice(self,food_name):	
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from foods where foodname = %s'
		cursor=conn.cursor()
		cursor.execute(query,(food_name,))
		row=cursor.fetchone()
		price=row[2]
		return price


	def checkbevprice(self,bev_name):	
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from bevs where bevname = %s'
		cursor=conn.cursor()
		cursor.execute(query,(bev_name,))
		row=cursor.fetchone()
		price=row[2]
		return price



	def delfood(self):
		food_name = self.food1_cmb.currentText()	
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'delete from foods where foodname = %s'
		cursor = conn.cursor()
		cursor.execute(query,(food_name,))
		conn.commit()
		self.showmessagebox('Food Deletion','Food data deleted successfully')
		self.food_cmb.clear()
		self.food1_cmb.clear()
		self.uptfbcmb_details()


	def delbev(self):
		bev_name = self.bev1_cmb.currentText()	
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'delete from bevs where bevname = %s'
		cursor = conn.cursor()
		cursor.execute(query,(bev_name,))
		conn.commit()
		self.showmessagebox('Beverage Deletion','Beverage data deleted successfully')	
		self.bev_cmb.clear()
		self.bev1_cmb.clear()
		self.uptfbcmb_details()

	def updatefood(self):
		food_name = self.food1_cmb.currentText()
		try:
			food_price = float(self.food1price_edt.text())	
			conn = connect(host='localhost',database='prototype',user='root',password='')
			query = 'update foods set price = %s where foodname = %s'
			cursor = conn.cursor()
			cursor.execute(query,(food_price,food_name))
			conn.commit()
			cursor.close()
			self.showmessagebox('Food Updation','Food data updated successfully')
			self.food_cmb.clear()
			self.food1_cmb.clear()
			self.uptfbcmb_details()
			self.food1price_edt.clear()
		except Exception:
			self.showmessagebox('Food Updation','Enter food price properly')	

	def updatebev(self):
		bev_name = self.bev1_cmb.currentText()
		try:
			bev_price = float(self.bev1price_edt.text())	
			conn = connect(host='localhost',database='prototype',user='root',password='')
			query = 'update bevs set price = %s where bevname = %s'
			cursor = conn.cursor()
			cursor.execute(query,(bev_price,bev_name))
			conn.commit()
			cursor.close()
			self.showmessagebox('Beverage Updation','Beverage data updated successfully')
			self.food_cmb.clear()
			self.food1_cmb.clear()
			self.uptfbcmb_details()
			self.bev1price_edt.clear()
	
		except Exception:
			self.showmessagebox('Beverage Updation','Enter Beverage price properly')
				





	def display_customergraph(self):
		d = {}
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from customer_record'		
		cursor=conn.cursor()
		cursor.execute(query)		
		row = cursor.fetchone()
		while row is not None:
			d[row[0]] = row[2]
			row = cursor.fetchone()
		print(d)	
		d = Series(d)
		print(d)
		d.plot(kind='bar')
		plt.show()
	


	def display_foodgraph(self):
		d = {}
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from foods'		
		cursor=conn.cursor()
		cursor.execute(query)		
		row = cursor.fetchone()
		while row is not None:
			d[row[1]] = row[3]
			row = cursor.fetchone()
		print(d)	
		d = Series(d)
		print(d)
		d.plot(kind='bar')
		plt.show()
	
	def display_bevgraph(self):
		d = {}
		conn = connect(host='localhost',database='prototype',user='root',password='')
		query = 'select * from bevs'		
		cursor=conn.cursor()
		cursor.execute(query)		
		row = cursor.fetchone()
		while row is not None:
			d[row[1]] = row[3]
			row = cursor.fetchone()
		#print(d)	
		d = Series(d)
		#print(d)
		d.plot(kind='bar')
		plt.show()
		


	
	def exit_code(self):
		QApplication.quit()	



if __name__ =='__main__':
	application = QApplication([])
	centralperk = Centralperk()

	centralperk.show()
	application.exec_()
