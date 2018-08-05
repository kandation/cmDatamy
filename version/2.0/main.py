import requests
from bs4 import BeautifulSoup


con = {'keyfaculty': '06', 'keylevel': '1', 'keyyear':'2558'}
re = requests.post("https://www1.reg.cmu.ac.th/reg-stdsearch/index.php?action=cbyf",data=con)



bs = BeautifulSoup(re.text, "lxml")


big_tables = bs.find('table', {'class': 'table-condensed'})
tables = bs.find_all('table', {'class':'table-striped'})

# prepare data store
faculty_data = [[] for x in range(len(tables))]


theads_body = big_tables.find('tbody')

header_trs = theads_body.find_all('tr', {'class':'accordion-toggle'})
for index_header, header_tr in enumerate(header_trs):
    headers = header_tr.find_all('td')
    header_name = headers[2].contents[0]
    faculty_data[index_header] = {'name': header_name}



keywordFind_year = '58'
keywordFind_faculty = '06'
keywordFind_major = '10'

index_major = 0
for table in tables :
    tbodies = table.find_all('tbody')

    faculty_data[index_major]['id'] = index_major
    faculty_data[index_major]['students'] = []

    for tbody in tbodies:
        trs = tbody.find_all('tr')

        for tr in trs:
            if '58' in tr.text:

                p = tr.find_all('td')

                sid = str(p[0].text)
                sName = p[1].contents
                # ssss = " ".join(str(sName).strip().re)
                import re
                endSName = str(sName[0])
                thsSName = str(sName[1].text)

                engName = str(" ".join(re.split("\s+", endSName, flags=re.UNICODE))).strip()
                thaName = str(" ".join(re.split("\s+", thsSName, flags=re.UNICODE))).strip()

                tr_data = {'sid': sid, 'eng-name': engName, 'tha-name': thaName}

                faculty_data[index_major]['students'].append(tr_data)
                # print(tr.find_all('td')[0])
    index_major += 1

import pprint
pprint.pprint(faculty_data)

import json
fo = open('data/student_data'+con['keyyear']+'.txt', mode='w', encoding='utf8')
text = str(json.dumps(faculty_data, ensure_ascii=False))
fo.write(text)
fo.close()