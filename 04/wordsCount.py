import re

if __name__ == '__main__':

    table = {}
    with open("resource/content", 'rb') as reader:
        lines = reader.readlines()
        # contnt = reader.readline()
        for l in lines:
            print l
            l = re.sub('[^A-Za-z| |0-9|\']', '', l)
            la = re.split(' ', l)
            print la
            for a in la:
                a = a.lower()
                if table.has_key(a):
                    table[a] = table[a] + 1
                else:
                    table[a] = 1

    for key in table.keys():
        print "{0}:{1}".format(key,table[key])