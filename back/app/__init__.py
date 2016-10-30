# coding: utf-8

import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key is here'
app.config['QINIU_ACCESS_KEY'] = os.getenv("DRAG_QINIU_ACCESS_KEY")
app.config['QINIU_SECRET_KEY'] = os.getenv("DRAG_QINIU_SECRET_KEY")
app.config['QINIU_BUCKET_NAME'] = os.getenv("DRAG_QINIU_BUCKET_NAME")
app.config['QINIU_BUCKET_DOMAIN'] = os.getenv("DRAG_QINIU_BUCKET_DOMAIN")

from . import views
