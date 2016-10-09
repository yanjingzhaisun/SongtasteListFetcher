from scrapy.spider import Spider  
import scrapy
from scrapy.selector import Selector  
from songtastList.items import SongtastlistItem
from urllib.parse import urljoin

class DmozSpider(Spider): 
    name = "songtaste"
    allowed_domain = ["songtaste.com"]
    start_urls= [
            "http://www.songtaste.com/user/84084/albumlist"
    ]
    def parse(self, response):
        albumlists = response.xpath('//div[@class="pages"]/a')
        for albumlist in albumlists:
            url = urljoin("http://www.songtaste.com",albumlist.xpath('@href').extract()[0])
            print('thisUrl', url)
            yield scrapy.Request(url,callback = self.parse_page)

    def parse_page(self, response):
        albums = response.xpath('//div[@id="sub_bright"]/div/div/ul/li/a')
        for album in albums:
            url = urljoin("http://www.songtaste.com",album.xpath('@href').extract()[0])
            print('album_url: %s', url)
            yield scrapy.Request(url,callback = self.parse_content)

    def parse_content(self,response):
        wss = response.xpath('//div[@class="song_left"]/table/script').extract()[0]
        wss.replace(';','\n')
        item = SongtastlistItem()
        item['desc'] = wss
        yield item
        #print(wss)

