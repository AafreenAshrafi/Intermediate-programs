import bs4 as bs
import urllib.request
import re
postal_code = input('enter the postal code for weather: ')
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
    soup = bs.BeautifulSoup(z,'lxml')
    table = soup.find('table')
    table_row = table.find_all('tr')
    for tr in table_row:
        td = tr.find('td')
        for celcius in td:
            temperature = td.find('span')
            print(temperature)
        
     
except Exception as e:
    print(str(e))
