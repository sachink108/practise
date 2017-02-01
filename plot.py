import matplotlib.pyplot as plt
from numpy.random import rand

irisData = dict()
with open('iris.data') as f:
    for line in f.readlines():
        sl, sw, pl, pw, irisClass = line.strip().split(',')
        if irisClass not in irisData:
            irisData[irisClass] = []
        irisData[irisClass].append((sl, sw, pl, pw))

for irisClass in irisData:
    print (irisClass)

ic = 'Iris-setosa'
# print sl to sw
'''
for idx, data in enumerate(irisData[ic]):
    plt.scatter(data[0], data[1], color='b')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
'''
fig, axarr = plt.subplots(2)
for idx, data in enumerate(irisData[ic]):
    axarr[0].scatter(data[0], data[1], color='b')
    axarr[1].scatter(data[2], data[3], color='r')
axarr[0].set_title('Sepal Length vs Sepal Width')
axarr[1].set_title('Petal Length vs Petal Width')
fig.text(0.5, 0.04, 'Length', ha='center', va='center')
fig.text(0.06, 0.5, 'Width', ha='center', va='center', rotation='vertical')

plt.legend()
plt.grid(True)
plt.show()