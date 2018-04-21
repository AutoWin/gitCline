import io
import fileinput
import json
str= 'Email, Người đại diện, Điện thoại người đại diện, Giám đốc, Điện thoại giám đốc, Tên chính thức, Mã doanh nghiệp, Địa chỉ trụ sở, Ngành nghề chính, Loại khoản'

fields = ['Tên chính thức', 'Mã doanh nghiệp', 'Địa chỉ trụ sở', 'Email',  'Người đại diện', 'Giám đốc', 'Điện thoại giám đốc',   'Ngành nghề chính',  'Cấp chương', 'Loại khoản','Điện thoại']
print (len(fields))
removes = ['Fax', 'Website', 'Thông tin liên hệ', 'Trạng thái', 'Ngày bắt đầu hoạt động', 'Địa chỉ người đại diện', 'Địa chỉ kế toán', 'Cơ quan thuế quản lý', 'Ngày cấp','Tên giao dịch','Lĩnh vực kinh tế',
           'Loại hình kinh tế', 'Loại hình tổ chức', 'Địa chỉ giám đốc', 'Điện thoại kế toán','THÔNG TIN CHI TIẾT', 'Thông tin đăng ký doanh nghiệp',  'THUẾ PHẢI NỘP', 'Môn bài', 'Thông tin liên hệ', 'NGÀNH NGHỀ KINH DOANH', 'Kế toán', 'Thông tin ngành nghề, lĩnh vực hoạt động']
print (len(removes))
end = ('='*50)

f  = open('def.txt','r')
data = f.read().splitlines()

with io.open('def2.txt','w', encoding='utf-8') as f:
    d = 0
    dictionary = {}
    while(d<len(data)):
        if data[d] == end:
            d = d+1
            f.write(json.dumps(dictionary, ensure_ascii=False)+'\n')
            dictionary.clear()
        elif data[d] in removes :
            d = d +1
        elif data[d] in fields:
            temp=0
            for i in range(d+1, d+20):
                if data[i] in fields or data[i] in removes:
                    temp = i
                    break

            for j in range(d+1, temp):
                dictionary[data[d]] = data[j]
            d = temp

        else:
            d  = d+1

