#coding=utf-8
#author:微信公众号：大数据前沿
#查看代码讲解，视频教程，请微信添加好友搜索公众号[大数据前沿]查看历史消息获取。
import json
import re
from pyecharts import Bar
from pyecharts import Grid
from pyecharts import WordCloud
from pyecharts import Pie
from pyecharts import Map
from collections import Counter
import jieba.analyse
import PIL.Image as Image
import os
import math
import codecs


def get_pie(item_name,item_name_list,item_num_list):
    totle = item_num_list[0]+item_num_list[1]+item_num_list[2]
    subtitle = "共有:%d个好友"%totle

    pie = Pie(item_name,page_title = item_name,title_text_size=30,title_pos='center',\
        subtitle = subtitle,subtitle_text_size = 25,width=800,height= 800)
    
    pie.add("", item_name_list, item_num_list,is_label_show=True,center=[50, 45],radius=[0,50],\
        legend_pos ='left',legend_orient='vertical',label_text_size=20)

    out_file_name = './analyse/'+item_name+'.html'
    #print(out_file_name)
    pie.render(out_file_name)

def get_bar(item_name,item_name_list,item_num_list):
    subtitle = "微信公众号：大数据前沿"
    bar = Bar(item_name,page_title = item_name,title_text_size=30,title_pos='center',\
        subtitle = subtitle,subtitle_text_size = 25)
    
    bar.add("", item_name_list, item_num_list,title_pos='center', xaxis_interval=0,xaxis_rotate=27,\
        xaxis_label_textsize = 20,yaxis_label_textsize = 20,yaxis_name_pos='end',yaxis_pos = "%50")
    bar.show_config()

    grid = Grid(width=1300,height= 800)
    grid.add(bar,grid_top = "13%",grid_bottom = "23%",grid_left = "15%",grid_right = "15%")
    out_file_name = './analyse/'+item_name+'.html'
    grid.render(out_file_name)


def get_map(item_name,item_name_list,item_num_list):
    subtitle = "微信公众号：大数据前沿"
    _map = Map(item_name,width=1300,height= 800,title_pos='center',title_text_size=30,\
        subtitle = subtitle,subtitle_text_size = 25)
    _map.add("", item_name_list, item_num_list, maptype='china', is_visualmap=True, visual_text_color='#000')

    out_file_name = './analyse/'+item_name+'.html'
    _map.render(out_file_name)


def word_cloud(item_name,item_name_list,item_num_list,word_size_range):

    wordcloud = WordCloud(width=1400,height= 900)
    
    wordcloud.add("", item_name_list, item_num_list,word_size_range=word_size_range,shape='pentagon')
    out_file_name = './analyse/'+item_name+'.html'
    wordcloud.render(out_file_name)
    
def get_item_list(first_item_name,dict_list):
    item_name_list = []
    item_num_list = []
    i = 0
    for item in dict_list:
        
        i+=1
        if i >=15:
            break
        
        for name,num in item.items():
            if name != first_item_name:
                item_name_list.append(name)
                item_num_list.append(num)


    return item_name_list,item_num_list

def dict2list(_dict):
    name_list = []
    num_list = []

    for key,value in _dict.items():
        name_list.append(key)
        num_list.append(value) 

    return name_list,num_list

def counter2list(_counter):
    name_list = []
    num_list = []

    for item in _counter:
        name_list.append(item[0])
        num_list.append(item[1]) 

    return name_list,num_list

def get_tag(text,cnt):
    text = re.sub(r"<span.*><span>", "", text)
    print ('正在分析句子:',text)
    tag_list = jieba.analyse.extract_tags(text)
    for tag in tag_list:
        cnt[tag] += 1

def mergeImage():
    print("正在合成头像")
    #对用户头像进行压缩
    photo_width = 200
    photo_height = 200

    #图像路径list
    photo_path_list = []

    #获取当前路径
    dirName = os.getcwd()+'/images'
    #print(dirName)
    #遍历文件夹获取所有图片的路径
    for root, dirs, files in os.walk(dirName):
            for file in files:
                if "jpg" in file and os.path.getsize(os.path.join(root, file)) > 0:
                    photo_path_list.append(os.path.join(root, file))
                elif "jpg" in file and os.path.getsize(os.path.join(root, file)) == 0:
                    photo_path_list.append(os.path.join("./source", "empty.jpg"))

    #print(photo_path_list)
    pic_num = len(photo_path_list)
    #每行每列显示图片数量
    line_max = int(math.sqrt(pic_num))
    row_max = int(math.sqrt(pic_num))
    print(line_max, row_max, pic_num)

    if line_max > 20:
        line_max = 20
        row_max = 20

    num = 0
    pic_max=line_max*row_max

    toImage = Image.new('RGBA',(photo_width*line_max,photo_height*row_max))


    for i in range(0,row_max): 

        for j in range(0,line_max):

            pic_fole_head =  Image.open(photo_path_list[num])
            width,height =  pic_fole_head.size
        
            tmppic = pic_fole_head.resize((photo_width,photo_height))
        
            loc = (int(j%row_max*photo_width),int(i%row_max*photo_height))
            toImage.paste(tmppic,loc)
            num= num+1

            if num >= len(photo_path_list):
                    break

        if num >= pic_max:
            break


    print(toImage.size)
    toImage.save('./analyse/merged.png')


if __name__ == '__main__':
    
    in_file_name = './data/friends.json'
    with codecs.open(in_file_name, encoding='utf-8') as f:
        friends = json.load(f)
    

    #待统计参数
    sex_counter =  Counter()#性别
    Province_counter = Counter()#省份
    NickName_list = [] #昵称
    Signature_counter = Counter()#个性签名关键词

    for friend in friends:
        #统计性别
        sex_counter[friend['Sex']]+=1
        #省份
        if friend['Province'] != "":
            Province_counter[friend['Province']]+=1
        #昵称
        NickName_list.append(friend['NickName'])
        #签名关键词提取
        signature=re.sub(r"<([^ ]*).*>(.*)</(.*)>", " ", friend["Signature"])
        get_tag(signature,Signature_counter)
        

    #性别
    name_list,num_list = dict2list(sex_counter)
    get_pie('性别统计',name_list,num_list)

    #省份前15
    name_list,num_list = counter2list(Province_counter.most_common(15))
    get_bar('地区统计',name_list,num_list)

    #地图
    get_map('微信好友地图可视化',name_list,num_list)

    #昵称
    num_list = [5 for i in range(1,len(NickName_list)+1)]
    word_cloud('微信好友昵称',NickName_list,num_list,[18,18])

    #微信好友签名关键词
    name_list,num_list = counter2list(Signature_counter.most_common(200))
    word_cloud('微信好友签名关键词',name_list,num_list,[20,100])
    
    #头像合成
    mergeImage()
