
# 微信好友分析

## 功能说明：用作者的微信号进行示范
#### 1：统计好友的性别
![python](https://github.com/yangxuanxc/wechat_friends/blob/master/source/1.jpeg)
#### 2：统计好友的地域分布，并且可视化在地图上展示
![python](https://github.com/yangxuanxc/wechat_friends/blob/master/source/2.jpeg)

![python](https://github.com/yangxuanxc/wechat_friends/blob/master/source/3.jpeg)
#### 3：将好友的昵称做成词云
因为这个信息比较私人，这里就不展示
#### 4：统计好友个性签名中的高频词汇
![python](https://github.com/yangxuanxc/wechat_friends/blob/master/source/4.jpeg)
#### 5：将所有好友的头像合并成一张大图
![python](https://github.com/yangxuanxc/wechat_friends/blob/master/source/5.jpeg)
#### 6：微信自动发送与回复消息
<img height="500" align="center" src="https://github.com/yangxuanxc/wechat_friends/blob/master/source/6.jpg" alt="">

## 依赖
本程序使用python3，请在python3环境下运行
#### Python 3
- PIL: pip3 install pillow
- pyecharts：pip3 install pyecharts
- pip3 install itchat
- pip3 install jieba

地图数据包：  
pip3 install echarts-china-provinces-pypkg  
pip3 install echarts-countries-pypkg

## 运行
#### 获取用户信息
需要将get_user_info.py第70行的二胖，改成随意一个好友的名字或者自己的名字  
  
python3 get_user_info.py
执行后会在data目录下生成friends.json
会在images目录下存放所有好友的头像
#### 统计用户信息
python3 analyse.py
会在analyse文件夹下生产合成后的图片以及可视化的文件

## 教程
本程序作者编写了介绍文档并且录制了相关视频讲解代码，如果有需要的朋友
- 请关注微信公众号：**大数据前沿** 
- 获得视频教程请在消息窗口回复：**微信好友**
- 同时更详细的介绍以及该程序更多的扩展请查看公众号历史消息查看相应文章获取。

扫码下方二维码关注

<img height="300" align="center" src="https://github.com/yangxuanxc/wechat_friends/blob/master/source/ewm.png" alt="">


## 赞赏与支持
- 如果你觉得本文还不错，请微信扫描下方小程序码赞赏支持，谢谢。
- 别忘记点个start哦。

<img height="300" align="center" src="https://github.com/yangxuanxc/wechat_friends/blob/master/source/zs.jpeg" alt="">
    
