# coding: UTF-8


import openpyxl


class MyWorkbook(object):

    def __init__(self, name):
        self.name = name


    def criar(self):
        self.wb = openpyxl.Workbook()
        self.wb.save(self.name)