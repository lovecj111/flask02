
from eth_keys import keys
from eth_utils import decode_hex
import uuid

# 创建私钥
private_key = keys.PrivateKey(decode_hex('150732a45d384215a9bf6c16ded0974285fa8a17c2350e254cf663a46c6f100c'))
print('private_key:   ', private_key)
#public_key = keys.PublicKey(decode_hex('0xf18866aa565fed80215863efc91fb98cacaf152ff59019fa43d1b17dd0964a736498badce47432221ea10a33051f36970baf44904206a1cc0bca7ee2e45f2ae4'))
public_key = keys.PublicKey(decode_hex('0456c60dd14168216d997c37d7d72673bfc6d7559cc136c1cea993a8ad7c48125e8ca5feb0c11b390a4cc52b20b0e55d069cce06f81c32a7602fb17d9990a99a6e'))
print('public_key:   ', public_key)

for i in range(10):
    msg = str(uuid.uuid1())
    print("msg", msg)
    # 私钥签名 公钥验签
    signature = private_key.sign_msg(bytes(msg, encoding='utf8'))
    print('签名:', signature.to_bytes().hex())
    # 通过公钥验证签名
    print(public_key.verify_msg(bytes(msg, encoding='utf8'), signature))
