### 腾讯视频评论抓取

1. 抓取普通评论
```python
# 抓取主要评论(不含跟评)
# fileName 保存的文件名
# aid varticle 文章Id
# size  评论条数
CrawlerComment("fileName","aid",1000)
```

2. 抓取深度评论
```python
# 抓取深度评论
# fileName 保存的文件名
# aid video 视频Id 
CrawlerDeepComment("fileName","aid")
```