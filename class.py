#!/usr/bin/python


class Calculator:
    def __init__(self,ina,inb):
        self.a=ina
        self.b=inb


    def add(self):
        return self.a+self.b

    def mul(self):
        return self.a*self.b


class Scientific(Calculator):
    def power(self):
        return pow(self.a,self.b)




newCalculation=Calculator(10,20)

print 'a+b: %d' %newCalculation.add()

print 'a*b: %d' %newCalculation.mul()



newpow=Scientific(7,13)

print '============================='

print 'a+b: %d' %newpow.add()
print 'aXb: %d' %newpow.mul()
print 'a POW b: %d' %newpow.power()


