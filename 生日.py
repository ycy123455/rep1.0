def fillFunction(message):
    message = bin(message)[2:]
    for i in range(4):
        if (len(message)%4 == 0):
            break
        else:
            message = '0'+message
    length = len(message)
    k = 448 - (length+1)%512
    if (k < 0):     #k是满足等式的最小非负整数
        k += 512
    addMessage = '1' + '0'*k + Int2Bin(length, 64)
    message += addMessage
    return message
 
def IterFunction(message):
    n = int(len(message)/512)
    v = []
    v.append(Int2Bin(cp.vi, 256))
    for i in range(n):
        w, w1 = msgExten(message[512*i:512*(i+1)])
        temp = CF(v[i], message[512*i:512*(i+1)], w, w1)
        temp = Int2Bin(temp, 256)
        v.append(temp)
    return v[n]
'''
消息扩展函数
b-int
'''
def msgExten(b):
    w = []
    w1 = []
    for i in range(16):
        temp = b[i*32:(i+1)*32]
        w.append(int(temp, 2))
    for j in range(16, 68, 1):
        factor1 = LoopLeftShift(w[j-3], 15)
        factor2 = LoopLeftShift(w[j-13], 7)
        factor3 = P1(w[j-16]^w[j-9]^factor1)
        factor4 = factor3^factor2^w[j-6]
        w.append(factor4)
    for j in range(64):
        factor1 = w[j]^w[j+4]
        w1.append(factor1)
    return w, w1

def birthday_attack(n):
    '''生日攻击前nbit碰撞'''
    for i in range(0,pow(2,n)):
        mes1=random.randint(0,pow(2,n))
        mes2=random.randint(0,pow(2,n))
        if(sm3(mes1)[:int(n/4)]==sm3(mes2)[:int(n/4)]):
            print('Succeed')
            return
    print('Failed')
