# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：百度翻译API——通用翻译API
通用翻译API通过HTTP接口对外提供多语种互译服务。您只需要通过调用通用翻译API，传入待翻译的内容，
并指定要翻译的源语言（支持源语言语种自动检测）和目标语言种类，就可以得到相应的翻译结果。
http://api.fanyi.baidu.com/api/trans/product/apidoc#joinFile
"""

# ######################################################################################################################
# 通用翻译API
# ######################################################################################################################

def BaiduFanyi(target, fromLang='auto', toLang='auto'):

    # 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import http.client, hashlib, urllib, random, json
    import pandas as pd

    # 百度API账户设置~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    appid = '20191018000342630'         # 填写你的appid
    secretKey = 'bkzYcLRtVPOjUU5Xac0i'  # 填写你的密钥

    # 百度翻译参数设置~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid + target + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(target) + '&from=' + fromLang + '&to=' + toLang + \
            '&salt=' + str(salt) + '&sign=' + sign

    # 百度翻译，翻译过程~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        # 返回结果处理~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        trans_result = pd.DataFrame(columns=['trans_target', 'trans_result', 'type_from', 'type_to'])
        trans_result['trans_target'] = [result['trans_result'][0]['src']]
        trans_result['trans_result'] = [result['trans_result'][0]['dst']]
        trans_result['type_from'] = [result['from']]
        trans_result['type_to'] = [result['to']]

        # 函数返回最终结果~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        return trans_result

    # 百度翻译，翻译报错~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    except Exception as e:
        print(e)

    finally:
        if httpClient:
            httpClient.close()

# ######################################################################################################################
# 主函数
# ######################################################################################################################

# 主函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    result = BaiduFanyi(target='翻译对象', fromLang='auto', toLang='auto')