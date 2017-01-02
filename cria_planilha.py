# coding: UTF-8


try:
	from openpyxl import Workbook

except Exception as error:
	print("[!] Ocorreu um erro: {}" .format(error))


class Planilha(object):

	def __init__(self, nome):
		self.nome = nome

	def criar(self):

		wb = Workbook()
		wb.save(self.nome)