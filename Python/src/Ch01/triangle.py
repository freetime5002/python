print('직삼각형 그리기\n')
leg = int(input('변의길이 : '))

for i in range(leg):
    print('* ' * (i+1)) 

area = (leg **2)/2
print('넓이:', area)
