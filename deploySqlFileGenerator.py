import os
import logging
import sys
import datetime

#整理sql，分类到dict
def handleSqls(file):
    global logger
    fileContent = file.read()
    sqls = fileContent.split(";")
    create = []
    update = []
    delete = []
    insert = []
    alter = []
    index = []
    for sql in sqls:
        logger.info('当前处理的sql：' + sql)
        if sql.split(' ')[0].lower().strip() == 'create':
            create.append(sql)
        elif sql.split(' ')[0].lower().strip() == 'insert':
            insert.append(sql)
        elif sql.split(' ')[0].lower().strip() == 'update':
            update.append(sql)
        elif sql.split(' ')[0].lower().strip() == 'delete':
            delete.append(sql)
        elif sql.split(' ')[0].lower().strip() == 'alter':
            alter.append(sql)
        elif sql.split(' ')[0].lower().strip() == 'index':
            index.append(sql)
        else:
            logger.error("sql类型没有匹配到：" + sql)
    return {"create": create, "update": update, "delete": delete, "insert": insert, "alter": alter, "index": index}



if __name__=="__main__":
    #日志
    logging.basicConfig(level=logging.INFO,format ='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    handler.setFormatter(logFormatter)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logFormatter)
    logger.addHandler(handler)
    #banner
    banner = '''
        __                          
   / /______  ____  ____ _____  
  / //_/ __ \/ __ \/ __ `/_  /  
 / ,< / /_/ / / / / /_/ / / /_  
/_/|_|\____/_/ /_/\__, / /___/  
             _ __////_/      __ 
  ___ _   __(_) / __ \____ _/ /_
 / _ \ | / / / / /_/ / __ `/ __/
/  __/ |/ / / / _, _/ /_/ / /_  
\___/|___/_/_/_/ |_|\__,_/\__/    
                                                                                                                       '''
    logger.info(banner)
    logger.info("=====================上线SQL脚本文件生成工具=====================")
    try:
        file = open("deploy.sql", 'r', encoding='utf-8')
    except Exception as error:
        logger.error(error)
        sys.exit()
    #源sql文件存在
    deployDate = input("请输入上线日期（yyyyMMdd）：")
    try:
        datetime.datetime.strptime(deployDate, '%Y%m%d')
    except ValueError:
        raise ValueError("时间格式有误，请修改为yyyyMMdd!!!")
    sqlDict = handleSqls(file)
    logger.info("sqlDict:")
    print(sqlDict)

    #文件名
    fileName = '亦庄-北京接口平台-生产-nglocal_bj-%(deployDate)s-%(fileNum)d-%(fileNo)d-%(sqlType)s-sql.txt'

    #文件头
    fileHeader = '''/*
*地址：198.115.168.53
*端口号：20001
*库名：nglocal_bj
*用户名：nglocal_bj
*操作数量：%(sqlNum)d
*是否中间件：否
*数据库类型：mysql
*工单联系人电话: 17610119557
*工单执行失败是否回滚:部分回滚
*/'''

    #文件序号
    fileNo=0

    #删除没有的sql类型
    for key in list(sqlDict.keys()):
        if sqlDict[key] == []:
            sqlDict.pop(key)

    #分类输出
    for sqlType in sqlDict:
        fileNo=fileNo + 1
        f = open((fileName % dict(deployDate=deployDate, fileNum=len(sqlDict), fileNo=fileNo, sqlType=sqlType)), 'w+', encoding='utf-8')
        f.write(fileHeader % dict (sqlNum=len(sqlDict[sqlType])))
        f.write('\n')
        for sql in sqlDict[sqlType]:
            f.write(sql)
            f.write(';')
        f.close()
        logger.info(sqlType + '类型的sql脚本文件已经生成。')

    logger.info("finish")

    input("press enter to exit...")