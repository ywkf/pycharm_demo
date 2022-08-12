import hmac, base64, struct, hashlib, time
import sys


class GetGoogleCode():

    def calGoogleCode(self, secretKey):
        secretKey = secretKey.upper()
        input = int(time.time()) // 30
        key = base64.b32decode(secretKey)
        msg = struct.pack(">Q", input)
        googleCode = hmac.new(key, msg, hashlib.sha1).digest()
        # 版本判断
        if (sys.version_info > (2, 7)):
            o = googleCode[19] & 15
        else:
            o = ord(googleCode[19]) & 15
        googleCode = str((struct.unpack(">I", googleCode[o:o + 4])[0] & 0x7fffffff) % 1000000)
        if len(googleCode) == 5:  # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
            googleCode = '0' + googleCode
        return googleCode


if __name__ == '__main__':
    qr = 'zuwhrtmfuo5rrmfe6jw2yb7w3sf3jc3g'
    code = GetGoogleCode().calGoogleCode(qr)
    print(code)
