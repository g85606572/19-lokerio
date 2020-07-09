import time
from database import *

def _serial():
    timestamp = int(time.time()*1000.0)
    return str(timestamp)
    

if __name__ == "__main__":
    pass 
