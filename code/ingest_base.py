from datetime import date
from player import *

class db_ingest_inf:
   def __init__(self):
      return

   def GetNextPlayer(self, player):
      return 1, Player(0, "dummy", "dummy", date(1970,1,1), ArmSide.RIGHT, ArmSide.RIGHT)

