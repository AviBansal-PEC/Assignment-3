a=int(input("Enter Grade:"))
dic = {10: "Your Grade is 'A+' and Outstanding performance.",
       9: "Your Grade is 'A' and Excellent performance.",
       8: "Your Grade is 'B+' and Very Good performance.",
       7: "Your Grade is 'B' and Good performance.",
       6: "Your Grade is 'C+' and Average performance.",
       5: "Your Grade is 'C' and Below Average performance.",
       4: "Your Grade is 'D' and Poor performance."}

if 4 <= a <= 10:
    statement = dic.get(a)
    print(statement)
else:
    print("\nError\nPlease enter grade in range [4,10]")