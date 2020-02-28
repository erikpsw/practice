import random

print('green')
time = 10000 #实验次数 输入任意整数
death = 0 #死亡次数

for i in range(time):
    count=0
    box =[1,1,0,0,0] #盒中苹果，1代表有毒，0代表无毒

    mc = random.randint(1,5) #第一次随机在5个苹果中选1个
    if box[mc - 1]==1: #如果选中的是有有毒的
        count = count + 1 #中毒计数器+1
        del box[mc-1]

    mc = random.randint(1,4) #第二次选苹果，只剩4个了
    if box[mc - 1]==1: #以下同上
        count = count + 1
        del box[mc-1]

    mc = random.randint(1,3) #第三次选苹果
    if box[mc - 1]==1:
        count = count + 1
        del box[mc-1]


    if count >=2: #三次选完以后，如果中毒计数器大于等于2
        death=death+1 #记作一次死亡


print("",death*100/time,"%") #计算概率，死亡次数/总实验次数

print('red')

deaths=0
for e in range(10000):
    box=[1,1,1,0,0]
    counts=0

    mc=random.randint(1,5)
    if box[mc-1]==1:
        counts+=1
        del box[mc-1]

    mc=random.randint(1,4)
    if box[mc-1]==1:
        counts+= 1
        del box[mc - 1]

    if counts == 2:
        deaths=deaths+1


print('',deaths*100/10000,"%")







