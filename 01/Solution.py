import random

vs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789'

def generation():
    r = ''
    for j in range(0, 20):
        index = random.randint(0, 71)
        r = r + vs[index]
        # r.append(vs[index])
        if j in (4, 9, 14):
            r = r + '-'
    return r

if __name__ == '__main__':
    for i in range(0,200):
        code = generation()
        print code
