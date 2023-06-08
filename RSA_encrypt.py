# -*- coding: UTF-8 -*-
# ! /usr/bin/env python
import base64,os
import rsa
from rsa import common


def RSA_keyTopem(save_path:str):
    pem_path=save_path if os.path.isdir(save_path) else os.getcwd()
    pub, pvt = rsa.newkeys(2048)    # 生成公钥public key、私钥private key
    pub_file=os.path.join(pem_path,"pub.pem")
    pvt_file=os.path.join(pem_path,"pvt.pem")
    with open(pub_file,"wb") as fp:
        pub=pub.save_pkcs1()
        fp.write(pub)
    with open(pvt_file,"wb") as fs:
        pvt=pvt.save_pkcs1()
        fs.write(pvt)
    return pub_file,pvt_file

PUBLIC_KEY_PATH = '/rsa_public_key.pem'  # 公钥
PRIVATE_KEY_PATH = '/rsa_private_key.pem'  # 私钥

# 使用 rsa库进行RSA签名和加解密
class RsaUtil(object):

    # 初始化key
    def __init__(self,
                 pub_file=PUBLIC_KEY_PATH,
                 pri_file=PRIVATE_KEY_PATH):

        if pub_file:
            with open(pub_file,"rb") as fp:
                pub_key=fp.read()
                self.public_key = rsa.PublicKey.load_pkcs1(pub_key)
        if pri_file:
            with open(pri_file,"rb") as fp:
                pvt_key=fp.read()
                self.private_key = rsa.PrivateKey.load_pkcs1(pvt_key)

    def get_max_length(self, rsa_key, encrypt=True):
        """加密内容过长时 需要分段加密 换算每一段的长度.
            :param rsa_key: 钥匙.
            :param encrypt: 是否是加密.
        """
        blocksize = common.byte_size(rsa_key.n)
        reserve_size = 11  # 预留位为11
        if not encrypt:  # 解密时不需要考虑预留位
            reserve_size = 0
        maxlength = blocksize - reserve_size
        return maxlength

    # 加密 支付方公钥
    def encrypt_by_public_key(self, message):
        """使用公钥加密.
            :param message: 需要加密的内容.
            加密之后需要对接过进行base64转码
        """
        encrypt_result = b''
        max_length = self.get_max_length(self.public_key)
        while message:
            input = message[:max_length]
            message = message[max_length:]
            out = rsa.encrypt(bytes(input,encoding="utf-8"), self.public_key)
            encrypt_result += out
        encrypt_result = base64.b64encode(encrypt_result)
        return encrypt_result

    def decrypt_by_private_key(self, message):
        """使用私钥解密.
            :param message: 需要加密的内容.
            解密之后的内容直接是字符串，不需要在进行转义
        """
        decrypt_result = b""

        max_length = self.get_max_length(self.private_key, False)
        decrypt_message = base64.b64decode(message)
        while decrypt_message:
            input = decrypt_message[:max_length]
            decrypt_message = decrypt_message[max_length:]
            out = rsa.decrypt(input, self.private_key)
            decrypt_result += out
        return decrypt_result

    # 签名 商户私钥 base64转码
    def sign_by_private_key(self, data):
        """私钥签名.
            :param data: 需要签名的内容.
            使用SHA-1 方法进行签名（也可以使用MD5）
            签名之后，需要转义后输出
        """
        signature = rsa.sign(bytes(data,encoding="utf-8"), priv_key=self.private_key,hash_method="SHA-256")
        return base64.b64encode(signature)

    def verify_by_public_key(self, message, signature):
        """公钥验签.
            :param message: 验签的内容.
            :param signature: 对验签内容签名的值（签名之后，会进行b64encode转码，所以验签前也需转码）.
        """
        signature = base64.b64decode(signature)
        return rsa.verify(bytes(message,encoding="utf-8"), signature, self.public_key)

if __name__=="__main__":
    print(os.path.abspath(".\\pem"))
    pub_key_path,pvt_key_path=RSA_keyTopem(os.path.abspath(".\\pem"))
    rsaUtil = RsaUtil(pub_key_path,pvt_key_path)
    message = 'ChatGPT world' # should be str
    print("明文内容：>>> ")
    print(message)
    encrypy_result = rsaUtil.encrypt_by_public_key(message)
    print("加密结果：>>> ")
    print(encrypy_result)
    decrypt_result = rsaUtil.decrypt_by_private_key(encrypy_result)
    print("解密结果：>>> ")
    print(decrypt_result)
    sign = rsaUtil.sign_by_private_key(message)
    print("签名结果：>>> ")
    print(sign)
    print("验签结果：>>> ")
    print(rsaUtil.verify_by_public_key(message, sign))

