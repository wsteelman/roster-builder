from seasons import *


class Stint:
   #__m_roster
   #__m_location
   #__m_status
   #__m_option
   #__m_end_code
   #__m_start
   #__m_end
   #__m_days
   #__m_cost
   #__m_season

   def __init__(self, roster, loc, status, option, code, start, end):
      self.__m_roster = roster
      self.__m_location = loc
      self.__m_option = option
      self.__m_end_code = code
      self.__m_start = start
      self.__m_end = end
      self.__m_days = (end - start).days
      self.__m_cost = 0
      self.__m_season = seasons[start.year]

   def ComputeCost(self, base_salary)
      self.__m_cost = base_salary * (self.__m_days / self.__m_season.Days())


