def insertionSort(arr):
    "插入排序"
    #打印传入的参数
    print("传入:", arr)
    #默认第一个数值为有序数列的第一个数,索引从第二个数开始循环
    for i in range(1,len(arr)):
        #第i轮待插入的值
        current = arr[i]
        #待插入值的前一个索引(有序列表的索引)
        preIndex = i - 1
        #将待插入的值-从后到前 与有序数列中的数进行比较。
        #如果有序数列比较完了,或者待插入的数值>=了有序数列的值,那么说明找到了插入位置。
        while preIndex >= 0 and current < arr[preIndex]:
            #将比较后的值往后移
            arr[preIndex + 1] = arr[preIndex]
            #继续往前比较
            preIndex -= 1
        #将待插入的值赋值到该位置
        arr[preIndex + 1] = current

        #打印处理一轮后的列表
        print("第",i,"轮:", arr)

    #打印处理完毕的list
    print("返回:", arr)
    #返回处理后的列表
    return arr

#要测试的lis
testArray = [6,2,7,4,5]
# [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

#调用函数排序list
insertionSort(testArray)


# def insertionSort2(arr):
#     #i为当前索引,需要以当前的值(待插入的值)与待插入之前的值进行比较，找到对应位置后插入
#     #从索引1开始,因为索引0前没有数,所以需要从索引1开始 与 索引0进行比较
#     for i in range(1,len(arr)):
#         #待插入的值
#         current = arr[i]

#         for preIndex in range(i - 1, -2, -1):
#             print("preIndex = ",preIndex)
#             if arr[preIndex] > current and preIndex > -1:
#                 arr[preIndex + 1] = arr[preIndex]
#             else:
#                 break
#         print("preIndex end = ",preIndex)

#         #将待插入的值赋值到该位置
#         arr[preIndex + 1] = current  
 
#         print(arr)
#     return arr

# #打印函数返回的列表
# print(insertionSort2([6,2,7,4,5]))



# a = list(range(10))
# a.reverse()
# print(a)

# for i in range(10, -1, -1):
#     print(i)