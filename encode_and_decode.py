import hashlib
import useful_codes
import aes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from random import randrange

class irreversible_encrypt:
    class sha_family:
        def sha_family_encode_all(want_to_encode:str,vaule:str,loop_times:int):
            """
                it's encode is an irreversible encrypt,but if the same key and vaule, 
                it can get the same result

                it has sha256,384,224,1 encrypt
            """
            if i <= 1:
                raise TypeError("the number is too small(at least 2")
            
            for i in range(0,loop_times):
                hash1 = hashlib.sha256(want_to_encode.encode("utf-8"))
                hash1.update(vaule.encode("utf-8"))
                hash1 = hash1.hexdigest()
                
                hash2 = hashlib.sha384(hash1.encode("utf-8"))
                hash2.update(vaule.encode("utf-8"))
                hash2 = hash2.hexdigest()
                
                hash3 = hashlib.sha224(hash2.encode("utf-8"))
                hash3.update(vaule.encode("utf-8"))
                hash3 = hash3.hexdigest()
        
                hash4 = hashlib.sha1(hash3.encode("utf-8"))
                hash4.update(vaule.encode("utf-8"))
                encoded = hash4.hexdigest()
    
            return encoded
    class md5:
        def md5encode(rawdata:str,encodetimes:int):
            if encodetimes <= 1:
                raise TypeError("This number is too small(need to >1)")
            
            for i in range(0,encodetimes):
                rawdata = hashlib.md5(rawdata.encode("utf-8")).hexdigest
            return rawdata
    class aes:
        def aesencode(rawdata:str,key_length:int,want_to_save:bool):
            """
                this is aes encrypt.\n
                *note:key_length is in byte,but key is in bit
            """
            key = get_random_bytes(key_length)
            generated = PBKDF2(rawdata,key,dkLen=key_length).decode("utf-8")
            if want_to_save == True:
                open("key.bin","x").close
                file = open("key.bin","a")
                file.write(generated)
                file.close
            elif want_to_save == False:
                pass
            return generated

class generater:
    def random(start:int,end:int):
        return randrange(start=start,start=end)