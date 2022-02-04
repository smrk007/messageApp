# messageApp

### Prerequesites

```
virtualenv
npm
```

### Starting up the website

```
git clone https://github.com/smrk007/messageApp.git

cd messageApp/messaging-app-backend
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd messaging_app
python manage.py runserver > django_logs.txt 2>&1 &

cd ../../messaging-app-frontend
npm install
npm run start > react_logs.txt 2>&1 &
```

### Testing out the website

Simply go to http://localhost:3000/ !
