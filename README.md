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

### Manage pulses

Implement endpoints that can:

- Create a new pulse

Two endpoints:
1. post method at 'api/create_pulse/'
2. post method at 'api/pulse'

- List all pulses (five per page)
1. get method at 'api/pulses'

- Get a specific pulse
1. get method at 'api/pulse/:id'

- Update a specific pulse

1. put method at 'api/pulse/:id'
2. post method at 'api/pulse/:id'----for post method if the id is exist it will update, if not it will create a new one.

- Delete a specific pulse
1.delete method at 'api/pulse/:id'

### Upload pulses

1. upload files by post method 'api/csv' it need 'Content-Type':'multipart/form-data' as head. It need header for upload files.


---

### Download pulses

1. download files as response csv format


### TestCases in tests fold

Test unit tests:

`python manage.py test tests`


### Notice

1. In order to avoid confliction of build_in function in python 3, I use ctype replace type in database.

