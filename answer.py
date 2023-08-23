# 一、物件導向、介面/繼承
# 今有車輛「汽車」和「機車」,請使用物件的繼承/介面描述二者相同與差異,及二物件的執行程式碼
# 因 python 沒有interface，此題改用 golang 作答，並將答案置於Q1.go中

# 二、資料處理-字串
# 請寫出將字串「人易科技:上機測驗-演算法」中的:

# 1. 字元「:」改成全型
strings = "人易科技:上 機 測 驗 - 演算法"
def func(strings):
    strings = list(strings)
    for index in range(len(strings)):
        if strings[index] == ":":
            strings[index] = '：'
    return "".join(strings)
print(func(strings))
#人易科技：上 機 測 驗 - 演算法


# 2. 去掉中文字間的空白(保留-號二側空白)
strings = "人易科技:上 機 測 驗 - 演算法"
def func(strings):
    strings = list(strings)
    for index in range(len(strings)):
        if strings[index] == " ":
            strings[index] = ""
        elif strings[index] == "-":
            strings[index] = " - "
    return "".join(strings)
print(func(strings))
#人易科技:上機測驗 - 演算法

# 3. 列印出符號:到-之間的字元
strings = "人易科技:上 機 測 驗 - 演算法"
def print_between(strings):
    charflag = 0 
    char2flag = 0 
    for index in range(len(strings)):
        if strings[index] ==":":
            charflag = index
        if strings[index] =="-":
            char2flag = index
    if charflag>char2flag:
        return
    else:
        for i in strings[charflag+1 : char2flag]:
            print(i)

print_between(strings)
#上
# 
#機
# 
#測
# 
#驗
#

# 三、資料處理-陣列
# 今有陣列資料 0,1,2,3,4,5,6,7,8,9請寫出資料處理程式碼

# 1. 計算出「奇數值總和」減去「偶數值總和」
nums = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]

def odd_minus_even(nums):
    odd = 0
    even = 0
    for i in nums:
        if i%2:
            odd += i
        else:
            even += i
    return odd-even
print(odd_minus_even(nums))
#5

# 2. 分割成二陣列,分別存放「偶數值」及「奇數值」
nums = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
def split(nums):
    odd_nums = []
    even_nums = []
    for i in nums:
        if i%2:
            odd_nums.append(i)
        else:
            even_nums.append(i)
    return even_nums , odd_nums 

even_nums ,odd_nums = split(nums)

print(even_nums , odd_nums)
#[0, 2, 4, 6, 8] [1, 3, 5, 7, 9]

# 四、資料排序-正序
# 今有一陣列資料77 , 5 , 5 , 22 , 13 , 55 , 97 , 4 , 796 , 1 , 0 , 9 請寫出正序排列處理程式碼
# 本題需自行完成演算法,不可使用現成排序函式
nums = [77 , 5 , 5 , 22 , 13 , 55 , 97 , 4 , 796 , 1 , 0 , 9]
def sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort(left) + middle + sort(right)

print(sort(nums))
#[0, 1, 4, 5, 5, 9, 13, 22, 55, 77, 97, 796]

# 五、邏輯處理-交集、差集、聯集
# 今有二陣列,請寫出資料處理程式碼
# 陣列a:77.5.5.22,13,55.97.4,796,1,0,9
# 陣列b:0,1,2,3,4,5,6,7,8,9
# 本题需自行完成演算法,不可使用現成交集/差/聯集函式

# 1.陣列c = 陣列a 交集 陣列b
a = [ 77 , 5 , 5 , 22 , 13 , 55 , 97 , 4 , 796 , 1 , 0 , 9 ]
b = [ 0 , 1 , 2 , 3 , 4 ,4 , 5 , 6 , 7 , 8 , 9 ]
def intersec(nums1 , nums2):
    result = []
    num_dict = dict.fromkeys(nums1, True)
    for i in nums2:
        if num_dict.get(i): result.append(i)
    return list(set(result))
print(intersec(a ,b))
#[0, 1, 4, 5, 9]

# 2.陣列d = 陣列a 差集 陣列b
a = [ 77 , 5 , 5 , 22 , 13 , 55 , 97 , 4 , 796 , 1 , 0 , 9 ]
b = [ 0 , 1 , 2 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
def  diff(nums1 , nums2):
    result = []
    num_dict = dict.fromkeys(nums1, True)
    inter_dict = {}
    for i in nums2:
        if not num_dict.get(i): 
            result.append(i)
        else:
            inter_dict[i] = True
    for i in nums1:
        if not inter_dict.get(i): 
            result.append(i)
    return list(set(result))

print(diff(a ,b))
#[2, 3, 6, 7, 8, 77, 22, 13, 55, 97, 796]

# 3.陣列e = 陣列a 聯集 陣列b
a = [ 77 , 5 , 5 , 22 , 13 , 55 , 97 , 4 , 796 , 1 , 0 , 9 ]
b = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
def  union(nums1 , nums2):
    result = []

    num_dict = dict.fromkeys(nums1, True)
    for i in nums2:
        if not num_dict.get(i): 
            result.append(i)
    
    return list(set(result + list(num_dict.keys())))

print(union(a , b ))
#[2, 3, 6, 7, 8, 77, 5, 22, 13, 55, 97, 4, 796, 1, 0, 9]

# 六、兩數總和
# • 給定一個整數陸列 nums 和一個整數 target,當兩數總和為target時,返回兩數的索引。
# * 您可以假設每個輸人都只有一個解決方案,並且您可能不會兩次使用相同的元素。
nums = [ 2,7,11,15]
target = 9
def twoSum(nums ,target):
    temp = {}
    for index in range(len(nums)):
        if temp.get(nums[index]) is not None:
            return [temp.get(nums[index]) , index]
        else:
            temp[target-nums[index]] = index

    return []
print(twoSum(nums , target))
#[0, 1]