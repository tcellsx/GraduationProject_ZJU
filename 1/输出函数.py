#   tcellsx


#字符串
print("hello world")
#int型
print(520)
#浮点型
print(520.1314)
#表达式
print(520+1314*1000)
#将数据输出文件I/O
fp=open('D:/text.txt','a+')# a+表示文件不存在就创建，存在就在文件后面追加
print("hello world",file=fp)
fp.close()

#不换行输出
print("hello","world","Python")