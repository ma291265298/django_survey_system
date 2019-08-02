import rsa
from django.http import JsonResponse
from django.shortcuts import render
import json
import base64

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from survey.models import *
rsa_private_key=b"-----BEGIN RSA PRIVATE KEY-----\n\
MIIEowIBAAKCAQB+D6XE0YI03iyftOeE5bRedEKinVYiYbZmAEM833FoBIfY28ZT\
2a1Npnb5YTS7tw2bQTpvydZwq229r53y2/jO/VdtCjCsMtNnpSAhahCbdrbMSPkL\
vLrkHsZh55hX+drId74HU4oaMtk9DROdOWd2MzBhxaA97Z3uSB1ICX4P1Xmeif2c\
CgUFefMFPOiWn8OgpeI+vkne5xpbGP5HT5y7JtRsg5H9wn87MvwaRyQNH7ep7Lvt\
555ZBtUiKDRX5MgMmg1eVgvayibFLP7fOHHSe+5yjnf08wsNsd/vltiCAeRhUzFe\
4Ux8NWz4XX3Nn6zUj8jx5wSswDnzDbv27lcJAgMBAAECggEAVeN7YjoMqNCnPrkW\
9Ok8lw5HSFxCj3Jbv+t15EepEOHlXM+AtSied0Vv0kF0mGEEGD+8/OVcAbALOS4q\
Q4m0X/MkWdqThv+qIffTiHCnmASuT0l4xZJ1E3AUYihVF7vYYLWU95DniyoR8RKz\
xm+SGmqOEE+B+i+nZu4jZS1ygn5Ht+A/MeqkBNIJ9F/YrO/TvdOBCoYLrcuN033j\
4O87Y4Pyx2fB6+OiKN9EAlo3bYidazvD3smw1maRFvIKz8AgKw9eB8T+nmfFTv0j\
kTLBUMAjhFH/ZKzKr3jbsDfo4HeF6gOcs/WUd3joavGTKQARLPUsuQzAmKQzE3Zu\
NM7QcQKBgQDmxIG9kIh9M32YLXYh52Su7xYvQip4savNCdjdE/qkFWLaWBseoDBQ\
/EKWzQYeLoxv2MKUsIobUIpsW4gjaXXOFmammlo5dfHu6eAdRMIxbu7Gn+admUVZ\
jX3f6hw2cDKSeVqUCacEHUBPDo2TvxsMkIHz27Wan29J+EmeY5bsvwKBgQCL2EQ/\
e25TGcEC8z1hCpez9ACU11bwx3W23C3+Tan7UJ6VRTe16zf5SndT7qp7LDP0V5cu\
cu12vZcsxlUFBNhUpKGQmaHXpiTQ04MUemNun9tJU0E0+T/ZMjYAA+Yi4avf/VX7\
Vlx5JKd3d5hKOPincB4a55W8fOFTGPXHVEsGNwKBgQCiuIXTqYrU3e391HCsT4HL\
aIN4J2vTV1URa5Qjr+bYtMvTsrTMz5/CO16o/0EFH0WfyHTMa/+2awBwj8pbTg3n\
mBwh9k0Qn35NPVTuzoEwYky0eiQflOg10XOk5GuoZ00Bw9h+8p92YznphRWHzQXB\
wlQgJBjWQv4yZoVizk6p+QKBgHfMJnrzdAlAULYERZpyBo8kAbN/3Xyagd7KM6Rc\
R7eA0rkw+I6hF+w4vIxsMiMeNMumlV43GfHUbELxDDgmdGPePIGw+pHQRE2YQ/ww\
9Cj6TFI+PefxdZ7MgrH0pRtQk3pofVW4H7OvkL6o9w7uSyS0yTVnGkDEAgq7oSDG\
txZ1AoGBAL2GAoBwNX9Of9yTR0kuUzAgK71woQjhcRnzxA6fyxKlyrmQRCWKz0p0\
LCpy80fp1aJ94Gm6D9xlb8FMJB9x7PgGv/JRJqm+FTmDCM8JSZqhC+5pKeJo5LWM\
Gi1fnSi64V61IhX/YTLXf7lLcXtIyPa8TSVHqavI0kKQQlo7OT5j\n\
-----END RSA PRIVATE KEY-----"

def addView(request):
    return render(request, "login.html")
def erro(request):
    return render(request, "404.html")

def addSuccess(request):
    paper_obj=Paper(name=request.POST.get('paperName'),
                    detail=request.POST.get('paperDetail'))
    paper_obj.save()
    for i in json.loads( request.POST.get('questions')):
        question_obj=Question(no=i['no'],content=i['questionName'],type=i['type'],ismustfill=i['ismustfill'],pid=paper_obj)
        question_obj.save()
        count=1
        for k in i['option']:
            option_obj=Option(no=count,content=k,qid=question_obj)
            count+=1
            option_obj.save()
    return JsonResponse({'resultCode':0})

def sendRegisterEmail(request):
    m=request.POST.get('raw')
    rsakey = RSA.importKey(rsa_private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(m), None)
    c=text.decode('utf8')
    adict=eval(c)
    print(adict['name'])
    print(adict['email'])
    print(adict['password'])

