import requests,json

url = 'http://127.0.0.1:5001/process'
data = {'start_number': 10, 'end_number': 20}
response = requests.post(url, data=data)

# エスケープされたJSON文字列をデコードしてリストに変換
decoded_list = json.loads(response.text)

print(decoded_list)
