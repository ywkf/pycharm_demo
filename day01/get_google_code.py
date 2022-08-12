import hmac, base64, struct, hashlib, time
import sys

from po1.tools.get_log import GetLog


class GetGoogleCode():

    def calGoogleCode(self, secretKey):
        GetLog.get_log().info('secretKey: {}'.format(secretKey))
        secretKey = secretKey.upper()
        GetLog.get_log().info('secretKey upper: {}'.format(secretKey))
        input = int(time.time()) // 30
        GetLog.get_log().info('time.time(): {}'.format(time.time()))
        GetLog.get_log().info('input: {}'.format(input))
        key = base64.b32decode(secretKey)
        GetLog.get_log().info('key: {}'.format(key))
        msg = struct.pack(">Q", input)
        GetLog.get_log().info('msg: {}'.format(msg))
        googleCode = hmac.new(key, msg, hashlib.sha1).digest()
        GetLog.get_log().info('googleCode: {}'.format(googleCode))
        # 版本判断
        if (sys.version_info > (2, 7)):
            GetLog.get_log().info('sys.version_info: {}'.format(sys.version_info))
            o = googleCode[19] & 15
            GetLog.get_log().info('googleCode type: {}'.format(type(googleCode)))
            GetLog.get_log().info('googleCode[19]: {}'.format(googleCode[19]))
            GetLog.get_log().info('o: {}'.format(o))
        else:
            o = ord(googleCode[19]) & 15
            GetLog.get_log().info('o: {}'.format(o))
        googleCode = str((struct.unpack(">I", googleCode[o:o + 4])[0] & 0x7fffffff) % 1000000)
        GetLog.get_log().info('googleCode: {}'.format(googleCode))
        if len(googleCode) == 5:  # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
            GetLog.get_log().info('googleCode: {}'.format(googleCode))
            googleCode = '0' + googleCode
        return googleCode


if __name__ == '__main__':
    qr = 'zuwhrtmfuo5rrmfe6jw2yb7w3sf3jc3g'
    google = GetGoogleCode()
    code = google.calGoogleCode(qr)
    print(code)

    pmake_secret = 'ne4weqjz7utzgkryur5ptgogu5oj2zig'
    check_secret = 'rcb6oqkkhofdlj5ompri3hdejfkt2yro'
    check_fin_secret = 'n4reogis6cxodn34hryo7f7l3vvfdb4o'
    print(pmake_secret.upper())
    print(check_secret.upper())
    print(check_fin_secret.upper())

    code1 = google.calGoogleCode(pmake_secret)
    code2 = google.calGoogleCode(check_secret)
    code3 = google.calGoogleCode(check_fin_secret)
    print(code1)
    print(code2)
    print(code3)
