import random
def generation():
    vs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789'
    res = []
    for i in range(0,200):
        r = ''
        for j in range(0,20):
            index = random.randint(0,71)
            r = r + vs[index]
            # r.append(vs[index])
            if j in(4,9,14):
                r = r + '-'
        res.append(r)

    for i in range(0,200):
        print res[i]
if __name__ == '__main__':
    generation()
