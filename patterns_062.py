import re

date = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2}'
phone = r'\b01[\s-]?\d{7}\b'
email = r'\b(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*\b'
ldate = r'\b\d{1,2}[\s-]\w{3}[\s-]\d{2,4}\b'