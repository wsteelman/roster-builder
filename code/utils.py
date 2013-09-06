import math

DAYS_PER_SEASON = 172

# throws enum
class ArmSide:
   LEFT = 0
   RIGHT = 1
   Map = ["LEFT", "RIGHT"]

class Positions:
   SP = 1
   C = 2
   B1 = 3
   B2 = 4
   B3 = 5
   SS = 6
   LF = 7
   CF = 8
   RF = 9
   RP = 10
   UT = 11
   OF = 12
   Map = ["SP", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "RP", "UT", "OF"]

def ServiceTimeToDays(years):
   years_floor = math.floor(years);
   days = years_floor * DAYS_PER_SEASON 
   days += (years - years_floor)*1000;
   return days

def ServiceTimeToYears(days):
   years = math.floor(days / DAYS_PER_SEASON);
   days_left = days % DAYS_PER_SEASON;
   return years + (days_left / 1000);
