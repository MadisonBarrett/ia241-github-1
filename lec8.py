'''
lec8
'''

def my_function(a,b=0):
    
    print(a)
    
    result = a + b
    
    return result
    
    print(b)
    
#print (my_function(b=1, a=2))

#ex1 cal abs values

def cal_abs(a):
    
    if type(a) is str:
        return ('wrong data type')
    elif a >=0:
        return a
    else:
        return -a
        
print(cal_abs(-1))

#ex2

def cal_sigma(n,m):
    
    result = 0
    for i in range(n,m+1):
        result = result + 1
        
    return result
    
print(cal_sigma(1,6))

def cal_pi(n,m):
    
    result = 1
    
    for i in range(n,m+1):
        result = result * i
        
    return result
    
print(cal_pi(1,6))

#ex3

def cal_f(m):
    
    if m == 0:
        return 1
    else:
        return m*cal_f(m-1)
        
print(cal_f(0))
