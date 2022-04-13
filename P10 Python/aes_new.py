# -*- coding: utf-8 -*-
import base64
from Crypto.Cipher import AES


def AES_Encrypt(key, data):
  vi = '0102030405060708'
  pad = lambda s: s + (16 - len(s)%16) * chr(16 - len(s)%16)
  data = pad(data)
  cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
  encryptedbytes = cipher.encrypt(data.encode('utf8'))
  print(encryptedbytes)
  encodestrs = base64.b64encode(encryptedbytes)
  print(encodestrs)
  enctext = encodestrs.decode('utf8')
  return enctext


def AES_Decrypt(key, data):
  vi = '0102030405060708'
  data = data.encode('utf8')
  encodebytes = base64.decodebytes(data)
  cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
  text_decrypted = cipher.decrypt(encodebytes)
  unpad = lambda s: s[0:-s[-1]]
  text_decrypted = unpad(text_decrypted)
  text_decrypted = text_decrypted.decode('utf8')
  return text_decrypted


key = '0123456789ABCDEF'
data = 'ZKPY'
#AES_Encrypt(key, data)
enctext = AES_Encrypt(key, data)
text_decrypted = AES_Decrypt(key, enctext)
