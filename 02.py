try:
    hours = input('enter hours')
    hours = float(hours)
    rate = input('enter rate')
    rate = float(rate)
    def compute_pay(hours, rate) :
        return min(40,hours)* rate + max(0, hours-40)*1.5 * rate 

    print('pay:', compute_pay(hours, rate))

except: 
    print ('error, please enter numeric input')




