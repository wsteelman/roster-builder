
class ContractYear:
   #__m_year
   #__m_option
   #__m_value
   #__m_buyout
   #__m_bonus
   #__m_exercised
   
   def __init__(self, year, option, value, buyout, bonus, exercised):
      self.__m_year = year;
      self.__m_option = option
      self.__m_buyout = buyout
      self.__m_bonus = bonus
      self.__m_exercised = exercised
      self.__m_value = value
      if option and not exercised:
         self.__m_value = buyout

   def GetValue(self)
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
      self.__m_total_value = 0
      self.__m_years = {}

   def AddYear(self, year, option, value, buyout, bonus):
      cy = ContractYear(year, option, value, buyout, bonus)
      self.__m_total_value += cy.GetValue()
      self.__m_years[year] = cy

   def CoversYear(self, year):
      if (year >= self.__m_start_year and 
          year < (self.__m_start_year + self.__m_length)):
         return True
      else:
         return False 
