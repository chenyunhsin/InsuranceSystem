# InsuranceSystem
InsuranceSystem

## Mac Os
1. 安裝poetry
```
brew install pyenv
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
curl -sSL https://install.python-poetry.org | python3.11
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
poetry --version
```

2. 建立虛擬環境
```
poetry shell
```
3. migrate migration files 
```
python manage.py migrate
```
4. 導入預先件好的資料
```
python manage.py loaddata policyholders_fixture.json
```
5. 跑後端服務
```
python manage.py runserver
```
> 即可使用api  
> ex: http://127.0.0.1:8000/api/policyholders/0000000001/  
> ex2: http://127.0.0.1:8000/api/policyholders/0000000002/top/  

## 前端
1. 下載node.js 
```
brew install node
```
2. 下載vue
```
npm install -g @vue/cli
npm install axios
```
3. 進入前端專案
```
cd insurance_system_frontend 
```
4. 啟動前端專案
```
npm run serve
```

## DEMO影片
https://youtu.be/NGWaakp0FLQ

## 補中資料結構： 除spec外新增boolean: is_direct 判斷是否為直接保戶
{"code": "0000000001", "name": "\u5442\u6977\u7965", "registration_date": "2024-01-10", "introducer_code": null, "l": [{"code": "0000000002", "name": "\u59dc\u5609\u59ae", "registration_date": "2024-01-10T13:15:00.516764Z", "introducer_code": "0000000001", "is_direct": true}, {"code": "0000000004", "name": "\u5353\u6d77\u6dc7", "registration_date": "2024-01-10T13:15:56.042303Z", "introducer_code": "0000000001", "is_direct": true}, {"code": "0000000005", "name": "\u674e\u4fde\u975c", "registration_date": "2024-01-10T13:16:18.748174Z", "introducer_code": "0000000001", "is_direct": true}, {"code": "0000000008", "name": "\u53f2\u4e3b\u82b8", "registration_date": "2024-01-10T13:18:10.670172Z", "introducer_code": "0000000002", "is_direct": false}, {"code": "0000000009", "name": "\u9023\u5bb6\u6cf0", "registration_date": "2024-01-10T13:18:45.356271Z", "introducer_code": "0000000003", "is_direct": false}, {"code": "0000000010", "name": "\u6731\u5e74\u7d1a", "registration_date": "2024-01-10T13:19:33.395651Z", "introducer_code": "0000000003", "is_direct": false}, {"code": "0000000011", "name": "\u8463\u5a97\u7fbd", "registration_date": "2024-01-10T13:20:03.842064Z", "introducer_code": "0000000003", "is_direct": false}], "r": [{"code": "0000000003", "name": "\u99ac\u5fc3\u777f", "registration_date": "2024-01-10T13:15:33.233345Z", "introducer_code": "0000000001", "is_direct": true}, {"code": "0000000006", "name": "\u6b66\u6603\u7a0b", "registration_date": "2024-01-10T13:16:49.460311Z", "introducer_code": "0000000002", "is_direct": false}, {"code": "0000000007", "name": "\u65bd\u82ae\u6986", "registration_date": "2024-01-10T13:17:17.057202Z", "introducer_code": "0000000002", "is_direct": false}], "status": true}
