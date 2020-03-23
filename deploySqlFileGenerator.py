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
    for sql in sqls:
        logger.info('当前处理的sql：' + sql)
        if sql.strip().split(' ')[0].lower() == 'create':
            create.append(sql)
        elif sql.strip().split(' ')[0].lower() == 'update':
            update.append(sql)
        elif sql.strip().split(' ')[0].lower() == 'delete':
            delete.append(sql)
        elif sql.strip().split(' ')[0].lower() == 'insert':
            insert.append(sql)
        else:
            logger.error("sql类型没有匹配到：" + sql)
    return {"create": create, "update": update, "delete": delete, "insert": insert}



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
                                                                                                                           
                                                                                                                       
KKKKKKKKK    KKKKKKK                                                                                                   
K:::::::K    K:::::K                                                                                                   
K:::::::K    K:::::K                                                                                                   
K:::::::K   K::::::K                                                                                                   
KK::::::K  K:::::KKK   ooooooooooo   nnnn  nnnnnnnn       ggggggggg   gggggzzzzzzzzzzzzzzzzz                           
  K:::::K K:::::K    oo:::::::::::oo n:::nn::::::::nn    g:::::::::ggg::::gz:::::::::::::::z                           
  K::::::K:::::K    o:::::::::::::::on::::::::::::::nn  g:::::::::::::::::gz::::::::::::::z                            
  K:::::::::::K     o:::::ooooo:::::onn:::::::::::::::ng::::::ggggg::::::ggzzzzzzzz::::::z                             
  K:::::::::::K     o::::o     o::::o  n:::::nnnn:::::ng:::::g     g:::::g       z::::::z                              
  K::::::K:::::K    o::::o     o::::o  n::::n    n::::ng:::::g     g:::::g      z::::::z                               
  K:::::K K:::::K   o::::o     o::::o  n::::n    n::::ng:::::g     g:::::g     z::::::z                                
KK::::::K  K:::::KKKo::::o     o::::o  n::::n    n::::ng::::::g    g:::::g    z::::::z                                 
K:::::::K   K::::::Ko:::::ooooo:::::o  n::::n    n::::ng:::::::ggggg:::::g   z::::::zzzzzzzz                           
K:::::::K    K:::::Ko:::::::::::::::o  n::::n    n::::n g::::::::::::::::g  z::::::::::::::z                           
K:::::::K    K:::::K oo:::::::::::oo   n::::n    n::::n  gg::::::::::::::g z:::::::::::::::z                           
KKKKKKKKK    KKKKKKK   ooooooooooo     nnnnnn    nnnnnn    gggggggg::::::g zzzzzzzzzzzzzzzzz                           
                                                                   g:::::g                                             
                                                       gggggg      g:::::g                                             
                                                       g:::::gg   gg:::::g                                             
                                                        g::::::ggg:::::::g                                             
                                                         gg:::::::::::::g                                              
                                                           ggg::::::ggg                                                
                                                              gggggg                                                   
                                                                                                                       
                                                                                                                       
                                             iiii  lllllll RRRRRRRRRRRRRRRRR                             tttt          
                                            i::::i l:::::l R::::::::::::::::R                         ttt:::t          
                                             iiii  l:::::l R::::::RRRRRR:::::R                        t:::::t          
                                                   l:::::l RR:::::R     R:::::R                       t:::::t          
    eeeeeeeeeeee  vvvvvvv           vvvvvvviiiiiii  l::::l   R::::R     R:::::R  aaaaaaaaaaaaa  ttttttt:::::ttttttt    
  ee::::::::::::ee v:::::v         v:::::v i:::::i  l::::l   R::::R     R:::::R  a::::::::::::a t:::::::::::::::::t    
 e::::::eeeee:::::eev:::::v       v:::::v   i::::i  l::::l   R::::RRRRRR:::::R   aaaaaaaaa:::::at:::::::::::::::::t    
e::::::e     e:::::e v:::::v     v:::::v    i::::i  l::::l   R:::::::::::::RR             a::::atttttt:::::::tttttt    
e:::::::eeeee::::::e  v:::::v   v:::::v     i::::i  l::::l   R::::RRRRRR:::::R     aaaaaaa:::::a      t:::::t          
e:::::::::::::::::e    v:::::v v:::::v      i::::i  l::::l   R::::R     R:::::R  aa::::::::::::a      t:::::t          
e::::::eeeeeeeeeee      v:::::v:::::v       i::::i  l::::l   R::::R     R:::::R a::::aaaa::::::a      t:::::t          
e:::::::e                v:::::::::v        i::::i  l::::l   R::::R     R:::::Ra::::a    a:::::a      t:::::t    tttttt
e::::::::e                v:::::::v        i::::::il::::::lRR:::::R     R:::::Ra::::a    a:::::a      t::::::tttt:::::t
 e::::::::eeeeeeee         v:::::v         i::::::il::::::lR::::::R     R:::::Ra:::::aaaa::::::a      tt::::::::::::::t
  ee:::::::::::::e          v:::v          i::::::il::::::lR::::::R     R:::::R a::::::::::aa:::a       tt:::::::::::tt
    eeeeeeeeeeeeee           vvv           iiiiiiiillllllllRRRRRRRR     RRRRRRR  aaaaaaaaaa  aaaa         ttttttttttt  
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

    print("fuck")

