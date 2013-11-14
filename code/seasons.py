from datetime import date

class Season:
   def __init__(self, year, start, end, mlb_min_salary):
      self.__m_year = year
      self.__m_start = start
      self.__m_end = end
      self.__m_days = (end - start).days
      self.__m_mlb_min_salary = mlb_min_salary

   def Days(self):
      return self.__m_days

   def PercentLeft(self):
      d = date.today()
      if (self.__m_start > d):
         return 1
      elif (d > self.__m_end):
         return 0
      else:
         return (d - seld.__m_start) / self.__m_days

seasons = {}
seasons[2013] = Season(2013, date(2013,3,31), date(2013, 9, 29), 490000)
