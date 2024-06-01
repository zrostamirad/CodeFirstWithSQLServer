from connection import *


class Repository():

    def Add(self, obj):
        try:
            session.add(obj)
            session.commit()
            return True
        except:
            return False
