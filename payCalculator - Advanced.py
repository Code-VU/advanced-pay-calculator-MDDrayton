def calculatePay():
    # This first line is provided for you
        hrs = input("Enter Hours:")
        rte = input("Enter Rate: ")

        if float(hrs) <= 40:
            gross = float(hrs)*float(rte) 
        else:
            otHrs = float(hrs) - 40
            hrs = 40
            gross = (float(hrs)*float(rte)) +  (otHrs*float(rte) * 1.5)
        print(gross)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculatePay()





