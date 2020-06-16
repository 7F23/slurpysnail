from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BaiduImageCrawler
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import FlickrImageCrawler

# Configuration
output_dir = '../data/negative/food'
thread_num = 8
query_num  = 100
query_off  = 0

def query(crawler, keyword):
    global query_off
    crawler.crawl(keyword,
        max_num=query_num, file_idx_offset=query_off)
    query_off += query_num
    
# Crawl Bing
bing_crawler = BingImageCrawler(
    downloader_threads=thread_num,
    storage={'root_dir': output_dir})

query(bing_crawler, 'meal')
query(bing_crawler, '食物')

# Crawl Baidu
baidu_crawler = BaiduImageCrawler(
    downloader_threads=thread_num,
    storage={'root_dir': output_dir})

query(baidu_crawler, 'meal')
query(baidu_crawler, '食物')
