from ooptelivision import telivision

class sony(telivision):
    def __init__(self):
        print('this is the top model of sony telivision')

tv1= sony()        
tv1.screen()
tv1.wallhang()
tv1.resolution()

print('------------------------------')

class samsung(telivision):
    def __init__(self):
        print('One of the best tv in India')


tv2= samsung()        
tv2.screen()
tv2.wallhang()
tv2.resolution()        

