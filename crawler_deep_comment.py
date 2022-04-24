import time
import urllib.request
import common
import random

# 抓取深度评论
# fileName 保存的文件名
# aid video 视频Id
def CrawlerDeepComment(fileName, aid):
    saveFile = open("./data/deep_comment_" + fileName + ".txt", "w", encoding='utf-8')
    pageSize = "10"
    lastId = "0"
    count = 0

    headers = ("User-Agent", random.choice(common.userAgent))
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

    while 1:
        try:
            url = common.VQQDeepCommentUrl(aid, lastId, pageSize)
            request = urllib.request.urlopen(url)
            body = request.read().decode("utf-8", "ignore")
            request.close()

            list, lastId , isEnd = common.ParseDeepCommentBody(body)
            for item in list:
                count += 1
                content = str(item[0]).replace("\n", "").replace("\r", "")
                print("第" + str(count) + "评论" + content + str(item[1]))

                saveFile.write(str(item[0]) + str(item[1]) + "\n")
            if isEnd == False:
                print("crawler done!")
                break
            time.sleep(10)

        except:
            print("Exception wait")
            time.sleep(20)
            continue
