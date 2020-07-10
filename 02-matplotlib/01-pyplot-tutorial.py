import numpy as np
import  matplotlib.pyplot as plt
a=20
#x列表，y列表，然后展示形式（2个字符构成包括颜色和形状）
plt.plot([1,2,3,4,5],[1,4,9,16,25],'bs')
#限制x轴和y轴的范围
plt.axis([0,20,0,30])
plt.ylabel("some nums")
plt.show()
