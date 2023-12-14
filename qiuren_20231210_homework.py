"""
1、难度等级 II
给定⼀个整数数组 nums 和⼀个整数⽬标值 target，请你在该数组中找出 和为⽬标值
target 的那 两个 整数，并返回它们的数组下标。
如 nums = [2,7,11,15], target = 9
输出：[0,1]
⽤两种⽅法实现（实在想不出，⾄少实现⼀种）
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def find_index1(nums=[2, 7, 11, 15], target=9):
    result_l = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result_l.extend((i, j))
                return result_l
    return "没有这样的两个下标"


def find_index2(nums=[2, 7, 11, 15], target=9):
    result_l = []
    for i in range(len(nums) - 1):
        n = target - nums[i]
        if n in nums[i + 1:]:
            j = nums.index(n)
            result_l.extend((i, j))
            return result_l
    return "没有这样的两个下标"


# print(find_index1([3, 7, 11, 3, 6, 5, 5, 6, 7]))
# print(find_index2([3, 7, 11, 3, 6, 5, 5, 6, 7]))

"""
2、难度等级I
从字符串⾥提取单词，例如”my name is cc“，将单词放到列表⾥，
不要⽤ split ⽅法
"""


def split_str(strs="my name is cc"):
    result_l = []
    for i in strs:
        if i == " ":
            s_end = strs.index(i)
            result_l.append(strs[:s_end])
            strs = strs[s_end + 1:]
    result_l.append(strs)
    return result_l


# print(split_str())

"""
3、难度等级I
⽣成矩阵
已知两个列表
lst_1 = [1, 2, 3, 4]
lst_2 = ['a', 'b', 'c', 'd']
将两个列表交叉相乘 得到
[['1a', '2a', '3a', '4a'],
 ['1b', '2b', '3b', '4b'],
 ['1c', '2c', '3c', '4c'],
 ['1d', '2d', '3d', '4d']]
"""


def make_matrix1(lst_1=[1, 2, 3, 4], lst_2=['a', 'b', 'c', 'd']):
    result_l = []
    for x in range(len(lst_2)):
        l = []
        for y in lst_1:
            l.append(str(y) + lst_2[x])
        result_l.append(l)
    return result_l


# print(make_matrix1())

# 1、先生成n维列表
# 2、填充n维列表
def make_matrix2(lst_1=[1, 2, 3, 4], lst_2=['a', 'b', 'c', 'd']):
    result_l = [[[] for i in range(len(lst_1))] for j in range(len(lst_2))]
    for x in lst_1:
        for y in range(len(lst_2)):
            result_l[y][x - 1] = (str(x) + lst_2[y])
    return result_l


# print(make_matrix2())

"""
4.难度等级II
B站⾯试题
⽐较版本号，给⼀个["2.1.0", "1.5", "2", "1.1.999.1.2.3", "0.10.0"] 要求
从⼩到⼤排序
"""


def versions_sort(versions=["2.1.0", "1.50", "2", "1.1.999.1.2.3", "0.10.0"]):
    # 处理数据转换成列表（试过去掉.转换成数字类型来比较大小，失败因为：1.10、11.0，无法区分）
    versions_l = list(map(lambda x: x.split("."), versions))
    # print(versions_l)
    # 需要转换成数字再依次进行比较，因为字符"21"比”4“小
    for i in versions_l:
        for j in range(len(i)):
            i[j] = int(i[j])
    # 排序
    versions_l.sort(key=lambda x: x[:])
    # print(versions_l)
    # 还原数据
    for i in versions_l:
        for j in range(len(i)):
            i[j] = str(i[j])
    versions_ll = list(map(lambda x: ".".join(x), versions_l))
    return versions_ll


print(versions_sort(["2.1.0", "21.3.0", "4.4.0", "21.2.9"]))
print(versions_sort(["11.1", "4.0.2", "1.12"]))
print(versions_sort())

"""
5. 难度等级I
完成 163邮箱从登录到发送邮件的线性代码
"""


def locate_element(driver, type, express):
    try:
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element(type, express))
    except Exception as e:
        raise e
    return driver.find_element(type, express)

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://mail.163.com/")
driver.maximize_window()
iframe = locate_element(driver, By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
locate_element(driver, By.NAME, "email").send_keys("qiuren202312")
locate_element(driver, By.NAME, "password").send_keys("qiuren12345A")
locate_element(driver, By.ID, "dologin").click()
locate_element(driver, By.XPATH, '//*[@id="_mail_component_76_76"]').click()
locate_element(driver, By.CLASS_NAME, "nui-editableAddr-ipt").send_keys("qiuren202312@163.com")
locate_element(driver, By.XPATH,
               '/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input').send_keys("123")
locate_element(driver, By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/section/footer/div[1]/span[2]').click()
sleep(5)
driver.quit()