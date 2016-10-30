# coding: utf-8
import os
import sys
import urllib2
import urllib
import json
from . import app
from flask import render_template, request, jsonify
from flask_zero import Qiniu

qiniu = Qiniu(app)

@app.route('/config/', methods=['POST'])
def config():
    """
    七牛配置
    """
    if request.method == 'POST':
        QINIU_ACCESS_KEY = request.get_json().get('QINIU_ACCESS_KEY')
        QINIU_SECRET_KEY = request.get_json().get('QINIU_SECRET_KEY')
        QINIU_BUCKET_NAME = request.get_json().get('QINIU_BUCKET_NAME')
        QINIU_BUCKET_DOMAIN = request.get_json().get('QINIU_BUCKET_DOMAINi')
        app.config['QINIU_ACCESS_KEY'] = QINIU_ACCESS_KEY
        app.config['QINIU_SECRET_KEY'] = QINIU_SECRET_KEY
        app.config['QINIU_BUCKET_NAME'] = QINIU_BUCKET_NAME
        app.config['QINIU_BUCKET_DOMAIN'] = QINIU_BUCKET_DOMAIN
        return jsonify({'config': 'ok'}), 200


@app.route('/upload/', methods=['POST', 'GET'])
def upload():
    """
    国内: 上传文件到七牛
    """
    if request.method == 'POST':
        fileobj = request.files['mypic']
        qiniu.save(fileobj, fileobj.filename)
        return jsonify({
            'url': qiniu.url(fileobj.filename)
        })
    else:
        return jsonify({'msg': 'please post the data'}), 405

# @app.route('/oupload/', methods=['POST', 'GET'])
# def oupload():
#     """
#     国外: 上传文件到 Imgur
#     """
#     if request.method == 'POST':
#         fileobj = request.files['mypic']
#         fileobj.save(os.path.join('/Users/apple/down/', fileobj.filename))
#         os.system('imguru /Users/apple/down/' + fileobj.filename + ' > /Users/apple/log.log')
#         with open('/Users/apple/log.log', 'r') as f:
#             line = f.readline().strip()
#         if len(line) == 0:
#             return jsonify({
#                 'msg': 'failed'
#             }), 500
#         else:
#             return jsonify({
#                 'url': line
#             })
#     else:
#         return jsonify({'msg': 'please post the data'}), 405

@app.route('/oupload/', methods=['POST', 'GET'])
def oupload():
    """
    国外: 上传文件到 Imgur
    """
    if request.method == 'POST':
        fileobj = request.files['mypic']
        urldata = urllib.urlencode({"image": fileobj.read()})
        url = "https://api.imgur.com/3/upload"
        r = urllib2.Request(url)
        r.add_data(urldata)
        r.add_header('Authorization', 'Client-ID 1c49486ec8e9565')
        res = json.loads(urllib2.urlopen(r).read())
        return jsonify({
            'url': res['data']['link']
        })
