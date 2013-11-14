from seasons import *
from utils import *

class Stint:
   #__m_org
   #__m_reserve
   #__m_level
   #__m_status
   #__m_option
   #__m_end_code
   #__m_start
   #__m_end
   #__m_days
   #__m_cost
   #__m_season

   def __init__(self, org, reserve, level, status, option, code, start, end):
      self.__m_org = org
      self.__m_reserve = reserve
      self.__m_level = level
      self.__m_status = status
      self.__m_option = option
      self.__m_end_code = code
      self.__m_start = start
      self.__m_end = end
      self.__m_days = (end - start).days
      self.__m_cost = 0
      self.__m_season = seasons[start.year]

   def ComputeCost(self, base_salary):
      self.__m_cost = base_salary[self.__m_level] * (self.__m_days / self.__m_season.Days())

   def Cost(self):
      return self.__m_cost

   def Level(self):
      return self.__m_level

   def Location(self):
      return self.__m_location

   def End(self):
      return self.__m_end

   def Start(self):
      return self.__m_start

   def Days(self):
      return self.__m_days

