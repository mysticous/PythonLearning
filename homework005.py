string = input("")
if string[0:3] == 'RMB':
    print('USD{:.2f}'.format(eval(string[3:]) / 6.78))
elif string[0] == '￥':
    print('${:.2f}'.format(eval(string[1:]) / 6.78))
elif string[0:3] == 'USD':
    print('RMB{:.2f}'.format(eval(string[3:]) * 6.78))
elif string[0] == '$':
    print('￥{:.2f}'.format(eval(string[1:]) * 6.78))
