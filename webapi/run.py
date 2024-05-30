# from datetime import datetime, timedelta
# import jwt
# from time import time


# secret = 'rs12345'

# def encode_token(user_id):
#     print(user_id)
#     payload = {
#         'exp': datetime.now() + timedelta(days=7, minutes=5),
#         'iat': time(),
#         'sub': user_id
#     }

#     options = {
#         'expires': f"{datetime.now() + timedelta(days=7, minutes=5)}",
#         'httpOnly': True,
#         'sameSite': 'none',
#         'secure': True,
#     }
#     return jwt.encode(
#         payload,
#         secret,
#         algorithm='HS256'
#     ), options


# def decode_token(token):
#     try:
#         return jwt.decode(token, secret, algorithms=['HS256'])
#     except jwt.ExpiredSignatureError as e:
#             print("......................1")
#             raise e
#     except jwt.InvalidTokenError as er:
#         print("......................2")
#         raise er
    
# e = encode_token('123456rsdq')  

# d = decode_token(e[0])

# print(d)

# # jwt.decode(jwt.encode({'iat': time()}, 'secret', algorithm='HS256'), 'secret', algorithms=['HS256'])
# import json
# a = [ 1,2]


# k = {"id": 'tgrrgrg25'}
# print(json.dumps(list(k.keys())))

# a[2]= 3
# print(a)

# userSocketMap = {}

# def getReceiverSocketId(receiverId):
# 	return userSocketMap[receiverId]

# a = getReceiverSocketId("123456")
# print(a)

a = {'a': '1', 'b': '2'}
print(list(a.keys())[0])