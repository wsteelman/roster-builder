from datetime import date
from utils import *
from contract import *
from stint import *
from seasons import *

class PlayerSeason:
   #__m_season
   #__m_prorated_salary
   #__m_projected_salary
   #__m_stints
   #__m_last_stint
   #__m_contract_years

   def __init__(self, year, contracts):
      self.__m_season = seasons[year]
      self.__m_prorated_salary = 0
      self.__m_projected_salary = 0
      self.__m_stints = []
      self.__m_last_stint = None; 
      for c in contracts:
         cy = c.GetYear(year)
         if (cy is not None): 
            self.__m_contract_years.append(cy)

   def AddStint(self, stint):
      self.__m_stints.append(stint) 
      if (self.__m_last_stint is None):
         self.__m_last_stint = stint
      elif (stint.Start() > self.__m_last_stint.End()):
         self.__m_last_stint = stint
         
   def ProjectedValue(self):
      if self.__m_contract_year is None:
         self.__m_projected_salary = self.__m_prorated_salary
      else:
         tmp = self.__m_prorated_salary
         tmp = tmp + (self.__m_contract_year.GetValue(self.__m_last_stint.Level()) * 
                      self.__m_season.PercentLeft())
         self.__m_projected_salary = tmp

   def ProjectedSalary(self):
      return self.__m_projected_salary

class Player:
   #__m_id
   #__m_first_name
   #__m_last_name
   #__m_dob
   #__m_bats
   #__m_throws
   #__m_first_signing
   #__m_draft_round
   #__m_service_time_days
   #__m_agent 
   #__m_position
   #__m_options
   #__m_contracts
   #__m_current_contract
   #__m_seasons

   def __init__(self, id, first, last, dob, bats, throws):
      self.__m_id = id
      self.__m_first_name = first
      self.__m_last_name = last
      self.__m_dob = dob 
      self.__m_bats = bats
      self.__m_throws = throws
      
      #set default values
      self.__m_first_signing = date(1970,1,1)
      self.__m_draft_round = 0
      self.__m_service_time_days = 0
      self.__m_agent = ""
      self.__m_position = []
      self.__m_options = []
      self.__m_contracts = []
      self.__m_seasons = {}

   def SetProfessionalSigningDate(self, d):
      self.__m_first_signing = d

   def SetDraftRound(self, round):
      self.__m_draft_round = round

   def SetServiceTimeDays(self, days):
      self.__m_service_time_days = days

   def SetServiceTimeYears(self, years):
      self.__m_service_time_days = ServiceTimeToDays(years)

   def SetAgent(self, agent):
      self.__m_agent = agent

   def AddPosition(self, position):
      self.__m_position.append(position)

   def AddOptionYear(self, year):
      self.__m_options.append(year)

   def AddContract(self, contract):
      self.__m_contracts.append(contract)
      if (contract.CoversYear(date.today().year)):
         self.__m_current_contract = contract     

   def AddStint(self, stint):
      year = stint.Start().year
      if (year not in self.__m_seasons):
         print "Adding player season " + str(year)
         self.__m_seasons[year] = PlayerSeason(year, self.__m_current_contract)
      season = self.__m_seasons[year]
      season.AddStint(stint)    
   
   def GetPlayerSeason(self, year):
      if (year in self.__m_seasons):
         return self.__m_seasons[year]
 
   def __str__(self):
      return '%s, %s %s, %s, %s' % (self.__m_id, self.__m_first_name, 
                                    self.__m_last_name, str(self.__m_dob), 
                                    ArmSide.Map[self.__m_bats])
