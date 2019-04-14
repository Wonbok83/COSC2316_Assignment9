'''
Created on Apr 13, 2019

@author: wonbokyang
'''
#kangaroo
x1 = 5 
B2 = [['0'] * x1 for i in range(x1)]

def print_board(b2):
    for row in b2:
        print(' '.join(row))

print("Let's play puck and plant")
print_board(B2)

kang_row = 0
kang_col = 0
flo_row = 0
flo_col = 3       

B2[kang_row][kang_col]="k"
B2[flo_row][flo_col]="*"

print("Kangaroo and flower initial")
print_board(B2)



B2[kang_row][kang_col]="0"
B2[flo_row][flo_col]="0"
B2[flo_row+2][flo_col]="*"
B2[kang_row+2][kang_col+4]="k"
print("Kangaroo and flower after kangaroo moved")
print_board(B2)