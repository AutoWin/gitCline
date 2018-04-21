import io
import json
from _datetime import datetime
import time

st = time.time()
with io.open('fileFilter.json', 'w+', encoding='utf-8') as f:
    dateM = datetime.strptime('01/09/2017', '%d/%m/%Y')
    dictionary = {}
    with open('def2.json', 'r') as fd:
        for line in fd:
            jsonObj = json.loads(line)

            #date =  ''.join(i for i in str(jsonObj['Ngày cấp']).split('/'))
            #print (date>dateM)
            #print (jsonObj['Điện thoại'] is not None)
            #status = 'đang hoạt động'
            #print (status in jsonObj['Trạng thái'])
            print (type(jsonObj))
            try:
                status = 'đang hoạt động'
                date = datetime.strptime(jsonObj['Ngày cấp'], '%d/%m/%Y')
                if (jsonObj['Điện thoại'] is not None) and (date>dateM) and (status in jsonObj['Trạng thái']):

                    f.write(json.dumps(jsonObj, ensure_ascii=False)+'\n')
            except KeyError:
                pass

et = time.time()
print ("Time: {}".format(et-st))