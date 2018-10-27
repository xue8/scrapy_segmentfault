# scrapy爬虫
> segmentfault.com的问答内容爬虫，爬虫数据保存在Mysql，自动过滤采集过的url，不重复采集。
## 配置
> 1. `scrapy_question/dingshi.py`为定时爬虫文件，修改里面的`time.sleep(3000)`爬虫频率.
> 2. `scrapy_question/settings.py`的`IMAGES_STORE`为图片保存目录.
> 3. `scrapy_question/spiders/segmentfault.py`的`existence`方法中的`file`为已采集的url文件（没采集过的，url文件设置为空即可）。
> 4. `scrapy_question/pipelines.py`的`dbHandle`爬虫数据保存的`mysql`信息,修改成你的。
## 教程
> 1. python `dingshi.py`即可.
