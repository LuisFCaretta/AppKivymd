#pylint:disable=W0614
#pylint:disable=W0401
#pylint:disable=W0401
#pylint:disable=W0611
#pylint:disable=W0611
#pylint:disable=W0311
from kivy import platform
from kivy.properties import ObjectProperty
from datetime import date, datetime, timedelta
from calendar import monthrange
import locale
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from math import fsum
from arquivos.Database import *
from kivy.core.window import Window
from plyer import orientation





locale.setlocale(locale.LC_TIME, '')
db = DataBaseControle

class PrimeiraTela(MDScreen):
	pass
	
class SegundaTela(MDScreen):
	
	def drpdown_(self):
		self.menu_list = [
					{"viewclass": "OneLineListItem",
					"text": "Cartão de crédito",
					"on_release": lambda x = "Cartão de crédito": self.cartao()
					},
					{"viewclass": "OneLineListItem",
					"text": "Residencial",
					"on_release": lambda x = "Residencial": self.residencial()
	 },
	 				{"viewclass": "OneLineListItem",
					"text": "Outros",
					"on_release": lambda x = "Outros": self.outros()
	 				    
	 				},
					
					{"viewclass": "OneLineListItem",
					"text": "Á vista",
					"on_release": lambda x = "A vista": self.a_vista()}
			]
		self.menu = MDDropdownMenu(
				caller = self.ids.botao_categoria_,
				items = self.menu_list,
				width_mult = 3
		)
		self.menu.open()
		
	def cartao(self):
		self.ids.input_categoria.text = 'Cartão'
	
	def residencial(self):
		self.ids.input_categoria.text = 'Residencial'
		
	def outros(self):
		self.ids.input_categoria.text = 'Outros'
	
	def a_vista(self):
	    self.ids.input_categoria.text = 'Á vista'
	
	
	
	
				
	
class TerceiraTela(MDScreen):
	pass

class QuartaTela(MDScreen):
	def drpdown_ver_(self):
		self.menu_list = [
					{"viewclass": "OneLineListItem",
					"text": "Cartão de crédito",
					"on_release": lambda x = "Cartão de crédito": self.cartao()
					},
					{"viewclass": "OneLineListItem",
					"text": "Residencial",
					"on_release": lambda x = "Residencial": self.residencial()
	 },
	 				{"viewclass": "OneLineListItem",
					"text": "Outros",
					"on_release": lambda x = "Outros": self.outros()
	 				    
	 				},
	 				
	 				{"viewclass": "OneLineListItem",
					"text": "Receita",
					"on_release": lambda x = "Receita": self.receita()}
					
				
			]
		self.menu = MDDropdownMenu(
				caller = self.ids.botao_categoria_,
				items = self.menu_list,
				width_mult = 3
		)
		self.menu.open()
		
	def cartao(self):
		self.ids.input_categoria_ver.text = 'Cartão'
	
	def residencial(self):
		self.ids.input_categoria_ver.text = 'Residencial'
		
	def outros(self):
		self.ids.input_categoria_ver.text = 'Outros'
		
	def receita(self):
		self.ids.input_categoria_ver.text = 'Receita'
	
			
	def sit_ver_(self):
		self.menu_list = [
						
					{"viewclass": "OneLineListItem",
					"text": "Em aberto",
					"on_release": lambda x = "aberto": self.aberto()},
			
					
					{"viewclass": "OneLineListItem",
					"text": "Pago",
					"on_release": lambda x = "A vista": self.a_vista_()}
					
			]
		self.menu = MDDropdownMenu(
				caller = self.ids.botao_sit_,
				items = self.menu_list,
				width_mult = 3
		)
		self.menu.open()
		
	def aberto(self):
	    self.ids.input_sit_ver.text = 'Em aberto'
	
	def a_vista_(self):
	    self.ids.input_sit_ver.text = 'Pago'
	    
	    		
	def select_year(self, value):
		busca_ano = []
		busca_mes = []
		busca_mes.append(self.ids.botao_mes.text)
		busca_ano.append(self.ids.botao_ano.text)
		self.ids.input_data_inicio.text = f'01/{busca_mes[0][:2]}/{busca_ano[0]}'
		
		
		
		dat_final = f'{busca_ano[0]}-{busca_mes[0][:2]}-28'
		dat_final = datetime.strptime(str(dat_final), "%Y-%m-%d").date()
		
		data_final_ = dat_final.replace(day=1) + timedelta(monthrange(dat_final.year, dat_final.month)[1] - 1)
		
		data_final = data_final_.strftime('%d/%m/%Y')

		self.ids.input_data_final.text = f'{data_final}'
			
		return busca_ano, busca_mes
			
	
