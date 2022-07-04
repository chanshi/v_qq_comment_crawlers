import time
import urllib.request
import common
import random

def CrawlerComment(fileName,aid,size):
    saveFile = open("./data/comment_"+fileName+".txt","w")
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
                print("at" + str(count) + " comment " + content )

                saveFile.write(content + "\n")
            print("lastId ===> " + lastId)
            if lastId == "":
                print("lastId empty")
                break
            if size == count:
                print("done")
                break
            time.sleep(10)

        except:
            print("Exception wait")
            time.sleep(20)
            continue
    saveFile.close()
