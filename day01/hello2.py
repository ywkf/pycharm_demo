import sys

import onetimepass as otp


my_secret = 'zuwhrtmfuo5rrmfe6jw2yb7w3sf3jc3g'
my_token = str(otp.get_totp(my_secret))
if len(my_token) == 5:
    my_token = '0' + my_token

print(my_token)

# my_token = 123456 # should be probably from some user's input
is_valid = otp.valid_totp(token=my_token, secret=my_secret)
print(is_valid)

code = b'*\x17N\xf4\xd7(P\x90\xa0\xf6\xa8e\xae\x89v5Z\xcd\xbb\\'
# codes = bytes.decode(code)
# print(codes)