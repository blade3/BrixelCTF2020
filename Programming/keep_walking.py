#/usr/bin/python3

#This is a challenge to test your basic programming skills.

#Pseudo code:
#Set X = 1
#Set Y = 1
#Set previous answer = 1
#answer = X * Y + previous answer + 3
#After that => X + 1 and Y + 1 ('answer' becomes 'previous answer') and repeat this till you have X = 525.
#The final answer is the value of 'answer' when X = 525. Fill it in below.

#Example:
#5 = 1 * 1 + 1 + 3
#12 = 2 * 2 + 5 + 3
#24 = 3 * 3 + 12 + 3

x = 1
answer = 1

for z in range(1,526):
    answer = z*z + answer + 3
    
print(answer)