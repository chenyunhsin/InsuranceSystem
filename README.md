# InsuranceSystem
InsuranceSystem

## Mac Os
1. 安裝poetry
brew install pyenv
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
curl -sSL https://install.python-poetry.org | python3.11
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
poetry --version
2. 建立虛擬環境
poetry shell
3. migrate migration files 
python manage.py migrate
4. 導入預先件好的資料
python manage.py loaddata policyholders_fixture.json
