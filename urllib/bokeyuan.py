#Author:ithuplion
import urllib.request
file=urllib.request.urlopen("http://www.cnblogs.com/alex3714/articles/5465198.html")
data=file.read()
dataline=file.readline()
# print(dataline)
# print(data)
fhandle=open("d:/Python35/myweb/part4/alex01.html","wb")
fhandle.write(data)
fhandle.close()