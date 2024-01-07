# This is an Online Auction Website

Some screenshots of the project

![](assets/ss/ss.png)

![](assets/ss/ss1.png)

![](assets/ss/ss2.png)

Clone the repo or download it 
---
### For Mac/Linux Users

Create virtual environment in python within the auction folder
```
python -m venv .
```


Activate the virtual environment
```
source bin/activate
```


Install the requirements
```
pip install -r requirements.txt
```


Migrate all the migrations
```
python manage.py migrate
```


Finally run the server
```
python manage.py runserver
```
---

### For Windows Users

Install python and pip first

For pip:
```
python3 get-pip.py
```


Create virtual environment in python within the auction folder
```
python3 -m venv env
```

Activate the virtual environment
```
env\Scripts\activate
```

Install the requirements
```
pip install -r requirements.txt
```


Migrate all the migrations
```
python manage.py migrate
```


Finally run the server
```
python manage.py runserver
```