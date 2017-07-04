#Author:ithuplion
import urllib.request
file=urllib.request.urlopen("http://v3.bootcss.com/")
data=file.read()
dataline=file.readline()
# print(dataline)
# print(data)
fhandle=open("d:/Python35/myweb/part4/bootstrap.html","wb")
fhandle.write(data)
fhandle.close()