# This is an Online Auction + E-commerce Website

This project integrates features from both an auction system and a traditional e-commerce platform. Customers have the flexibility to either make direct purchases of desired products or participate in bidding for the items they seek. 

Some screenshots of the project

![](assets/ss/ss.png)

![](assets/ss/ss1.png)

![](assets/ss/ss2.png)

![](assets/ss/ss3.png)

![](assets/ss/ss4.png)

![](assets/ss/ss5.png)

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