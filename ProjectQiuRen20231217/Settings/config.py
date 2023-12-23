import os.path

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_PATH)

iniFilePath = os.path.join(BASE_PATH, 'Settings/element_location.ini')
excelFilePath = os.path.join(BASE_PATH, 'TestData/163mail.xlsx')
