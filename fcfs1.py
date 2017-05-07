p={}
arrival_time=[]
brust_time=[]
for i in range(0,3):
	a=input("Enter arrival time    ")
	if(i==0):
		min=a
	elif(min>a):
		min=a
	arrival_time.append(a)

	b=input("Enter brust time:      ")
	brust_time.append(b)
	p[brust_time[i]]=[arrival_time[i],i+1]
for index in range(0,3):
	print arrival_time[index],"       ",brust_time[index]
total=min
for i in range(0,3):
	index=p.get(brust_time[i])[1]
	total=total+brust_time[i]
	print min, "_____________",total
	min=total

