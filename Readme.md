色图博客批量爬虫
建议使用python3.7或以上

使用方法：
1、安装所需环境包
pip install -r requirements.txt

2、设置settings.py中的第42行修改IMAGES_STORE的值，修改为你希望保存图片的路径


3、IDE中运行main.py或者
命令行执行python main.py
或者在文件目录下执行scrapy crawl setu

使用scrapy框架
爬取m4ex.com下的所有图片。按照tag创建文件夹，并以标题为文件名下载文件。下载的图片以数字递增排序。

ps:该网站需要科学上网，请自行配置代理