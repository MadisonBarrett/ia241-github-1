'''
lec6
'''

for item in ['a', 'b', 'c']:
    print (item)
    
demo_str = 'this is my string'

for c in demo_str:
    print(c)
    
for word in demo_str.split():
    print(word)
    
for num in range(5):
    print(num)
    
for num in range(1,5):
    print(num)
    
for num in range(1,5,2):
    print(num)
    
num_list = [1,2,3,1,2]

max_item = num_list[0]

for num in num_list:
    if max_item<= num:
        max_item = num
        
print (max_item)
