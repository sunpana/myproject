#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json, base64

reload(sys)
sys.setdefaultencoding( "utf-8" )

def OCR(filename):
    #百度ocr接口
    url = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'

    data = {}
    data['fromdevice'] = "pc"
    data['clientip'] = "10.10.10.0"
    data['detecttype'] = "LocateRecognize"
    data['languagetype'] = "CHN_ENG"
    data['imagetype'] = "1"
    data['sizetype']="big"
    data['image'] = "/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDABMNDxEPDBMREBEWFRMXHTAfHRsbHTsqLSMwRj5KSUU+RENNV29eTVJpU0NEYYRiaXN3fX59S12Jkoh5kW96fXj/2wBDARUWFh0ZHTkfHzl4UERQeHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHj/wAARCAAfACEDAREAAhEBAxEB/8QAGAABAQEBAQAAAAAAAAAAAAAAAAQDBQb/xAAjEAACAgICAgEFAAAAAAAAAAABAgADBBESIRMxBSIyQXGB/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/APawEBAQEBAgy8i8ZTVV3UY6V1eU2XoWDDZB19S646Gz39w9fkKsW1r8Wm2yo1PYis1be0JG9H9QNYCAgc35Cl3yuVuJZl0cB41rZQa32dt2y6OuOiOxo61vsLcVblxaVyXD3hFFjL6La7I/sDWAgICAgICB/9k="


    f = open(filename,'rb') 
    data['image'] = base64.b64encode(f.read()) 
    f.close()
    decoded_data = urllib.urlencode(data)
    req = urllib2.Request(url, data = decoded_data)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    req.add_header("apikey", "自己的key")
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        content = json.loads(content)
        words = ''
        if content['retData']:
            for data in content['retData']:
                word = data['word']
                words = words + word+'\n'
            return words

if __name__=='__main__':
    #list.txt是图片文件名列表
    f = open('list.txt','r')
    f = f.readlines()
    for filename in f:
        filename = filename.strip('\n')
        content = OCR('east_img/'+filename)
        file_txt = filename.rstrip('jpeg')
        if content:
            f_txt = open('east_model_file/'+file_txt+'txt','w')
            f_txt.write(content)
            print file_txt
    f_txt.close()
    print "完成。。。"
