import requests as rs
import base64
import csv

email='XXX@qq.com'#email
key='ded54489c80578b4fb2a1f473c819ee4' #key

class Fofa():
    def Run(self,qbase64,page=1):
        data={
            'email':email,
            'key': key,
            'qbase64' : base64.b64encode(qbase64.encode('utf-8')).decode('utf-8'),
            'size' : 100,
            'fields': 'host,ip,port',
            'page': page
            }
        base_url='https://fofa.so/api/v1/search/all'

        try:
            r=rs.get(base_url,params=data)
        except:
            print('Request error!')
            return True
        
        status=r.json().get('errmsg')

        if(status):
            if '401 Unauthorized' in status:
                print('api或邮箱不正确!')
            return True
        
        print("""
        *===============InFo================*
            grammar: {}     
            page: {}                 
            size: {}                                
        *===================================*
        """.format(qbase64,str(data['page']),str(data['size'])))

        results=r.json().get('results')

        f = open('fofa.csv','w+',encoding='utf-8',newline='')
        csv_writer = csv.writer(f)

        csv_writer.writerow(["url","ip",'port'])

        for i in results:
            csv_writer.writerow([i[0],i[1],i[2]])

        return False

if __name__ == '__main__':
    grammar=input('请输入要搜索的语法: ')
    page=input('请输入最大页数(一页100条): ')
    page=int(page) if page else 1

    for i in range(1,page+1):
        if(Fofa().Run(grammar,i)):
            break
