#Inspyre

Inspyre is delivering your daily motivational sports quote via mail.

`config.py`

This file contains the configuration for Inspyre.
```python
category = "sports" # ["inspire", "management", "sports", "life", "funny", "love", "art"]
sender_mail = "" # "sender@gmail.com"
sender_password = ""
recipient_mail = "" # "recipient@gmail.com"
smtp_server = "" # smtp.gmail.com:587
```

Schedule `inspyre.py` to run once a day.