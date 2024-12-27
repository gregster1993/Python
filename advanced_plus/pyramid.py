def print_pyramid(n):
    #outer loop for the number of rows
    for i in range(1, n+1):
        #Print spaces before the stars
        print(' ' * (n - i), end='')
        #Print stars for the current row
        print('*' * (2 * i - 1))
    
def print_upside_down_pyramid(n):
    #outer loop for the number of rows
    for i in range(n+1, 1, -1):
        #Print spaces before the stars
        print(' ' * ((n + 1) - i), end='')
        #Print stars for the current row
        print('*' * (2 * i - 3))
    

n = int(input("Enter the humber of rows: "))
print_upside_down_pyramid(n)
print_pyramid(n)
print_upside_down_pyramid(n)
print_pyramid(n)