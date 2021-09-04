import pywhatkit as pkit
from openpyxl import Workbook,load_workbook


data = load_workbook("database.xlsx")
Database = data.active
