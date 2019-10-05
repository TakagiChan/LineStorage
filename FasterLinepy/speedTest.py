from linepy import LINE,OEPoll
import time
import concurrent.futures
#coding:utf-8

def send(gid):
    j = 0
    for i in range(10):
        start = time.time()
        bot.sendMessage(gid,"message")
        stop = time.time()
        bot.sendMessage(gid,str(stop-start))
        j += stop-start
    else:
        bot.sendMessage(gid, "average time: " + str(j / 10))
def botCore(op):
    if op.type == 26:
        msg = op.message
        receiver = msg.to
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "速度测量仪表":
                    start = time.time()
                    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as excuter:
                        excuter.map(send(receiver))
                    stop = time.time()
                    bot.sendMessage(receiver,"result: " + str(stop - start))

def botOEupdater(oePoll):
    for i in loop:
        try:
            ops = oePoll.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    botCore(op)
                    oePoll.setRevision(op.revision)
                    loop.append(i + 1)
        except Exception as oeUpdaterError:
            bot.log(oeUpdaterError)

if __name__ == "__main__":
    loop = [0]
    bot = LINE("","")
    print(bot.authToken)
    botOE = OEPoll(bot)
    botOEupdater(botOE)