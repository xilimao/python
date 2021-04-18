import random
import copy
from matplotlib import pyplot as plt
from matplotlib import animation


def selection_sort(data_set, data_value):
    # FRAME OPERATION BEGIN
    frames = [data_set]

    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    ds_value = copy.deepcopy(data_value[0])

    for i in range(0, 10):
        minIdx = i
        for j in range(i+1, 10):
            # FRAME OPERATION BEGIN
            ds_r = copy.deepcopy(ds)
            ds_r_value = copy.deepcopy(ds_value)
            frames.append(ds_r)
            ds_r_value[i] = 'r'
            ds_r_value[j] = 'k'
            data_value.append(ds_r_value)
            # FRAME OPERATION END
            if ds[j] < ds[minIdx]:
                    minIdx = j
        if minIdx != i:
                ds[i], ds[minIdx] = ds[minIdx], ds[i]
    # FRAME OPERATION BEGIN
    frames.append(ds)
    data_value.append(ds_value)

    return frames


def get_value_color_list(value_color_list):
    list_color = []
    for value in x_list:
        list_color.append(value_color_list[value])

    # print("value_list:", value_list)
    # print("value_color_list:", value_color_list)
    # print("list_color:", list_color)
    return list_color




##获取X轴列表(共10组数据)
x_list = list(range(0, 10))
#print("x_list:", x_list)

##对应的10个值
y_list = list(range(0, 10))
random.shuffle(y_list)
# print("y_list:", y_list)
# y_list = [32,19,5,22,40,28,11,37,27,2]


##x轴索引显示
labels = []
for i in range(0, 10):
    labels.append(str(i))

##初始化color List
value_color = {}
for value in y_list:
    value_color[value] = '#0288b1'

##print("value_color:", value_color)
        

##list[list]
list_value_color = []
list_value_color.append(value_color)

# 获取所有数值列表
frames = selection_sort(y_list, list_value_color)


##创建画板1
fig = plt.figure(1)
##创建画布
axs = plt.subplot(111)


# Animation function. This is called sequentially.
# Note: fi is framenumber.
def animate(fi):
        if(len(frames) > fi):
                axs.cla()
                ##设置标题
                axs.set_title('Selection-Sort') 
                ##设置Y轴显示
                axs.set_ylabel('Y value') 
                ##设置X轴显示
                axs.set_xlabel('X index')
                ##创建柱形图
                bars = axs.bar(x_list,          # X
                        frames[fi],             # data
                        tick_label=labels,
                        color=get_value_color_list(list_value_color[fi]),

                        )
        return bars

##创建动画
anim = animation.FuncAnimation(fig, animate, frames=len(frames), repeat=False)


##显示
plt.show()