class QuintaTela(MDScreen):
	def drpdown_receita(self):
		self.menu_list = [
					{"viewclass": "OneLineListItem",
					"text": "Receita",
					"on_release": lambda x = "Receita": self.receita()}
			]
		self.menu = MDDropdownMenu(
				caller = self.ids.botao_categoria_receita,
				items = self.menu_list,
				width_mult = 3
		)
		self.menu.open()
	
	def receita(self):
		self.ids.input_categoria_receita.text = 'Receita'
				

			
class SextaTela(MDScreen):
	def drpdown_e_(self):
		self.menu_list = [
					{"viewclass": "OneLineListItem",
					"text": "Cartão de crédito",
					"on_release": lambda x = "Cartão de crédito": self.cartao()
					},
					{"viewclass": "OneLineListItem",
					"text": "Residencial",
					"on_release": lambda x = "Residencial": self.residencial()
	 },
	 				{"viewclass": "OneLineListItem",
					"text": "Outros",
					"on_release": lambda x = "Outros": self.outros()}
					
	            
			]
		self.menu = MDDropdownMenu(
				caller = self.ids.botao_categoria_,
				items = self.menu_list,
				width_mult = 3
		)
		self.menu.open()
		
	def cartao(self):
		self.ids.input_categoria.text = 'Cartão'
	
	def residencial(self):
		self.ids.input_categoria.text = 'Residencial'
		
	def outros(self):
		self.ids.input_categoria.text = 'Outros'
	
 
	
