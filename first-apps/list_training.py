from datetime import datetime

odds = list(range(1, 59, 2))
# print(odds)

right_this_minute = datetime.today().minute
# print(right_this_minute)

if right_this_minute in odds:
  print("This minute seems a little odd")
else:
  print("Not an odd minute")  
