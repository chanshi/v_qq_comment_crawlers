import argparse
import crawler_comment

flag = argparse.ArgumentParser()
#flag.add_argument("-url", help="this is url")
flag.add_argument("-t","--tid", type=str, help="targetId")
flag.add_argument("-s","--size",type=int,default=10,help="")
flag.add_argument("-type",help="get comment or deep comment")

args = flag.parse_args()
print(args.tid)
print(args.size)
crawler_comment.CrawlerComment("1",args.tid,args.size)
