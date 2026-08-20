height=input("enter every one height separating by space: ")
height_list=height.split()
count=0
for h in height_list:
    count=count+1
for i in range(0,count):
    height_list[i]=int(height_list[i])
    sum=0
for i in height_list:
    sum+=i
avg=sum/count
print(round(avg))