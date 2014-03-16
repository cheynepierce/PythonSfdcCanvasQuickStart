import base64
import hashlib
import hmac

class SignedRequest:
    def __init__(self, secret, sr):
        self.secret = secret
        self.sr = sr

    def verifyAndDecode(self):
        if self.secret == None:
            return None
        if self.sr == None:
            return None
        array = self.sr.split('.')
        if len(array) != 2:
            return None
    
        signature = array[0]
        payload = array[1]
        decodedSignature = base64.b64decode(signature)
        h = hmac.new(self.secret, msg=payload, digestmod=hashlib.sha256).digest()
        if decodedSignature != h:
            return 'the request has been tampered with'
        return base64.b64decode(payload)