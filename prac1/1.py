from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用
import requests
from bs4 import BeautifulSoup
import openpyxl

#放进excel里
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'new title，intern'
sheet['A1'] = 'company name'
sheet['B1'] = 'contact'
sheet['C1'] = 'contact_wechat'
sheet['D1'] = 'contact_3'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = "http://www.meltoday.com/flooring_carpet"
result_link = []
html_content = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(html_content, "html.parser")
link_nodes = soup.find_all('a')
for node in link_nodes:
   result_link.append(node.get("href"))

#print(result_link)
#爬取link
result_link =['http://www.meltoday.com/flooring_carpet112020481265008',
    'http://www.meltoday.com/flooring_carpet112020481265008',
    'http://www.meltoday.com/flooring_carpet112018228503001',
    'http://www.meltoday.com/flooring_carpet112018228503001',
    'http://www.meltoday.com/flooring_carpet112023445538023',
    'http://www.meltoday.com/flooring_carpet112023445538023',
    'http://www.meltoday.com/flooring_carpet112032575753013',
    'http://www.meltoday.com/flooring_carpet112032575753013',
    'http://www.meltoday.com/flooring_carpet112037751743010',
    'http://www.meltoday.com/flooring_carpet112037751743010',
    'http://www.meltoday.com/flooring_carpet112025747038017',
    'http://www.meltoday.com/flooring_carpet112025747038017',
    'http://www.meltoday.com/flooring_carpet112038254765016',
    'http://www.meltoday.com/flooring_carpet112038254765016',
    'http://www.meltoday.com/flooring_carpet112031341729020',
    'http://www.meltoday.com/flooring_carpet112031341729020',
    'http://www.meltoday.com/flooring_carpet111943454483004',
    'http://www.meltoday.com/flooring_carpet111943454483004',
    'http://www.meltoday.com/flooring_carpet112032552736027',
    'http://www.meltoday.com/flooring_carpet112032552736027',
    'http://www.meltoday.com/flooring_carpet111705435849002',
    'http://www.meltoday.com/flooring_carpet111705435849002',
    'http://www.meltoday.com/flooring_carpet112012268582008',
    'http://www.meltoday.com/flooring_carpet112012268582008',
    'http://www.meltoday.com/flooring_carpet112035538634025',
    'http://www.meltoday.com/flooring_carpet112035538634025',
    'http://www.meltoday.com/flooring_carpet112033428192010',
    'http://www.meltoday.com/flooring_carpet112033428192010',
    'http://www.meltoday.com/flooring_carpet112032143706015',
    'http://www.meltoday.com/flooring_carpet112032143706015',
    'http://www.meltoday.com/flooring_carpet112024457876010',
    'http://www.meltoday.com/flooring_carpet112024457876010',
    'http://www.meltoday.com/flooring_carpet112018681724001',
    'http://www.meltoday.com/flooring_carpet112018681724001',
    'http://www.meltoday.com/flooring_carpet112018674663036',
    'http://www.meltoday.com/flooring_carpet112018674663036',
    'http://www.meltoday.com/flooring_carpet112014275907022',
    'http://www.meltoday.com/flooring_carpet112014275907022',
    'http://www.meltoday.com/flooring_carpet111902769220037',
    'http://www.meltoday.com/flooring_carpet111902769220037',
    'http://www.meltoday.com/flooring_carpet112009470610073',
    'http://www.meltoday.com/flooring_carpet112009470610073',
    'http://www.meltoday.com/flooring_carpet111936161826038',
    'http://www.meltoday.com/flooring_carpet111936161826038',
    'http://www.meltoday.com/flooring_carpet111931438799081',
    'http://www.meltoday.com/flooring_carpet111931438799081',
    'http://www.meltoday.com/flooring_carpet111930579172048',
    'http://www.meltoday.com/flooring_carpet111930579172048',
    'http://www.meltoday.com/flooring_carpet111927154891062',
    'http://www.meltoday.com/flooring_carpet111927154891062',
    'http://www.meltoday.com/flooring_carpet111916147123036',
    'http://www.meltoday.com/flooring_carpet111916147123036']

list_all=[]
for url in range(0,len(result_link)):
    r=requests.get('http://www.meltoday.com/flooring_carpet112020481265008')
    r.encoding='utf-8'
    r.encoding=r.apparent_encoding
    result=r.text
    bs=BeautifulSoup(r.text,'html.parser')

    name=bs.find_all('div',class_="col-xs-6")
    contact=bs.find_all('div',class_="col-xs-6 no-padding-right")
    contact_wechat=bs.find_all('img',src_="/detail/str_to_image/XYDKsyrF_HOBw6kAFGWgtTeG/black")
    contact_3=bs.find_all('div',class_="yp-contact-detail")

    list_all.append([name,contact,contact_wechat,contact_3])
list_all=[]
    for i in list_all:
        name = i['company name']
        contact=i['contact']
        contact_wechat=i['contact_wechat']
        contact_3=i['contact_3']
        sheet.append([name,contact,contact_wechat,contact_3])

    wb.save('Intern.xlsx')

