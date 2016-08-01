import random
import redis

vs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789'

def generation():
    r = ''
    for j in range(0, 20):
        index = random.randint(0, 71)
        r = r + vs[index]
        if j in (4, 9, 14):
            r = r + '-'
    return r

if __name__ == '__main__':
    print 'begin to save'
    database = r = redis.StrictRedis(host="lsabcd.test.server",port=6379,db=0)

    cs = []
    for i in range(0,200):
        code = generation()
        cs.append(code)
        rcode = r.sadd('code',code)
        if rcode == 0:
            print code
    r.save()
    print 'saved!'