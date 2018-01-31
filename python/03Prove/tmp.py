def test():
    p = 2
    pa = 2
    a = [0,1,2,3,4,5,6,7,8,9]
    for i in range(5):
        print "Test:",a[p-pa:p]
        print "Train:",a[0:p-pa]+a[p:]
        p = (p + pa)%11

test()
