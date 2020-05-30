import base64
from Crypto.Cipher import AES
import json
#==============AES加密算法============================
from django.http import JsonResponse

BS = 16
unpad =lambda  s:s[0: -ord(s[-1])]

def decryptBase64(src):
    return base64.urlsafe_b64decode(src)

def defcryptAES(src,key):
    """
    解析AES密文
    :param src: 
    :param key: 
    :return: 
    """
    src =decryptBase64(src)
    iv = b"1172311105789011"
    cryptor =AES.new(key,AES.MODE_CBC,iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text)

def aes_encryption(request):

    app_key ='W7v4D60fds2Cmk2U'

    if request.method =='POST':
        data =request.POST.get("data","")
    else:
        return "error"

    #解密
    decode =defcryptAES(data,app_key)
    dict_data =json.loads(decode)
    return dict_data
#....


#嘉宾查询接口---AES算法
def get_guest_list(request):
    dict_data =aes_encryption(request)

    if dict_data =="error":
        return JsonResponse({'status':1001,'message':'request error'})

    #取出对应发布会id和嘉宾手机号
    eid =dict_data['eid']
    phone = dict_data['phone']