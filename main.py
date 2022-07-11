"""def is_leap(year):
    leap = False
    
    # Write your logic her
    if (year%4==0):
        leap = True
    if (year%100==0):
        leap=False
        if(year%400==0):
            leap=True

    return leap

year = int(input())
print (is_leap(year))"""



"""def cap_sentence(s):
   return ' '.join(w[:1].upper() + w[1:] for w in s.split(' '))

s = input()
print(cap_sentence(s))"""
 

"""def solve(s):

    # Capitalize in Python - HackerRank Solution START
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

s = input()
print(solve(s))"""
  



