import numpy as np

y_hat = np.random.rand(100)
print(y_hat)

y = []
for i in range(0,100,1):
    if(np.random.rand()<0.5):
        y.append(0)
    else:
        y.append(1)
print(y)

sum = 0
for i in range(0,100,1):
    sum = sum + y[i]*np.log2(y_hat[i]) + (1-y[i])*np.log2(1-y_hat[i])
sum = -sum/100
print('O= ',sum)


