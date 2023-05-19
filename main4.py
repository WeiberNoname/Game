import requests
from urllib.parse import urlparse
uuu = "https://www.youtube.com/watch?v=H8t4DJ3Tdrg"
ttt = requests.get(uuu)
ttt.encoding = ""
print(ttt.text)
o = urlparse(uuu)
print(o)
print("ccc{}".format(o.scheme))
print("xxx {}".format(o.netloc))
print("uuu{}".format(o.path))
print("uuu{}".format(o.port))
print("iii{}".format(o.query))
grade = []
vvv = ppp = lll = 0
while lll != 1:
    lll = int(input("www"))
    grade.append(lll)
print("%d" % (len(grade)-1))
for i in range(0,(len(grade)-1)):
    vvv += grade[i]
    ppp = vvv / (len(grade)-1)
print("%d___%d" % (vvv,ppp))
