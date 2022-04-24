import time
import urllib.request
import common
import random

# 抓取主要评论(不含跟评)
# fileName 保存的文件名
# aid varticle 文章Id
# size  评论条数
def CrawlerComment(fileName,aid,size):
    saveFile = open("./data/comment_"+fileName+".txt","w",encoding='utf-8')
    pageSize = "10"
    lastId = "0"
    count = 0

    headers = ("User-Agent", random.choice(common.userAgent))
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    while 1:
        try:
            url = common.VQQCommentUrl(aid,lastId,pageSize)
            request = urllib.request.urlopen(url)
            body = request.read().decode("utf-8","ignore")
            request.close()

            list,lastId = common.ParseCommentBody(body)
            for item in list:
                count += 1
                content = str(item).replace("\n", "").replace("\r", "")
                print("第" + str(count) + "评论 " + content )

                saveFile.write(content + "\n")
            if size == count:
                print("done")
                break
            time.sleep(10)

        except:
            print("Exception wait")
            time.sleep(20)
            continue
