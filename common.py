import json
import re
import datetime

userAgent =\
    [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.803.0 Chrome/14.0.803.0 Safari/535.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1",
    ]


def VQQCommentUrl(aid , lastId , pageSize ) :
    return "https://video.coral.qq.com/varticle/" + aid + "/comment/v2?callback=_varticle" + aid + "commentv2&orinum=" + pageSize + "&oriorder=o&pageflag=1&cursor=" + lastId + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132"

def ParseCommentBody( body):
    raw = re.compile('\({(.*?)}\)', re.S).findall(body)[0]
    j = "{" + raw + "}"
    res = json.loads(j)
    # print(res)
    data = []
    for con in res["data"]["oriCommList"]:
        # print(con)
        if con["parent"] == "0":
            tm = datetime.datetime.fromtimestamp( float(con["time"]) ).strftime("%Y-%m-%d")

            data.append(tm+" "+ con["content"])

    return data, res["data"]["last"]

def VQQDeepCommentUrl(videoId,lastId,pageSize):
    return "https://video.coral.qq.com/filmreviewr/c/upcomment/"+videoId+"?callback=_filmreviewrcupcomment"+videoId+"&reqnum="+pageSize+"&source=132&commentid="+lastId


def ParseDeepCommentBody(body):
    raw = re.compile('\({(.*?)}\)', re.S).findall(body)[0]
    j = "{" + raw + "}"
    res = json.loads(j)
    data = []
    for con in res["data"]["commentid"]:
        item = (con["content"], con["userinfo"]["gender"])
        data.append(item)

    return data, res["data"]["last"], res["data"]["hasnext"]