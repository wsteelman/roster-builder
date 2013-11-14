from datetime import date
from utils import *
from player import *
from ingest_base import db_ingest_inf

class db_ingest_dummy(db_ingest_inf):

   def __init__(self):
      self.__m_index = 0
      self.__m_player_cnt = 0
      self.__m_players = []

      p = Player(1, "Matt", "Holliday", date(1980, 1, 15), ArmSide.RIGHT, ArmSide.RIGHT)
      p.SetProfessionalSigningDate(date(1998,6,15))
      p.SetDraftRound(7)
      p.SetServiceTimeYears(9.000)
      p.SetAgent("Scott Boras")
      p.AddPosition(Positions.LF)
      p.AddOptionYear(2002)
      p.AddOptionYear(2003)

      c = Contract(7, 2010, True, "blah")
      c.AddYear(2010, 17000000, False, 0, 0) 
      c.AddYear(2011, 17000000, False, 0, 0) 
      c.AddYear(2012, 17000000, False, 0, 0) 
      c.AddYear(2013, 17000000, False, 0, 0) 
      c.AddYear(2014, 17000000, False, 0, 0) 
      c.AddYear(2015, 17000000, False, 0, 0) 
      c.AddYear(2016, 17000000, False, 0, 0) 
      p.AddContract(c)
      p.AddStint(Stint("STL", Levels.MLB, Levels.MLB, "A", 0, "END", date(2013, 3, 31), date(2013, 9, 29)))
      self.__m_players.append(p)
      self.__m_player_cnt += 1
     
      p = Player(2, "Yadier", "Molina", date(1982, 7, 13), ArmSide.RIGHT, ArmSide.RIGHT)
      p.SetProfessionalSigningDate(date(2000,6,15))
      p.SetDraftRound(4)
      p.SetServiceTimeYears(8.123)
      p.SetAgent("MDR Sports")
      p.AddPosition(Positions.C)
      self.__m_players.append(p)
      self.__m_player_cnt += 1

   def GetNextPlayer(self):
      if (self.__m_index < self.__m_player_cnt):
         player = self.__m_players[self.__m_index]
         self.__m_index += 1
         return 1, player
      else:
         return 0, 0 

