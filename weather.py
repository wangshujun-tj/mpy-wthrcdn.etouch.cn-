import urequests as requests
import json
import gzip
class weather(object):
    # 获取天气信息的uri
    weather_uri = "http://wthrcdn.etouch.cn/weather_mini?citykey=101030300"
    def get(self,uri=weather_uri):
        resp=requests.get(self.weather_uri)
        if (resp.status_code==200):
            a=gzip.decompress(resp.content)
            #print(a)
            b=a.decode("utf-8")
            #print(b)
            data = json.loads(b)
            #print(b)
            w_lei=str(data['data']['forecast'][0]['type'],'utf-8')
            w_di=str(data['data']['forecast'][0]['low'],'utf-8')
            w_gao=str(data['data']['forecast'][0]['high'],'utf-8')
            w_fx=str(data['data']['forecast'][0]['fengxiang'],'utf-8')
            temp=str(data['data']['forecast'][0]['fengli'],'utf-8')
            print(temp)
            temp1=temp.split("[")[2]
            print(temp1)
            temp2=temp1.split("]")[0]
            w_fl=temp2
            w_rq=str(data['data']['forecast'][0]['date'],'utf-8')
            #print(w_rq)
            return(w_rq,w_lei,w_di,w_gao,w_fx,w_fl)
            
            
if __name__ == "__main__":
    weather = weather()
    print(weather.get())