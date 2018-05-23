import urllib.request
import xdrlib

#coding:utf-8

str0 = 'blabla<a title="地震思考录" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'
title = str0.find(r'<a title')
print(title)
href = str0.find(r'href=')
print(href)
html = str0.find(r'.html')
print(html)
url = str0[href +6:html +5]
print(url)
filename = url[-26:]
print(filename)

req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0')
response = urllib.request.urlopen(url)
#html1 = response.read().decode('utf-8')
html1 = response.read().decode('utf-8')
open(filename,'w').write(html1)

print(html1)