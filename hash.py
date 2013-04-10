#!/usr/bin/python
# -*- coding: UTF-8 -*-
#点击Add，添加pydev的安装地址：http://pydev.org/updates/，如下图所示。
#1、安装依赖项
#- **Python 2.3 or newer**
#- **OpenSSL 0.9.7 or newer**
#sudo apt-get install openssl
#- **SWIG 1.3.28 or newer**
#sudo apt-get install swig
#2、安装 M2Crypto
#sudo apt-get install python-m2crypto

import M2Crypto
import time  

class HashBysha1Ormd5:
    def __init__(self,alg):
        self._alg = alg
    def hash(self,message):
        m=M2Crypto.EVP.MessageDigest(self._alg)
        m.update(message)
        return m.digest()

if __name__ == '__main__':  
    h = HashBysha1Ormd5("sha1")
    readbuf = ""
    filename = raw_input('enter filename:')
    with open(filename,'r') as f:
        print "reading..."
        for line in f: 
            readbuf += line
    f.close()
    print "length:%d byte" % len(readbuf)
    before = time.time()
    print "hash:%s" % h.hash(readbuf)
    elapsed = time.time() - before
    print "elapse:%s(s),rate:%s(byte/s)" % (str(elapsed) ,str(len(readbuf) / elapsed))
