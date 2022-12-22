print("Enter Date:")
def leapyear(x):
    if (x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False
Day=int(input("Enter Day [1-31]:"))
Month=int(input("Enter Month [1-12]:"))
Year=int(input("Enter Year [1800-2025]:"))
    if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
        condition1=False
    else:
        condition1=True