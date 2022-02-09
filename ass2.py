"""
Lizett Gonzales
2-8-22
"""
for star in range(5):#up to five times
    for add in range(star+1):
        print('*',end='')
    print()
    
#----------------

for i in range(0, 6):
      print(" " * (5-i) + "*" * i)
      #prints empty spaces until as it goes in order
      # as well as printing the number of stars for each position on the right
      
#above is question 1-------------------------------------------------------------------

n=int(input(' Enter a value to assign to n: '))
r=int(input(' Enter a value to assign to r: '))
difference=n-r
#code learned from in class example, thank you!
loopcounter=1
resultfnumber=1
while loopcounter<=n:
    resultfnumber=resultfnumber*loopcounter
    loopcounter+=1
print('this is the result for n:', resultfnumber)#factorial for n

loopcountertwo=1
resultfnumbert=1
while loopcountertwo<=r:
    resultfnumbert=resultfnumbert*loopcountertwo
    loopcountertwo+=1 
print('this is the result for r: ', resultfnumbert)#factorial for r

loopcounterthree=1 
resultfnumberthree=1
while loopcounterthree<=difference:
    resultfnumberthree=resultfnumberthree*loopcounterthree
    loopcounterthree+=1 

#permutation code first
print('this is permutation: ', resultfnumber/resultfnumbert*resultfnumberthree)
#combination code next
print('this is combination: ', resultfnumber/resultfnumberthree)





#above is question 2--------------------------------------------------

List = [20, 68, 41, 88, 16,40, 65, 97, 85]

first=0

while(first<len(List)):
    nextp=first+1
    while(nextp<len(List)):
        if(List[first]>List[nextp]):
            holder=List[first]
            List[first]=List[nextp]
            List[nextp]=holder
        nextp=nextp+1
    first= first+1
print(List)

#above is question 3 using loops to sort through a list and print it___________________

total=0 
for position in range(0,len(List)):
    total=List[position]+total
print('This is the total for the original list', total)

#---------------

print('the list for even numbers is: ')
for j in range(0,len(List)):
    if List[j]%2==0:#creates list of even numbers
        print(" ", List[j], end='')
print('\n')
   
sumof=0    
for i in range(len(List)):
    if List[i]%2==0:#sum of the list of even numbers
         sumof=sumof+List[i]
         i+=1
  
print('the sum of the even numbers is: ', sumof, end=' ')#prints list of even numbers

print('\nthe new list for odd numbers is: ')
for j in range(0,len(List)):
    if List[j]%2!=0:#creates list of odd numbers
        print(" ", List[j], end='')
print('\n')

sumofodd=0    
for i in range(len(List)):
    if List[i]%2!=0:#sum of the list of odd numbers
         sumofodd=sumofodd+List[i]
         i+=1
print('the sum of the odd numbers is: ', sumofodd, end=' ')


#-above is question 4----------------------------------------------------

print('\nwe will print prime numbers from a range')
for spot in range(2,50+1):
    if(spot>1):
        for j in range(2,spot):
            if(spot%j)==0:
                 break
        else:
         print(spot, end=' ')#continues printing on same line(i learned that indentation is important)
print('\n')
#above is question 5__________--------_####----------------------------------------------------------
  
number=int(input('\nenter a number to make check if armstrong number: '))


total=0 
hold=number
while hold>0:
    numeral=hold%10
    total+=numeral**len(str(number))
    hold//=10

if number==total:
    print(number, ' is an armstrong number')
else: 
    print(number, ' is not an armstrong number')
#above is question 7------------------------------------  

#tells us where to stop  
Fibonacci=int(input(" enter a number to make it ...Fibonacci(?)"))
i=0
digit=0 
digit2=1
while i<Fibonacci:
    print(digit, end=' ')
    nextdigit=digit+digit2
    digit=digit2#additionof the current and next and the sum is assigned to the other variable
    digit2=nextdigit
    i+=1 #up to number of numbers in the number entered
#above is question 8-----------------------------------------------------

print('\n -----------------------')
loop_counter=1 
while loop_counter<=10:
    if loop_counter%2==0:
        print(loop_counter, end=' ')
    loop_counter+=1 
 
#above is question 9--------------------------------------------
    
