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
