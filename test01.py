"""
ph1 = input("pls input 1 para:")
ph2 = input("pls input 2 para:")
ph3 = input("pls input 3 para:")

sep = {'1':'=','2':'*','3':'#'}
print('',
      '1.'+sep['1'],
      '2.'+sep['2'],
      '3.'+sep['3'],sep = '\n')           
choise = input("請問你要使用何種分隔符號(請輸入數字選擇) :")
print("以下為你的文章:\n")
print(ph1,ph2,ph3,
      sep = '\n' +sep[choise]*10+'我是分隔線'+
      sep[choise]*10 +'\n',
      end = '\n-文章結束-')

print('%-2s morning ' % 'Great'*2)

a = '%s Kitty, there are %.3f dollors'
b = a % ('Hello',2.5) 

a = 'hello {}, I am {}'.format('world','Mia')
print(a)  # hello world, I am oxxo
b = 'hello {:10s}, I am {:10s}'.format('world','Mia')
print(b)  # hello world     , I am oxxo
c = 'hello {:>10s}, I am {:>10s}'.format('world','Mia')
print(c)  # hello      world, I am       oxxo
d = 'hello {:-^10s}, I am {:+^10s}'.format('world','Mia')
print(d)  # hello --world---, I am +++oxxo+++hytqwddggxczcccccccccxq345o      qmzzz232465-
e = 'hello {:-^10.3s}, I am {:-^10s}'.format('world','Mia')
print(e)  # hello ---wor----, I am ---oxxo---
f = 'hello {:-^10.3s}, I am {:^10.3f}'.format('world',123.456789)
print(f)  # hello ---wor----, I am  123.457

"""

try:
    ans = input('晚上想要吃什麼?')
    print('放假前一天晚上 吃...'+ans)

    a=[]
    for i in 'abc':
        for j in range(1,4):
            a.append(i+str(j))
    print(a)     

    b=[i+str(j) for i in 'abc' for j in range(1,5)]   
    print(b)
      
except Exception as e:
    print(e)