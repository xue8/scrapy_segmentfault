import time
import os

while True:
    os.system("scrapy crawl segmentfault")
    time.sleep(3000)  #每隔一天运行一次 24*60*60=86400s