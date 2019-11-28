import requests
from lxml import etree
import os
import time

start_time = time.time()                 # 记录开始时间
for i in range(1,7):
    # 1.请求包图网拿到整体数据
    response = requests.get("https://ibaotu.com/shipin/7-0-0-0-0-%s.html" %str(i))

    #2.抽取 视频标题、视频链接
    html = etree.HTML(response.text)
    tit_list = html.xpath('//span[@class="video-title"]/text()')      # 获取视频标题
    src_list = html.xpath('//div[@class="video-play"]/video/@src')    # 获取视频链接
    for tit, src in zip(tit_list, src_list):
        # 3.下载视频
        response = requests.get("http:" + src)
        # 给视频链接头加上http头,http快但是不一定安全,https安全但是慢

        # 4.保存视频
        if os.path.exists("video1") == False:   # 判断是否有video这个文件夹
            os.mkdir("video1")                  # 没有的话创建video文件夹
        fileName = "video1\\" + tit + ".mp4"    # 保存在video文件夹下，用自己的标题命名，文件格式是mp4
                                                # 有特殊字符的话需要用\来注释它，\是特殊字符所以这里要用2个\\
        print("正在保存视频文件: " + fileName)  # 打印出来正在保存哪个文件
        with open (fileName,"wb") as f:         # 将视频写入fileName命名的文件中
           f.write(response.content)

end_time = time.time()                   # 记录结束时间
print("耗时%d秒"%(end_time-start_time))  # 输出用了多少时间
