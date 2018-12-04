#encoding:utf-8
import requests
import pprint

# APIを叩いて東京（1300010）の天気情報を取得
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'130010'}
weather_data = requests.get(api_url, params=payload).json()

# 当日の天気を表示
print(weather_data['forecasts'][0]['dateLabel'] + 'の天気は、' + weather_data['forecasts'][0]['telop'])
