# -- coding: UTF-8 --
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import sys
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import urllib.parse,urllib.request,urllib.error
base="https://nazrul-rachanabali.nltr.org/"
page=urllib.request.urlopen(base).read();
soup=BeautifulSoup(page,'html5lib')
ba=soup.find_all("ul",{"class":["slidedoormenu"]})
#print(ba)
d=soup.div.ul.find_all('a')
#type(d[3])
article_page=(d[3]).get("href")
#soup.div.ul.li.a


newurl_2=base+article_page
page1=urllib.request.urlopen(newurl_2).read()
soup1=BeautifulSoup(page1,'html5lib')
e=soup1.find_all('a')
arr1=[]
arr4=[]
for link in e[1:9]:
    f=link.get('href')
    f=base+f
    arr1.append(f)
    arr4.append(link.get_text())
#for k in arr2:
for m in range(0,len(arr4)):  
    page1=urllib.request.urlopen(arr1[m]).read()
    soup1=BeautifulSoup(page1,'html5lib')
    x=soup1.find_all('div',id='data')
    arr2=[];
    arr3=[];
    for i in x:
        g=i.find_all('a')
        for k in g[:-7]:
            arr2.append(k.get('href'))
            arr3.append(k.get_text())
            
    for z in range(0,len(arr3)):     
        final_url=base+arr2[z]
        #==============================================================================
    #    page1=urllib.request.urlopen(final_url).read()
    #    soup1=BeautifulSoup(page1,'html5lib')
    #    head = soup1.find_all("p",class_="head1")
    #    headd=head[0].get_text()
        #==============================================================================
        
        filenam = "D:\%s\%s"%(arr4[m],arr3[z])
        if not os.path.exists(filenam):
            os.makedirs(filenam)
        for i in range(0,110):
            if arr3[z].endswith(" "):
                arr3[z]=arr3[z][:-1]
            filename = "D:\%s\%s\%s_%d.txt"%(arr4[m],arr3[z],arr3[z],i)
            fi = open(filename, "wb")
            page1=urllib.request.urlopen(final_url).read()
            soup1=BeautifulSoup(page1,'html5lib')
            final_url=base+arr2[z]
            h=soup1.find_all('div',id="data")
            for j in h:
                fi.write(j.text.encode("utf-8"))
                s=j.text
            if not s.split():
                break
            a,b=final_url.split('1&titleid=')
            final_url=a+str(i+1)+"&titleid="+b
            print('************'+final_url+'***********')
        fi.close()





