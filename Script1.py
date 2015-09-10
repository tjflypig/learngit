import urllib
url0='http://blog.sina.com.cn/u/1347712670'
con=urllib.urlopen(url0).read()
'''
i=0
htmlindex=[]
html=[]
htmlindex.append(con.find('<a href='))
htmlindex1=con.find('</a>',htmlindex)
html.append(con[htmlindex+9:htmlindex1+4])
while (i<10 and i!=0):
    htmlindex.append(con.find('<a href=',htmlindex1))
    htmlindex1=con.find('</a>',htmlindex)
    html.append(con[htmlindex+9:htmlindex1+4])
    i=i+1
print html
'''
html=[]
i=0
htmlindex=1
htmlindex1=0
while (htmlindex):
	htmlindex=con.find('<a href=',htmlindex1)
	htmlindex1=con.find('</a>',htmlindex)
	if con.find('http',htmlindex,htmlindex1)!= -1 and con.find('html',htmlindex,htmlindex1)!= -1:
		html.append(con[con.find('http',htmlindex,htmlindex1):con.find('html',htmlindex,htmlindex1)+4])
	