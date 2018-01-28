import requests
import sys
from html.parser import HTMLParser

resultKilo = 0
class myParser(HTMLParser):
    resultKilo = 1
    a_text=False
    def handle_starttag(self,tag,attrs):
        if tag=="h3":
            self.a_text=True
    def handle_endtag(self,tag):
        if tag=="h3":
            self.a_text=False
    def handle_data(self,data):
        if self.a_text is True:
            myParser.resultKilo = data

# data={
#     'shikechaxun':'时刻查询',
#     'txtChufa':sys.argv[1],
#     'txtDaoda':sys.argv[2],
# }

qujian = ['北京', '上海', '厦门', '广州']
sum = 0
for i in range(len(qujian)):
    sum += i
print('sum: ',sum)



s=requests.session()
# raw=s.get('http://juli.liecheshike.com/juli/',data=data)
# result=raw.text
# query=myParser()
# query.feed(result)

data2 = {}
for i in range(len(qujian) - 1):
    for j in range(len(qujian)):

        if i >= j:
            continue
        else:
            data2 = {}
            data2['shikechaxun'] = '时刻查询'
            data2['txtChufa'] = qujian[i]
            data2['txtDaoda'] = qujian[j]
            raw=s.get('http://juli.liecheshike.com/juli/',data=data2)
            result=raw.text
            query=myParser()
            query.feed(result)
            query.close()
            print(qujian[i], '<->', qujian[j], ': ', myParser.resultKilo)