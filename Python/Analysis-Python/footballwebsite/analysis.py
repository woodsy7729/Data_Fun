import numpy as np
from scipy import stats
fp= file("FootballData/prem/refineddata", "r")
points_first=[]
for line in fp:
    arr= line.split(" ")
        #print(arr)
    if arr[1] == "1":
        points_first.append(int(arr[-1].strip()))
            #print(arr[-1])
        #print(arr[1])
points = np.array(points_first)
print(points.size)
y=[]
i=1
while i <24:
    y.append(i+1991)
    i+=1
#perform regression
slope, intercept, r_value, p_value, std_err = stats.linregress(points,y)
print(slope)
print(intercept)
#plot points, add linear regression line
#print(points)
def chels_pos(pos_mu):
    che_pos=[]
    for line in fp:
        arr=line.split(" ")
        if arr[2]=="Chelsea":
            che_pos.append(int(arr[1].strip()))
    pos=np.array(che_pos)
    print(pos)
    print(np.mean(pos))
    pval=stats.ttest_1samp(pos,pos_mu)
    print(pval[1])
#chels_pos(1)
#conf interval at 90% for range of "first points"
'''
n=points.size
samp_mean= np.mean(points)
samp_var= np.var(points)

t_num= samp_mean-mu
t_den=np.sqrt(samp_var/n)
t= t_num/t_den
'''


'''
Visualisation is very important -> have a colour scale red=0pval, green = 1 pval and have a sliding scale of colour.
do that for each team's ave position of past 10 years.
'''

#print(points)
