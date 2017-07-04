#Author:ithuplion
import urllib.request
file=urllib.request.urlopen("http://www.baidu.com")
data=file.read()
dataline=file.readline()
# print(dataline)
# print(data)
fhandle=open("d:/Python35/myweb/part4/baidu.html","wb")
fhandle.write(data)
fhandle.close()