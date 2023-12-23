import os

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
# ini文件路径
eleLocationPath = os.path.join(BASE_DIR, 'Settings/element_location.ini')
# print(eleLocationPath)


# 测试数据文件
testDataPath = os.path.join(BASE_DIR, 'TestData/163mail.xlsx')


