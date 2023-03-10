# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
import glob
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class SetuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print("获取URL")
        #设置一个统计数字i，用于给下载的图片数字递增命名
        i=0
        for url in item['image_urls']:
            i = i + 1
            #把i作为变量丢进meta里面，meta变量会原样传到接下来request，也就是被file_path调用
            yield scrapy.Request(url, meta={'item': item, 'index': item['image_urls'], 'i':i})

    def file_path(self, request, response=None, info=None):
        #获取for循环里面的统计数字i
        i = request.meta['i']
        item = request.meta['item']  # 通过上面的meta传递过来item
        #定义图片名，request.url.split('/')[-1].split('.')[-1]是截取最后出现的文件格式
        image_name = item['title'] + str(i) +"." + request.url.split('/')[-1].split('.')[-1]
        print("标题："+item['title'])
        print(item['title'] + str(i) +"." + request.url.split('/')[-1].split('.')[-1])
        #下载，item['tag']是文件夹路径，image_name是文件名
        down_file_name = u'/{0}/{1}'.format(item['tag'], image_name)
        #print("开始下载")
        return down_file_name

