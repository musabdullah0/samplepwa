# samplepwa
Here's the source code for Study Mode, a Flask Progressive Web App that helps you find where your friends are studying.

## How to Work on this

First, make your virtualenv by running 
`
  python3 -m venv /path/to/new/virtual/environment
`

Second, activate your virtualenv by running

`
  /path/to/virtualenv/bin/activate
`

Third, set up your firebase account and add the config object to your project


```python
  secrets.py
  ---
  config = {
    "apiKey": "YOUR-API-KEY",
    "authDomain": "YOUR-AUTH-DOMAIN",
    "databaseURL": "YOUR-DATABASE-URL",
    "projectId": "YOUR-PROJECT-ID",
    "storageBucket": "YOUR-STORAGE-BUCKET",
    "messagingSenderId": "YOUR-MESSAGING-SENDER-ID",
    "appId": "YOUR-APP-ID",
    "measurementId": "YOUR-MEASUREMENT-ID"
  }
```


Lastly, install all the dependencies by running
`
  pip install -r requirements.txt
`
