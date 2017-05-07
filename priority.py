p={}
arrival_time=[]
brust_time=[]
priority=[]
for i in range(0,3):
	a=input("Enter arrival time    ")
	if(i==0):
		min=a
	elif(min>a):
		min=a
	arrival_time.append(a)
	b=input("Enter brust time:      ")
	brust_time.append(b)
	p=input("Enter priority time:      ")
	priority.append(p)
	p[priority[i]]=[arrival_time[i],brust_time[i],i+1]
for index in range(0,3):
	print arrival_time[index],"       ",brust_time[index],"        ",priority[index]
priority.sort()
total=min
for ii in range(0,3):
	index=p.get(priority[ii])[1]
	total=total+p.get(priority[ii])[2]
	print min,"------------",total,"p",p.get(priority[ii])
	min=total
