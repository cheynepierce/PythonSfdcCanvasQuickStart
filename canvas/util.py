import base64
import hashlib
import hmac

class SignedRequest:
    def __init__(self, secret, sr):
        self.secret = secret
        self.sr = sr

    def verifyAndDecode(self):
        if self.secret == None:
            raise Exception('Secret is null')
        if self.sr == None:
            raise Exception('Signed request is null')
        array = self.sr.split('.')
        if len(array) != 2:
            raise Exception('Signed request is formatted incorrectly')
    
        signature = array[0]
        payload = array[1]
        decodedSignature = base64.b64decode(signature)
        h = hmac.new(self.secret, msg=payload, digestmod=hashlib.sha256).digest()
        if decodedSignature != h:
            raise Exception('the request has been tampered with')
        return base64.b64decode(payload)