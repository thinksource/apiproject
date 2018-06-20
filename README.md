## Before running

1. You need to install the requirements on 

`pip install -r requirements.txt`

2. Setting the database as your local enviornment:

My local mysql database is fellow with no pastwords:

```
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qctrl',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

## How to run it

`python manage.py runserver`


## Brief

The brief has been divided into three parts:

1.  [Manage pulses](#manage-pulses)
1.  [Upload pulses](#upload-pulses)
1.  [Download pulses](#download-pulses)