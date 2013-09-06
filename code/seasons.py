
class Season:
   def __init__(self, year, start, end):
      self.__m_year = year
      self.__m_start = start
      self.__m_end = end
      self.__m_days = (end - start).days

   def Days(self);
      return self.__m_days

seasons = {}
seasons[2013] = Season(2013, date(2013,3,31), date(2013, 9, 29))
