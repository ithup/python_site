#Author:ithuplion
import urllib.request
file=urllib.request.urlopen("http://www.36dsj.com/archives/13700")
data=file.read()
dataline=file.readline()
# print(dataline)
# print(data)
fhandle=open("d:/Python35/myweb/part4/36dsj.html","wb")
fhandle.write(data)
fhandle.close()