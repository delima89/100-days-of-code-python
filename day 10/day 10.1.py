

def days_in_month(year,month):
  check=True
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        check=True
      else:
        check=False
    else:
      check=True
  else:
    check=False

  if check==True:
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month=month_days[month-1]
    return month
  elif check==False:  
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month=month_days[month-1]
    return month
  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
