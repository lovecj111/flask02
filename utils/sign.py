#https://www.kancloud.cn/lengyueguang/linux/2507087
from eth_keys import keys
from eth_utils import decode_hex
from eth_keys.datatypes import Signature
import ecies
import uuid
# 创建私钥
private_key = keys.PrivateKey(decode_hex('150732a45d384215a9bf6c16ded0974285fa8a17c2350e254cf663a46c6f100c'))
print('private_key:   ',private_key)
public_key = keys.PublicKey(decode_hex('0xf18866aa565fed80215863efc91fb98cacaf152ff59019fa43d1b17dd0964a736498badce47432221ea10a33051f36970baf44904206a1cc0bca7ee2e45f2ae4'))
print('public_key:   ',public_key)
# 通过私钥获取公钥
public_key = private_key.public_key
print('public_key by private_key:   ',public_key.to_hex())
print('address:   ',public_key.to_address())

msg = str(uuid.uuid1())
print('msg:',msg)

#公钥加密 私钥解密
encrypted_msg = ecies.encrypt(public_key.to_hex(), bytes(msg, encoding='utf8')).hex()
print('加密:',encrypted_msg)
recovered_msg = ecies.decrypt(str(private_key), decode_hex(encrypted_msg))
print('解密:',recovered_msg.decode())

#私钥签名 公钥验签
print(bytes(msg, encoding='utf8'))
signature = private_key.sign_msg(bytes(msg, encoding='utf8'))
print('签名:',signature.to_bytes().hex(), type(signature.to_bytes().hex()))
sign1 = Signature(signature_bytes=decode_hex(signature.to_bytes().hex()))
print('验签:',sign1, type(sign1))
# 通过公钥验证签名
print(public_key.verify_msg(bytes(msg, encoding='utf8'), signature))
print(public_key.verify_msg(bytes(msg, encoding='utf8'), sign1))
