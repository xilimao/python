import numpy as np
import matplotlib.pyplot as plt

"SIMPLE"
# #X轴:从-Π到Π,256个点
# listX = np.linspace(start = -np.pi, stop = np.pi, num = 256)
# #Y轴:sin cos tan
# listYSin = np.sin(listX)
# listYCos = np.cos(listX)
# listYTan = np.tan(listX)

# #设置图像
# plt.plot(listX,listYSin)
# plt.plot(listX,listYCos)
# # plt.plot(listX,listYTan)

# #显示
# plt.show()


"CPMPLETE - 1"
# #创建一个6×8的图框，像素为100
# plt.figure(figsize=(6,8),dpi=100)
# #创建一个子图，网格为1×1
# plt.subplot(111)

# #初始化xy轴的点
# x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# y = np.sin(x)
# z = np.cos(x)
# #画图，使用不同的颜色和线条
# plt.plot(x,y,color='blue',linewidth=1.0,linestyle='-')
# plt.plot(x,z,color='red',linewidth=1.0,linestyle='-')
# #设置x轴的范围
# plt.xlim(-4,4)
# #设置x轴的标尺刻度，从-4到4，取9个值
# plt.xticks(np.linspace(-4,4,9,endpoint=True))

# #设置y轴的范围
# plt.ylim(-1,1)
# #设置y轴的标尺刻度，从-1到1，取5个值
# plt.yticks(np.linspace(-1,1,5,endpoint=True))

# plt.show()


"CPMPLETE - 2"
#创建一个6×8的图框，像素为100
plt.figure(figsize=(6,8),dpi=100)
#创建一个子图，网格为1×1
plt.subplot(111)

#初始化xy轴的点
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.sin(x)
z = np.cos(x)
#画图，使用不同的颜色和线条.以及图例
plt.plot(x,y,color='blue',linewidth=1.0,linestyle='-',label='Sin(x)')
plt.plot(x,z,color='red',linewidth=1.0,linestyle='-', label='Cos(x)')
plt.legend(loc='upper left')#将图例放在左上角

#放大x和y轴
plt.xlim(x.min()*1.1,x.max()*1.1)
plt.ylim(y.min()*1.1,y.max()*1.1)

#设置x轴的刻度值，显示pi
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.xticks([-np.pi, -np.pi/3*2, -np.pi/2, -np.pi/3, -np.pi/6, 0, np.pi/6, np.pi/3, np.pi/2, np.pi/3*2, np.pi],
[r'$-\pi$', r'$-\pi2/3$', r'$-\pi/2$', r'$-\pi/3$', r'$-\pi/6$', r'$0$', r'$\pi/6$', r'$\pi/3$', r'$\pi/2$', r'$\pi2/3$', r'$\pi$'])
plt.yticks([-1, 0, 1],[r'$-1$',r'$0$',r'$1$'])


"移动边界线，构建坐标系，原点为0"
ax = plt.gca()#获取当前轴线实例
ax.xaxis.set_ticks_position('bottom')#x轴线，使用spine中的bottom线
ax.yaxis.set_ticks_position('left')#y轴线，使用spine中的left线
ax.spines['bottom'].set_position(('data',0))#将bottom线的位置设置为数据为0的位置
ax.spines['left'].set_position(('data',0))#将left线的位置设置为数据为0的位置
ax.spines['top'].set_color('none')#将top线的颜色设置为无
ax.spines['right'].set_color('none')#将right线的颜色设置为无


#在图上增加标注信息
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\cos(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
xy=(t, np.cos(t)), xycoords='data',
xytext=(+10, +30), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


plt.show()