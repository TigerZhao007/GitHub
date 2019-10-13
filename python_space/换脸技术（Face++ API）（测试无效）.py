
# ######################################################################################################################
# 超简单使用Python换脸
'''
本篇介绍的换脸方法需要借助Face++，关于Face++的API，大家可自行查看说明文档，都比较简单，小编在这里就不做具体
文档地址：https://console.faceplusplus.com.cn/documents/20813963
获取Face++ api_key和secret, Face++网址：https://console.faceplusplus.com.cn/dashboard
'''
# ######################################################################################################################

# 调用的库~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import requests
import simplejson
import json
import base64

# 第一步，获取人脸关键点~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def find_face(imgpath):
    print("finding")
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    data = {"api_key": 'cNA_ootbumlhGDJzYM-Zq_Q69kK0sZFw',
            "api_secret": 'CAUNWbHd5t4lPxUz5SnPMHYB8GUer92',
            "image_url": imgpath, "return_landmark": 1}
    files = {"image_file": open(imgpath, "rb")}
    response = requests.post(http_url, data=data, files=files)
    req_con = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con)
    this_json = simplejson.dumps(req_dict)
    this_json2 = simplejson.loads(this_json)
    faces = this_json2['faces']
    list0 = faces[0]
    rectangle = list0['face_rectangle']
    # print(rectangle)
    return rectangle

# 第二步，换脸，其中图片的大小应不超过2M~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# number表示换脸的相似度
def merge_face(image_url_1, image_url_2, image_url, number):
    ff1 = find_face(image_url_1)
    ff2 = find_face(image_url_2)
    rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) + "," + str(ff1['width']) + "," + str(ff1['height']))
    rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + "," + str(ff2['width']) + "," + str(ff2['height'])
    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
    f1 = open(image_url_1, 'rb')
    f1_64 = base64.b64encode(f1.read())
    f1.close()
    f2 = open(image_url_2, 'rb')
    f2_64 = base64.b64encode(f2.read())
    f2.close()
    data = {"api_key": 'cNA_ootbumlhGDJzYM-Zq_Q69kK0sZFw',
            "api_secret": 'CAUNWbHd5t4lPxUz5SnPMHYB8GUer92',
            "template_base64": f1_64, "template_rectangle": rectangle1,
            "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}
    response = requests.post(url_add, data=data)
    req_con = response.content.decode('utf-8')
    req_dict = json.JSONDecoder().decode(req_con)
    result = req_dict['result']
    imgdata = base64.b64decode(result)
    file = open(image_url, 'wb')
    file.write(imgdata)
    file.close()


def test():
    image1 = r"D:\Work\GitHub\python_space\data\1.png"
    image2 = r"D:\Work\GitHub\python_space\data\2.png"
    image = r"D:\Work\GitHub\python_space\data\0.png"
    merge_face(image2, image1, image, 90)

