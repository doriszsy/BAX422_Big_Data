
# coding: utf-8

# In[1]:


read = open('data/msnbc990928.seq', 'r')


# In[2]:


# note the file has several lines of comment before record of sessions  
# read only sessions into seq
seq = []
for eachLine in read:
    numbers = eachLine.split()
    currLine = []
    check = 0
    for num in numbers:
        if(num.isdigit() == False):
            check = 1
        currLine.append(num)

    if(check == 0 and len(currLine) != 0):
        seq.append(currLine)


# In[3]:


# res1 count % of pg12 AND pg17 in the same session
# res2 count % of pg12 AFTER pg17 in the same session

res1 = 0;
res2 = 0;

for eachLine in seq: 
    if('12' in eachLine and '17' in eachLine):
        res1 += 1
        if(eachLine.index('17') < (len(eachLine) - eachLine[::-1].index('12') - 1)):
            res2 += 1


# In[4]:


#print result
res = (res1 / len(seq)) * 100
res = round(res, 4)
print (res, "% of visitors visited page 12 AND page 17.")

res = (res2 / len(seq)) * 100
res = round(res, 4)
print (res, "% of visitors visited page 12 AFTER page 17.")

