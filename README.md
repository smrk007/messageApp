# messageApp

### Important

So far it has only been tested to work using localhost, so please use locally when testing.

### How to run

```
git clone https://github.com/smrk007/messageApp.git

cd messageApp/messaging-app-backend
virtualenv venv
source venv/bin/activate
pip install -r requirements
cd messaging_app
python manage.py runserver > django_logs.txt 2>&1 &

cd ../../messaging-app-frontend
npm install
npm run start > react_logs.txt 2>&1 &
```
