from player import *
from ingest_test import db_ingest_dummy

db = db_ingest_dummy()

rc, player = db.GetNextPlayer()
while (rc == 1):
   print str(player)
   rc, player = db.GetNextPlayer()
