#   tcellsx

#\  +转义功能首字母
print('hello\nworld')   #n表示newline换行
print('hello\tworld')   #t表示table制表空格，o和w中间空三格
print('helloooo\tworld')    #通常四位一个制表位hell一个oooo一个所以o和w空四格
print('hello\rworld')   #r表示回车，world将hello覆盖了
print('hello\bworld')   #b表示back，退格一个

print('http:\\tcellsx.cn')
print('http:\\\\tcellsx.cn')    #正常

print('the teacher said \'hello\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，在字符串之前加r或者R
print(r'hello \n world')

#最后一个字符不能是\,可以两个
#print(r'hello \n world\')