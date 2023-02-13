from eth_keys import keys
from eth_utils import decode_hex

h = decode_hex('0x56c60dd14168216d997c37d7d72673bfc6d7559cc136c1cea993a8ad7c48125e8ca5feb0c11b390a4cc52b20b0e55d069cce06f81c32a7602fb17d9990a99a6e')
print(h)
public_key = keys.PublicKey(h)
print('public_key:   ', public_key)
