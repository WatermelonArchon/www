y=[0,1,2, 3, 4, 5, 6, 7, 8]
x=[3,6,9,11,17,29,33,52,69]
isk=666
jump=int(len(x)**0.5)
index=0
is_found=False
for i in range (0, len(x), jump):
    if isk<x[i]:
        for j in range(i-jump, i):
            if x[j]==isk:
                index=j
                is_found=True
                break
    if x[index]==isk:
        index=j
        is_found=True
        break
for j in range(i, len(x)):
    if x[j]==isk:
                index=j
                is_found=True
                break
if is_found==True:
    print(index)     
else:
    print('А сё, а надо было писать норм циферки')

           