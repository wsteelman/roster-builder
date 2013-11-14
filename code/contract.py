from utils import * 

class ContractYear:
   #__m_year
   #__m_option
   #__m_value
   #__m_buyout
   #__m_bonus
   #__m_exercised
   
   def __init__(self, year, value, option_year, buyout, bonus, exercised, guaranteed):
      self.__m_year = year;
      self.__m_option = option_year
      self.__m_buyout = buyout
      self.__m_bonus = bonus
      self.__m_exercised = exercised
      self.__m_value = []

      # if option year, compute the value 
      if (option_year and not exercised):
         value = buyout

      value = value + bonus

      # set value at MLB level 
      self.__m_value.append(value)
      
      # set value at other levels
      if (guaranteed):
         for i in range(1, Levels.COUNT):
            self.__m_value.append(value)
      else:
         for i in range(1, Levels.COUNT):
            self.__m_value.append(0)

   def SetValue(self, level, value):
      self.__m_value[level] = value + self.__m_bonus

   def GetValue(self, level):
      return self.__m_value[level]

   def GetValues(self):
      return self.__m_value

class Contract:
   #__m_length
   #__m_guaranteed
   #__m_years
   #__m_total_value
   #__m_start_year
   #__m_description

   def __init__(self, length, start_year, guaranteed, desc):
      self.__m_length = length
      self.__m_guaranteed = guaranteed
      self.__m_start_year = start_year
      self.__m_description = desc
      self.__m_years = {}

   def AddYear(self, year, value, option, buyout, bonus):
      self.__m_years[year] = ContractYear(year, value, option, buyout, bonus, 
                                          False, self.__m_guaranteed)
 

   def CoversYear(self, year):
      if (year >= self.__m_start_year and 
          year < (self.__m_start_year + self.__m_length)):
         return True
      else:
         return False 

   def GetYear(self, year):
      if (year is in self.__m_years): 
         return self.__m_years[year];

   def Guaranteed(self):
      return self.__m_guaranteed


