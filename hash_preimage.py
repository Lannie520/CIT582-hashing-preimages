import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
#Function written starts here
    l = len(target_string)
    while True:
        x = os.urandom(64)
        hash = bin(int(hashlib.sha256(x).hexdigest(),16))[-l:]
        if (hash == target_string):
            return(x)

