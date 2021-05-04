# 题目描述
# 电脑组的童鞋们经常玩一些智力PK小游戏，某月某日，发源于小朋友又发明了一种新的序列：双调序列，所谓的双调呢主要是满足如下条件描述：

# 假定有n(n<=1000)个整数（都在longint范围内，即-2147483648~2147483647），双调序列的第一个数是n个整数中的最大数，第二个数是n个整数中的最小数，第三个数是n个数中的第二大数，第四个数是n个数中的第二小数……取过的数不能再取，依次类推，直到结束。

# 聪明的你听完描述就抿嘴笑了吧？那就请你用程序正确的帮他找出这n个数的双调序列。

# 输入格式
# 第1行为一个整数n。

# 接下来n行给出了题目中所述的n个整数，每行包含一个整数。

# 输出格式
# 有n行，每行为一个整数，是满足条件的双调序列



def dealNum(array):
    for i in range(len(array) - 1):
        # print("i=",i)
        #判断是第几个数字:如果为偶数说明需要排序最大值
        if i % 2 == 0:
            # print("times % 2 == 0")
            #先令最大值的索引为第i轮的第一个数字
            max_index = i
            for j in range(i+1, len(array)):
                if  array[j] > array[max_index]:
                    max_index = j
            if max_index != i:
                array[i], array[max_index] = array[max_index], array[i]
        else:
            # print("times % 2 == 1")
            #排序最小值
            min_index = i
            for k in range(i+1, len(array)):
                if array[k] < array[min_index]:
                    min_index = k
            if min_index != i:
                array[i], array[min_index] = array[min_index], array[i]

testList = [-10, 10,-5, 5, 6]
dealNum(testList)
print(testList)


# if __name__== '__main__':
#     #获取输入长度
#     length = int(input())

#     #获取输入列表
#     list_number = []
#     for i in range(length):
#         list_number.append(int(input()))

#     dealNum(list_number)
#     # print(list_number)
#     for i in list_number:
#         print(i)