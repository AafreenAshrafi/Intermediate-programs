#import bs4 as bs
import urllib.request
import re
postal_code = input('enter the postal code for weather like 106,105(us): ')
#call site and pass the zip and read the data
#https://www.wunderground.com/weather-by-zip-code.asp
#https://www.wunderground.com/cgi-bin/findweather/getForecast?query=pz:106&zip=1
a = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query=pz:'
b= postal_code
c ='&zip=1'
url = a+b+c
#print(url)
headers ={}
headers['User-Agent'] = "mozilla/5.0 (Xll; Linux 1686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
try:
        
    req = urllib.request.Request(url, headers = headers)
    sauce = urllib.request.urlopen(req)
    z = sauce.read()
    td = re.findall(r'<span class="wx-value">(.*?)</span>',str(z))
    for eachtd in td:
        print(eachtd)
    savefile = open ('temperature.txt','w')
    savefile.write(str(z))
except Exception as e:
    print(str(e
              ))
      