class MainApp(MDApp):
	drpdown_ver_ = ObjectProperty(None)
	data_table = ObjectProperty(None)
	drpdown_ = ObjectProperty(None)
	dialog = None
	dialog_exit = None
	
	
	def on_start(self):
	    from kivy.base import EventLoop
	    EventLoop.window.bind(on_keyboard=self.hook_keyboard)
	def hook_keyboard(self, window, key, *largs):
	    if key == 27:
        	self.show_alert_exit()
        	return True
        	
        	
	def build(self):
		self.theme_cls.material_style = "M3"
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'BlueGray'
		return Builder.load_file('main.kv')
		
		
		
	    		
							
	def on_save(self, instance, value, date_range):
		data = str(value)
		dat = datetime.strptime(f'{data}', "%Y-%m-%d").date()
		dataFormatada = dat.strftime('%d/%m/%Y')
		self.root.ids.janela2.ids.input_data.text = f'{dataFormatada}'
		self.root.ids.janela6.ids.input_data.text = f'{dataFormatada}'
		self.root.ids.janela5.ids.input_data_receita.text = f'{dataFormatada}'
		
	def on_cancel(self, instance, value):
		pass
		
		
	def show_date_picker(self):
		date_dialog = MDDatePicker()
		date_dialog.bind(on_save=self.on_save,  on_cancel=self.on_cancel)
		date_dialog.open()
		
	
	def on_save1(self, instance, value, date_range):
		dati = datetime.strptime(str(date_range[0]), "%Y-%m-%d").date()
		datf = datetime.strptime(str(date_range[-1]), "%Y-%m-%d").date()
		data_inicio = dati.strftime('%d/%m/%Y')
		data_final = datf.strftime('%d/%m/%Y')
		#data_final_ = dati.replace(day=1) + timedelta(monthrange(dati.year, dati.month)[1] - 1)
		self.root.ids.janela4.ids.input_data_inicio.text = f'{data_inicio}'
		self.root.ids.janela4.ids.input_data_final.text = f'{data_final}'
		
		
	def on_cancel1(self, instance, value):
		pass
	
	def show_date_picker1(self):
		date_dialog1 = MDDatePicker(mode= "range")
		date_dialog1.bind(on_save=self.on_save1,  on_cancel=self.on_cancel1)
		date_dialog1.open()
 
 
	def valores(self):
		meses = ['01 Janeiro', '02 Fevereiro', '03 Março', '04 Abril', '05 Maio', '06 Junho', '07 Julho', '08 Agosto', '09 Setembro', '10 Outubro', '11 Novembro', '12 Dezembro']
		for mes in meses:
		    if self.root.ids.janela4.ids.botao_mes.text in mes:
		    	self.root.ids.janela3.ids.date_filter.text = f'{mes[2:]}/{self.root.ids.janela4.ids.botao_ano.text}'
		sub = float()
		debitos = float()
		menos = float()
		saldo = float()
		saldo_atual = float()
		for row in db().fetch_all():
			if row[5] == 'Receita':
				saldo += float(row[2].replace(',', '.'))
				
			if row[5] == 'Pago':
				sub += float(row[2].replace(',', '.'))
				
			if row[5] == 'Em aberto':
				debitos += float(row[2].replace(',', '.'))
				
		
		saldo_atual = saldo - sub
		self.root.ids.janela3.ids.label_valor.text = f'{debitos:.2f}'.replace('.', ',')
		self.root.ids.janela3.ids.label_saldo.text = f'{saldo_atual:.2f}'.replace('.', ',')
		
		
		
	def get_all_data(self):
		Categoria = self.root.ids.janela4.ids.input_categoria_ver.text
		data_inicio = self.root.ids.janela4.ids.input_data_inicio.text
		data_final = self.root.ids.janela4.ids.input_data_final.text
		status = self.root.ids.janela4.ids.input_sit_ver.text
				
		if Categoria and data_inicio != '':
		    Categoria = self.root.ids.janela4.ids.input_categoria_ver.text
		    dati = datetime.strptime(str(self.root.ids.janela4.ids.input_data_inicio.text), "%d/%m/%Y").date()
		    data_inicio_ = dati.strftime("%d/%m/%Y")
		    
		    datf = datetime.strptime(str(self.root.ids.janela4.ids.input_data_final.text), "%d/%m/%Y").date()
		    data_atual = date.today()
		    data_final_ = dati.replace(day=1) + timedelta(monthrange(dati.year, dati.month)[1] - 1)
		    data_final = datf.strftime("%d/%m/%Y")
		    data = []
		    debit = float()
		    if status == '':
		    	for row in db().filter_all(Categoria, data_inicio, data_final_):
		    		data.append(row)
		    		if row[5] == 'Em aberto':
				        debit += float(row[2].replace(',', '.'))
		    	self.valores()
		    	self.root.ids.janela3.ids.debit_filter.text = f'R${debit:.2f}'.replace('.', ',')
		    	return data
		    	
		    else:
		      for row in db().filter_all(Categoria, dati, data_final_):
		      	if f'{status}' in row[5]:
		      		data.append(row)
		      		if row[5] == 'Em aberto':
				        debit += float(row[2].replace(',', '.'))
		    self.valores()
		    self.root.ids.janela3.ids.debit_filter.text = f'R${debit:.2f}'.replace('.', ',')
		    return data
			
		    	
		    
		
		if data_inicio != '':
			dati = datetime.strptime(str(self.root.ids.janela4.ids.input_data_inicio.text), "%d/%m/%Y").date()
			data_inicio = dati.strftime("%d/%m/%Y")
			data_atual = date.today()
			data_final_ = dati.replace(day=1) + timedelta(monthrange(dati.year, dati.month)[1])
			data = []
			debit = float()
			if status == '':
				for row in db().filter_month(dati, data_final_):
					data.append(row)
					if row[5] == 'Em aberto':
				    		debit += float(row[2].replace(',', '.'))
				self.valores()
				self.root.ids.janela3.ids.debit_filter.text = f'R${debit:.2f}'.replace('.', ',')
				return data
				
				
			else:
				for row in db().filter_month(dati, data_final_):
					if f'{status}' in row[5]:
						data.append(row)
						if row[5] == 'Em aberto':
							debit += float(row[2].replace(',', '.'))
					self.valores()
					self.root.ids.janela3.ids.debit_filter.text = f'R${debit:.2f}'.replace('.', ',')
					return data
				
				
	
		elif Categoria != '':
		    Categoria = self.root.ids.janela4.ids.input_categoria_ver.text
		    data = []
		    debit = float()
		    if status == '':
		        for row in db().filter_categoria(Categoria):
		        	data.append(row)
		        	if row[5] == 'Em aberto':
		        		debit += float(row[2].replace(',', '.'))
		        self.root.ids.janela3.ids.debit_filter.text = f'R${debit:.2f}'.replace('.', ',')
		        self.valores()
		        return data
		    
		    else:
		        for row in db().filter_categoria(Categoria):
		        	if f'{status}' in row[5]:
		        	    data.append(row)
		        	    if row[5] == 'Em aberto':
		        	    	debit += float(row[2].replace(',', '.'))
		        self.valores()
		        self.root.ids.janela3.ids.debit_filter.text = f'R${debit:.2f}'.replace('.', ',')
		        return data
			    	
		    
		else:
			data_atual = date.today()
			data_inicio = date.today().replace(day=1)
			data_final = data_atual.replace(day=1) + timedelta(monthrange(data_atual.year, data_atual.month)[1])
			data = []
			debit = float()
			if status == '':
				for row in db().filter_month(data_inicio, data_final):
					data.append(row)
					if row[5] == 'Em aberto':
					     debit += float(row[2].replace(',', '.'))
				self.root.ids.janela3.ids.debit_filter.text = f'R${debit:.2f}'.replace('.', ',')
					
				self.valores()
				return data
				
			
			else:
				for row in db().filter_month(data_inicio, data_final):
					if f'{status}' in row[5]:
					    data.append(row)
				self.valores()
				return data


	   
	def show_alert_dialog(self):
		if not self.dialog:
			self.dialog = MDDialog(
				text = 'Deseja marcar como pago?',
				buttons = [
						MDFlatButton(
							text = 'Cancel', text_color = self.theme_cls.primary_color, on_release = self.fechar_alerta),
						MDRectangleFlatButton(
							text = 'Ok', text_color = self.theme_cls.primary_color, on_release = self.atualizar_status)
						]
			)
		self.dialog.open()
	
	def fechar_alerta(self):
		self.dialog.dismiss()
		
				
	def show_alert_exit(self):
		if not self.dialog_exit:
			self.dialog_exit = MDDialog(
				text = 'Deseja sair?',
				buttons = [
						MDFlatButton(
							text = 'Cancel', text_color = self.theme_cls.primary_color, on_release = self.fechar_alerta_),
						MDRectangleFlatButton(
							text = 'Ok', text_color = self.theme_cls.primary_color, on_release = exit)
						]
			)
		self.dialog_exit.open()

		
	def fechar_alerta_(self, obj):
		self.dialog_exit.dismiss()
		

	


	def ver_tabela(self):
		self.data_table = MDDataTable(							background_color_header= '#657895',
																										background_color_selected_cell='#657895',
							
				      	  size_hint=(1.07, 0.68),
				        	pos_hint= {'center_x': 0.48, 'center_y': 0.58},
				            use_pagination= False,
				            rows_num = 500,
				            column_data=[
				               ("id", dp(10)),
				               ("Conta", dp(25)),
				               ("Valor", dp(20)),
				               ("Vencimento", dp(25)),
				               ("Categoria", dp(25)),
				               ("Status", dp(20))
				               
				            ]
				        )
		
		self.data_table.bind(on_row_press = self.row_selected)
		
		
		self.data_table.row_data = self.get_all_data()
		self.valores()

		
		self.root.ids.janela3.add_widget(self.data_table)
		return self.data_table
		
	
					
	def row_selected(self, table, row):
		start_index, end_index = row.table.recycle_data[row.index]["range"]
		self.populate_form(row.table.recycle_data[start_index]["text"])
		
		
		
		
	def cadastrar_dados(self):
		conta = self.root.ids.janela2.ids.input_conta.text.strip()
		valor = self.root.ids.janela2.ids.input_valor.text
		data = self.root.ids.janela2.ids.input_data.text.strip()
		categ = self.root.ids.janela2.ids.input_categoria.text
	
		if conta or valor or data or categ == '':
			self.root.ids.janela2.ids.msg_label.text = 'Necessario preencher todos os campos.'
				
		if conta and valor and data and categ != '':
			
				conta = self.root.ids.janela2.ids.input_conta.text
				valorf = float(valor)
				valorFormatado = f'{valorf:.2f}'.replace('.', ',')
				
				dat = datetime.strptime(str(self.root.ids.janela2.ids.input_data.text), "%d/%m/%Y").date()
				data = dat.strftime("%d/%m/%Y")
				categoria = self.root.ids.janela2.ids.input_categoria.text
				Status = 'Em aberto'
				if categoria == 'Á vista':
				    Status = 'Pago'
				
				if categoria != 'Cartão':
					db().insert(conta, valorFormatado, dat, categoria, Status)
					self.remove_campos()
					self.root.ids.janela2.ids.msg_label.text = 'conta adicionada com sucesso!'
					return
				if categoria == 'Cartão':
					quant = self.root.ids.janela2.ids.label_parcela.text
					cur_date = dat
					if quant == '':
						self.root.ids.janela2.ids.msg_label.text = 'Obrigatório definir uma quantidade.'
					else:
						conta = f'{self.root.ids.janela2.ids.input_conta.text} 1/{quant}'
						db().insert(conta, valorFormatado, dat, categoria, Status)
						quant= int(self.root.ids.janela2.ids.label_parcela.text)
						for p in range(2, quant+1):
							conta = f'{self.root.ids.janela2.ids.input_conta.text} {p}/{quant}'
							cur_date += timedelta(days=31)
							
							db().insert(conta, valorFormatado, cur_date, categoria, Status)
						self.remove_campos()
						self.root.ids.janela2.ids.msg_label.text = 'conta adicionada com sucesso!'
						return
				
				
				
	def cadastrar_receita(self):
		conta = self.root.ids.janela5.ids.input_receita.text.strip()
		valor = self.root.ids.janela5.ids.input_valor_receita.text
		data = self.root.ids.janela5.ids.input_data_receita.text.strip()
		categ = self.root.ids.janela5.ids.input_categoria_receita.text
	
		if conta or valor or data or categ == '':
			self.root.ids.janela5.ids.receita_label.text = 'Necessario preencher todos os campos.'
				
		if conta and valor and data and categ != '':
			
				conta = self.root.ids.janela5.ids.input_receita.text
				valorf = float(valor)
				valorFormatado = f'{valorf:.2f}'.replace('.', ',')
				
				dat = datetime.strptime(str(self.root.ids.janela5.ids.input_data_receita.text), "%d/%m/%Y").date()
				data = dat.strftime("%d/%m/%Y")
				
				
				categoria = self.root.ids.janela5.ids.input_categoria_receita.text
				Status = f'{categoria}'
			
			
				db().insert(conta, valorFormatado, dat, categoria, Status)
				self.remove_campos()
				self.root.ids.janela5.ids.receita_label.text = f'{conta} adicionado com sucesso!'
	
				
	def atualizar_status(self,id):
		self.dialog.dismiss()
		if self.root.ids.janela6.ids.id.text == '':
			pass
		else:
			id = self.root.ids.janela6.ids.id.text
			db().update_status(id)
			self.data_table.row_data = self.get_all_data()
			self.remove_campos()
													
				
	def atualizar_dados(self):
		if self.root.ids.janela6.ids.id.text == '':
			pass
		else:
			id = self.root.ids.janela6.ids.id.text
			conta = self.root.ids.janela6.ids.input_conta.text
			valorf = float(self.root.ids.janela6.ids.input_valor.text.replace(',', '.'))
			valor = f'{valorf:.2f}'.replace('.', ',')
			dat = datetime.strptime(self.root.ids.janela6.ids.input_data.text, "%Y-%m-%d").date()
			data = dat.strftime('%d/%m/%Y')
				
			categ = self.root.ids.janela6.ids.input_categoria.text
			if categ == 'Receita':
				status = 'Receita'
			if categ == 'Á vista':
				status = 'Pago'
			else:
				status = ' Em aberto'
				
					
					
				db().update(conta, valor, dat, categ, status, id)
				self.data_table.row_data = self.get_all_data()
				self.remove_campos()
			
			
	def delete(self):
		id = self.root.ids.janela6.ids.id.text
		db().delete(id)
		self.data_table.row_data = self.get_all_data()
		self.remove_campos()
			

	def remove_campos(self):
		self.root.ids.janela2.ids.msg_label.text = ''
		self.root.ids.janela2.ids.input_categoria.text = ''
		self.root.ids.janela2.ids.input_conta.text = ''
		self.root.ids.janela2.ids.input_valor.text = ''
		self.root.ids.janela2.ids.input_data.text = ''
		self.root.ids.janela2.ids.label_parcela.text = ''
		
		self.root.ids.janela4.ids.input_categoria_ver.text = ''
		self.root.ids.janela4.ids.input_data_inicio.text = ''
		self.root.ids.janela4.ids.input_data_final.text = ''
		self.root.ids.janela4.ids.input_sit_ver.text = ''
		self.root.ids.janela4.ids.botao_mes.text = f'{date.today().month}'
		self.root.ids.janela4.ids.botao_ano.text = f'{date.today().year}'
		self.root.ids.janela5.ids.input_receita.text = ''
		self.root.ids.janela5.ids.input_valor_receita.text = ''
		self.root.ids.janela5.ids.input_data_receita.text = ''
		self.root.ids.janela5.ids.input_categoria_receita.text = ''
		self.root.ids.janela6.ids.date_label.text = ''
		self.root.ids.janela6.ids.input_categoria.text = ''
		self.root.ids.janela6.ids.input_conta.text = ''
		self.root.ids.janela6.ids.input_valor.text = ''
		self.root.ids.janela6.ids.input_data.text = ''
		self.root.ids.janela6.ids.id.text = ''
		
	def populate_form(self, row_id):
		row_data = db().get_record_by_id(row_id)
		self.root.ids.janela6.ids.id.text = str(row_data[0])
		self.root.ids.janela6.ids.input_conta.text = row_data[1]
		self.root.ids.janela6.ids.input_valor.text = str(row_data[2])
		self.root.ids.janela6.ids.input_data.text = row_data[3]
		self.root.ids.janela6.ids.input_categoria.text = row_data[4]
			
	
if __name__ == '__main__':
	orientation.set_sensor('portrait')
	MainApp().run()