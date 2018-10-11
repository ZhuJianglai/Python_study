# author：zhu

for i in range(10):
    print('----------',i)
    for j in range(10):
        print(j)
        if j>5:
            break
    if i==6:
        break