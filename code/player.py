from datetime import date
from utils import *
from contract import *

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
 
   def __str__(self):
      return '%s, %s %s, %s, %s' % (self.__m_id, self.__m_first_name, 
                                    self.__m_last_name, str(self.__m_dob), 
                                    ArmSide.Map[self.__m_bats])
