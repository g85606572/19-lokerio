import time
from database import *

def _serial():
    timestamp = int(time.time()*1000.0)
    return str(timestamp)
    
def AInc(column,parent,child):
    try:
        col = db.reference(column).get().values()
        ttl = []
        for item in col :
            t = item.get(parent)
            ttl.append(t)
        return str(ttl.count(child))
    except Exception : 
        return 0
if __name__ == "__main__":
    pass 
