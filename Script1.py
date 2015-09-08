import urllib
url0='http://blog.sina.com.cn/u/1347712670'
con=urllib.urlopen(url0).read()
i=0
html=[]
htmlindex=con.find('<a href=')
htmlindex1=con.find('</a>',htmlindex)
html.append(con[htmlindex+9:htmlindex1+4])
while (i<10 and i!=0):
    htmlindex=con.find('<a href=',htmlindex1)
    htmlindex1=con.find('</a>',htmlindex)
    html.append(con[htmlindex+9:htmlindex1+4])
    i=i+1
print html
