def calculatePay():
    # This first line is provided for you
        hrs = input("Enter Hours:")
        rte = input("Enter Rate:")
        hrs = float(hrs)
        rte = float(rte)

        if hrs <= 40:
            gross = hrs * rte
        else:
            otHrs = hrs - 40
            hrs = 40
            gross = (hrs * rte) +  (otHrs * rte * 1.5)
            str(gross)
        print("calculating pay ", gross)       
        #print(gross)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()





