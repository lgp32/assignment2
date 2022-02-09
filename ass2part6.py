"""
lizette gonzales
2-8-22
"""

def main():
  questionone()
  
  questiontwo()
  
  questionthree()
    
    
    
    
def questionone():
    for star in range(5):#up to five times
        for add in range(star+1):
            print('*',end='')
        print()
    for i in range(0, 6):
        print(" " * (5-i) + "*" * i)
    
def questiontwo():
    n=int(input(' Enter a value to assign to n: '))
    r=int(input(' Enter a value to assign to r: '))
    print('n and r are: ', n , r, end=" ")
    
    
    
def questionthree():
    print('\n')
    List = [20, 68, 41, 88, 16,40, 65, 97, 85]
    print(List, end=' ')    

main()
