# #connector操作
# # import mysql.connector
# # # 注意把password设为你的root口令:
# # >>> conn = mysql.connector.connect(user='root', password='password', database='test')
# # >>> cursor = conn.cursor()
# # # 创建user表:
# # >>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # # 插入一行记录，注意MySQL的占位符是%s:
# # >>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# # >>> cursor.rowcount
# # 1
# # # 提交事务:
# # >>>
# # # 运行查询:
# # >>> cursor = conn.cursor()
# # >>> cursor.execute('select * from user where id = %s', ('1',))
# # >>>
# # >>> values
# # [('1', 'Michael')]
# # # 关闭Cursor和Connection:
# # >>> cursor.close()
# # True
# # >>> conn.close()
#
#
#
# # import mysql.connector
# # conn_des = mysql.connector.connect(user='root', password='pqc19960320',
# #                                database='Hackerthon',host="120.77.220.239",port=32777)
# # conn_src=mysql.connector.connect(user='root', password='pqc19960320',
# #                                database='sourceData',host="120.77.220.239",port=32777)
# # #源游标
# # cursor_src = conn_src.cursor()
# # #目标游标
# # cursor_des=conn_des.cursor()
# #
# # cursor_src.execute("select * from comments limit 1")
# # values = cursor_src.fetchall()
# # for i in  values:
# #     string=i[1].decode('utf-8').strip()
# #     print(string)
# #     cursor_des.execute("insert into commentsdes (contentsrc,contentsplit,poscount,nagcount,emotion) values('%s','%s',%d,%d,%d)" %(string ,string,0,0,0))
# #
# # conn_src.commit()
# # cursor_src.close()
# #
# # conn_des.commit()
# # cursor_des.close()
# # #
# #
#
#
# a="""
# <!DOCTYPE html>
# <html lang="zh-cmn-Hans" class="ua-linux ua-ff56">
# <head>
#     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
#     <meta name="renderer" content="webkit">
#     <meta name="referrer" content="always">
#     <title>肖申克的救赎 短评</title>
#
#     <meta name="baidu-site-verification" content="cZdR4xxR7RxmM4zE" />
#     <meta http-equiv="Pragma" content="no-cache">
#     <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
#
#     <meta name="keywords" content="肖申克的救赎,The Shawshank Redemption,影讯,排片,放映时间,电影票价,在线购票"/>
#     <meta name="description" content="肖申克的救赎短评" />
#     <meta name="mobile-agent" content="format=html5; url=http://m.douban.com/movie/subject/1292052/comments"/>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
#
#     <link rel="apple-touch-icon" href="https://img3.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
#     <link href="https://img3.doubanio.com/f/shire/94213e812acbb00123f685909b4768bb304d16f3/css/douban.css" rel="stylesheet" type="text/css">
#     <link href="https://img3.doubanio.com/f/shire/ae3f5a3e3085968370b1fc63afcecb22d3284848/css/separation/_all.css" rel="stylesheet" type="text/css">
#     <link href="https://img3.doubanio.com/f/movie/8864d3756094f5272d3c93e30ee2e324665855b0/css/movie/base/init.css" rel="stylesheet">
#     <script type="text/javascript">var _head_start = new Date();</script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js"></script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/1efae2c2d48b407a9bed76b9dd5dd8de37a8dbe1/js/douban.js"></script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js"></script>
#
#     <style type="text/css"></style>
#     <style type="text/css">img { max-width: 100%; }</style>
#     <script type="text/javascript"></script>
#     <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/64e6b112e4964d9.css">
#
#     <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
# </head>
#
# <body>
#
#     <script type="text/javascript">var _body_start = new Date();</script>
#
#
#
#
#
#
#     <link href="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.css" rel="stylesheet" type="text/css">
#
#
#
# <div id="db-global-nav" class="global-nav">
#   <div class="bd">
#
# <div class="top-nav-info">
#   <a href="https://www.douban.com/accounts/login?source=movie" class="nav-login" rel="nofollow">登录</a>
#   <a href="https://www.douban.com/accounts/register?source=movie" class="nav-register" rel="nofollow">注册</a>
# </div>
#
#
#
# <div class="top-nav-doubanapp">
#   <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
#   <div id="top-nav-appintro" class="more-items">
#     <p class="appintro-title">豆瓣</p>
#     <p class="slogan">我们的精神角落</p>
#     <p class="qrcode">扫码直接下载</p>
#     <div class="download">
#       <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
#       <span>·</span>
#       <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
#     </div>
#     <div id="doubanapp-tip">
#       <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 5.0 全新发布</a>
#       <a href="javascript: void 0;" class="tip-close">×</a>
#     </div>
#   </div>
# </div>
#
#
#
#
# <div class="global-nav-items">
#   <ul>
#     <li class="">
#       <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
#     </li>
#     <li class="">
#       <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
#     </li>
#     <li class="on">
#       <a href="https://movie.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
#     </li>
#     <li class="">
#       <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
#     </li>
#     <li class="">
#       <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
#     </li>
#     <li class="">
#       <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
#     </li>
#     <li class="">
#       <a href="https://www.douban.com/time&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
#     </li>
#     <li class="">
#       <a href="https://dongxi.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-commodity&quot;,&quot;uid&quot;:&quot;0&quot;}">东西</a>
#     </li>
#     <li class="">
#       <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">市集</a>
#     </li>
#     <li>
#       <a href="#more" class="bn-more"><span>更多</span></a>
#       <div class="more-items">
#         <table cellpadding="0" cellspacing="0">
#           <tbody>
#             <tr>
#               <td>
#                 <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
#               </td>
#             </tr>
#           </tbody>
#         </table>
#       </div>
#     </li>
#   </ul>
# </div>
#
#   </div>
# </div>
# <script>
#   ;window._GLOBAL_NAV = {
#     DOUBAN_URL: "https://www.douban.com",
#     N_NEW_NOTIS: 0,
#     N_NEW_DOUMAIL: 0
#   };
# </script>
#
#
#
#     <script src="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.js" defer="defer"></script>
#
#
#
#
#
#
#
#
#     <link href="//img3.doubanio.com/dae/accounts/resources/321e246/movie/bundle.css" rel="stylesheet" type="text/css">
#
#
#
#
# <div id="db-nav-movie" class="nav">
#   <div class="nav-wrap">
#   <div class="nav-primary">
#     <div class="nav-logo">
#       <a href="https:&#47;&#47;movie.douban.com">豆瓣电影</a>
#     </div>
#     <div class="nav-search">
#       <form action="https:&#47;&#47;movie.douban.com/subject_search" method="get">
#         <fieldset>
#           <legend>搜索：</legend>
#           <label for="inp-query">
#           </label>
#           <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="电影、影人、影院、电视剧" value=""></div>
#           <div class="inp-btn"><input type="submit" value="搜索"></div>
#           <input type="hidden" name="cat" value="1002" />
#         </fieldset>
#       </form>
#     </div>
#   </div>
#   </div>
#   <div class="nav-secondary">
#
#
# <div class="nav-items">
#   <ul>
#     <li    ><a href="https://movie.douban.com/cinema/nowplaying/"
#      >影讯&购票</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/explore"
#      >选电影</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/tv/"
#      >电视剧</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/chart"
#      >排行榜</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/tag/"
#      >分类</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/review/best/"
#      >影评</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/annual2016/?source=navigation"
#      >2016年度榜单</a>
#     </li>
#     <li    ><a href="https://movie.douban.com/standbyme/2016?source=navigation"
#      >2016观影报告</a>
#     </li>
#   </ul>
# </div>
#
#   </div>
# </div>
#
# <script id="suggResult" type="text/x-jquery-tmpl">
#   <li data-link="{{= url}}">
#             <a href="{{= url}}" onclick="moreurl(this, {from:'movie_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
#             <img src="{{= img}}" width="40" />
#             <p>
#                 <em>{{= title}}</em>
#                 {{if year}}
#                     <span>{{= year}}</span>
#                 {{/if}}
#                 {{if sub_title}}
#                     <br /><span>{{= sub_title}}</span>
#                 {{/if}}
#                 {{if address}}
#                     <br /><span>{{= address}}</span>
#                 {{/if}}
#                 {{if episode}}
#                     {{if episode=="unknow"}}
#                         <br /><span>集数未知</span>
#                     {{else}}
#                         <br /><span>共{{= episode}}集</span>
#                     {{/if}}
#                 {{/if}}
#             </p>
#         </a>
#         </li>
#   </script>
#
#
#
#
#     <script src="//img3.doubanio.com/dae/accounts/resources/321e246/movie/bundle.js" defer="defer"></script>
#
#
#
#
#
#
#     <div id="wrapper">
#
#
#
#     <div id="content">
#
#     <h1>肖申克的救赎 短评</h1>
#
#         <div class="grid-16-8 clearfix">
#
#
#             <div class="article">
#
#
#
#
#
# <div class="clearfix Comments-hd">
#     <ul class="fleft CommentTabs">
#             <li class="is-active">
#                 <span>看过(210530)</span>
#             </li>
#
#             <li>
#                 <a href="?status=F">想看(6378)</a>
#             </li>
#     </ul>
#     <div class="fright">
#         <a href="javascript:;" class="comment_btn j a_show_login" name="cbtn-1292052">我来写短评</a>
#     </div>
# </div>
#
#
#     <div class="title_line clearfix color_gray">
#         <div class="fleft Comments-sortby">
#                 <span>热门</span>
#                 <a href="?sort=time&status=P">最新</a>
#                 <a href="follows_comments?status=P" class="j a_show_login"> 好友</a>
#         </div>
#     </div>
#
#     <div class="mod-bd" id="comments">
#
#
#         <div class="comment-item" data-cid="10780045">
#
#
#         <div class="avatar">
#             <a title="眠去" href="https://www.douban.com/people/rebekah/">
#                 <img src="https://img3.doubanio.com/icon/u1418881-44.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">395</span>
#                 <input value="10780045" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/rebekah/" class="">眠去</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2007-02-20 10:56:01">
#                     2007-02-20
#                 </span>
#             </span>
#         </h3>
#         <p class=""> hope is a good thing
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="356793494">
#
#
#         <div class="avatar">
#             <a title="叶荣添" href="https://www.douban.com/people/39994655/">
#                 <img src="https://img3.doubanio.com/icon/u39994655-1.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">341</span>
#                 <input value="356793494" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/39994655/" class="">叶荣添</a>
#                     <span>看过</span>
#                     <span class="allstar20 rating" title="较差"></span>
#                 <span class="comment-time " title="2011-02-21 11:07:22">
#                     2011-02-21
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 大众经典我从不感冒，为什么？我欣赏水平不行？
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="3658777">
#
#
#         <div class="avatar">
#             <a title="veronique" href="https://www.douban.com/people/xiaoxiaohong/">
#                 <img src="https://img3.doubanio.com/icon/u1067216-5.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">461</span>
#                 <input value="3658777" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/xiaoxiaohong/" class="">veronique</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2006-06-15 18:56:18">
#                     2006-06-15
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 一部没有爱情与美女的电影,却光芒四射
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="4200627">
#
#
#         <div class="avatar">
#             <a title="老鸡｜扶立" href="https://www.douban.com/people/jimo/">
#                 <img src="https://img1.doubanio.com/icon/u1190351-9.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">330</span>
#                 <input value="4200627" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/jimo/" class="">老鸡｜扶立</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2008-01-10 13:23:26">
#                     2008-01-10
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 我最喜欢的电影
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="537314500">
#
#
#         <div class="avatar">
#             <a title="葱" href="https://www.douban.com/people/mmysl/">
#                 <img src="https://img3.doubanio.com/icon/u3410472-120.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">401</span>
#                 <input value="537314500" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/mmysl/" class="">葱</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2012-05-28 22:57:42">
#                     2012-05-28
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 这样的男人谁会舍得背叛。。。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="4851558">
#
#
#         <div class="avatar">
#             <a title="徐小花" href="https://www.douban.com/people/vivipico/">
#                 <img src="https://img3.doubanio.com/icon/u1176223-276.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">280</span>
#                 <input value="4851558" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/vivipico/" class="">徐小花</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2006-08-16 17:46:16">
#                     2006-08-16
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 酣畅淋漓
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="906193">
#
#
#         <div class="avatar">
#             <a title="毛驴哥" href="https://www.douban.com/people/MMT/">
#                 <img src="https://img3.doubanio.com/icon/u1067099-973.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">212</span>
#                 <input value="906193" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/MMT/" class="">毛驴哥</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2005-12-26 22:57:17">
#                     2005-12-26
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 不多说了
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="380050">
#
#
#         <div class="avatar">
#             <a title="我要去荷兰" href="https://www.douban.com/people/Uvo/">
#                 <img src="https://img3.doubanio.com/icon/u1030253-145.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">202</span>
#                 <input value="380050" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/Uvo/" class="">我要去荷兰</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2005-10-08 14:35:04">
#                     2005-10-08
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 因为1994年台湾引进了一部比较卖座的老片The Sting，被错译成了《刺激》。到了1995年本片上映时，片商觉得其剧情与《刺激》有类似的地方（大概都属于高智商的复仇？），因此被译成了《刺激1995》，1998年又有一部片子Return To Paradise因为含有牢狱情节，被译成《刺激1998》！
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="32824487">
#
#
#         <div class="avatar">
#             <a title="乐安蓝" href="https://www.douban.com/people/neverblue/">
#                 <img src="https://img1.doubanio.com/icon/u2261504-67.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">265</span>
#                 <input value="32824487" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/neverblue/" class="">乐安蓝</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2008-03-02 15:00:17">
#                     2008-03-02
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 明修栈道，暗渡陈仓
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="301170212">
#
#
#         <div class="avatar">
#             <a title="吃梨的芳汀" href="https://www.douban.com/people/melody1971/">
#                 <img src="https://img3.doubanio.com/icon/u1917650-823.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">283</span>
#                 <input value="301170212" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/melody1971/" class="">吃梨的芳汀</a>
#                     <span>看过</span>
#                     <span class="allstar40 rating" title="推荐"></span>
#                 <span class="comment-time " title="2010-10-06 15:50:54">
#                     2010-10-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 墙里的人老是喊自由，可是墙外的我们真正得到了吗？
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="479009803">
#
#
#         <div class="avatar">
#             <a title="南笙" href="https://www.douban.com/people/ranwei/">
#                 <img src="https://img1.doubanio.com/icon/u3517544-109.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">226</span>
#                 <input value="479009803" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/ranwei/" class="">南笙</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2012-01-06 23:02:43">
#                     2012-01-06
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 对不起，我戒酒了。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="209421890">
#
#
#         <div class="avatar">
#             <a title="小海" href="https://www.douban.com/people/xseac/">
#                 <img src="https://img1.doubanio.com/icon/u34037196-7.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">168</span>
#                 <input value="209421890" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/xseac/" class="">小海</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2010-01-28 22:52:32">
#                     2010-01-28
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 这部电影没什么好说的，史上最完美的电影，没有一秒尿尿时间！
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="27014356">
#
#
#         <div class="avatar">
#             <a title="Doublebitch" href="https://www.douban.com/people/new4new4/">
#                 <img src="https://img1.doubanio.com/icon/u1917438-178.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">143</span>
#                 <input value="27014356" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/new4new4/" class="">Doublebitch</a>
#                     <span>看过</span>
#                     <span class="allstar40 rating" title="推荐"></span>
#                 <span class="comment-time " title="2007-12-24 17:50:21">
#                     2007-12-24
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 绝对是期待过高导致有点失望
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="950155075">
#
#
#         <div class="avatar">
#             <a title="释凡" href="https://www.douban.com/people/seafans/">
#                 <img src="https://img1.doubanio.com/icon/u2037426-27.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">114</span>
#                 <input value="950155075" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/seafans/" class="">释凡</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2015-08-15 02:57:42">
#                     2015-08-15
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 被誉为影史最棒，不管排名却肯定经典。缜密逃狱者，现代版《基督山恩仇记》，弗兰克·德拉邦叙事有板有眼，斯蒂芬·金大师经典小说很会靠精妙铺垫，转移注意力，一幅美女画背后是地道。蒂姆·罗宾斯冤狱者饱受欺凌，监狱内黑暗与腐朽，摩根出狱后难融社会遭遇，对自由曙光的伟大向往，很棒人性反思力作
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1125152560">
#
#
#         <div class="avatar">
#             <a title="雨果" href="https://www.douban.com/people/154019316/">
#                 <img src="https://img3.doubanio.com/icon/u154019316-3.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">96</span>
#                 <input value="1125152560" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/154019316/" class="">雨果</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2016-12-23 19:03:28">
#                     2016-12-23
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 好片，但是远比这部片更好的还很多，大家整天把这部电影稀奇得不行，其实同年的电影我更喜欢阿甘。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1105845843">
#
#
#         <div class="avatar">
#             <a title="蓉儿" href="https://www.douban.com/people/151135671/">
#                 <img src="https://img3.doubanio.com/icon/u151135671-20.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">104</span>
#                 <input value="1105845843" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/151135671/" class="">蓉儿</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2016-11-05 20:36:25">
#                     2016-11-05
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 这是一部关于希望的经典之作。监狱关不住希望。主人公安迪遭人误解，身陷囹圄，靠着内心无比的坚定，在无尽的等待中，利用智慧和希望，用一把小铁锤救赎了生命，同时救赎了监狱，并将希望的种子播种到每个人的心里。所以说，安迪是英雄，是强者。安迪与瑞德的缘份和友情也很打动人心。值得一看再看。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1108151989">
#
#
#         <div class="avatar">
#             <a title="yocofcjx28" href="https://www.douban.com/people/149120019/">
#                 <img src="https://img3.doubanio.com/icon/u149120019-4.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">90</span>
#                 <input value="1108151989" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/149120019/" class="">yocofcjx28</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2016-11-12 16:01:50">
#                     2016-11-12
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 太感人的电影！完整看过四遍！安迪从下水道爬出后，在水里在雨中仰天长啸时，就瞬间泪奔！
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1067157636">
#
#
#         <div class="avatar">
#             <a title="灰溜溜的熊" href="https://www.douban.com/people/73942837/">
#                 <img src="https://img3.doubanio.com/icon/u73942837-1.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">79</span>
#                 <input value="1067157636" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/73942837/" class="">灰溜溜的熊</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2016-07-28 18:30:00">
#                     2016-07-28
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 终于✔到为什么这部影片被列入IMDB第一的位置了~自由与希望是人类亘古不变的话题，更不必说一位本就是清白无辜，本应该在金融界大展宏图的银行家了~最近非常喜欢看这类剧情片~已经和教父系列并入最爱剧情片之一
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="376616685">
#
#
#         <div class="avatar">
#             <a title="Epidics" href="https://www.douban.com/people/travisthomas/">
#                 <img src="https://img1.doubanio.com/icon/u7601767-87.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">58</span>
#                 <input value="376616685" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/travisthomas/" class="">Epidics</a>
#                     <span>看过</span>
#                     <span class="allstar20 rating" title="较差"></span>
#                 <span class="comment-time " title="2011-04-10 14:05:23">
#                     2011-04-10
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 虚假的巧合被当作精妙对比，突兀的后果往往使人惊叹而不是受启发，脱离过去过于决绝。
#         </p>
#     </div>
#
#         </div>
#         <div class="comment-item" data-cid="1082159430">
#
#
#         <div class="avatar">
#             <a title="__轻笑" href="https://www.douban.com/people/150807637/">
#                 <img src="https://img3.doubanio.com/icon/u150807637-2.jpg" class="" />
#             </a>
#         </div>
#     <div class="comment">
#         <h3>
#
#             <span class="comment-vote">
#                 <span class="votes">66</span>
#                 <input value="1082159430" type="hidden"/>
#                 <a href="javascript:;" class="j a_show_login">有用</a>
#             </span>
#             <span class="comment-info">
#                 <a href="https://www.douban.com/people/150807637/" class="">__轻笑</a>
#                     <span>看过</span>
#                     <span class="allstar50 rating" title="力荐"></span>
#                 <span class="comment-time " title="2016-09-07 16:24:54">
#                     2016-09-07
#                 </span>
#             </span>
#         </h3>
#         <p class=""> 坚持就是胜利啊 最终在墙上弄了个洞
#         </p>
#     </div>
#
#         </div>
#
#
#
#
#         <div id="paginator" class="center">
#                 <a href="?start=0&amp;limit=20&amp;sort=new_score&amp;status=P" data-page="1"><< 首页</a>
#                 <a href="?start=19&amp;limit=-20&amp;sort=new_score&amp;status=P" data-page="">< 前页</a>
#                 <a href="?start=41&amp;limit=20&amp;sort=new_score&amp;status=P" data-page="" class="next">后页 ></a>
#         </div>
#
#
#
#
#
#
#     </div>
#
#             </div>
#             <div class="aside">
#
#
#
# <p class="pl2">&gt; <a href="https://movie.douban.com/subject/1292052/">去 肖申克的救赎 的页面</a></p>
#
#     <div class="indent">
#
#
#
#
#
#
#
#
#
#
# <div class="movie-summary">
#         <div class="movie-pic"><a  href="https://movie.douban.com/subject/1292052/" ><img alt="肖申克的救赎 The Shawshank Redemption" title="肖申克的救赎 The Shawshank Redemption" src="https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p480747492.jpg" rel="v:image" width="100px"></a></div>
#     <span class="attrs">
#
#
#         <p>
#             <span class="pl">导演:</span>
#                 <a  href="https://movie.douban.com/celebrity/1047973/">弗兰克·德拉邦特</a>
#         </p>
#
#
#
#         <p>
#             <span class="pl">主演:</span>
#                 <a  href="https://movie.douban.com/celebrity/1054521/">蒂姆·罗宾斯</a> / <a  href="https://movie.douban.com/celebrity/1054534/">摩根·弗里曼</a> / <a  href="https://movie.douban.com/celebrity/1041179/">鲍勃·冈顿</a> / <a  href="https://movie.douban.com/celebrity/1000095/">威廉姆·赛德勒</a> / <a  href="https://movie.douban.com/celebrity/1013817/">克兰西·布朗</a> / <a  href="https://movie.douban.com/celebrity/1010612/">吉尔·贝罗斯</a> / <a  href="https://movie.douban.com/celebrity/1054892/">马克·罗斯顿</a> / <a  href="https://movie.douban.com/celebrity/1027897/">詹姆斯·惠特摩</a> / <a  href="https://movie.douban.com/celebrity/1087302/">杰弗里·德曼</a> / <a  href="https://movie.douban.com/celebrity/1074035/">拉里·布兰登伯格</a> / <a  href="https://movie.douban.com/celebrity/1099030/">尼尔·吉恩托利</a> / <a  href="https://movie.douban.com/celebrity/1343305/">布赖恩·利比</a> / <a  href="https://movie.douban.com/celebrity/1048222/">大卫·普罗瓦尔</a> / <a  href="https://movie.douban.com/celebrity/1343306/">约瑟夫·劳格诺</a> / <a  href="https://movie.douban.com/celebrity/1315528/">祖德·塞克利拉</a>
#         </p>
#
#
#
#         <p>
#             <span class="pl">类型:</span>
#                 犯罪, 剧情
#         </p>
#
#
#
#         <p>
#             <span class="pl">地区:</span>
#                 美国
#         </p>
#
#
#
#         <p>
#             <span class="pl">片长:</span>
#                 142 分钟
#         </p>
#
#
#
#         <p>
#             <span class="pl">上映:</span>
#                 1994-09-10(多伦多电影节), 1994-10-14(美国)
#         </p>
#
#         <a  class="trail_link" data-trailer-id="108756" href="https://movie.douban.com/trailer/108756/#content" >预告片</a>
#     </span>
# </div>
#
#
#
#     </div>
#     <div id="dale_movie_subject_comments_bottom_right"></div>
#
#             </div>
#             <div class="extra">
#
#             </div>
#         </div>
#     </div>
#
#
#     <div id="footer">
#             <div class="footer-extra"></div>
#
# <span id="icp" class="fleft gray-link">
#     &copy; 2005－2017 douban.com, all rights reserved 北京豆网科技有限公司
# </span>
#
# <a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>
#
# <span class="fright">
#     <a href="https://www.douban.com/about">关于豆瓣</a>
#     · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
#     · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
#     · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>
#
#     · <a href="https://help.douban.com/?app=movie" target="_blank">帮助中心</a>
#     · <a href="https://www.douban.com/doubanapp/">移动应用</a>
#     · <a href="https://www.douban.com/partner/">豆瓣广告</a>
# </span>
#
#     </div>
#
#     </div>
#     <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/22866658146e39d1.js"></script>
#
#
#     <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" />
#     <link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/movie/1d829b8605b9e81435b127cbf3d16563aaa51838/css/movie/mod/reg_login_pop.css" />
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" data-cfg-autoload="false"></script>
#     <script type="text/javascript" src="https://img3.doubanio.com/f/shire/3d185ca912c999ee7f464749201139ebf8eb6972/js/ui/dialog.js"></script>
#     <script type="text/javascript">
#         var HTTPS_DB='https://www.douban.com';
# var account_pop={open:function(o,e){e?referrer="?referrer="+encodeURIComponent(e):referrer="?referrer="+window.location.href;var n="",i="",t=382;"reg"===o?(n="用户注册",i="https://accounts.douban.com/popup/login?source=movie#popup_register",t=480):"login"===o&&(n="用户登录",i="https://accounts.douban.com/popup/login?source=movie");var r=document.location.protocol+"//"+document.location.hostname,a=dui.Dialog({width:478,title:n,height:t,cls:"account_pop",isHideTitle:!0,modal:!0,content:"<iframe scrolling='no' frameborder='0' width='478' height='"+t+"' src='"+i+"' name='"+r+"'></iframe>"},!0),c=a.node;if(c.undelegate(),c.delegate(".dui-dialog-close","click",function(){var o=$("body");o.find("#login_msk").hide(),o.find(".account_pop").remove()}),$(window).width()<478){var u="";"reg"===o?u=HTTPS_DB+"/accounts/register"+referrer:"login"===o&&(u=HTTPS_DB+"/accounts/login"+referrer),window.location.href=u}else a.open();$(window).bind("message",function(o){"https://accounts.douban.com"===o.originalEvent.origin&&(c.find("iframe").css("height",o.originalEvent.data),c.height(o.originalEvent.data),a.update())})}};Douban&&Douban.init_show_login&&(Douban.init_show_login=function(o){var e=$(o);e.click(function(){var o=e.data("ref")||"";return account_pop.open("login",o),!1})}),Do(function(){$("body").delegate(".pop_register","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("reg",e),!1}),$("body").delegate(".pop_login","click",function(o){o.preventDefault();var e=$(this).data("ref")||"";return account_pop.open("login",e),!1})});
#     </script>
#
#
#
#
#
#
#
#
# <script type="text/javascript">
#     (function (global) {
#         var newNode = global.document.createElement('script'),
#             existingNode = global.document.getElementsByTagName('script')[0],
#             adSource = '//erebor.douban.com/',
#             userId = '',
#             browserId = 'rNeNoCgjq8s',
#             criteria = '3:/subject/1292052/comments?start=20&amp;limit=20&amp;sort=new_score&amp;status=P',
#             preview = '',
#             debug = false,
#             adSlots = ['dale_movie_subject_comments_bottom_right'];
#
#         global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
#         global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);
#
#         newNode.setAttribute('type', 'text/javascript');
#         newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/665e3c991277c040b1e32d136d4270f23fc2d0c3/ad.release.js');
#         newNode.setAttribute('async', true);
#         existingNode.parentNode.insertBefore(newNode, existingNode);
#     })(this);
# </script>
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# <script type="text/javascript">
# var _paq = _paq || [];
# _paq.push(['trackPageView']);
# _paq.push(['enableLinkTracking']);
# (function() {
#     var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
#     _paq.push(['setTrackerUrl', u+'piwik']);
#     _paq.push(['setSiteId', '100001']);
#     var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
#     g.type='text/javascript';
#     g.defer=true;
#     g.async=true;
#     g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
#     s.parentNode.insertBefore(g,s);
# })();
# </script>
#
# <script type="text/javascript">
# var setMethodWithNs = function(namespace) {
#   var ns = namespace ? namespace + '.' : ''
#     , fn = function(string) {
#         if(!ns) {return string}
#         return ns + string
#       }
#   return fn
# }
#
# var gaWithNamespace = function(fn, namespace) {
#   var method = setMethodWithNs(namespace)
#   fn.call(this, method)
# }
#
# var _gaq = _gaq || []
#   , accounts = [
#       { id: 'UA-7019765-1', namespace: 'douban' }
#     , { id: 'UA-7019765-19', namespace: '' }
#     ]
#   , gaInit = function(account) {
#       gaWithNamespace(function(method) {
#         gaInitFn.call(this, method, account)
#       }, account.namespace)
#     }
#   , gaInitFn = function(method, account) {
#       _gaq.push([method('_setAccount'), account.id]);
#       _gaq.push([method('_setSampleRate'), '5']);
#
#
#   _gaq.push([method('_addOrganic'), 'google', 'q'])
#   _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
#   _gaq.push([method('_addOrganic'), 'soso', 'w'])
#   _gaq.push([method('_addOrganic'), 'youdao', 'q'])
#   _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
#   _gaq.push([method('_addOrganic'), 'sogou', 'query'])
#   if (account.namespace) {
#     _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
#     _gaq.push([method('_addIgnoredOrganic'), 'douban'])
#     _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
#     _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
#   }
#
#       if (account.namespace === 'douban') {
#         _gaq.push([method('_setDomainName'), '.douban.com'])
#       }
#
#         _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])
#
#         _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);
#
#       _gaq.push([method('_trackPageview')])
#     }
#
# for(var i = 0, l = accounts.length; i < l; i++) {
#   var account = accounts[i]
#   gaInit(account)
# }
#
#
# ;(function() {
#     var ga = document.createElement('script');
#     ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
#     ga.setAttribute('async', 'true');
#     document.documentElement.firstChild.appendChild(ga);
# })()
# </script>
#     <!-- daisy6d-docker-->
#
#   <script>_SPLITTEST=''</script>
# </body>
#
# </html>
# """
#
#
#
#
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(a,'html.parser')

#
# import json
# with open('movieid.json','r') as f:
#     a=json.loads(f.read())
# for index,vaule in enumerate(a):
#     print(index,vaule)

y1292052="""
大头绿豆 评论 肖申克的救赎 2005-05-12 20:44:13距离斯蒂芬·金（Stephen King）和德拉邦特（Frank Darabont）
们缔造这部伟大的作品已经有十年了。我知道美好的东西想必大家都能感受，但是很抱歉，我的聒噪仍将一如既往。
在我眼里，肖申克的救赎与信念、自由和友谊有关。［1］信 念瑞德（Red）说，希望是危险的东西，是精神苦闷的根源。
重重挤压之下的牢狱里呆了三十年的他的确有资格这么说。因为从进来的那一天起，狱长就说过，「把灵魂交给上帝，把身体交
给我。」除了他能弄来的香烟和印着裸女的扑克牌，任何其他异动在这个黑暗的高墙之内似乎都无法生长。然而安迪（Andy）告诉他，
「记住，希望是好事——甚至也许是人间至善。而美好的事永不消失。」所以安迪能够用二十年挖开瑞德认为六百年都无法凿穿的隧洞。当
他终于爬出五百码恶臭的污水管道，站在瓢泼大雨中情不自禁的时候，我们仿佛看到信念刺穿重重黑幕，在暗夜中打了一道夺目霹雳。亮
光之下，我们懦弱的灵魂纷纷在安迪张开的双臂下现形，并且颤抖。庸常生活里的我们，似乎已经习惯了按部就班，习惯了先说「那不可能」
，习惯了没有奇迹，习惯了，习惯了。可是正如《飞越疯人院》（One Flew over the Cuckcoo’s Nest）中说的那样，「不试试，怎么
知道呢？」试着留住一些信念，在它们丧失殆尽之前。它们也许无法最终实现，也许无法让我们更有意义的活着——甚至对于我自己而言，
它们只会愈加带给我来更多的虚无感。然而我知道我有多需要这样的虚伪与自欺，因为你可以说我在做梦，但我不会是仅有的一个。
——我们已经看到监狱长打开藏有安迪凿石锤的《圣经》时，翻至那页正是《出埃及记》。这个章节详细描述了犹太教徒逃离埃及的过程。
我到今天也始终不明白，这两个意大利女人在唱什么。事实上，我也不想去明白。有些东西不说更好。我想，那是非笔墨可形容的美境。
然而却令你如此心伤。那声音飞扬，高远入云，超过任何在禁锢中的囚犯们所梦，仿佛一只美丽的小鸟，飞入这灰色的鸟笼
，让那些围墙消失，令铁窗中的所有犯人，感到一刻的自由。当安迪不顾一切地在监狱的喇叭里放《费加罗的婚礼》（Le Nozze di Figaro）
时，镜头缓缓划过正在广场上放风的犯人们和狱警们。他们叫人感动地静立当地，抛却所有愤懑、狠毒和怨怼，沐浴着我从未觉得如此自由
的阳光。莫扎特的乐声铺洒在这些人们身上，来自俗世的美妙音符似乎将他们都濯洗得纯净无比。强者自救，圣者渡人。我这才明白安迪的
用意。修屋顶的时候，他为大家争取来啤酒，事实上是为大家争取到那种像在修缮自家的屋顶一般自在的感觉，所以他不喝酒，微笑却带着巨
大的幸福；放费加罗的婚礼，也是要唤醒他们已丧失殆尽的自由感。然而强者终究是少数。自由面前，更多的人们纷纷选择禁锢。在监狱图
书馆呆了五十年的布鲁克斯（Brooks），为了不被假释，竟然想通过伤害狱友来达到留在监狱的目的。很奇怪吗？自由本来应该是人们向往和
追求的东西。可是布鲁克斯们却早已经被监狱的规则之下规则了自己，他们需要规则，需要秩序，如果没有它们，甚至无法生存。
「监狱里的高墙实在是很有趣。刚入狱的时候，你痛恨周围的高墙；慢慢地，你习惯了生活在其中；最终你会发现自己不得不依靠它而
生存。这就是体制化。」假瑞德之口，斯蒂芬·金直指卑微。布鲁克斯得到了身体的自由，灵魂却已经被无可挽回地体制化。他终于没
有能够摆脱对自由无法适应的困境，悬梁自尽。而睿智如瑞德，在出狱之后也悲哀地发现，自己竟然连撒尿都要向经理报告，否则一
滴尿都挤不出来。他也考虑如何违规以便回到监狱，甚至考虑与 布鲁克斯一样离开。要么忙着生活，要么忙着等死（Busy for living, 
 or busy for death）。步履匆匆的人们也许应该偶尔驻足，跳出来看看自己的模样。我们终会知道，习惯于服从规则的
 人们将付出巨大代价来习惯本来属于每一个个体的自由。 此片无关爱情，除了背叛。有的只是监狱中的男人间的友谊。瑞
 德和安迪的那种友谊置放在高墙之下，似乎比我们纷繁俗世中的友情来得更加纯粹和干净。他们都是内敛的人，然而洞悉
 一切，心意契合。我喜欢这种感情。所以在他们终于相会在太平洋小岛的阳光沙滩之上的时候，忍不住一人笑了。如果我在肖申克，
 我会是谁？如果你在肖申克，你又会是谁？"""

y1291546="""
 又看《霸王别姬》，不一样的环境，一样的感动。
有几大矛盾对象：
程蝶衣与段小楼
蝶衣从最开始近京剧班，就与小楼有着很深厚的感情。我们可以看到许多感人的画面：小楼受罚，黑夜冬天在院子了跪着，蝶衣则隔着窗子心疼地看着他，等小楼回来后则自己光着身子，却把被子给小楼裹上。接着那个他们依偎在一起睡觉的场面大家一定很难忘记，蝶衣紧紧地搂着小楼，仿佛怕失去了他。而小楼对蝶衣也是身份的爱护，他开始知道蝶衣不想学京戏了，那一次，他却把蝶衣放走了，尽管他十分的不舍的。还有后来让老板来，听蝶衣总唱不好“我本是女娇娥”，就用烟斗烫他，从而使蝶衣第一次唱对。
毋庸置疑，他们都是相互喜欢的，但是，小楼对蝶衣只是好兄弟一样的感情，而蝶衣对小楼则超越了亲情。由于总在戏中扮演青衣，唱的是女腔，学得是女形，久而久之，在社会及角色中，他则比较倾向于女性。对小楼，他也一直是以一个女性的角色，例如帮小楼舔伤口，给小楼画脸谱，其亲昵的动作无不体现出他对小楼的超出一般的感情。尤其是在出现了菊仙以后，他对菊仙的嫉妒和对小楼的怨恨，都很明显的变现了他社会角色中女性化的特点。
程蝶衣与小癞子
小癞子给蝶衣留下的最深的印象，莫过于一句话：“等以后我成角儿了就天天吃糖葫芦”和一个场景了“最后因为害怕被师傅毒打，而上吊自杀。”他的自杀是有准备的，由于看着蝶衣被打的恐怖的场面，或许还由于他觉得成为一个角儿还要挨很多很疼的打而觉得害怕？总之，他有准备的自杀了，死之前他把自己身上所有的吃的东西都急急忙忙的吞了下去。这也许是许多学京戏却没有成角儿的人的另一种选择吧。梦不能成真，就只有在虚无的世界中去寻找了。
但他却留给蝶衣一生的印象。在蝶衣成角儿后，一次入场前他听到了冰糖葫芦的吆喝声，就愣住了。那时候，他想到了什么呢？小癞子的梦想？小癞子的死？或许是震惊和无奈？
程蝶衣与张公公
张公公玷污了蝶衣。成了角儿，也并不一定只是荣誉和欢乐。他们或许还不知道，开始只是拼命的向前奔，可后来等达到了目标，却才发现这结果也许并不是美好的，可却，只能接受而不能改变了。
讽刺的是，后来的新中国成立前夕，曾经呼风唤雨，为所欲为的太监，张公公，却成了一个买烟的贫苦的老人，并且已经神智不清，只知道买烟的人。他曾干过的一切，就在他的混沌中被遗忘了吗？可是受到伤害的人，却是一生的无法挽回的创痛。社会中人与人之间，一件事也许对一个人来说微乎其微，何时对另一个人来讲也许是决定性的。
程蝶衣与菊仙（妈妈）
从一开始蝶衣对菊仙就充满了敌意，嫉妒，因为她抢走了小楼，一个蝶衣生命中最最重要的人。他们之间也许存在着一场战斗，而蝶衣注定是失败者。
可是，在一幕幕蝶衣与菊仙的对视中，他有对蝶衣有一定的依恋，是一种对于母亲的依恋。尤其在他戒毒瘾时菊仙抱着他哄他睡觉更表现得淋漓尽致。蝶衣从小就被妈妈送到京戏班，连妈妈的最后一眼，那个空荡荡的没有人影的门，都没有看到。因此他对母爱是渴望的。并且菊仙和蝶衣妈妈得出身一样，都是妓女，更给他一种幻象，菊仙有着他妈妈的众多特性，女性，泼辣，妓女。
因此他对菊仙的感情就非常的矛盾了，在敌视与依恋中徘徊。
程蝶衣与袁四爷
也许袁四爷是他的知音，在京戏方面。他在蝶衣失去小楼的最痛苦的时候，让蝶衣产生了幻觉。他很欣赏蝶衣，他也给过蝶衣很多的帮助，各个方面。但小楼对他是充满敌意的，也许是因为他对蝶衣的特殊的关照也令小楼嫉妒了？但他的命运让小楼和蝶衣都很惊讶，一个社会上游刃有余的名流，终会遇到一种无法逍遥自在的社会。他就那么的死了，被历史碾死了。
程蝶衣与小四
蝶衣捡来了小四，在师傅死后，又收养了小四。他是想让小四延续京剧的发展。可时候来，小四却无情的将蝶衣打下了地狱。他抢占了蝶衣的上台的机会，他抢占了虞姬的角色。而对于蝶衣，一个把京剧视为生命，甚至比生命还重要的人，如果连京戏都被剥夺了，那他还能剩下什么呢？
程蝶衣与京戏（师傅）
师傅把蝶衣领进了京剧的世界，一个严厉的，传统的，却对京剧充满理解的师傅，他最终在唱京剧时倒下了，辞世了。无疑，他给了蝶衣很大的影响。蝶衣慢慢的从只知其声，其形，到了解其中的精粹，最终把其视为生命。他在表演时非常的入境，常到达一种与戏中的人物和一的境界。那种潜心投入的表演，一切外在的喧闹和烦扰都不能够影响。
程蝶衣与时代（清末，侵华，民国，新中国初期，文化大革命，之后）
一个动荡的年代，人们的思想也是非常慌乱的，不确定的。连国家，民族，你都不能确信，你就更不能确信任何其他的一切了。人们仿佛都是漂浮在空气中的，没有根基。善于生活的人也不一定能够生（比如袁四爷），懂得人生常识的人也不一定能够生，（比如菊仙）。
清末，百姓，戏子，被动得像旗子一样受封建残余的玩弄，不能把握自己的命运。
日寇来了，无辜的人们的姓名也不能幸免。或许艺术能够无国界，可是舆论却不能够接受，民族感情不能接受。
民国呢，仍然是动荡不安，随时都回发生变动。
短暂的新中国初期，对于京剧形式的变形，蝶衣很难接受，毕竟，那不是他心中的京剧的印象。可是他不能决定一切，因为时间的车轮在不停的转着。
他一直都在唱着，不管是哪一个时期，或许，每个时期都需要艺术。艺术没有时间性。可是，在这其中蝶衣总要时不时地受到外界的干扰，政治，一个无聊的却无法避免的东西，在艺术前进的道路上洒满了图钉。
文化大革命来了，一切真的都颠覆了？革文化的命，对文化进行批判，打破固有的一切文化。或许如果这只在学术界进行，只是行而上的批判是好的，可是当权力掌握在了不成熟的头脑发热的人的手中，也许就变味了。没有了文化，没有了标准，没有了历史，每个人都可以是他想是的了，最终，也就什么都不是了。
程蝶衣与死
蝶衣真的累了，经历了那么多辉煌与动荡，得到，失去，又得到。最终，他选择了在戏中结束自己的生命。一生都无法把握住自己，一生都宿命的漂泊，终在死亡这件事上他做了自己的主人。一幅完美的画面——霸王别姬，永不能重演了。留下了孤零零的楚霸王，人生，也许真的只是一场戏。爱，别，离，怨，憎，恚，总得有一个苦涩的结局来收场。
程蝶衣与张国荣
虞姬死了，呈蝶衣死了，张国荣死了。戏里戏外，真真假假，可是，结果都一样。
"""
y1295644="""
喝了些酒，光线很暗。最喜欢趁着这时候写东西，畅快淋漓。放着贝多芬的小提琴协奏曲。想起那个变态恶人说的：“贝多芬的开场很好，让我感觉非常爽，但是到后来，它就开始他妈的无聊。——知道我现在还不杀你的原因了么？”话说完，一阵乱扫之后，硕大的身躯倒地。一次屠杀完成。
  《Leon》的每一个角色都出乎意料的精彩出色。它没有很多高深的思索，却又太能让人琢磨。做为职业杀手的Leon，他的生活是单纯的——单纯的甚至像旧时代的手艺人，早出晚归，为生计而奔波，一次又一次的训练，完成任务，因为危险的职业他连睡觉也要坐着，面对爱情和可能的闲适生活，也要保持克制提醒自己。他与其说是一个杀手，莫不如说已成了一种生活本身——他代表着男人最极端的一面——对待强大残暴的敌手冷酷无情，对待温顺的女人和娇弱的儿童时却必须保持规则——不伤害他们，甚至妥协，而温情甚至是他们的阿迦琉斯之踵，最后以生命为代价去报答。“一行有一行的规则。不杀女人，不杀小孩。”这个规则和禁忌的背后，印照的是他渴望又欲求不得的爱情和亲情。麻痹很多年后一个小女孩的意外闯入又令他把这些遗忘给想起，就像想起他儿时的故事。老头子说：“你刚来这个国家的时候，乱七八糟，被女人弄的一塌糊涂。现在，却是一个优秀的杀手。”人的强大和冷酷，是在痛苦和摧毁的土壤上生出的根，却注定成了杀手手中精心照料却开不出花结不出果的植物。玛婷达的出现成了他一生的光亮，也成了她的自己的毁灭和新生和救赎。就像他在面对她家人被血洗之后惊慌无措时刻的那一瞬的开门，光亮照亮了她的脸也照亮的自己的人生。他被她改变，而他，成了她的热爱和新生。痛苦人生的一切至此完成颠覆。
    我一直为结尾的情节猜测不已。大多数人认为，杀手走向门的时候，是向往着新的生活——那个生活里，屠杀和警惕将不复存在，有的只有他的玛婷达，和那株不开花不结果的他的心爱。他脸上希冀的眼神和迷茫又向往的表情出卖了他的情感，却令他丧失了杀手的本能——一只手枪跟在后面，他竟然全无察觉，最后，枪响，杀手死在了暗黑的走廊尽头，离光亮的门口只差一步。但我却隐隐倾向于认为，杀手知道后面的手枪，他在寻找他遍寻不得的梦，那个梦连着长廊与出口，也连接着现世的痛苦与来生的梦幻——它是死亡。他一人斗百人，最后已经没有手枪，无法为玛婷达报仇，唯一和希望，是和那个变态同归于尽。更重要的是，他出去了，又能怎样呢？有他的玛婷达，更好还是更坏？依然和他在一起，小女孩的生活恐怕还是在仇恨中度过，没有新生，一切重新归回到旧的轨道——练习，杀人，执行任务，生活像尖利的刀寒光闪闪。他选择了死亡，倒下后的最后一刻，将炸弹拉环送到变态恶人的手中，几乎深情款款，柔和的仿佛是临终的嘱托：“这是——来自——玛婷达——”炸弹引爆，报仇完成，杀手已死。
    “这是，来自，玛婷达——”一种意义上，显然，这是他为玛婷达报了仇。但更根本的，是他代她完成了他不要她此生完成的使命。报仇的使命完成了，玛婷达作为杀手的使命完成了，两个杀手痛苦的生命同时结束——一个得到永恒的休息，另一个终于解脱。不开花不结果的植物最终被种进了草地，它可以生长因为它从来没有这样靠近过自然。他从来都是被扭曲被节制的，直到有一天疯狂执拗又天真的玛婷达拯救了他，最后他用他的全部力量作为对她长久以来热情的报答，杀人者终于完成了拯救。偶遇照亮了他，就像最后榴弹爆发出最猛烈的光——“人生是一直这么痛苦，还是只有是小孩子的时候才这样？”杀手沉默了一会，喃喃地说：“一直如此。”一直如此，但现在可以不要这样了，她也可以不要这样了，生活和爱情把他逼上了这条道路，但最后又把拿走的东西还给他。不同的是，这一次他心甘情愿，也为自己不开花不结果的植物找到了主人——她终于把它根植于土壤。
   变态恶人喜欢贝多芬，理解莫扎特，推荐自己的猎物尝试勃拉姆斯，却疯狂残忍冷漠之极；杀手不识字，不懂得经典电影，不认识梦露和卓别林，却在冷酷的一生中找到了归依，打开了心灵的窗和门。原来艺术能够陶冶性情，却不能改变灵魂——什么东西都不可能改变灵魂，因为灵魂根深蒂固，它就是人们自己——就像杀手的职业让他性情冷酷，但磨不掉他心中原本温情脉脉的灵魂——那个灵魂引而不发，坚忍地埋伏，终于在积聚了太久之后，把他交还给自己。它就像那株植物和牛奶，来自自然，容不得半点污染，却找不到自己的土地。但它最后还是回家了。是绿色，它就属于土壤。是天真的女儿，她就必将属于另一个世界，只是那是他有生之年所不能给予的、渴望而不可及的，过去的时光。原来我们每一个人寻找的，不是成熟的个性，也不单是幸福，而是被自己丢失已久的灵魂，它属于昨夜的领地和昔日的城堡。它起源于我们童年时候的梦幻。它长着一张孩子般的天真的脸。孩子可以爱，可以幻想，可以单单凭着自己的生存本能打碎成人世界的游戏。而人的成长和岁月的磨砺，不过是在动荡中把它抛弃，在爱情中被它迷乱，在严酷的生存法则中把它压抑，但它依然坚强隐忍，藏的隐秘。看不见它的，它也一直在那里；看见它了，它为我们把全部秘密揭示。它会一直引领我们，如迷藏般不断的隐埋又不断的揭露，直到死亡把这场诡异眩丽的梦幻从我们身上抛开
"""

y1292720="""
一个南阿拉巴马州的傻子阿甘，一辈子喜欢的一个女人就是珍妮，从小到大阿甘和珍妮就是好朋友，他们一起上学，一起长大，最后虽然相隔很远但是阿甘始终爱着珍妮，不管她做什么，不管她是谁，不管她变得多老多丑，不管她身在何方，阿甘始终在哪个南阿拉巴马的家里，日夜思念他的姑娘，日夜等待着珍妮的归来。

这就是阿甘，这就是他的爱情，这就是他的珍妮。

我们回想第一个场景，阿甘在珍妮的宿舍，珍妮问他将来要成为什么样的人，阿甘楞了一下，说：我不是做我自己吗？珍妮说她想成为一个歌手，成名，阿甘还是不懂，说他只想成为他自己。

我被这个场面深深打动，因为阿甘虽然是个傻子，但是他明白自己真正需要的是什么。成名，赚钱，成为一个成功的人，这些都不重要，重要的是我们要做好自己，我们为什么值得让别人尊敬？是因为我们的职业？地位？还是家产？如果这样，那人的本身才成为这些头衔的附属品，我应该成为我，而且我只想成为我，对于阿甘来说，他只想做他自己，只想爱一个女人叫做珍妮。

在华盛顿的那一场，珍妮问阿甘为什么他对她这么好，土鳖一点的男人会拉着珍妮的手，含情脉脉的说因为我爱你。阿甘不是，他又摆出那个招牌一样的白痴表情，对这珍妮说： you are my girl（因为你是我的女孩）。

为什么不是I love you ？为什么不是我爱你？因为我爱你已经无需多言，如果我爱你，而你不爱我，那么对于我来说这就不能承受，我可能会找另外一个女人去爱，但是因为你是我的女孩，所以我可以承受你的背叛，你的逃离，我也可以忍受孤独，忍受没有你的日子，重要的不仅仅是我爱你，而是因为从我看见你的那一刻起我就知道，你是我的女孩，你是我的姑娘。

如果有人仔细想想这句话，看看阿甘那张单纯的脸，那双眼睛，就能体会到什么是爱一个人，什么是喜欢一个人，什么是认识一个人，什么是放弃一个人。

我常常会遇到这样的事情，恋爱中的男女，不管他们究竟为了什么恋爱，不管他们付出了多少，在付出较多的一方经常会抱怨，说自己付出的太多，或者回报很少。于是第三个声音就会告诉你：不要把男人（女人）太当回事，你越把他（她）当回事，他（她）越不把你当回事。

在我看来，这些都是懦弱的人，愚蠢的人，因为你们其实根本没有在恋爱。你们只是在爱情的称呼下自我陶醉，却在付出回报的时候露出了真正的不足。

因为爱情本来就是奢侈品，你不能因为孤独寻找爱情，你不能因为贫穷寻找爱情，就好像你不能因为自己还是一个处男（处女）而跟别人上床一样。爱情的价值在于当你的生活本来就已经很丰富的时候，突然你想找一个人来分享这一切，在你本来幸福的时候，爱情会让你更幸福。

所以这个时候的你根本不需要从对方身上获得什么，你有的就是付出的欲望，这才是爱情。

没有束缚，不要求回报，在爱对方的同时能够承受住他（她）的背叛和逃离。这才是真正的爱情。

爱一个人很容易，但是能想阿甘那样承受所谓的痛苦却非常难，因为这些不是爱，更像是对自我价值的证明。

那个南阿拉巴马的傻子阿甘，最终娶了珍妮，生了一个小阿甘。他们快乐的生活在一起。在影片最后，当阿甘站在珍妮墓前，用南阿拉巴马的口音说：我爱你珍妮。这是我们的眼里才会闪烁着泪花，为的不是这个傻子终于娶了珍妮，而是因为这个傻子拥有许多聪明人没有的感情：爱情。而那些自以为拥有了爱情的聪明人其实并没有得到爱，也不知道什么是爱。

这样来说，阿甘并不是一个傻子，至少不是一个普通的傻子。 

"""

y1292063="""
就算在最艰难最黑暗的日子里，就算了无希望，死亡近在眼前，他依然深爱着并用生命与智慧保护着他的妻子与儿子。他的勇气与智慧，即使在战争的硝烟弥漫中，即使在集中营的暗无天日中，即使在最后枪声响起死亡来临的那一刻，依然闪现着耀眼夺目的光芒。
 
他用尽全力，在集中营的悲惨世界里，为儿子，营造了一幕美好的幻想，他告诉儿子，所有的残酷只不过是一场游戏，游戏的奖励是一辆崭新的坦克。于是，他的儿子便有了足够的勇气，熬过那段水火的岁月，最后，当他坐上盟军的坦克时，他的幸福无可言语，而那种幸福，正是他的父亲用生命为他交换的。他不放弃任何机会为他风雨中的家庭制造哪怕是点滴的欢欣，在路过集中营的广播室时，他冒着危险在广播里呼喊妻子的名字，他想告诉她，他和儿子都还活着。他趁着做侍者的机会，为妻子播放了《船歌》，这首曾经响在他们定情之夜的歌曲，飘过沉沉迷雾的阻挡，在黑夜里，给他的妻子带去安慰，也让他们一家人，都鼓起了勇气，共同经历灰暗的时光。
 
就在他生命的最后一晚，他将儿子安顿在一个铁箱子里，然后，去寻找他的妻子。当他被捕之后，路过那个铁箱子时，他知道他的儿子正注视着他，于是，他装出一副滑稽的模样，惹得儿子笑出声，他仍然坚持着，坚持着使儿子相信这一切都只是一个游戏，千万不要害怕，永远要微笑而乐观地去面对。然后，枪声响起，他去了，而他的儿子与妻子终于获得解放，当他们在阳光下搂抱在一起的时候，他的儿子说道，我们赢了！确实，在这一场浩劫当中，他们赢了，因为，他们有一个英雄的丈夫与父亲，他的名字叫基度。
 
《美丽人生》是一部相当浪漫的电影，犹太青年基度到一个意大利小镇上准备以开书店为生，在那里，他遇见了美丽的姑娘多拉，然后，是一系列充满了智慧、滑稽、阴错阳差、浪漫的轻松片段，终于，基度与多拉终成眷属，镜头一转，他们从房间里追着他们的儿子来到院子里，一家三口的幸福生活令人羡慕，基度用自行车载着美丽的妻子，车框里坐着机灵的儿子，他们飞驰而过，而街道上，却已经出现了纳粹的铁丝网。
 
没有什么比快乐的戛然而止更令人感到揪心。当基度的幸福生活刚刚开始之时，他的犹太身份使他被抓去了集中营，而他的妻子，本来并不用去集中营，却毅然的随他们跳上了火车。最真挚的爱情，有时候真不需要太多的言语，连执手相看都不需要，只是纵身一跃，跟去天涯海角。在影片当中，演多拉的演员有很好的演技，那是一种很克制的平静，当她在集中营里听到孩子将要被杀掉的消息时，她的脸上没有任何表情，只是站在楼梯上，由着后面的人群在她身上冲撞，她望向窗外，目光深远。后来，她被派去挑拣死难者的衣服，那种小心翼翼，不敢也不愿发现儿子衣服的感觉很到位。从这里也可以看出，一个人最深沉的爱，其实，是很平静的，能够撕心裂肺哭出来的，往往也是释然的开始。
 
最后，基度的儿子和多拉在阳光下抱在一起，他大声喊叫着，我们赢了。那时候，他还不知道他的父亲已经死去。电影响起旁白，以基度儿子的语气，听声音，他也已经步入老年，那么，这部电影就能理解成他的回忆。在他的回忆里，他的父亲，依旧是那样鲜活，这，何尝不是另一种活着。枪炮、炸药、毒气、死亡、饥饿，这些东西看似强大，最后的胜利者，却只能是人和生活。真正的光芒，就像基度朝他儿子眨眼的那一刹那，意思是，无论怎样，只要我们不害怕，坚强、快乐、盼望，人生终究美丽，于是，我们总会赢。
"""

y1291561="""
我的一个朋友每看到在花丛下白给千寻吃他用魔法做的饭团那一段就泣不成声。很多人不明白，但是我并不奇怪，因为我也是一样。
 也许没有童年创伤的孩子不会明白那一段的感人之处。我想也许每个孩子都会幻想自己能够有一个白龙朋友，平时他也就和自己差不多大，可以陪自己玩，但是在遇到危险的时候，他就会变身为矫健的白龙，挺身而出。是的，那并不足为奇。但是不会每个孩子都曾设想自己遭遇绝境，孤立无援，满目都是神情漠然、居心叵测的陌生人，当然，更不可能都真的遭遇这样的事情。

 一个受宠的孩子会觉得他所拥有的都是理所应当的，而一旦没有得到，就会觉得百般委屈。这样的委屈固然也是无可厚非，但是却没有什么可以在其中生成，换言之，如果一直如此，那么就会是一个长不大的孩子。但是遭遇绝境却并非如此。
 其实绝境并不非要是穷山恶水或是危机四伏，对一个孩子来说，在人海中一时间脱开了妈妈原先紧握的手，就可能是一个绝境。在这个绝境中并非步步杀机，而仅仅只是陌生。当然，陌生中也的确会有邪恶，但更多的只是中立的环境。孩子离开了倚靠，忽然发现自己孤立无援，并不需要被迫害，就会感到自己被遗弃。自感被遗弃的荒野的孩子，在最初的惊慌失措之后，终于认识到这一次不是坐倒在地上哭泣就能等来救援的了，于是他开始倚靠自己仅有的判断和力量，独立面对当前的局面。然而很显然的是，他那点仅有的东西是那么不够用，他总是四处碰壁，然而却没有人为他擦干泪痕，没有人替他点亮明灯。这个情境在他即便摆脱出来之后都会被深深铭记，在此后的漫长的人生中他每当遇到相似情境都会想起，那时候他所获得的实际经验也许早已过时，但是那份感受却能照亮自己，曾经走出困境的孩子就会明白如何靠自己的力量坚强地走下去。
 也许，那个迷失在绝境的孩子曾有一份幸运，得到过哪怕是一个小小的指引，一点微不足道的善意，那么所有这一切也都将被深深铭记。只有经历绝境的人才知道那份举手之劳对他人可能意味着什么，在今后的人生中，他也不会忘记在力所能及的范围内给予，他知道，那并不是一个多么高的要求，也并不困难。那个迷失的孩子在如同快要溺水一般的感受中苦苦支撑，忽然周遭的陌生中浮现一丝亮色，某个方向上伸出了一双温暖的手，那个也许本来一脸倔犟的孩子一下子就泣不成声了。在那个时候，要俘获一个孩子的心是多么的容易。惟其如此，伸出手来的你就该知道肩头重负，你在那一刻为他背负了什么，他在此后的人生中亦将始终背负下去。如果他在那一刻遭到欺骗或者伤害，那么他亦将以他全部的不信任去伤害这个世界。

 千寻是幸运的，她既没有在溺爱中沉沦，也没有在绝境中沉陷，那一点点的苦难，来得刚刚好。她眼中的世界会有艰辛，但却不失温暖，她能够倚靠自己，却也没有失去对人世的谅解。我不知道是否所有的孩子都那么幸运，也许不全是吧。有人仍在刻骨铭心地报复着这个世界，也有人仍在予取予求得那么理所当然，他们都是不幸的，其实，是不幸的。
 当我看到千寻在花丛中接过白递来的饭团，我怎么能不泪流满面？毕竟，我也曾有过漂泊无定的童年，那个时候，我曾被深深伤害，也曾被深深地温暖，无论是什么，都让我一直以来在内心深深地铭感。成长其实真的很不容易啊，稍稍不小心，就在心底留下了阴暗，就不再是那么一个健康的孩子。若你不想仅仅怪罪于这个时代，那么，就请妥善对待每个孩子的童年。

（二）千与千寻之成长之旅

宫崎骏原本是想安排白龙、千寻同无脸男大战一场作为结局的，但是后来觉得不妥，就改成了一次旅行。幸好改了！否则这部经典的动画巨作就不会象现在如此完美了。是的，千寻的旅行也是让我至为感动的一幕，就如宫崎骏自己所说的，所有的成长到最后总是一次旅行。
 身处童年情境之中，很多事情都是出于被动。陷入绝境也好，倍受宠爱也罢，那些都并非出于自己的选择。因此，那里面还没有新的东西生长出来，那还不能叫做成长。要在经历种种之后，离开当时所处的特定的情境，方才可以获得对当下的领会，而那些种种的经历方能为自己呈现新的东西，换言之，方才真正成为自己的一部分。那时的自我，如果没有在经历中受损，就会变得更加的完整。
 要明白这一点，其实也不困难。回想一个人的恋爱历程就是如此。当一个人开始了他一生中第一次的热恋，他的生命中忽然涌入了许许多多新的内容，仿佛每一天都是全新的，他精力旺盛、情绪饱满，不写日记的开始写日记，不懂诗歌的变成了诗人，一起早起锻炼，一起游山玩水，仿佛有做不完的事情。可是，那些内容完全外在于他，从不曾成为他自己身上的一个部分，他就像一个受命运宠爱的孩子，满屋子的玩具却不懂得其价值。
 忽然有一天，因为这样或者那样的原因，谁知道呢？我们见多了这样的情形：他失恋了。整个世界仿佛崩塌下来一般，他忽然发现自己的贫乏：当初他抱了满怀的珍宝瞬间就成了一堆垃圾，什么电影院的票根，什么夹着虞美人花瓣的情书，全都成了废纸。而他掉过头来却发现，他早在某个时刻就遗失了自我，他疏远了自己的朋友圈子，他忽略了自己一贯的追求，他甚至因为两人世界的支出而使得自己大加破费。更重要的是，原先在恋爱中他是快乐的，他认为全世界都在自己手中，即便那时候一文不名也不曾烦扰到他，可是，如今他觉得自己一无所有，所有曾经的种种都毫无例外地离他而去了。
 他如果真的爱过，那么失去的时候，请允许他在自己的世界里孤单地抽泣两声，我们暂时不必要去打搅他的悲伤。
 
 但是，如果我们的这位主人公他就此沉溺于那份悲伤之中，甚至开始自暴自弃，开始怨天尤人，甚至因此成了一个愤青或者虚无主义者，那么，他其实从来不曾离开过原地，在恋爱之前他拥有多少，在那之后他不可能变得更加丰富，相反还可能变得偏激而贫乏。那时候，他将不能再给予，因此也就不能再获得，不能再拥有可能的幸福。
 在对当下情境的沉溺之中，人是永远不会成长起来的。纵然愤怒足以燃烧整个世界，纵然哀怨足以窒息所有生命，都是一样的苍白无力。那么，该怎么办呢？其实很简单：我们的主人公只需要离开原地，离开那曾经带给他最大的快乐和安慰也带给他最深的痛切和孤独的种种经历，然后，走开去。
 离开原地，走开去，那就是所谓最后的旅行。
 千寻乘上那班有去无回的列车，就像我们有去无回的青春，开始了她最后的旅行。
 那已不再是一个被动的决定，而是她独立的自由意志作出的选择，如今她不再听从他人的指令，她只听从她内心的声音。其实周遭依然如此陌生，那些乘客无一不是面目模糊，不知何为，而此行依然吉凶未卜，千寻的身上并无多出任何的足以面对危险的装备，她依然一无长物，她所能倚靠的依然只有自己。然而那一刻千寻却没有了慌张与迟疑，她神情安祥，行动坚定，她很知道她究竟要什么，她究竟在做什么，她并不怀疑。她的眼中于是呈现出惊人的美丽：水泊波光闪动，落木苍翠绵延，灿烂的霞光映照着遥远的地平……
 其实，我们不难发现，那并不是一次陌生的旅行，相反，那只是一个缓缓推远的长焦距。当迈出离开原地的那一小步的时候，她挣脱了当下情境永不驻停的重负，她拥有了一个审美的距离。于是她看到了完全不同的风景。这时候，我们方才可以说，她成长了。
 当然，不难预料，在某个十字路口，命运可能再度将她推入泥沼，但是，那已经没有关系，擦干眼泪之后，深吸一口气，苦难和坎坷转瞬即会成为过去的风景。若我们能以一种发生后的眼界来看待当前迷惑我们的种种，也许我们就可以不那么迷惑，也许我们相反可以从我们所承受的那些之中获得一些什么。
 在你我的生活之中，那并不必要是一次实际的旅行，那极有可能只是在呼吸或者转身之间的事情。但是如果你处于那熟悉的周遭环境之中，不利于你从其中抽身，那么，你也不妨真的离开当下的情境，作一次轻快的短途旅行。去那些水土新鲜、莺飞草长的地方，你看到的将绝不仅仅只是沿途的风景。
 也许，人生终究是一程没有归途的远航，也许航行所带给我们的终究是苦大于乐，聚不如散，但是，我们却绝不仅只是被动的接受者。面对每一个命运的打击，人都以其最高的精神娱乐着自己。从旧时少年的离家修行，到释迦牟尼的出走得道，所有成长到最后总是一次旅行。当那段饱含清冽和忧伤的旋律在耳边飘荡起来，当千寻静静地坐在长座位上，面对空空落落的车厢，站台的钟声敲响，沿途的风景映照于她的脸上，也许我说不出那许多的字，我惟有满含热泪，在心底用一种极度婉转的声音轻轻吟唱。
"""

y1295124="""
世界反法西斯胜利60周年
　　1945-2005
　　
　　NO.00-【即将来临的黑夜】
　　一个普通的犹太人家庭在低声吟唱着圣咏曲，微弱的烛光渐渐熄灭，一缕白烟缓缓升起，慢慢变成火车轰鸣的烟雾…影片字幕：1939年9月，德国武装在两个星期内击败了波兰军队。下令犹太人登记全家人口，重新安顿集居到各大城市，每天有一万多犹太人从乡村抵达克拉科夫。
　　
　　NO.01-【优雅俊朗的企业家】
　　酒会中，伴随着悠扬的小提琴乐曲，高大俊朗的辛德勒(利亚姆.尼森 饰)优雅的抽着烟，望着不远处邻座的女子，眼光深邃。其实，他是在打探着女郎身旁的德国纳粹军官，做为一名德国企业家，辛德勒无时不刻不在寻找着挣钱的机会。
　　
　　NO.02-【充满魅力的辛德勒】
　　德国军官看着派去打探的手下居然和辛德勒坐到一块儿，于是亲自上前：“他在搞什么？”。辛德勒亲切的拉着他的手很绅士的说：“这种地方怎么能让女士没有护花人？”，并挽着女人的手说：“各位，男士伏特加，而女士呢？”。风度翩翩、出手阔绰，言谈举止极富感染力，这使得辛德勒短时间内和在场的德国军官们建立起了“亲密”的友谊。
　　
　　NO.03-【左右逢源的商人】
　　贵宾留席的主人，一名德国高级长官到来，看到这个场面，不解的问待应生：“那个人是谁？”。一会后，辛德勒和长官把酒言欢，并愉快合影留念。辛德勒的个人魅力非常吸引人，不光吸引女士，也包括男士。在交际场合的熟练老道，使的他在商场上也是左右逢源。
　　
　　NO.04-【临时的犹太人参议会】
　　德国士兵涌进波兰城市酋登拉特，大量的波兰犹太人在市政厅门前排队等候。影片字幕：“犹太人参议会，由二十四位被选举出来的犹太人组成，负责在克拉科夫执行伪政权的命令，包括分配劳役、安顿食宿、排解纷争等”。
　　
　　NO.05-【“我并不工作”】
　　辛德勒到临时参议会找犹太人史丹(本.金斯基 饰)商量合作开厂事宜，史丹问：“他们出钱，我出力，请问…你呢？”，辛德勒轻松的回答：“负责公司的公关、宣传，我的专长是形象设计，并不工作(Not work，Not work，说了两遍)，搞门面工夫…”，做为唯利是图的商人，他只关心如何快速、有效、安全的挣钱。
　　
　　NO.06-【犹太人的最后期限】
　　街道上全是流动的人群，影片字幕：“1941年3月20日，进入犹太人区的最后期限，44/91号布告建立了维斯拉河南岸犹太人封闭区，犹太人被强迫居住在这个关起来的区域，所有从克拉科夫及其附近地区的犹太人被迫离开他们的家，并被集中到一个只有16个居住方块的区域”。
　　
　　NO.07-【“再见，犹太佬！”】
　　一个个犹太家庭在德国军人的监视下，默默的收拾细软。街道上非犹太种族的孩子们用石块向犹太人扔去，一个小姑娘眼里充满了仇恨与轻蔑，嘴里大声的喊叫着：“再见，犹太佬！”，与此相对应的是，大多数犹太人选择了沉默。
　　
　　NO.08-【伪造的蓝卡】
　　德方对犹太人进行职业鉴别，某个大学教授面对德国军方抱怨说：“我教历史、文学怎么算不重要？”，好心的史丹连夜为他伪造了一份五金磨工的职业证明，在他即将被装上卡车运走前拉过他，交到他手里，教授违心的承认自己是五金磨工而获得象征着暂时生存的蓝卡。
　　
　　NO.09-【面试打字员】
　　辛德勒为他的德国珐琅工厂面试打字文员，前几个年轻漂亮的女子虽然打字技术差，他一再向前挪着身子，并幽雅的托着下巴“深情凝望”，其间还帮着一位行动笨拙的女子换行，可后面在某位年纪较大但技术娴熟的妇人面前，他却端坐着望向别处，丝毫没有任何兴趣，从这一侧面也说明了辛德勒的本色风流。
　　
　　NO.10-【“我更需要会计”】
　　辛德勒对史丹说：“家父曾说过，人生所需者有三：高明的医生、宽大的牧师、聪明的会计。前两者，我很少与其打交道，不过，第三者…”，言下之意是他身体健康、不迷恋宗教，但热衷于经商之道，辛德勒是个标准的商人。
　　
　　NO.11-【“那个人是独臂的，有什么用？”】
　　辛德勒工厂的效益蒸蒸日上，一天，史丹告诉他有个叫鲁荣斯坦的技师，想感谢他的录用。辛德勒出于礼貌会见，却没想到居然是个独臂的老人，于是他怒气冲冲的质问史丹：“那个人是独臂的，是吗？有什么用？怎么用？”…这时的辛德勒的确是个标准的商人。
　　
　　NO.12-【“我是个重要技工”】
　　工人们走在下班的路上，不料沿途被德国军人强迫铲雪，刚才向辛德勒致谢完后心情愉快、哼唱着歌儿的独臂老人却被微笑着拉过一旁，是的，两名纳粹士兵脸上带着微笑，独臂老人知道事情不妙，试图解释：“我是个重要技工，我是辛德勒的雇员…”，微笑的军人一枪击毙了他。睁大眼睛的老人脑后流出的血液浸染了雪地，雪是白色的，血却不是红色的。铲雪中的工人们没有人抬头，一切都是在平静中进行。
　　
　　NO.13-【“你叫什么名字？”】
　　工厂会计史丹因忘记带工作证而被装上火车，辛德勒前去营救，受到德国军人的阻挠，他先问记录员：“你是文员，叫什么名字？”，又问闻讯赶来的德军官：“你叫什么名字？”，德军官感觉受到了侮辱，轻笑着报了全名后反问他，辛德勒轻描淡写的说：“两位，万分感谢，我可以保证，月底，你们俩将调去南俄罗斯，再见”，然后继续寻找史丹。在辛德勒大叫着“史丹”的声中，记录员与德军官也同样卖力的喊相同的名字。这段戏拍的很讽刺。
　　
　　NO.14-【桌上的金牙】
　　车站货仓里，工人们正在挑拣着堆积如山的货物给其分类，这些都是火车上被运走的犹太人的，当然，这些对于它们的主人来说已经没用了，因为他们踏上的是一辆死亡列车，即将开往屠宰场……一名黄金鉴定师望着倒在桌上的一大堆金牙，面色呆滞，因为他知道，一颗金牙代表着一个生命的终结。
　　
　　NO.15-【明确的化分】
　　“犹太人城”：1942年冬天，克拉科夫犹太人区，波兰人与波兰犹太人这时已经被明确的化分开来。
　　
　　NO.16-【A区与B区的分别】
　　新来的司令官阿曼·歌德大尉(拉尔夫.芬尼斯 饰)在吉普车上听着下属解释：“这条街道将犹太区分成两半，右边，A区，公务员、生产工人之类；左边，B区，多余的劳工，老弱残疾…”，A区，B区，哪个会是天堂，哪个会是地狱？
　　
　　NO.17-【挑剔的德国司令官】
　　歌德大尉视察建造中的普瓦索夫集中营，挑中了没做过佣人的海伦做他的佣人，原因是：“别人的女佣我没兴趣，懒的矫正她那些陋习”。
　　
　　NO.18-【Today is history】
　　歌德大尉在广场发表了他的“就职演讲”：
　　“今天，是历史时刻，今天将长留青史，许多年后，年青人将以敬佩的心情谈起今天的事。今天，是历史时刻，六百年前，欧洲大瘟疫，死人无数，犹太人被指为祸端，当时的波兰国王，批准犹太人前来克拉科夫市，他们来了，源源而至，一车车行李，落地生根，发展起来，在企业、科学、教育、艺术等各方面…他们来时赤手空拳，一无所有，然后昌盛繁荣。六个世纪以来，犹太人，盘据着克拉科夫，你们不妨想想，由今晚开始，这半个世纪的事迹，将成为流言，可视为从未发生过…今天，是历史时刻”。
　　
　　NO.19-【屠杀前的准备】
　　画面中出现字幕：“1943年3月13日，准备屠杀犹太人”。事实上，入侵波兰后，战争的进程深入使得希特勒不再满足于驱逐、分隔犹太人，而想实行“彻底”的种族灭绝，于是，被称为“最后解决”的大屠杀开始了。除了党卫队特别行动队自身外，还有募招当地警察和反犹的极端民族主义分子，带头的还往往是些教员、医师或教士之流。他们的残暴比德国人有过之而无不及，不得不说是波兰人的悲哀，或者，是人类的悲哀。
　　
　　NO.20-【塞进面包里的手饰】
　　当穷凶极恶的德国士兵们咆哮着闯入居民楼时，在平凡的一个家庭里，母亲正把一些金银手饰塞入面包让家人各自吞进肚里。因为，她可能还在想着行动结束后不应该让家庭财产得到流失。
　　
　　NO.21-【死亡与微笑】
　　德国士兵一边将年迈的老者推到地上一枪打死，一边微笑着哄那因失去丈夫而痛哭的老妇人怀里的小孩子…他们是什么，是地狱来的魔鬼吗？
　　
　　NO.22-【“你差点儿打到我！”】
　　街道上，德国军人正在检查蓝卡，一个孩子由于看见父亲被德国兵大声训斥而“过份”害怕跑了出去，德兵抬枪欲射击，父亲拼尽全身力气阻挡，被当场打死。两名德兵架着他的儿子回来，砰的一枪击穿身体，就在他母亲的眼前……旁边的德国兵过去怒喝，观众还以为他会训斥杀害小孩子的行为，谁知他竟然高声指责同伙差点打到他---残忍之极，简直令人不敢相信自己的眼睛。
　　
　　NO.23-【善意的投毒】
　　诊所的大夫将毒药掺进水里喂垂死的病人喝下，随后德国兵闯进来向他们的身体扫射，但病人们已经安静的死去，医生们这么做是为了不让他们遭到痛苦。
　　
　　NO.24-【同样的年轻人】
　　诊所外的年轻医生哀求让年轻的女病人获得治疗，同样年轻的德国士兵没有丝毫犹豫一枪将女病人的头打烂，头颅迸出的鲜血和脑浆喷了医生一脸一身。
　　
　　NO.25-【“不，这里已经没有地方了”】
　　老妇人杜斯纳带着女儿趁乱逃到阁楼上，谁知躲在其中的人只允许她女儿丹卡一人下来，她百般恳求也不济于事，强烈的母亲天性让她忍住害怕，安慰女儿：“别动，留在这里不要乱闯…”，在女儿大声的叫喊声中她看着地板慢慢的合上。
　　
　　NO.26-【二根手指的军礼】
　　一个年青人从下水道钻出来，却碰上德军，他急中生智，装做收拾散落在街道上的行李，并用二根手指向歌德上尉敬礼，引得刽子手们一阵狂笑，暂时侥幸躲过一劫。
　　
　　NO.27-【“片刻的生命，终归是生命”】
　　被小孩儿亚当藏在楼梯下的杜斯纳，却看见本已“安全藏起”的女儿跑出来奔向她的怀里，刚刚经历了生死离别的母女二人紧紧的搂在一起，母亲说：“片刻的生命，终归是生命”。
　　
　　NO.28-【黑与白间的一点红色】
　　在山头上骑马驻足的辛德勒静静的看着下面异常混乱的街道，在黑白颜色的人群中，一个衣着红色的小女孩儿在其中快速的毫无目的穿梭着。值得一提的是，全片只有两种色调，黑与白，所以，这个红衣小女孩儿显得特别的醒目。在由童声合唱组成的低沉背景音乐中，小女孩儿身上的红色代表着生命，尽管它看上去是那么的脆弱。
　　
　　NO.29-【节省子弹的好办法】
　　大楼前，德军将几个犹太人排成一串，一枪就全部打死，充分展现了帝国精英们杀人的高效率性。山头上的辛德勒望着这一切，脸上以往的优雅被莫名的表情所占据，眼晴里尽是茫然。
　　
　　NO.30-【诊听器】
　　夜里，德军找来大夫，持医用诊听器来勘察楼层夹缝中是否有人藏匿……诊听器本来是给人以生的希望，在这里，却带来了死亡的信息。
　　
　　NO.31-【“完美的合弦”】
　　经过搜查，德军发现了白天躲在窗帘后的一群犹太人，冲上去一阵扫射，黑暗楼道里闪着刺眼的白光，那是死亡之光。就在这充满了血腥味道的人间地狱，一名军官竟然“饶有兴致”的弹起了钢琴，琴声急速而短促，和密集的机枪扫射声构成了一道“完美的合弦”，两个德国兵闻声而来，却讨论起弹奏的是巴克还是莫扎特。静静的城市，只有射击声与钢琴声来回作响…静静的城市，死一般的城市。
　　
　　NO.32-【歌德上尉的晨练】
　　早晨起来的歌德上尉光着上身，居高临下望着操场上列队的犹太人，拿起狙击枪将空地上一名妇女击毙，没有任何理由；四周观望后，又将台阶上的一名妇女击毙，同样，没有任何理由，射杀犹太人对于歌德上尉来说，就像林中打猎时射杀兔子或獐子，没有什么分别。操场上的工人快速的干起活来，唯恐下一个目标会是自己。
　　
　　NO.33-【“可能是撞针出了毛病”】
　　普瓦索夫集中营：金属加工厂。
　　歌德上尉视察工作进度，走到一个老人身边问他是做什么的，老人回答做门铰。他要求老人立刻做个门铰给他看，并掏出手表计时，老人不敢怠慢，快速熟练的做完并看着上尉期待表扬。歌德上尉先是赞赏，然后指着桌上稀少的门铰说：“非常棒，但是我有点不明白，你从今天早上六点起就一直工作，但只有这小小一堆的门铰”，老人没有争辩，他闭上眼晴像小鸡一样被拖出车间，歌德上尉用手枪对准跪在地上的老人头部射击，却因为手枪失灵而再三重试，无奈好像中邪一样，换了几次都无法正常发射。到这儿，仿佛是在上演一出标准的喜剧，但是我想，没人会笑的出，不管口中还是心里。
　　一个即将被处死的老人歪着脖子跪在地上，没有任何反抗，身旁要取他性命的人却在讨论着如何解决杀人武器的技术故障：“可能是角杆弯曲所致…”…“检查一下撞针…”…“可能是染了铀…”，影片在这里将黑色幽默玩的令人触目惊心，但是，只见黑色，不见幽默。
　　
　　NO.34-【Him！】
　　歌德上尉训在操场上斥问是谁偷的鸡，没人敢回答，于是他随便拽出一人枪毙，正当他要杀第二人时，一个小孩低头出列，歌德问他是谁时，出人意料的是，这个哭泣的孩子一指地上的死人大声喊道：“是他！”…真是聪明。
　　
　　NO.35-【“他坏的可爱”】
　　史丹因介绍没有技能的老年人到厂里工作，辛德勒知道真相后大为光火，他怒斥史丹道：“人死在所难免，他想杀光所有人，我有什么办法？将所有人送来？行得通吗？送他们去辛德勒那里去，统统送去！他那处是避难所，不是工厂…你知道吗，这很危险，非常危险！”，这时的辛德勒还完全不把犹太人的生死放在眼里，他只关心自己的安危及工厂的效益，并为歌德的所做所为辩护，称歌德“完全是为这个营着想”、“责任重大”、“战争把人邪恶的一面露了出来”、“他坏的可爱”。
　　
　　NO.36-【史丹的反驳】
　　史丹面对辛德勒的冲天怒火，平静的诉说他自己听贝基说的一件事：某天，一个人越狱，歌德上尉将越狱人同营的人排成一队，他先杀贝基左边的人，然后枪杀右边的人，将列队的人通通杀掉，25个人，整整25个人，镜头前的歌德上尉面目狰狞，脸上沾满了飞溅血迹……辛德勒听到这些，若有所思。
　　
　　NO.37-【This…is…P.O.W.E.R！】
　　上尉别墅，夜晚酒会后的辛德勒与歌德上尉一起在阳台闲聊，歌德因饮酒过量摔倒在地，辛德勒没有去扶，歌德蹒跚的爬起来坐在椅子上问他：“你从来没喝醉，显示出你有非凡的控制力，能控制，就有权力，控制力就是权力”，辛德勒沉思片刻，说：“杀人不是权力，是正义，与权力不同，权力是…有足够理由去杀一个人，但却不去杀，而是赦免。”，歌德盯着他：“我认为你喝醉了”，辛德勒没有理会，靠近他凝视：“歌德，这就是权力，这…就是…权力”。
　　
　　NO.38-【“算了吧”】
　　歌德在马厩发现服侍他的男孩失手将马鞍掉在地上，大怒后居然温和的说：“算了吧”，随同的史丹却面带诧色，他不敢相信“暴君”般的歌德会如此“宽待”一个冒犯他的下人。
　　
　　NO.39-【“告诉她不要再吸”】
　　操场上，一名德兵正拽着一位妇女的头发欲拉到空地处死，只因为她工作时吸烟，路过的歌德迟疑了一下，说：“告诉她不要再吸”，放了生路，这名德兵在其走后大摇其头，他也不明白司令官今天是抽什么疯了，往常抬手就是一枪，现在却像个善人。
　　
　　NO.40-【“我赦免你”】
　　仆人男孩因擦不干净歌德浴缸的污迹而胆颤心惊，歌德告诉他下回用浓酸液，然后说：“走吧，可以了，我赦免你”。歌德盯着着镜子中的自己重复刚才的命令：“我赦免你”。看来，辛德勒昨晚上的话似乎起了作用。
　　
　　NO.41-【歌德上尉的“赦免”】
　　被“赦免”的小男孩走在操场上，身边响起了枪声，但没有打中，是歌德，他在用这种方式警告他的仆人吗？这时，拿着帐本的史丹在前行中突然身子一震，走过后的空地上，刚才被“赦免”的小孩已经躺在血泊之中了。相信这一幕会给大家带来极大的震撼，就在歌德逐渐改变处事方式，观众们也在改变对他的看法时，这一枪，把观众们对法西斯那海市蜃楼般的希望彻底打碎了。
　　
　　NO.42-【歌德上尉的自述】
　　在地下室，歌德找到女仆人海伦，并向她诉说：“原来你躲在这里来避开我，我是来告诉你，我是巧手的橱具师、熟练的仆人，是真心话。战后，你要写书，我会…乐意替你写。听到楼上大家在寻欢作乐，这里必然显得寂寞。”、“有时，我们俩都是寂寞的”，他似乎像个温温而雅的绅士，向情人述说心曲。但接下来，他又变回了平时的歌德，大骂海伦：“不，我怎么可以同情你？你这个犹太婊子，几乎引诱我上钩…”，随后疯狂的殴打海伦。歌德自知已经爱上了海伦，一个犹太女人，一个像蛇、鼠、虫、蚁般的犹太婊子，他找不到方向，只有籍着殴打她来发泄，狠狠的发泄。
　　
　　NO.43-【荒谬的传闻】
　　女工寝室中，一个女工在叙述她所听到的在集中营里发生的骇人听闻的故事：“…火车抵达后，人们被赶了出来，在两个货仓前列队。一个货仓写着“衣帽室”，另一个则写着“贵重品”。他们在那里脱掉衣服，一个犹太小孩用绳把他们的鞋子绑在一起，士兵剃光他们的头发，说头发是用来制作东西给潜艇用，人们沿着一条大走廊，被推进密室，门口画上大卫星，并写着“沐浴及氧气室”，党卫军发给他们肥皂，叫他们深呼吸，说是有助于消毒，然后，放出毒气…”。这时，她上铺的一个女工问为什么要给他们肥皂，她回答到：“用来哄他们进去的…”，但这时，很多女工对此持怀疑态度，并不相信身为“极其重要”的劳动力的她们会遭到如此下场，是“荒谬”的。
　　
　　NO.44-【“腾出地方来”】
　　某天上午，广播通知全体人员到操场集合，因为刚从匈牙利运来了一批新的犹太人，营中准备检查身体状况，以便把患病者抽出，“腾出地方来-(歌德语)”。
　　
　　NO.45-【操场上的奔跑者，为了生存而奔跑】
　　操场上放送着舒缓的音乐，身着白色医服的大夫开始“工作”，全营人不分男女，均脱光了衣服在操场上跑圈，德军看到身体孱弱者就马上拉出来放到另一旁。面对屏幕中满场奔跑的裸体，我的心中没有一丝一毫的色情感，只有彻骨的寒意。
　　
　　NO.46-【特殊的化妆品】
　　寝室中的几个女工，为了不显得太虚弱，用针刺破手指，把血染在惨白的脸颊上使其“看起来红润一些”。
　　
　　NO.47-【法西斯的催眠曲】
　　这时，德方换了一张唱片，耳畔传来的是一首祥和、温柔的女声独唱，低吟的声调听起来就像是慈祥的母亲在轻轻哄着自己的宝贝入睡，营中所有的小孩子应声合唱着被带了出来。他们手牵着手，天真无邪的笑着，井然有序的走上运输车，他们这次不是去温暖的房间睡下午觉，而将会被带到奥斯威辛…
　　
　　NO.48-【大喜大悲的落差】
　　在身体检查中侥幸未被抽出的女工们脸上洋溢着发自内心的喜悦，她们轻笑着穿上衣服、互相祝贺着，场地中升腾着一派欢乐的气氛……但不一会儿，她们却发现自己的孩子们在货车上高兴的向自己挥着手示意，母亲们顿时面如死灰，大声叫嚷着、哭喊着奔向汽车、奔向自己的孩子，但，无济于事…这一切仅仅发生在短短的几分钟里，大喜大悲的巨大落差，仅仅发生在短短的几分钟里。
　　
　　NO.49-【粪坑里的孩子们】
　　小男孩奥利趁乱逃出，四处找寻但找不到可以藏身的地方，只好钻进厕所的粪坑里，就是在这个极其肮脏的地方，还躲着四五个小孩。孩子们稚嫩的脸上沾满了污秽的粪水，奥利望着头上的蓝天，那肮脏的空气中还在回响着慈母般的音乐。
　　
　　NO.50-【“残忍”的辛德勒】
　　在火车站，辛德勒看到火车上闷热难奈的人们，向歌德提议用水管向火车喷水取乐。歌德一时没弄明白，以为辛德勒是在虐玩囚犯，还取笑他：“辛德勒很残忍，你给他们希望，不应该那样做，残忍！”。
　　
　　NO.51-【歌德上尉的异样感觉】
　　“残忍”的辛德勒亲自拿着水管向火车上可以喷洒的地方喷洒着清水，车内早已闷极的人们拼命挣扎着享受着这次清凉，最后一次清凉。当看到辛德勒嘱咐火车的德兵每次停车给囚犯们喝水解渴的时候，军官们停止了调笑，歌德望着辛德勒，隐约的感到了什么。
　　
　　NO.52-【天空中落下的灰尘】
　　在大街上行走的辛德勒用手拈起从天上落下散在车上的“灰尘”，这并不是普通的“灰尘”，而是焚尸后从烟筒冒出的骨灰。影片字幕：“1944年4月，休伊瓦高尔加。D处命令歌德挖出尸体焚化，在普瓦索夫和克拉科夫犹太人区惨案中被杀害的犹太人超过一万”。犹太人们负责挖掘尸体具体工作，如山的尸堆里可能就有他们的朋友、亲戚。歌德告诉旁观的辛德勒，刚收到命令，二、三十日后将会把营区内的所有人送到奥斯威辛集中营，辛德勒听到这里，心中忽然滑过一个念头。
　　
　　NO.53-【生命的颜色】
　　黑白镜头中，一辆运尸车上赫然出现了影片开始那个穿红衣的小女孩，辛德勒看在眼前，捂着嘴悲痛万分，这让他坚定了刚才心中产生的念头！
　　
　　NO.54-【More、More…】
　　工厂里，整夜未眠、眼睛红肿的辛德勒开始实施他的计划，让史丹打印他念出的名字，“More、More…”，辛德勒不断的念着记忆中的人名，打字机飞快的印出铅字，“300、450、600、800…”……这就是著名的“辛德勒名单”，所有的代价就是送给歌德一箱箱厚重的钞票。
　　
　　NO.55-【“这名单…就是生命”】
　　辛德勒因资金临近耗完而让史丹终结名单，史丹喃喃的说：“这名单太好了，这名单…就是生命！”、“名单外的世界，是深渊”。
　　
　　NO.56
　　-【辛德勒的名单】
　　在辛德勒的名单中列出的人们纷纷到操场上报名：
　　杜斯纳一家：朱迪、朱纳、当娜、查也；
　　诺士纳一家：亨利、温茜、利奥，儿子奥利；
　　玛莉亚·米雪；
　　占·路华；
　　马加·胡朗；
　　林柏·米高；
　　史丹；
　　莉贝嘉、约瑟·鲍；
　　蕾莎·纳士·鲍、威廉··纳士·鲍；
　　杰克·利瓦杜；
　　露西·法本、亚志；
　　莎拉、菲卓·费舍尔；
　　米特·彭巴；
　　波特、美娜·费化堡；
　　多瑞·何路；
　　阿当·里维；
　　马素·高拔；
　　依素·奇士坦；
　　艾沙·阿曼；
　　玛利·根堡；
　　艾丽·陆定；
　　爱华·希文；
　　艾玛·路堡；
　　杰迪·苏克文；
　　海伦·凯丝；
　　……
　　这些都是不幸中的幸运者，他们被以男女分类，运往兹维陶·布伦利兹·捷克斯洛伐克-----那是奥斯卡·辛德勒的家乡。
　　
　　NO.57-【“欢迎光临布伦利兹！”】
　　辛德勒在站台上欢迎先抵达的男工人们说：“装载妇女的列车，已离开普拉绍夫，即将抵达。我知道你们旅途劳顿，但步行不远，就到达工厂…，欢迎光临布伦利兹！”
　　
　　NO.58-【一个孩子的“割喉礼”】
　　这时，在女工们乘坐火车上的海伦却无意中瞥见雪地中的一个孩子向她敬“割喉礼”，到站后，已是深夜，刚才还讨论顿肉、土豆的妇女们发现到了一个陌生的地方，那里没有欢迎她们的奥斯卡·辛德勒，也没有顿肉、土豆，只是荷枪实弹的德国兵及恶狠狠的狼狗。
　　
　　NO.59-【冒着白烟的大烟筒】
　　她们排成队，四处寻找名单登记台，却发现远处发出巨大轰鸣声响的……冒着滚滚白烟的大烟筒，她们来到了…奥斯威辛集中营，犹太种族的“最后解决”处。
　　
　　NO.60-【“淋浴室”里的淋浴】
　　更为不幸的是，她们这次遇到了以前那个“极其荒谬”的传说，同样，她们在那里脱掉衣服，一个犹太小孩用绳把他们的鞋子绑在一起，士兵剃光他们的头发，人们沿着一条大走廊，被推进密室，门口画上大卫星，并写着“淋浴及氧气室”。突然，室内灯光全部熄灭，屋里顿时发出绝望的喊叫。黑暗中的妇女们一个个因恐惧而面容扭曲，母女、姐妹们紧紧的拥抱在一起，她们在静静的等待，静静的等待着毒气的到来……但没想到的是，是淋浴，居然真的是淋浴！人群中发出欢快的笑声，伴随着哭泣的笑声。
　　
　　NO.61-【下一拨人】
　　无疑她们是幸运的，出来后，却看到另外一大群人走向那里，死一般的夜里，高高矗立的焚尸炉继续冒着白烟。
　　
　　NO.62-【“她们可以打磨子弹！”】
　　经过辛德勒用重金贿赂德政高官，她们才得已重新踏上列车，但德兵不允许小孩上车，母女被强迫分离的场面令人感到撕心裂肺。
　　
　　NO.63-【走在工人中间的辛德勒】
　　费尽周折，妇女们终于回到工厂，在厂里的大道上，舒缓的音乐中，辛德勒与她们走在一起，肩并肩的走在一起，这个场景非常感人。此时的辛德勒已经不是一个标准的商人了。
　　
　　NO.64-【“你入狱、我收钱！”】
　　辛德勒向德国兵说到：“根据W部门条例，无端杀害工人是违法的。根据企业赔偿基金，工人遭到滥杀，我有权要求赔偿。如果胡乱杀人，你入狱、我收钱！，这是办事规矩，因此，这里不准即时处决，生产不可受到任何干预，为确保，没有我的批准，卫兵不得进入工厂”。为了犹太人，而不惜与德国军人谈规则，此时的辛德勒的确已经不是一个标准的商人了。
　　
　　NO.65-【辛德勒的开销】
　　影片字幕：“在七个月的时间里，辛德勒的布伦利兹军火厂充分运转，却都是无产品的模范。与此同时，他花了数百万德国马克以供养他的工人及对德国官员行贿，倒致了他濒临破产边缘…”…
　　
　　NO.66-【收音机里传来的消息】
　　工厂的工人们与德国官兵一起默默的听着收音机播送的特别报道：“昨天早晨，凌晨2:41，在艾森豪威尔将军的总部，德国的祖度将军，签署了无条件投降条约，将德国在欧洲一切的领土、领空、领海移交欧美联军及最高苏维埃指挥。德国战事因此结束！”，1945年，德国法西斯无条件的向盟军投降。
　　
　　NO.67-【狡猾的辛德勒的演讲】
　　辛德勒在工厂对着车间里的所有工人及台阶上持枪的德国军人们发表演讲：“刚听到宣布，德国无条件投降，今晚午夜，战争将结束。明天，你们着手找寻生还的亲人，大部分人…你们不会找到。经过六年的杀戮，受害者举世哀悼，我们得以生存。你们很多人来向我致谢…向你们自己致谢吧。感谢你们无畏的史丹，以及其他随时面对死亡的人”。
　　辛德勒顿了一下，接着说：“我是纳粹分子，军火生产商，努力劳力的剥削者，我是……一个罪犯。到午夜你们获得自由，我被追缉，我会和你们相聚至零时五分，届时，请恕我失陪…我必须亡命去了。”
　　辛德勒望着台阶上的德国军人，平静的说：“我知道你们接到领导人辗转传来命令，清除所有的工人，现在大可下手，他们都在这里，这是你们的机会…”“否则，你们可以离去，回家去做一个人，而不是一个凶手”…几分钟后，德国士兵一个个沉默的离去。
　　影片这时闪过一个不易察觉的镜头，辛德勒对惊愕的史丹偷偷使个了眼色，然后舒了一口气，狡猾的商人，“狡猾”的辛德勒。
　　
　　NO.68-【由德国商人提议的默哀】
　　辛德勒对工厂工人提议：“为纪念你们无数的受害者，我请求大家，静默三分钟…”，场地上传来了悲怆的歌声。
　　
　　NO.69-【卓利的金牙】
　　车间里，一群工人不住的向一个名叫卓利的工人致谢，原来是他将自己的金牙拔下来化成戒指，准备献给辛德勒。
　　
　　NO.70-【“凡救人一命，即救全世界！”】
　　深夜，收拾好行装的辛德勒离厂前，接受了工人递上的可证明他无罪的工人联名担保书，然后，史丹送给他那枚用金牙打造的金戒指，并说到：“希伯来文，取自《塔木德》经书，意为“凡救人一命，即救全世界！””。
　　
　　NO.71-【哭泣的辛德勒】
　　辛德勒戴上戒指，没有向史丹致谢，他眼含着泪水，对史丹说：“我或许可以多带些人出波兰，或许可以多带些…”，史丹说：“拜你所赐，1100人得已生还…”，辛德勒：“我当时多赚点钱就行…”，他自嘲似的笑了笑，“我太挥霍了…”，接着，他从笑转为哭泣：“只要我…”，史丹说：“你所救人的后代，也蒙你的恩”，辛德勒指着自己的汽车说：“这辆车，可以换回十个人的生命，我要来干什么？十个人…”，取出领针：“这领针，两个人，黄金造的，两个人…”，他大声痛哭着，像个孩子一样，工人们上前去抱住辛德勒，紧紧的抱着他。
　　-【财注：这部影片，从头到尾，笔者始终努力保持一个“冷静”的心态观看，但是到这里，每次到这里，总是禁不住的泪流满面，尽管我不清楚是为了辛德勒、劫后余生的工人们还是这场战争…】
　　
　　NO.72-【影片的小玩笑】
　　早晨，镜头里出现了躺了一地的工人，七零八落，使人怀疑是德军反悔，夜里返回将其杀害…影片在这里开了个小小的玩笑，却着实吓人不轻，随着一名苏联士兵的到来，工人全起来了，他们原来是在露宿。
　　
　　NO.73-【“波兰还有犹太人吗？”】
　　年轻的苏联士兵大声的喊到：“你们已经被苏联军队解放了！”，史丹问他波兰还有没有犹太人，苏联士兵沉寂了半晌没有作声。
　　
　　NO.74-【久违的市镇】
　　当工人问苏联士兵哪里可以找到食物时，他一指不远处，“那边不就有市镇吗？”随着轻松的口哨声，白云下的旷野中，工人们向着久违的市镇走去……
　　
　　NO.75-【歌德上尉遇到的麻烦事】
　　穿插的镜头中，集中营司令官，歌德上尉整理了一下头发，他挣了挣脖子上的绳索，费力的吐出一句“希特勒万岁”，行刑的士兵们想踹去他脚下的木凳，却半天没奏效，折腾了半天，才踢掉，歌德被应声吊死。回想影片中间，歌德也曾遇到过这类麻烦事，不过那时他是行刑者……
　　影片字幕：“阿曼·歌德在拜德托尔兹疗养时被捕，他在史拉科夫因反人类罪被处以绞刑”。
　　
　　NO.76-【耶路萨冷的纪念】
　　影片字幕：“奥斯卡·辛德勒在战后婚姻破裂，事业上也屡受重创。1958年，耶路萨冷的浩劫纪念馆宣布他为义人，并邀请他在义人大道上种了一棵树。”
　　
　　NO.77-【彩色的画面】
　　影片字幕：“此树仍然在那里生长着…”。
　　旷野中行走的人们黑白群像渐渐变成了彩色，这是影片第一次出现了全屏的彩色画面，阴沉了近三个小时的银屏陡然放出绚烂的光彩，象征着受尽苦难的犹太人们来之不易的自由。影片的这处出人易料的色彩变化，体现了制作者非凡的构思，同时带给观众们极大的艺术震撼力。
　　
　　NO.78-【辛德勒犹太人】
　　奥斯卡·辛德勒的墓碑前：
　　电影中各个角色的扮演者与原型一起携手来为他祭奠。
　　按出场顺序，他们分别是：
　　亚奈克·德拉斯那；
　　丹卡·德拉斯那；
　　莫德塞·吾尔堪；
　　叶萨德·霍罗维奇；
　　钮西娅·霍罗维奇；
　　约瑟夫、里伯卡·保；
　　奥利克·罗斯那；
　　曼赛·罗斯那；
　　亨利·罗斯那；
　　里奥普尔德·罗斯及其妻子海伦；
　　米拉·塞费莱伯格；
　　里奥普尔德·塞费莱伯格；
　　杰哈克·斯坦太太；
　　海伦·希来奇；
　　……
　　这时，影片中出现了一位坐着轮椅的白发苍苍的老妇人，她面容很安详，字幕介绍：“艾米莉·辛德勒太太”……
　　前来祭奠的人络绎不绝，排着长长的队，他们全都上了年纪，却没有一点声响，安静的排着队…
　　……
　　影片字幕：
　　“今天的波兰只剩下不到四千活下来的犹太人，有六千以上辛德勒犹太人的后裔…”
　　
　　NO.079-【奥斯卡·辛德勒】
　　影片的结尾，在放满象征着感激的石块的奥斯卡·辛德勒的墓碑上，一个人轻轻的将一束花放在上面，放在辛德勒的名字上面，远景中看去，一个衣着黑衣、身材高大的人默默的驻留在那里，是他，奥斯卡·辛德勒，永远活着的奥斯卡·辛德勒……
　　
　　-----------------------------------------------------
　　【资料】
　　《辛德勒名单》是美国著名导演史蒂芬.斯皮尔伯格于1993年拍摄的一部轰动世界的伟大作品，深刻地揭露了德国法西斯疯狂屠杀犹太人的恐怖罪行，以其极高的艺术性成为1994年全球最为瞩目的一部影片，其思想的严肃性、非凡的艺术表现力都达到了几乎难以超越的高度。
　　影片获得了金球奖最佳影片奖和最佳导演奖，并获得了美国导演工会奖。在1994年第66届奥斯卡金像奖中，《辛德勒名单》一片更是毫无争议地夺得了最佳影片、最佳导演、最佳改编剧本、最佳艺术指导、最佳摄影以及最佳电影剪辑等6项金像奖。
　　作为犹太人的斯皮尔伯格，谢绝了片酬并将个人所得全部捐献给美国大屠杀博物馆。
　　------------------------------------------------------
　　
　　整部影片时间长达3小时15分钟，将近两个标准商业片的长度，可是，并没有让人感到分毫的沓长与拖拉，因为其中的一个个真实的片段深深震撼着观众的心灵，对我亦是如此。
　　
　　以上是我在其中遴选出的79个难忘的场景，有屠杀的残酷，也有感恩的激动，事实上，看过本片的读者们会觉的电影中的每个场景，或许都可以称为经典。
　　
　　在本文的最后，我想特别说一下留在脑海中至今难忘的一幕：
　　
　　NO.080-【“请记住，我才二十三岁”】
　　那是在影片的前面，刚到集中营上任的歌德大尉听到有人大声喊：“拆掉它！”，手下人报道：“她是工程师，说地基造错了，我已经告诉她是营房，不是大酒店。”，女工程师急切的过来解释说：“整个地基必须砸掉，再倒水泥，否则，营房的南端必然会下沉。先下沉，然后倒塌”。歌德大尉问她：“你是工程师吗？”，女工程师自我介绍：“是的，我叫丽达，在米兰大学修学工程”，歌德大尉说：“啊，受过教育的犹太人，就像马克思…”。他顿了一下，接着说：“枪毙她！”。
　　
　　女工程师感到不可思议：“长官，我只是职责所在”，同样感到不可思议的手下也为她辩解：“但她是建筑的主管…”，并拉过她准备关进牢房，但歌德大尉不动声色的重复命令：“照我的命令，枪毙她！”…
　　跪在地上的年轻女工程师面无表情的说：“杀绝我们没那么轻易…”，砰的一枪，她登时一头扎到地上，一个年轻的生命没有任何准备就此毙命。
　　
　　【财注：在这之前，小时候我看过很多革命军事体材的影片，在记忆中，好人死去的时候，似乎要比生存还要费一番劲，通常是这样的。但在这里，人的死亡就在一刹那间发生，没有挣扎，哪怕一点点的挣扎…所以，这个镜头始终深深的印在我的脑海中，至今难忘。
　　
　　熟悉或者不熟悉这段历史的朋友们可能会听说过这么一个故事：
　　
　　在苏联的乌克兰杜布诺镇，有个德国工程师赫尔曼·格瑞比特看到：卡车送来的犹太男人、女人和孩子无言地脱掉衣服，按外衣、内衣、鞋和帽子分别推放，其中鞋堆足有上千双。然后一家人一家人互相拥抱吻别。一个八口之家，有祖母，五十多岁的夫妇和一二十岁的五个孩子，满头银发的祖母抱着一周岁的小孙子唱起一支犹太古歌。低声细语的告别后，二十多个赤裸的犹太人被枪托点出走进大坑，其中一位黑头发的漂亮姑娘指着自己对他说：“请记住，我才二十三岁。” 】
　　
　　----------------------------------
　　第二次世界大战中
　　德国纳粹对犹太人的大屠杀是人类历史上最惨烈的种族灭绝灾难
　　纳粹用“死亡坑”、“死亡营”等大批量、集中的手段屠杀了五百八十二万犹太人
　　使欧洲犹太人骤然减少了二分之一，世界犹太人减少了三分之一
　　最残酷的奥斯威辛死亡营用毒气室杀害了一百万人

"""

y1292722="""

题记
一个特殊的时代造就了[泰坦尼克]。今年11月，是[泰坦尼克]十周年，我们郑重其事回头打量，发现它在商业和文艺领域的巨大成功绝非个案这么简单。尽管就连当时华尔街分析人士也认为，若这部耗资两亿的电影成功，势必把好莱坞带进“高投资、高风险”的龙潭虎穴。

但事实是，如果以1997年的[泰坦尼克]为节点盘点前20年和后10年，会发现，97前延续许久的纯明星制已经渐露疲态，之后混搭ＣＧ和明星的大片利刃开始所向披靡。这自然跟电脑技术成熟和全球市场一体化密不可分，恰好1997年前后，中国开始融入全球文化消费品市场——以1994年中影集团开始大片引进为标志。

表面上，是[真实的谎言]、[空军一号]之类擦亮了影迷的眼睛，但仔细想想就会发现，真正校准大片商业和文艺标杆的电影，非[泰坦尼克]莫属。不仅因为票房，各种延伸品排山倒海地涌来，更让国人首次见识电影产业的惊人威力。

更为重要的是，在国产大片年年见面的今日今时，回头再看[泰坦尼克]，才发现所谓影人勒紧裤腰带探索多年的经验，十年前，就已经有人做到了近乎完美，不仅赚得票子和眼泪，赢了口碑，而且承载了整整一代人的记忆和青春。

一个传奇的诞生
话说很久很久以前，有一个小名叫吉姆的加拿大人，由于拍过[终结者]系列、[真实的谎言]等几部叫好叫座的大傻片，一时间呼风唤雨、拥者成众。私下里，这个吉姆还是一潜水发烧友，一直对八十多年前沉于大西洋底的一艘破船倍感兴趣，曾潜下去拍了几个片断，便兴致勃勃想要搞成电影，这时有人出了个“馊主意”：纪录残骸多没劲，我们还原它的辉煌，来它一个催人泪下的沉船故事!

吉姆一听言之有理，立即禀报了上级，上级一见吉姆大导都这样激动，我们岂有不掏钱之理？因此，一个叫二十世纪福克斯和一个叫派拉蒙的，联手凑了1亿3500万美元的份子，拿来交给这位吉姆尽情败坏，于是一部电影就此开工，它的名称几经更改，最终定为[泰坦尼克]。

电影涅磐
让我们来到1997年5月，彼时仍处狂拍阶段的[泰坦尼克]北跑加拿大、南奔墨西哥，上窜下跳鸡飞狗叫，不仅把1亿3500万银子花了个精光，越看越不靠谱的卡梅隆还狮子大开口，让公司再度追加拨款，加到史无前例的两亿。

更要命的是，影片后期制作无限延长，原定暑期上映基本无望。28日，派拉蒙主席罗勃·佛里德曼亲自宣布，影片上映日期从7月2日延至12月9日，并称：“做这个决定很难，意味着我们先期预计的供求关系不再平衡。”但是派拉蒙“不平横”的不过是小头，他们只投了6500万已深感肉痛，而二十世纪福克斯已经扔进去了两倍这个数字……

华尔街的专家特别计算了一番，结论是此举将导致影片收入骤减、血本无归。

10月，连福克斯自己人都公然喊出，影片票房前景将是“一场不亚于泰坦尼克号沉船本身的灾难”。11月，关于败家导演卡梅隆无节制花钱的争论仍如火如荼，当月[泰坦尼克]在东京电影节上首映亮相，被媒体们幸灾乐祸地形容为“场面冷清、门可罗雀”。12月19日，定有三部重量级影片同时亮相：[007之明日帝国]、[捕鼠记]和[泰坦尼克]，对于三者谁能拔得票房头筹，平日惯于坐而论道的影评人们竟然集体沉默，对于结果毫无把握。

[泰坦尼克]终于揭开神秘面纱后，媒体评论纷纷出炉，虽然《今日美国》拍手叫好，《纽约时报》称之为“多年来唯一一部堪与[乱世佳人]媲美的杰作”，但以《洛杉矶时报》和《华盛顿邮报》为首的大多媒体并不感冒，而且口径无比统一：这电影真他妈值两个亿吗？

算了，先让影评人见鬼去吧，来看看观众怎么个反应。周一票房数字出炉，结果仍然让人灰心——三天累计收入2760万，还不及前一周[惊声尖叫3]的3300万，而后者的成本仅是它的八分之一。福克斯的发言人连忙说，我们在海外还赚了500万呢，当即被人传为笑柄。这一天，福克斯的高层也许在想，我们终于创造了一部比[埃及艳后]更臭名昭著的赔钱电影——枪击和跳楼，哪种死法更体面？

只有始作俑者——自愿降薪垫钱的詹姆斯·卡梅隆不以为然，他在等待奇迹的出现。

奇迹降临人间
奇迹真的发生了。[泰坦尼克]第二周全周狂收了6000多万，第三周更高达7000多万，实现了开今辟古的票房逆增长异象。第二年1月，大家很高兴地发现[泰坦尼克]海外票房果然不俗，因而为其成绩仅仅低于高不可攀的[独立日]而弹冠相庆——显然，他们太容易满足了。

影片继续以每周不少于2000万的票房收入坚挺着，1月27日，《洛杉矶时报》小心翼翼地说，[泰坦尼克]很可能成为影史票房最高的电影，人们对此将信将疑，仍在拿史上某某影片来类比。但是三月以后，全世界人类对[泰坦尼克]一刻不停的票房长势终于彻底麻木——这个星球上，再也没有被成为电影的东西可以与之相比了。

[泰坦尼克号]就这样应全世界影迷哭着喊着要看的需求，冬春夏秋、不知疲惫地行驶了长达281天，创下北美上映天数之最。更骇人听闻的是它的终极票房：美国国内6亿，全球18亿——这个数字什么时候才能被超越？我们等不到了，让上帝去等吧。

堵住学院派的嘴
单仅票房创造的奇迹，似乎仍不足以确立[泰坦尼克号]永垂影史的地位，因为更多的桂冠尚未加冕，更多的符号尚未确立。

身属电影这种重看率极低的媒介，长达三个多小时的[泰坦尼克]回头率却比美女都高，一般观众重看两三遍竟算稀松平常，时代广场上一位正排队买刚发行的影片录象的女孩接受采访时，声称自己在影院已经足足看了14遍。影片的原声大碟在未得奥斯卡之前，已经卖出了百余万张。

1998年初的整个地球，处处弥漫着[泰坦尼克]的悲壮气息，影院里泪流成河，汇起来足够让卡梅隆再拍一部，如果你想从这些个个肿着眼睛、拧着手帕出来的观众口中得出对影片的冷静评价无疑是白日做梦。不少起初一度等着看热闹的影品界人士，这会儿也开始纷纷归顺，熙熙攘攘地叫好起来。

这时，一切只等待向来在清高与媚俗之间摇摆不定的奥斯卡来终极决定。二月，学院评委对今年风格给出明确答案——最具人气的[泰坦尼克]夺得令人咂舌的14项提名，与影史奥斯卡提名纪录保持者[彗星美人]持平。

1998年的另外几部提名电影是[尽善尽美]、[洛城机密]、[心灵捕手]和[一脱到底]，论整体实力并不算低，尤其是[洛城机密]，被影评人一致看好，只是连[洛城机密]的导演柯蒂斯·汉森自己都酸溜溜地说：“结果还用说吗，当然是[泰坦尼克]。”

于是3月23日的奥斯卡颁奖礼，宛如成了人人达成共识的[泰坦尼克]登基大典，那些揪着影片未被提名最佳编剧说事儿、仍等着翻盘出现的少数派观众，迎来了的只是[泰坦尼克]平了[宾虚]纪录、十一项大奖拿到手软的不争事实。毕竟，学院派再曲高和寡，也难违背电视机前5500万观众的殷切期望——奥斯卡颁奖礼收看人数，至今十年也再没有超过这个数字。

[泰坦尼克]成了票房之巅，詹姆斯·卡梅隆成了“世界之王”。一个奇迹，诞生了。

巨片时代驾到
[泰坦尼克]票房刚刚漂红时，二十世纪福克斯总裁比尔·米切尼克曾拣了便宜又卖乖地声称：“虽然[泰坦尼克]很成功，但我们再也受不了TMD这种烧钱法了。”因而号召影业还是要回归精打细算的中小制作。

但趋势来了，挡是挡不住的，单许你[泰坦尼克]赚到盆满钵溢，就不许见钱眼开的我们如法炮制了？于是 高投资大制作如雨后春笋，个个都想复制[泰坦尼克]的惊世成功。

1997年时，影片成本达到一亿美元，已够让业内大惊小怪，[泰坦尼克]的两亿，更是令人闻风丧胆的创纪录性数字，而1997年后，大公司还拿区区一亿当巨资看？连[牧场是我家]、[绿巨人]这种姥姥不疼舅舅不爱的都敢没事拿一亿美元打水漂玩，更不用说[星战前传]、[007]这种出身优良的娇贵品种了。

自[骇客帝国]、[哈利·波特]等“电视连续剧”渐成气候以来，续集电影投资若不过亿，简直都对不起咱这张脸；及至[蜘蛛侠]和[加勒比海岛]系列一再突破预算新高，现在各大电影公司谁还把两亿成本当个新鲜事儿说？

希望总是美好的，而现实却并不总是如意，有[指环王]这样赚得笑逐颜开的，便也有[超人归来]这样归得自讨没趣的。但即便是赚着了银子的幸运儿，比起当年[泰坦尼克]那样翻着倍的收、打着滚的赚，仍是难以望到项背的。

因而像詹姆斯·卡梅隆这种，虽然赚钱能力是有历史明证，但只因花钱太过没谱，大公司皆不敢轻易启用，导致其十年有价无市，几成失业中年。毕竟[泰坦尼克]那样的盛况，无论靠钱还是靠人，都难再重现。

[泰坦尼克号]的另一个开创性意义在于，它是一个用金钱和技术联手造梦的典范，卡梅隆这个多年在技术派里摸爬滚打的狂人，能用以假乱真的缩微模型让你提心吊胆，也能以对着绿幕的逼真表演让你泣不成声，打破了人们之前认为技术只能增加影片商业刺激度的成见，令虚拟影象同样可以引人思索、荡气回肠。自此以后，技术造梦派成为好莱坞商业片主流。“像[泰坦尼克]那样，把请一线明星的钱省下来制造更多更猛的大场面”，成了各大制片公司熟稔于心的金科玉律。

一种现象，从[泰坦尼克]开始，十年寒暑，奇迹不灭。
"""
y3541415="""
Inception就好象是玄幻小说，你必须接受它里面的无数天马行空的设定；但是它是最好的玄幻小说，因为在它的设定下情节无懈可击。所以首先要解释片中提到的所有设定：


1. 首先，片中一共有六层世界。如果我们把片子中小组计划的现实世界作为参照物的话，按照做梦依次向上分别是：现实世界，第一层梦境，第二层梦境，第三层梦境，第四层梦境，limbo（迷失域）。

2. 正常人活动在现实世界，做梦的时候在第一层梦境。如果要进入第二层梦境，也就是梦里的梦，必须要服用一般性药物。在服用一般性药物的情况下，要从梦中醒来（不管是第一层还是第二层）有两种方法：第一种就是所谓的‘kick’，也就是重力下坠的冲击。第二种就是被杀死。当然，等药物效果过期也是一种不是办法的办法。

3. 如果要进入第三层梦境，也就是梦里的梦里的梦，一般性药物就无效了，必须要加强型药物。但是加强型药物的副作用是如果在梦里被杀死不能醒来，而会进入Limbo（后面解释什么是limbo），所以只能用 Kick的方式来苏醒。

4. 所谓的Synchronize a kick （协同刺激），也就是说要在各层同时刺激才能把梦中人唤醒。比如说对于在第四层梦境活动的人需要在第一至四层同时Kick（刺激）才能使其在第一层苏醒；如果只在第三和第四层Kick（刺激）则其会在第三层苏醒；而如果中间有某层没有同时Kick（刺激），比如只在第一，第二和第四层Kick（刺激）或者只在第一和第二层Kick（刺激），则活动在第四层的梦中人不会苏醒，这也就是所谓的Miss a kick （错过刺激）。所以当片中小组计划侵入深层梦境的时候，每一层必须留人醒着负责Kick（刺激），而且用音乐的结束来协调同时Kick（刺激）的时刻。

5. 层与层之间的时间以大约二十倍的数量延缓。在台词中给出的约数是现实世界十小时的航班，在第一层梦境是大约一个星期，在第二层梦境是大约六个月，而在第三层梦境是大约十年。

6. Inception的片名，直译是开启，在电影里面是一个盗梦术语，不是指在梦中偷窃情报，而是指把某种想法植入目标人物使得他觉得这想法是自己本来就有的。而Inception必须至少要在第三层完成。这是有原因的，我们可以在片中目标人物的梦中看到，第一层梦境很浅，意识很多，是整个城市，第二层是一个酒店，到了第三层只有白茫茫大雪里的一个堡垒。在意识越少的梦境里面植入效果越强。

7. 每个梦都有一个梦主（Dreamer），他和别人分享自己的梦境。梦境中的场景可以由专门的设计师设计然后告诉梦主的，所以设计师不一定是梦主。理论上来说进入这个梦境的人都会带来自己的一些意识投影，但是除了目标人物之外其他人都知道自己在做梦所以意志不会被迷惑。而设计师设计的梦境不能太离谱有不现实的场景，否则目标人物就会意识到自己在做梦，他的投影会对侵入到他梦境的其他人发动进攻。当然，如果目标人物的投影是经过特殊防盗梦训练的话，即使梦境场景很真实侵入者也会被投影围攻。

8. 迷失域（Limbo）不是一个梦境，也不因人而异。只有在服用加强型药物而且又在梦境中死去时才能进入。Limbo里面时间无穷尽。而且这个世界里只有之前到过这里的人留下的一些场景碎片，在日本人去之前只有leo夫妇到过，所以开头结尾日本人的迷失域里的房子和之前leo对他进行盗梦时给他造的一样。进到迷失域里面如果死亡会回到现实，但是问题是在迷失域记忆会丧失记不得这种方法，所以进入迷失域是不得已的选择。

9. 梦可以嫁接。也就是说A，B进入C的第一层梦境（这一层的梦主为C）之后B可以带A进入B的第二层梦境（这一层的梦主为B）。

设定大致就是这样，下面我们来看情节。

按照时间顺序，首先是leo和他女人的事情。这两个人是梦境世界的先驱者，当年结婚时许诺要一起变老，对于梦境世界的共同追求使得他们在自己身上试验。他们在实验中进入了女人为梦主的第四层梦境。人的第三层梦境世界东西就很少了，第四层更是什么都没有。因为只有两个人实验所以前面几层没留人不能帮他们kick，而由于时间延缓的效应，在现实中入睡一天在第四层就是五十年。所以他们在第四层梦境世界中携手共老，闲暇之时只有随便创造东西玩。五十年之后他们在梦境中老死了。以为他们是服用了加强型药物的，所以双双进入了Limbo迷失域。迷失域中女人贪恋着无时间尽头的厮守就认为这是现实，不想回现实，而leo却想着自己的孩子想回现实。最终说服了女人和他一起卧轨自杀，他也不确定这样就能从limbo脱身，所以自杀前把怀疑一切，尝试一切的想法灌输给了女人，这是他的第一次inception。在迷失域自杀之后，他们回到了现实，可是那个inception的副作用产生了，那就是女人开始怀疑现实其实是梦境，认为只有死亡才能脱离。于是女人自杀而造成是leo杀的假象，终极目的是想让leo也被处死这样可以一起脱离梦境。可怜leo只能抛弃了孩子们而逃亡国外。而leo的潜意识里面充满了他老婆的影子（就是shade那个角色），只要他再从事设计梦境的工作，那个他妻子模样的影子（代表了他潜意识里的悔恨和对杀死妻子梦境工作的怨恨）就会出来坏事。
（leo和妻子经历了第四层梦境和limbo两个世界，最明显的证据是在limbo卧轨自杀回到现实时两人都是年轻的，而在第四层梦境两人有老年的样子。）

话说leo在国外随便接盗梦的工作，接到了一个窃取日本大亨情报的工作。这就是开头的枪战戏，也是简单的梦中梦，所以这里只有一般性药物，梦里死了立刻就醒。结果团队的设计师先出错在梦境中穿帮，然后又在现实中出卖了他们。日本人却看重他的能力，反要雇佣他进行inception：让竞争对手公司年轻的掌门人切分自己父亲留下的基业，许诺他可以让他回国看孩子。所以他找了新的设计师小女孩和新的团队。对于inception的计划是在年轻掌门人心中播撒对于父亲的好的印象。leo在讨论中提到说反面的东西会产生正面的影响，如果年轻掌门人恨父亲的话，反而会把企业做好来证明自己比父亲强。

这次Inception的地点选在悉尼飞往美国的十小时航班上。这对leo来说不成功便成仁，因为他在美国因为谋杀妻子被通缉，而日本人许诺说只要他完成任务就会在飞机上打电话解决这个问题。

一进入年轻掌门人的第一层梦境就出了问题。这个人被其他盗梦专家训练过，梦境虽然是小女孩创造的，但是目标人物的意识会化身武装人员对异常梦境里的人物进攻。更重要的是这次inception要在第三层梦境实行，而leo之前并没有把加强型药物的副作用给大家说。这时候只有华山一条路完成任务了。印度人留在第一层负责kick，他们进入了第二层的酒店，小帅哥留在第二层负责kick，其余又进入了第三层梦境的雪堡，目的是让年轻掌门人自己见到他们设计出来的父亲而接受想法。就在即将成功的时候，leo的妻子的影子再次出现搅局，开枪击中了年轻掌门人，这时候年轻掌门人没死，只是昏迷，情急之下，小女孩提出把年轻掌门人嫁接入leo的第四层梦境，在那里用‘kick’，加上第三层的电击把年轻掌门人唤醒。于是，小女孩和leo进入leo的第四层梦境，在那里小女孩把年轻掌门人kick回了第三层梦境（同时第三层有人对他的身体电击）。在雪堡深处，年轻掌门人听到了设计中的父亲的最后遗言：I am disappointed that you tried… （意思是我对你极力想试着成为我这样的人很失望），也就是说让他作他自己别管公司。打开保险箱之后他看到的是自己最珍爱的和父亲照片中的纸风车，对父亲愧疚之下自然会实现同样在保险箱中的伪遗嘱分拆公司。到这里inception的任务圆满完成。第三层梦境世界的爆炸kick，第二层的电梯kick，第一层的落水kick同时进行。小女孩，小帅哥，印度人等人成功脱险到第一层。只有日本人死在了第三层梦境世界，所以跳过第四层直接进了迷失域limbo。

与此同时，leo在第四层梦境世界终于狠下心来杀死了妻子的影子，也在争斗中被影子刺中身亡，同样来到了迷失域。在这里他见到了日本人，并且说服他用枪杀死leo然后自杀而双双回到现实。
（从梦境世界到limbo记忆会不太好使，所以leo说他忘了第一次进迷失域之前和妻子在第四层一起老去的事情，他第二次进迷失域见日本人的时候也想了半天才想起来来的目的——日本人回不了现实不能实现许诺的让他回家的报酬了。）

至此，leo的心结解开，他的对妻子死去的悔恨因为回忆起了和妻子在第四层梦境世界白头到老的幸福而被冲淡。日本人在飞机上醒来后也兑现了诺言打了电话解除了他的通缉。

最终的结尾是开放性的，陀螺不知道停没停，但也无伤大雅。假如这作为参照的现实的确是梦境的话，那也只不过把六层世界变成七层。如同电影中出现多次的循环封闭上下楼梯一样，电影中的多层世界也不过就是增加了维度的莫比乌斯圈，1到2到3到0到1到2到3到0…….. 如此往复。

如果对我的解释或者其他地方有疑问的话请回帖。我会编辑更新。

补充一下关于老臣的情节。Forger在第一层梦境伪装成富二代老臣，除了套取他和父亲关系的情报之外，还设下了在第二层梦境诬陷老臣的伏笔。第二层里面的老臣是富二代意识里面的老臣的投影（projection），所以如果富二代心里面认为这个老臣是中心的话投影就会表现出忠心的，反之亦然。所以forger在第二层和日本人说他在跟踪老臣的投影根据投影的表现判断富二代有没有上套。这个套的目的是让富二代认为第三层梦境中那些自己意识投影的私人军队是老臣意识中的投影，所谓台词中的让他自己击破自己的意识防卫来完成inception。

如果还有什么疑问，大家可以去看一下网易的解梦手册，那也是我写的，更详细一些，地址是：

http://ent.163.com/special/inception6/



imrains：
　　有两个疑点：
　　1. Kick的顺序，我理解Kick应该是发生在N层，然后把N+1层中的人拉回到N层。所以我对最后在Cobb第四层的Kick不太认同，他们在第四层Kick怎么能唤醒第三层的人；
　　2. 你说在Limbo里面死了就回到现实，那当时完全Saito在第一层中弹的时候完全没有必要紧张啊，直接告诉他你到limbo里自杀就OK了。而且，如果这么容易的话，没必要一层一层的安排Kick，完成任务后大家一起都死了，然后再LImbo里再死一次就好了...

回答：1. 如设定中所补充的，对N层睡眠的人体电击+对N+1层活动的人体kick可以模拟N层的kick。当然要同时。所以最后第三层的队员不知道目标人物什么时候在第四层跳所以不停地电击昏迷的他。
2. 进入迷失域会失忆，所以leo直到最后才记起他曾经和自己的妻子在第四层白头到老过，而且第二次进入迷失域的时候也是凭借日本人一句熟悉的台词才想起自己来的目的。

 漪木:
　　我一直想不通的就是leo怎么就从第四层来到了老年日本人的面前（迷失域），”被影子刺中身亡"，这个桥段还真的记不清楚了呢。

回答：嗯，其实leo是故意用言语刺激影子来刺杀他。影子刺了他之后也被小女孩枪杀。小女孩还提醒快死的leo要找到日本人。刺有动作没有镜头，因为要保证这片子PG13的等级划分。有刀刺入身体镜头就R级了，票房损失啊。

朱时茂：
　　我想听楼主说说陀螺.
　　Cobb说这是我老婆给我的, 她在你说的第四层把它锁在保险柜里, 然后Cobb让它在保险柜里转动起来. 然后就是最后一个镜头.
　　它是一种象征(特别是保险柜段落), 还是关键的道具?

回答：陀螺如果转起来一直不停就说明不是在现实。所以无论在第四层还是在迷失域都会转起来不停。leo女人在第四层和迷失域都把陀螺藏起来，是不想让这个东西提醒自己这不是现实。然而leo找到了被藏的它，因此知道女人不想离开的心意，因此想用inception来改变她的心意。这是很容易的，因为当leo和他老婆最初实验的时候，leo是梦主也就是设计师。此后陀螺就一直被leo带着。

seren
　　但是日本人花那么多功夫最后好像只是免费帮助富二代竞争对手解决了父子情结嘛。。。。。。
回答：日本人的拆分公司的目的达到了，请看关于完成任务的那一段。

 LX抛出异常
　　一个小小的问题，应该是如果他知道整个梦境的结构，那么shade也会知道，然后潜意识里shade就会来找他。这和如果他设计，那么shade就会来坏事儿有点不同。
回答：嗯，对。shade不管怎么样都会出来坏事，但是如果leo设计的话，shade就会知道所有场景结构坏事更容易。

 chibababa1
　　but limbo中的日本人为毛那么老？因为limbo中的时间会更加放慢么？可是他也只比leo早去一下下啊
　　还有，如果在limbo里面回失忆，不知道自杀能回现实，为啥leo和老婆去的时候，他知道要用卧轨自杀来回去？

回答：1. 日本人是在第三层死的富二代醒过来之前很久就死了，leo虽然是在第四层死的，但是明显可以看出是在第三层富二代醒过来之后死的，这一段时间加上两层（3到4，4到limbo）的时间延缓，所以日本人比leo老很多。所谓limbo里面时间无穷尽，也就是因为limbo的时间延缓倍数很大，虽然具体数字在电影里面没有给出。
2. 他们也不确定，只是试一下。实际上，因为他们是先驱者，所以很多问题都是从实践中得来的。比如，第四层的时间延缓倍数就超出了他们的预计没有准备，不要然他们不会在第四层滞留五十年。leo卧轨时候一直说在等火车，但是不是很确定火车会把他们，带到哪里就是这个意思。而后来leo老婆的怀疑也来源于此，既然你不确定，为什么不可能是从limbo卧轨自杀死了之后还是一个非现实世界。

ZephyrO：
　　第一层梦境很浅，意识很多，是整个城市，第二层是一个酒店，到了第三层只有白茫茫大雪里的一个堡垒。
　　---------------你怎么不说第四层也是整个城市啊，不要误导别人好伐------

回答：嗯，我的意思是：小女孩设计第一层梦境里，富二代的意识幻化成大城市中的很多人，第二层只有酒店中的少数人，第三层之只有雪堡中的保安。第四层是leo设计的梦境，里面的城市是空无一人，是他和妻子之前创造的，其他人进入的时候，不管是早前的妻子还是小女孩，除本身外都没有带来其他的人物projection。

shoujuan
　　1。 cobb 和妻子在limbo的时候，他是怎么知道那不是现实，而需要自杀回到现实 世界的？
　　2。 在 limbo 里面，只有自杀才能回到现实吗？他杀可不可以？在梦境里面他杀是可行的。
　　3。 为什么是模比乌斯环呢？没看出来梦境是循环的。
回答：1. 之所以知道不是现实有多种途径，比如陀螺转不会停，最后日本人在limbo里面转的时候就没停。至于为什么知道自杀。前面chibababa1的问题已经回答过了。
2. 他杀似乎是可以的。因为最后暗示日本人举枪在limbo里面先杀了leo再自杀回到现实。
3. 第一层楼上到第二层楼上到第三层楼，第三层楼再上回到第一层楼。这样的意思，现实，四层梦境，加上limbo每个都是一层楼。

 阿兵♨降龙伏虎
　　难道所有人都认为是开放式的结局？
　　电影本身就是一个puzzle，
　　我认为结局只有一个，另一个结局在电影中逻辑上会有问题，
　　导演不公布结局正是因为电影本身是一个智力题
回答：嗯，我也倾向于认为最后陀螺会倒下来。但其实如果不倒的话总还是可以完满解释的，比如Limbo有两层之类，因为关于梦境的真正结构即使是片中人物也是一点一点从实践中学到的，所以没有不可能。不过那样就太无趣了。 

"""

y2131459="""
也许这一刻，我正在庞大的超市门口拎了几个大袋子笨拙地走。Wall-e正在尘土满天的废弃城市里把一堆垃圾吃力地压成立方体。

也许下一刻，我已回到家里爬上床看连续剧，看其实老也跳不出窠臼的模式剧情。Wall-e已回到家里点起灯打开电视，看它仅有的几分钟歌舞片段。

我们都可以按部就班地工作，我们都可以沉默而独立的生活，日升日落之间时间平静流走，恶劣天气来袭时我们都会往自己的蜗居一躲。然后继续工作，继续生活。

只是我想，总会有那样的时刻，Wall-e在电视里男女主人公牵手的时候只能自己去握住自己的手。我在剧中恋人深情的拥吻中只能轻轻揽住自己的手臂。就像一定有那样的时刻，那个电影屏幕里的Wall-e，或这个现实世界中的我，一定会站在初升的明月或是西沉的夕阳前，看着这个这么美的世界，期待某个谁存在，让我们把这所有喜悦分享。


Wall-e这样期待了几百年。在没有蓝天没有河流的地球表面，在没有生命迹象一片死寂荒凉的世界尽头，在枯燥肮脏而疲惫的生活中间，在金属构造冰冷坚硬的躯壳里面，期待着，渴望着。一直渴望着，与某个谁，轻轻牵一下手，来个十指紧扣。

在它发生前，所有的期待和渴望，也许只能被视为荒谬；但Eva出现在他生活里的那一天起，一切都不再一样。一见钟情是件太自然的事，因为，为了这一刻，他已等待太久。他只想多看看她，如果可能，还想跟她说说话。她看起来好像不太友好，可不要紧，他会尝试模拟微笑的神态。飓风来袭，让他来保护她到家里躲避，他要把自己所有的宝贝都拿给她看，灯泡、魔方、能打着小火苗的打火机，当然还有，还有他最珍藏的最爱看的歌舞片片段。那场面太浪漫，他都已不好意思了。那么，把最新发现的宝贝献给她吧，他刚刚从垃圾堆里捡到的一棵嫩苗，他大概都几百年没见过了，她一定也会惊喜吧。

谁知她一看到这个，立刻一把拿过揣进怀里，转而一动不动，不再有面容表情，不再有双手，也不再发出声音。他哑着嗓子唤了她好久，都没能把她叫醒。那么，就在她醒来之前好好照顾她吧。怕她电池耗光，于是把她搬到屋顶晒太阳；怕雷雨把她淋坏，于是在屋顶撑了伞守着她，被雷劈坏了好几把伞，好在他素来有所积攒；其余的时间，他带她在栏边看远山日落，看黛青山影紫色云霞，他一定盼望着某一天，她会醒来，会对他微笑，会伸出双手，会和他一起看这世界。

但是没过几天，当初从天而降的这个她就被偷偷地运走，要送回天上去了。他在千分之一秒之内做了决定，不管前面是什么，他都要追随到底。于是他挂在飞行器外壁上横穿了整个宇宙，在移居太空的人类生存群落里掀起轩然大波，醒来的Eva通过体内记录的录像了解了Wall-e付出的一切并被彻底感动，两个机器“人”互相扶助着终于把来自地球的生命之绿色传达给了人类并协助人类重返地球。


所有英雄式的故事之外，我只看到Eva似嗔似怒似了然又似欣喜的两眼，只看到Wall-e似怕似惶似坦然又似无畏的神色，只看到Wall-e救Eva时的拼命三郎模样，只看到Eva以为Wall-e要死在爆炸的宇航球的时候伤心欲绝的表情。他明明是铁锈的金属壳脑袋，却简直已满脸是汗；她明明是液晶屏眼睛，却几乎要有泪流出来。这世界尽头的两个机器人，俨然原来就是我，是你，是他，是她。单相思的乐在其中，两情相悦的狂喜，关心则乱的鲁莽，因爱而生的勇敢，对永失我爱的巨大恐惧，失而复得的欢天喜地，并肩作战的信任感，共赴生死的羁绊。那些巨大而猛烈的感情，为何让我们不禁为之动容，还不是因为我们自己原是如此渴望身处其中。


是的，若我伸出手掌，那一定是在等你递过你的手过来，轻轻吻合，十指紧扣。

让我五指牢牢夹住你五指，不再放开，不让你离开。

因为我过去所有等待，都是为了和这一刻有关的现在和未来。

就算没法在星河里追逐穿梭，也总算把彩虹看过。就算不曾互相拉扯着度过绝境，也总有随时狂奔去救你的勇气。就算并没有打火机和老电影，可以让你看到就想起我而我看到也必想起你……

就算没有能写成故事的经过，也是你知我知的传奇。

原谅我和这金属脑袋的Wall-e一样，都这么浪漫主义死性不改：直到世界灭亡，依然对爱渴望。
"""

y1292001="""
关于钢琴，关于尽头，关于彼岸，这些我都不想说。我只想说说1900这个人。

众人叫他天才，众人为之疯狂。1900，从拥有这个不平凡的名字起，就注定是个不平凡的人。目光、掌声和荣耀，平凡人可能终其一生都得不到的东西，对于天才的1900就像空气一样稀松平常。
但目光、掌声和荣耀并不能令人幸福，也不长久。
电影里有一个镜头让我特别难受：人们围绕在1900身边为音乐起舞的时候，有人看见了自由女神，一下子所有的人呼啦啦作鸟兽散，只剩下1900孤寂的身影。再多的荣耀也挽救不了孤独，此刻他非天才，是个可怜的被遗弃者。

天才其实是世界上最不幸的人。所有的天才都是异类。而再体面的异类都不会被人真正地爱。那些为1900的琴声瞠目结舌的人，在琴声终结的时候，他们也就咂巴着嘴散去。1900这样的天才更像是个宠物。人们会喜欢它、呵护它、痴迷它，但它跑到马路中间迎面驰来飞车，谁也不会扑过去用自己的身体挡住。

大概只有小号手是愿意聆听1900的内心而非琴声的人，他不理解他，但是他尊重他。他用尊重成全了1900完整的独立。我看到有人说如果他是那胖子他就会把1900敲昏然后拖下船。我想这样的想法也就注定他成不了那个胖子，成不了1900唯一的真正的朋友。

如果我们较真一点，假设小号手真的把1900弄下船了，故事将怎样延伸？我们都知道，落魄的小号手没有能力去为朋友找一艘新的船，找88个琴键和尽头。1900将无可避免被磨去棱角和平庸，落入红尘变成一个凡人。

活着，还是活得安心。这也是个问题。凡人的选择是无论如何先活下去再说，"活着"这件事情本身比什么都重要。而天才则把心灵的舒适看得更重，生死则次之。所以凡人可以忍辱，天才却情愿玉碎。每一种人都获得了他最看重的东西，说起来谁也不比谁亏。



其实我不太乐意用天才这个词儿来定义1900。天才已经被用滥了。我更愿意说1900是个ET。我们生活在这个星球上的人，想表达就开口说话。这是人类的方式。但是1900不属于人类范畴。他的手指是他的发声器官，连着他的心和眼睛。他的身体机能是人类的，他的感知和内心是ET的。
ET很神奇，但不算稀奇。因为我们每个人都是ET。

小时候看哲学入门读物《苏菲的世界》，哲学老师说，你是否想过自己或许是个火星人？你是否有一天会停下脚步，审视自己然后想："我是一个不同凡响的存在。我是一个神秘的生物。"——我并不理解。我看着每一个人都有两个眼睛一张嘴，我无法理解这一模一样的人怎么会是不同星球的物种。

直到后来我发现人的内心比海还深，发现一个人和一个人的差异比天和地的相错都大。我才渐渐相信，我们每个人都是ET，至少都曾经是ET。我们生下来的时候如此千差万别，就像从宇宙的各个角落聚集到这个星球。我们透过眼睛看世界的角度，我们吃奶头的力度，我们尿裤子的姿势，都如此独立如此百花齐放。

我们曾经都很与众不同，鲜活跳跃。但是后来，我们被教育，被纠偏，被放入轨道。于是我们从一个个ET变成一群地球人。我们鲜活的面容淹没在人群之中变得模糊不清，一眼望去毫无分别。只有那些因缘巧合的，比如1900，侥幸（或者说是不幸？）保存了自身的独立和ET本色，成为地球人眼中的天才和异类。

差异导致孤独。葆存了差异性的ET在承受异样目光的同时也承受着巨大的孤独，远超出凡人的孤独。凡人们如我们虽然也还都残留一些差异，但大致面貌八九不离十。我们失恋了后觉得痛苦比谁的都大，我们拥抱心爱的人自认比谁都幸福。但一个残酷的事实是：每个人的痛苦和幸福都没什么区别。我们在不断重复，千篇一律。

我们丢了个性却换来了共鸣。我们借助艺术寻找通感，在人性中相交叉的部分，抹着眼泪互相慰藉，或者说，互相平衡（原来有人比我还惨啊，这下心里舒坦多了）。而被称为天才的人站在人群之外，忧郁地注视这群有些像他又不是他的物种。用他们ET的本能将那些交叉部分，提炼、放大、直抵内心。那些永远无法交叉的部分，则作为孤独的源头，令他们永远无法融入人群。他们只有躲在自己的轮船里，躲在自己的内心世界里，孤独地活着，然后死去。

"""

y3793023="""
有识之士路过请原谅我把这两部电影放在一起比较，事情的起因是前几天我向别人推荐了一部除了名字翻译得恶俗，内容却属上乘的印度电影佳作《三傻大闹宝莱坞（three idiots）》，结果居然被贬成还不如《人在囧途》，对于此人的艺术欣赏水平我只能用影片里的一句话形容——剧情太复杂了，而且没有字幕，不适合你。此人我就不点名批评了，只在这里帮你分析一下剧情，让你了解到两部影片PK是完全没有悬念的事，顺便帮你上一堂影视欣赏的扫盲课。

首先，作为喜剧片，在叙事手段上，两部影片的差距是显而易见的。喜剧片发展至今，想在笑料上取得很大突破实在是很难的事。因此，一部优秀的喜剧片手段高明与否取决于对笑料的组织结构。

《三傻》在全片的叙事结构上，采用了现在、过去两条叙事线索交替进行，互为解释。从而加强了影片的因果联系，增加了紧凑感。如果《三傻》采用顺叙的方式拍摄，结果就会成为《囧途》这种拖沓的电影。

再说《囧途》，全片只有一条线索，一种节奏，镜头打一开始就感觉没离开过徐峥。这就不说了，还愣把“春运”和“小三”这两个八竿子打不到一起的主题牵强的放在一起讨论，估计是剧本内容不够硬加的。全片就是一个主人公不停倒霉的故事，这么多倒霉事凑在一起的几率得多低？虽然说无巧不成书，但是把一连串的没有前因后果的巧合毫无组织的机械拼凑在一起，就太脱离生活了吧。举个例子说吧，人踩到屎这种笑料够无聊了吧？但人连续踩到十耙屎难道就变得有趣了。这岂不荒唐？而且连续踩到十耙屎这种烂俗的剧情你信吗？当观众是傻子啊！《囧途》就是一部主人公不停踩到屎的闹剧，而且屎都是清一色的（全是交通问题），看开头就猜得到结尾。我想不通居然中国还有这么多人买账，票房还嗖嗖的，居然买到四千万，成本才五百万，作为商业片来说它成功得一塌糊涂，但演技派徐峥一世英名就砸这片子上了。

第二，真正的幽默是含蓄的，不经意间就埋下伏笔，也就是我们所说的“包袱”，是笑料在细节层次上的组织结构。下面我们再来比较一下两片的“包袱”：

《三傻》中伏笔比比皆是，我随便就能举出十几个：1，开学时“消音器”不会说印度语导致后来演讲时稿子被改了也发现不了（影片也顺便抨击了填鸭式的学习方式）；2，开学时门口撒尿被电那一幕，结合“消音器”多次在野外随地小便，使最后“消音器”小便被电的发生得很自然；3，太空笔这个线索是影片的一个亮点，套用美苏航天局“太空笔-铅笔”的典故，使“病毒”和Rancho之争到和解以及后来Rancho签名这几幕一气呵成；4，“微薄的供奉”这个举动也是贯穿全片的一个笑料，虽然这种笑料略显粗俗，但是影片用几种不同情感的“供奉”完美的化解了这种粗俗感，给人一种辛酸的喜剧感；5，Rancho教“豪米”免费蹭课，由后来得知的Rancho小时候的蹭课经历回应；6，“病毒” 在开学典礼上说自己儿子三年都没考上工程师，又对自杀的那个学生说儿子死后的第一天他就恢复工作了，这两句话一开始可能没人注意，可是为后来得知他儿子是自杀的真相埋下了伏笔；7，Joy Lobo喜欢发明遥控直升机，最后发现他自杀也是通过遥控直升机； 8，Rancho说教育制度谋杀了Joy Lobo与pia说“病毒”谋杀了他儿子相互呼应； 9，“病毒”双手写字和午睡时修胡子的习惯，分别为后来双手写告状信和被迫履行诺言刮掉胡子埋下伏笔； 10，为瘫痪在床的Raju Rastogi报喜讯的Farhan用的是乒乓球室的电脑视频，而后来pia的姐姐生孩子那一幕也是用的这台电脑的视频作遥控指挥，两者小小的呼应一下； 11，Rancho在pia姐姐的婚礼现场急中生智说要发明一个电瓶供电的装置，并且以“病毒”的名字命名，就是被pia摔坏那一个，最后在生孩子那一幕发挥了供电作用； 12，此外，还有免费建议和薄荷酱等包袱层出不穷，就不一一列举了。

    第三，在影片立意上，两片的差距就更大了。

《三傻》反映了许多印度的社会问题：教育制度，贫富差距，高校自杀率，医疗状况等等。当然，重点是教育制度。与此对应，通过主人公Rancho之口提出了“追求卓越，成功就会出其不意的找上门”的人生哲学和求学态度（与我们老祖先“追求而不强求”的人生哲学有异曲同工之妙），反击了功利的教育动机和机械的教育制度，以及励志性的口号“Aal izz well”。 “Aal izz well”来自于英文的“All is well”，意为一切都会顺利，一切都会好的意思。这种印式英语也为口号本身增加了喜剧和乐观的色彩。

回过头来看看《囧途》反映了什么。春运，这是个社会问题，在他那儿就完全变成了单纯的交通问题，而且完全没有提出解决方案，甚至连思考都没有，只有反映没有探讨，就像单纯发牢骚一样。你丫是信访主任出身啊？农民工讨薪，这倒是解决了！怎么解决的？路上遇见老板了，跟老板整出了交情，老板被感化了。真有你的！那没遇见老板的农民工怎么办？纯粹一美化资本家，缓和阶级矛盾的政治宣传片！是资产阶级阵营投向我工农无产阶级的糖衣炮弹！然后是小三，连社会问题都不是，就是个社会现象，解决办法？丈夫良心发现，小三情节高尚的退出，资本家的情操再次得到升华。这太童话了吧？唬爹呢？

看看人家印度在探讨制度问题的时候，我们在纠结什么？我们在现象上打转转！人家追求卓越，是一种聪明的理想主义；而我们崇尚王宝强的执拗，是一种傻不拉几的理想主义。“Aal izz well”不是盲目乐观，是贫民在印度贫富差距巨大的社会现实面前给自己打气的信念。Rancho和“王宝强”都扮演着单纯的角色。可人家推崇的是睿智的单纯，我们崇尚的是憨傻的单纯；（我就想不通王宝强在中国怎么这么受欢迎？一没长相二没演技的，他演的所有片子全部一个性格，就是本色演出，一个傻劲，连口音都不带改的。中国人就这么喜欢看二傻子学二傻子吗？）人家呼吁把未来掌握在自己手中（像Rancho），我们则期望老老实实的有一天会遇上贵人（像“王宝强”）。中国人看这种片子长大，这不是愚民误国吗？长此以往，友邻阿三要想灭了我天朝岂不易如反掌？

 最后，让我们再来回顾一下《三傻》的亮点吧，《囧途》就不用比了，因为完全没有。唯一跑错房间这一幕尚算巧妙，都是炒《虎口脱险》的冷饭：

内容和立意上，前文已经讨论过，就不做赘述了；

从风格上，“辛酸的喜剧感”是本片一大特色。一部满是自杀、贫穷、疾病和压力的片子却拍的完全没有沉重和压抑。这种用幽默化解痛苦的风格结合印度歌舞片的热闹正好承载了本片“aal izz well”的乐观精神；

台词对白上，经典层出不穷。如刚才所说的“剧情太复杂了，而且没有字幕，不适合你。”以及“人类行为学第一课：朋友没及格。你觉得悲伤；朋友考第一，你觉得更悲伤。”这样的对白实在令人捧腹；

镜头语言的应用上，花样也推陈出新。Rastogi跳楼时，让他的脚挂到台灯线，然后用台灯的运动代替跳楼的画面，效果比直接拍摄跳楼更悲壮；影片一到Rastogi的家时就变成黑白片，还故意整出劣质胶片的粗糙，这种幽默的方式化解了Rastogi家贫如洗的沉重感；大家兴奋的把遥控直升机升到Joy Lobo的窗前时却拍到他上吊的画面，巨大的感情反差给观众突然的震撼；

桥段的设计也屡见特色。如生孩子那一幕Farhan要主任办公室的钥匙时，“病毒”和Rancho以相同的动作同时扔给他时便产生了喜剧感（Rancho的钥匙是偷的“病毒”的）；歌舞部分的幽默桥段就更不用说了，这是宝莱坞的强项；

同时本片在桥段的设计上也有很多实验性的探索。如，教授骂Rancho白痴，Rancho转身回来，都以为要跟教授争，但是他是回去拿书，并经典的诱导教授自己驳倒了自己的迂腐；“消音器”夺刀都以为要干过激的事，结果只为在墙上刻字挑战Rancho；Farhan父亲先说把作为儿子礼物的电脑还回去，却原来是换成照相机支持儿子最求自己的理想。“在细节上出人意料”打破了传统的许多桥段和套路，小小的给人耳目一新的感觉。

演技：“病毒”的演技可谓是已臻化境，把一个迂腐、偏执、严厉的父亲和老师演绎的淋漓精致；其他演员，如扮演Pia、Rancho和Rastogi的演员都有不俗表现，特别是前两者；在配角中，真的Rancho、Rastogi的母亲的扮演者的表现，令人眼前一亮。

如此之多的亮点，不得不说《三傻》的创作团队确实是一个富有创造力和激情的团队。我就纳闷儿，同样是新近上映的商业片，人家为什么能把商业元素与艺术以及社会责任感结合得这么好？

我不得不为他们喝彩！祝他们越走越远，祝印度电影重新崛起！

而在篇末，我不免俗的要大声疾呼：中国拍喜剧的倒霉孩子们，别老盯着容易钱挣！少整点象《人在囧途》、《唐伯虎点秋香2》这样屎黄屎黄的烂片，多拍点象《疯狂的石头》、《疯狂的赛车》这样辉煌的经典，救救中国人满目疮痍的智商和幽默感吧！若能这样，衷心的，请您接受我们这点微薄的供奉吧！

PS:强烈谴责此片片名的翻译，你的媚俗和《人在囧途》有一拼。
"""

y3011091="""

水来我在水中等你，火来我在灰烬中等你。 ————洛夫
八（はち）、Hachiko，这是一个被爱注册过的名字。它的意思是延伸到天际又降落到大地。

                           【许你一世的欢颜】

它是一只狗。一只被他捡回来的小狗。它看起来一无所长。
倒叙、慢镜头、长镜头、对景深镜头的自然追求，一切温情片惯用的手法。
他们本来形同陌路，属于两个不同的物种。
他们的生活也许不会有交集。

他恰好遇到了它，无家可归的它。
它把他带回家，他给它温暖，给它一个家。
他爱它，所以它等他。

太平常太俗套的故事了。
只是很多事情，只有回过头，才会看到它的洁净与美好。

我总希望有人在什么地方等我，你也总希望有人在什么地方等你吧。 ——几米《照相本子》

这情感竟能那般顽强地蹒跚过十年，恍恍惚惚，清浊相间，一点一点穿过世间最遥远的距离。
生与死的距离，对于一条狗来说，它无法参透，它只相信，他会来。
它的生命如一注流水，一点一点在车站的青石台上年复一年地流逝。它等待。
作为一只狗，它有它的原则。不离不弃。不论生老病死。
它卧在那里，十年，透彻成一种风景。
死生契阔，与子成说。

这样的故事并不比别的故事更惨烈，比如《海豚湾》。
它只是，“怅然遥相望，疑是故人来”。
他让它懂得了爱。于是它用了十年，它的一生来坚守。那些记忆里的美好，从未消逝。

                           【一场寂寞凭谁诉】

华尔街有一句著名的话“若你需要朋友，就养条狗吧。外面的世界是场近身战。”从什么时候起，人情薄似秋云；从什么时候起，这个社会变得面目可憎。

我不相信爱情，不相信等待。
我相信有很多人和我一样。看过了一些电影一些书籍以及人间冷暖。
我一直知道，我的心在一点一点硬起来，对这个世界越来越不满，常常冷嘲热讽。
偶尔还会写些温暖的文字。可有时就连澄净的心境下写出的文字也难免沾染浮华。

我常觉得寂寞。
这样的寂寞常不是我一个人的。是我们的。是这一代人的。
我常宅在家里。
觉得这样的自己就安全了放松了温暖了。
我看海豚湾，我听说有人杀狗，我每每哭得稀里哗啦，又心知那样的惨烈也许自己永远不会遇到。

小时候，我养过金鱼，它们死了，我哭得很伤心。后来妈妈给买了两只小兔子，它们几个月后也死了，我哭得很伤心。家里陆续养过三只猫，又陆续送走了。
我再也不敢养宠物了。

2009年5月，我遇到了生命中第一个亲人的死亡。
外公去世前的一个月，外婆将家里的养了8年的狗送了出去。
我怕狗，我不和它亲。虽然每次去外公家，它都会向我摇尾巴。
后来，我问妈妈：为什么要在狗那么老的时候送出去了呢？
妈妈说，从外公重病起，那只狗就已经不吃不喝了。
我不知道那只狗现在在哪里。
我没有勇气再问。
我参加了外公的葬礼，从亲手捧起外公的骨灰的那一刻起，我不再害怕死亡。

我知道，有一天，我也会死去。
连同我深爱的人。都会告别这个人世。
有一些会先我而去。

而对于另外的人，我可以先死。
可以把骨灰撒进离他最近的花盆里。开出一朵花来。
他可以等我，或者不等。
他总归可以知道，我是在那里等着他的。等他回家。

永远不要忘记你所爱的人。

这是Hachiko教给我的。那是一个被爱注册的名字。

“这是八月初的一个早晨，美国南部的阳光舒迟而透明，流溢着一种久经忧患的让人鼻酸的，古老而宁静的幸福。”                                               ——张晓风
"""

y1291549="""
描写老师和孩子们关系的影片很多，感人的也不少，在电影＜放牛班的春天＞里，辅读学校的孩子们被新来的学监兼音乐老师马修先生吸引，爱上了音乐爱上了合唱。事后我发现，观看这部电影的过程是一个纯私人事件。
我就读的的初级中学曾经非常烂，它座落在市郊结合部。当时没有公共交通直达，沿大马路走入一个小镇，穿过农田，翻过小桥（不知什么原因人们在小桥上锁住了铁门，只能从铁门上翻过去），过河后沿苗圃走，路边是硕大的建筑工地，四十五分钟后到达新开的学校。
我们是第一届入学生，都是考重点高中的落选生。老师分为三类：外地急待回沪的各色人物，新分配到学校工作的大学生，本市混得不得意的老师们。这样组合效果自然有趣。我们班上曾有一位娘娘腔男生上课练习京戏，被老姑娘班主任阻止，两人互相抓脸对打，一路厮打到教务处长办公室，后者阻止了暴力继续。班上还出过一少年犯，长得很帅，是击剑队的高手，人很善良但爱偷东西，很长时间里我都以他为骄傲，还背着老师组织了同学们去少管所探监。可以想像那是一段多么混乱的时光，那所学校的学生缺乏是非观念。
我们的音乐老师姓顾，原谅我当初年纪小，没有打听他的前世今生。如果很想知道他是什么样子的人，可以参考＜放牛班的春天＞。
顾老师告诉同学们他在组织一个合唱队，既然大家都闲，不如过去磨磨牙。他有一架钢琴，站在钢琴前咿呀几句就可以站队分组，我被分到女中音组。
电影里马修老师的嘴脸顾老师都给演示过：”腹收紧，胸要挺，头要抬，眉眼要往高里拉，气息顶得牢牢的。“他的右手五指撮成一团，做成撮东西的样子，在自己头顶百汇穴上轻轻一抓，看样子像是通过揪一把头发的手段要把自己提到半空中，然后他说：“让声音向上竖起来，像管子一样通到天上。”这个动作马修老师在电影里也做过，表情和气势都十足一样，可惜没给配上台词。
顾老师那样一抓，我们的声音都变成管子，一路通上去，可惜功力不够，通到半空里突然咣当一声掉下来。顾老师把琴声停下来，跑过去打开大音箱，那是我第一次见识大音箱，里面传出维也纳童声合唱团的声音。顾老师指指丹田说：“如果你们用这里的气把声音顶住，管子就一直通到天上，和他们唱得一样了。”我们就继续顶管子。顶管子是个体力活，可惜电影里简笔带过，观众会误以为放牛班的孩子们一日间就顶起了管子，尤其是那个莫杭治同学，简直惊为天人张嘴就是管子，其实有副好嗓子和顶起直管子之间还不能划等号，且得花点时间才能踩到准点上。
有一次在我努力顶管子时顾老师把同学们一并招集到我跟前，他请大家看我的嘴，他说你们看她的舌头，紧张地顶满口腔。他说声音是纯自然的东西，舌头这么不老实，声音就死在肚子里，管子爬不上去了。我面红耳赤，但同学们没笑，我突然意识到他们舌头都不老实不好意思笑话我。经此一役，只要一竖管子，我的舌头都软瘫在口腔底部，不敢乱摸乱动，给吓出来的。
但声音是不可琢磨的东西，如何自然地发出声音来，这个秘密不是讲课能讲清楚的。有一天我的同学在二楼向着三楼的顾老师喊：“顾老师上班迟到了。”顾老师上课时表扬了这个同学，他说你们可听见她的声音了？像小云雀一样向我抛出来，听得我浑身舒服。“终于有人发对声音了。”他笑着说。听他那么说，我才知道他忙了半天是在教我们如何正确发声。
孩子的懵懂都是相通的，放牛班的孩子唱半天歌也不见得知道自己在钻研音乐或者合唱艺术，他们只是走在马修老师指出的路上。而孩子们的聪明也是相通的，他们知道哪条路能给人带来快乐，一直走下去会通到天堂。从学校到家里的路十分漫长，原本我们是一路打闹，到桥洞底下打几把牌，在路上偷几个玉米才回家。但现在有点不一样了，所以一路走一路哼哼练谱视唱，时间过得快得多。
和放牛班一样，我们自然而然就获得了小小的成就，初二时荣获了上海市合唱比赛的第二名，因为这个比赛跨越了各年龄组，而我们学校又是一穷二白的烂学校，这也算是奇迹了。遗憾的是我们中间没有一个莫杭治那样的音乐天才，否则顾老师的执教生涯会更添浓重一笔。
以我本人来说，五音不是太全，节奏感就更差了。顾老师肯定明白这一点，记得他试图让我在某次合唱排练时承担三角铁的击打工作。显然我的表现一塌糊涂，此后顾老师就不敢再让我做与节奏相关的任何工作。你们看到电影里的小男生完全抓不住音准，马修老师就安排他做谱架子，这一段让我想到了三角铁，微笑ing。
但顾老师的女中音选择并不多，所以我还是被他弄进了三人组去单独排练。我们参加了另一次比赛，在半决赛被刷了下来。顾老师也许有点失望，但他的情绪没让别人看出来，他只说别的学校都选小小孩子，没变过声，还是有很大区别的，但我们已经够强了，现在所有人都知道我们学校的孩子懂得唱歌。
顾老师五十多岁，微胖身材，他的声音非常好听，松软可口像新出炉的面包，我想他应该能唱相当美的歌，可惜无此耳福。他的手指粗而柔软，击打钢琴时而有力时而灵巧，这样的手指用来做指控合唱团的工作实在很妥当，不信的话你们可以看看马修老师的手指头。后来还见过一个男人拥有顾老师同样的手，这是我痴迷他的原因之一。
顾老师和马修老师的不同是，他从来没有介入我们的个人生活或者思想教育。现在想来他是一个非常职业的教师，除了音乐之外，他和我们没有什么关系，两年的密切接触下来，我只知道他有一个音乐家的女儿，专攻某种乐器。也正是因为他只问音乐而马修老师还介入了孩子们的生活，我才会更吃惊于他的成功，他仅仅通过自己对音乐的热情和专注改变了孩子们的生活。
我的成长路上没有任何艺术的启蒙教育，我出身于理工科家庭，母亲是个从不看电影不读书不听音乐的工人，初中时代是鬼混的三年，高中时间花在准备高考上，大学在医学院里度过。我不是文学爱好者，按某朋友的推理，我缺乏人文教养。如果今天的我对生活甚至艺术还存在一点欣赏的热情，那就是顾老师留下的礼物了。从这个意义上说，他改变了我的生活。音乐可以改变一个人的生活，即使是最简单的音乐。它改变人的方式可以是惊人一致的，比如顾老师与马修老师。
大学时候我去过一次母校，那天顾老师不在。写这篇回忆时去google了一下，找不到他的任何记录，这说明顾老师已经很老了，落后于这个时代了，也说明他日后没有扬名立万。我不知道我的大多数同学散落在哪里，估计没人成为音乐家。
"""

y1292213="""
你在看大话西游的时候，如果笑得腹背抽筋，龇牙咧嘴，那么你很有幽默感。如果你看完了大话西游，你还笑得满地打滚，那么你其实什么都没看懂。如果你看完了大话，你忽然发现脸上不知什么时候已经有泪水，你总算看懂了大话的第一层了。如果你看完大话，笑也笑过了，泪也流过了，忽然怔在那里，忽然觉得不知是该哭还是该笑，那么你看懂第二层了。如果你看完了大话，默默的坐在那里，你感到无处可去，你感到一种深入骨髓的悲哀和无奈,你看懂第三层了。
　　大话西游是个寓言,躲在古老神话的背壳里似乎很搞笑很爱情很世俗很感伤地讲述一个因为时间的渺茫和个体的彷徨所构筑的问题和它不确定的答案。
　　"那个人样子好怪。" "我也看到了，他好像一条狗。" 大话西游的最后一句对白你还记得么。其实这一句，就是整个电影的主题。用男人的思想就是：一个男人的无奈。
　　你喜欢至尊宝，还是喜欢孙悟空？答案不言自明。至尊宝放荡不羁，无拘无绊，但敢爱敢恨，纯真可爱。那么你又仰慕谁？谁是英雄？
　　其实从至尊宝到孙悟空的蜕变，正是反应了一个从男孩到男人的心路历程。
　　"等你明白了舍生取义的道理，你自然会回来和我唱这首歌的。"
　　唐僧是谁？我们是不是想起了我们的父母，我们的老师，我们的前辈。哪一个男人没有经历过他们的谆谆教导，又有哪一个人没有产生过一种强烈的逆反心理，没有反抗。但是，当每一个人成熟起来后，成为了男人，都会由衷地感谢他们的教诲，或者后悔没有听他们的话。
　　"我知道有一天他会在一个万众瞩目的情况下出现，身披金甲圣衣，脚踏七色云彩来娶我。"紫霞仙子是那种令每一个男孩子倾心的女性，她对自己的意中人要求不高，仅此而已，但是试问，你能做到吗？至尊宝做到了吗？他做到了，不过代价却是......其实，紫霞仙子就是我们心目中的女性形象，她的要求就代表了女性对男人的要求。
　　牛魔王又是谁？他代表了这世界上一种无形的力量，他夺走了紫霞，夺走了晶晶，也夺走了至尊宝的快乐。这种力量使至尊宝和他代表的男孩子们失去了往日的伊甸园，要想找回昔日的快乐，就必须战胜它。
　　说到这里，先整理一下思路，看看我们发现了什么。随着牛魔王的出现，至尊宝再也不能享受往日无忧的时光。他要找回心爱的晶晶，也要夺回更加深爱的紫霞。他曾一度寄望于月光宝盒转自，是的，月光宝盒。它有一种神奇的力量，可以使至尊宝避开同牛魔王直接交锋而获得自己想要的东东。其实，每一个男孩子在成长的过程中都曾经有过这样的幻想，但是，面对无情的现实，幻想一次又一次地破灭。直到最后的关头，至尊宝终于醒悟，靠月光宝盒不行，至尊宝更是没有那个本事，只有成为孙悟空，只有戴上那个金刚圈，他才有能力同牛魔王一较高下。
　　这真是一个极大的讽刺。你想要得到吗？那么好吧，你先放弃吧。你必须做出选择，作至尊宝，那么快乐总是很短暂，作孙悟空，你就要忍受无尽的痛苦。这个世界的规则好象是牛魔王制定的，那么恶毒，在它面前，那段经典的台词显得多么的苍白无力，只能成为一个男孩子蜕变成男人的时候留在心底最深的伤痛。
　　唐僧说话的方式从来就没有变过，只是在至尊宝醒悟的前后听来有完全不同的感受。那么至尊宝是自觉自愿的醒悟吗？不，他并不愿意，但是他必须拯救紫霞，必须化解人间的恨，他别无选择。虽然成为了孙悟空，成了大英雄，但他对自己的生存状态极度不满。片子的最后，孙悟空将他心中残存的至尊宝的影子幻化作一位夕阳武士，在对现实世界彻底失望后，只能构造一个虚幻的想象来了却这桩心愿，并借武士的口中表达了对自己生存状态的不满，活得好象是一条狗一样。唉，一个男人的悲怆和无奈。
　　"生又何哀，死又何苦。"
　　很早就听说过，如果你能理解大话中，"他好象一条狗"那么你才是真正理解了《大话》
　　也许我还不能完全明白..............喜欢大话喜欢那种明明相爱却又不能死守终生的遗憾和悲哀。我只能这样骗自己，也许他也有他的苦衷。发现自己真的的接近于疯狂。大概是太过于同情怜悯自己了，才深深地喜欢着这个故事。
      爱情篇罗曼蒂克、海誓山盟、生死相许……面对爱情这些都是琐碎
　　爱情篇罗曼蒂克、海誓山盟、生死相许……面对爱情这些都是琐碎，不值一提。爱情就是爱情，不是别的什么东西。能与爱情同在的只有生命，其他都滚一边儿去. 你爱了，难道还不够吗？
　　悟空爱了，不论晶晶还是紫霞，他都要将爱情进行到底。紫霞爱了，“谁拔出我的紫青宝剑，谁就是我的如意郎君。” 爱一个人需要理由吗？
　　孙悟空会爱白骨精，猪八戒爱上了蜘蛛精。紫霞爱他至深，因为他拔出了一把剑。故事里的人找爱人的理由永远千奇百怪：王子要用水晶鞋才能找到灰姑娘，薛宝钗要那有玉的人来配……可生活永远现实得多，芸芸众生，谁又能许谁一个未来，自欺欺人罢了。
　　有理由也好，没理由也罢，可还是要爱。让我去，过程就是结果，无悔。
　　爱无须掩饰无须矫做无须患得患失，只要像紫霞一样说：“让我们立刻开始这段感情吧！先亲我一下。” 爱是身不由己。
　　至尊宝梦中也要叫紫霞的名字七百四十一次，不知道的人觉得紫霞一定欠了他很多钱。紫霞说：“就象飞蛾，明知会受伤也要扑到火上。”“我无力抗拒，向你狂奔去。”无可救药的痴迷。爱是奋不顾身。
　　至尊宝对晶晶说：“你杀了我吧，我不希望你看我的时候心里却想着别的人。”晶晶以为：“都是骗我的。”跳下崖去。紫霞把身体挡在至尊宝面前，刺进牛魔王的铁叉里。一时间，以后的人生如何，大家都无所谓了。连那样宝贵的性命，也打算随时给爱作了祭品。一个个一头扎进这情爱苦海，宁愿永生永世不得超生。爱深刻莫测。
　　三十娘流着泪说：“想我春三十娘貌美如花，却跟这么丑的人有了。”这是多少美丽自负的女子的宿命：心中的他是能文能武翩翩少年，枕边人却鼾声如雷大腹便便。谁敢说多年后眼望自己的丈夫或妻子不会有如此感觉，真不知幸福还是心酸。不过还是要为他挺身而去无限牺牲，像春三十娘为猪八戒放下断龙石与牛魔王同归于尽。
　　至尊宝爱晶晶，紫霞爱至尊宝，“他爱你你爱我我爱他”，千古无解的方程。所以紫霞说：“爱一个人原来是那么痛苦。
　　至尊宝原以为可以与初恋共度今生，谁知初恋的时候并不懂情爱人生。当年被他推开的紫霞已经悄无声息地抵达他灵魂的最深处，而他却不自知。可紫霞死了：“我的意中人是个盖世英雄，有一天他会踩着七色的云彩来娶我，我猜中了前头，可是我猜不着这结局……” 没有人猜得中结局，一切随风而去。
　　恋爱的时候我们都不懂爱情，懂得爱情后却失去了可以相爱的时间。
　　最绝望不是他不爱你或他离你而去，最绝望是你忘记了怎么去爱一个人，你已丧失了爱的能力。
　　请记住下面的台词：“曾经有一份真诚的爱情摆在我的面前，但是我没有珍惜。等到了失去的时候才后悔莫及，尘世间最痛苦的事莫过于此。如果上天可以给我一个机会再来一次的话，我会对你说三个字”我爱你“。如果非要把这份爱加上一个期限，我希望是一万年！”也顺便记住这段话的原版，在王家卫的《重庆森林》里：“如果记忆是一个罐头，我希望它永远都不会过期，如果一定要加上一个期限的话，我希望是一万年。”
　　至尊宝第一次说这番话是骗紫霞，第二次说已痛不欲生。或许命运是总有一天，我会在灵魂最温柔的一隅为你重复这段话，为了我们即将封存的一万年。
　　此情可待成追忆 只是当时已惘然！
      人或仙，妖或魔，都不能脱离尘世
　　人或仙，妖或魔，都不能脱离尘世，都不会彻底陈腐。《大话西游》无论有多少时空要穿越，无论有多少玩笑要铺陈，无论有多少荒谬要展现，都是一场戏，所以牛魔王包二奶，孙大圣娶妻都在戏里，白晶晶既使没有刷牙，也可以象紫霞一样滴下同样意义泪。在传统港式的搞笑动作恐怖等等一切元素的包装之下，《大话西游》有意义在，有永远流传的风华。
　　“这时候的孩子都是玻璃罐里养蛤蟆，前途光明出路不大。”而你说，在妈那里自己永远是个孩子。居然再贴切不过。大闹天宫无非是20——22岁的黄金时光罢了，找到工作走上社会任你盖世的才华、浑身的个性也自有翻不出的五指山来压。只有戴上紧箍咒取经去，九九八十一难，做一个奇奇怪怪的佛。
　　你别无选择。五百年后的悟空叫至尊宝，在五岳山从事一份很有前途的职业——山贼。命运却要他扮演孙悟空，至尊宝只是个过渡罢了。
　　蜘蛛精来了，白骨精来了，菩你老母来了，牛魔王也来了……都是棋子，安静地立在命运棋盘的中央。
　　他的路线是早定好的：（1）一个人给他三颗痣（2）戴上紧箍咒（3）打败牛魔王（4）西天取经。
　　可怜的至尊宝什么都不知道，认认真真做山贼，还以为爱上了白骨精，和她结为百年之好。所有的事都瞒着他接二连三地发生。
　　真相将揭晓，在我临死的瞬间。
　　给至尊宝三颗痣的人是紫霞仙子。谁说的：如果你要真正了解一个人，就要认认真真的爱她，用心和她在一起。而爱上她就等于失去她，那简直是一定的。
　　非常喜欢紫霞的开场白：“现在我郑重宣布，这座山上所有的东西都是我的，包括你。”那样的气贯云霄，像一个童话故事。
　　而现实是：这个世界没有什么属于你，包括你自己。也许我们就是为了创造属于自己的东西才来到这个世上，因为年轻，所以押注于爱情。至尊宝拒绝了紫霞，他以为自己还爱晶晶。见到晶晶，他又发现紫霞才是真爱。
　　命运一直在同他开玩笑：至尊宝忽然成了孙悟空，千辛万苦找晶晶又爱上了紫霞。而抉择是那样残酷：要打败牛魔王救紫霞，就必须戴上紧箍咒做回神通广大的孙悟空；而戴上紧箍咒就不能有半点情欲，只有取经去。
　　为至尊宝不平：不明白在这样的故事里为何爱情总要成为牺牲品，干嘛不让至尊宝携紫霞纤纤小手——走先！我曾无数次在发表过类似意见，搞得很累。
　　爱情是那样美丽而脆弱，无法直面生活的琐碎和坚韧。哪段感情又没有绚烂的瞬间和艰难的长久，在一起就会幸福吗，未必。未必的未必，也未必。我可以等待，这是个决定。
　　至尊宝挖开自己的心，看到了紫霞留在那里的一滴眼泪，毕竟曾经沧海过。五百年又五百年，兜了一个大圈子又回到了原地。人没能战胜命运，而人的尊严却在抗争中得到了肯定，人的情感也必将不朽。
　　“生亦何欢，死亦何苦。”大彻大悟。紧箍咒，圈住昔日的梦想，圈住棱角分明的个性。成熟是一个很痛的词，它不一定会得到，却一定会失去。望着荧幕上渐渐飘远的紫霞，忽地明白了其实这是很自私的结局，这就是自私的好处至尊宝忘记或记得自己都不重要全片最后一句台词是：“你看那个人，好奇怪哟，象一条狗。”总有一天你也会走在路上，象一条狗。 
"""
y1291841="""

"""

y1291560="""
森林里藏匿着一种神奇的生物，它的名字叫多多洛。

它有着圆滚滚的庞大身躯与软软的毛，晚上会领着自己的小朋友在树枝的最顶端吹出悠扬的乐曲，下雨的时候戴着一顶荷叶小帽，要回家的时候则召来它威风凛凛的龙猫公交车。

你只能巧遇它，却无法找寻它。它会慷慨地帮助小朋友，只要它乐意。它淘气又无邪，如果你第一次见到它，不要被它惊天动地的吼叫声吓到，它只是在同你玩，你要像孩子一样，奋力地、尽情地以你最大的叫声回敬它的吼叫——什么时候我们开始无法像孩子一样肆意地大呼小叫了？心里的小情绪堆积得像山一样高，直到溢出来。与其如此，不如永远像孩子一样。他们发出听起来刺耳的清脆叫声，他们哭了，他们笑了，于是他们也就没有什么好烦恼的了。

我要和多多洛做朋友，我幻想着我认识它以后它也能送我一包种子，我把种子播撒在门口的土地，不知为什么那片地却没长出什么来。一天傍晚它带着我一起祈祷，用心的强大魔力，一使劲儿，只见小小的幼苗破土而出，转眼间就长成参天大树。我笑着笑着眼泪都掉了下来。

在人生的旅途上，年龄不能返程，心境却可以峰会路转。一部好电影的功效便是如此。我想今晚多多洛没准儿就会爬到我的梦里来了。
"""

y1292064="""
版权归作者所有，任何形式转载请联系作者。
作者：DIANLIN（来自豆瓣）
来源：https://movie.douban.com/review/1028479/


我们的时代究竟是一个怎样的时代？技术的发展、物质的充裕，究竟是解放了人还是束缚了人？究竟是把人推向了更加自主的方向，还是把他更加置于自己的对立面，更加失去了自我，更加远离了真实的世界和鲜活的人生？
 
《楚门的世界》用一个近乎残忍的故事，以一种寓言式的叙事，给了我们一个耐人寻味的回答。
 
很显然，楚门只属于楚门的世界——一个被操纵的虚拟世界。他的出生、成长，一切的喜怒哀乐，如果不出意外的话，包括他的死亡，都将在一个被人为操纵和设计好的舞台上上演，并被无以计数的生活于光鲜富足的现代世界的男男女女们驻足观看。他们与楚门融为一体，一起经历着成长的历程，离开楚门，他们的生活将无以为继，世界将大乱，生活将没有意义。
 
但一场被设计好的持续了三十年之久的旷古未有的真人秀，却终因楚门的疑心和探求欲被击碎了。在楚门历经了人造的风暴、雷电、巨浪的考验后，承载着他走向真相的船，无情地撞破了那个蓝得刺眼的美丽但却虚假的天空。在那一刹那，一个神话结束了，一个阴谋被置于阳光之下。更为重要的是，这深深的撞击，证明只要人性尚存，心灵是无法被永远操纵的。
 
然而，楚门又绝不仅仅属于楚门的世界。他同时就是生活在这个弥漫着电子硝烟的世界里的你和我。
 
从出生，到成长，到死去，我们对世界的认识，从来是都是局限的，我们永远无法做到像万能的上帝那样，可以对这个世界了然于胸。我们不得不借助于各种载体来超脱我们的肉体樊篱，从而使得心灵可以通达久远的过去，遥想漫长的未来，想象异邦的人世间，以满足我们无限的好奇心和知识欲望。在这个意义上，我们不得不赞同麦克卢汉的至理名言：“媒介是人体的延伸”。
 
然而，文明发展的吊诡正在于，它常常走向自身的反面，成为剥夺自由和消解主体性的帮凶。今天，电子媒介在全球范围内的普及和迅速扩张，已经完全实现了麦克卢汉关于“地球村”的天才预言。也正因为如此，全世界的人们才得以在同一个地球上，同时观看楚门的世界，从而在如此广袤的时空范围内把人性中的窥探欲演绎得如此淋漓尽致。
 
现实的悲剧性正在于，在这个媒介的时代，谁都难以逃脱楚门的命运，谁也没有十足的底气说自己与楚门无关。在各种形式的电视真人秀节目中，难道我们不会见到楚门的影子吗？当我们在为超级女声而狂热欢呼的时候，难道我们不会在自己的身上看到那些抱着电视与楚门厮守的观众的影子吗？在经济利益驱动一切的今天，商业逻辑的泛滥，已经逼迫我们不得不把我们自己玩弄于股掌之间，我们只有自娱自乐，并在狂欢的刹那间，出卖我们的金钱、隐私、自由，乃至生命。
 
如此看来，《楚门的世界》作为一个时代性的操纵隐喻，不仅讲述了真实和虚假的边界问题，更重要的则是提醒我们走出时代的骗局，走近我们的心灵，在一种顽强的反思中，保有一份不那么时髦的自由。
  
"""
y1300267="""
我上高中的时候有一个同学的家长在电视台工作，于是我就有了很多借录像带的机会。当时阴错阳差的借了一部长达三个多小时的电影《乱世佳人》。当时我没看过《飘》，对这部电影更是没有概念。完全是为了打法时间而看，一看就欲罢不能。
        
影片一开始吸引我的当然是美丽的南部风光与南方美女。绿草地上一座如同奶油蛋糕般美丽的白色庄园，穿着白色蓬蓬裙的郝斯嘉明眸皓齿，猫一样灵动的绿色眼珠左顾右盼，看究竟选哪位幸运的年轻男士去拿饮料。这样的任性，倔强，意气风发，这样的美丽，又如同一个普通的女孩一样充满缺陷，所以情路坎坷。

可这些，南部的塔拉庄园，穿着军服的美国男人，19世纪的大蓬蓬裙，还有黑妈妈灰色罩服下的巨大红色纱裙在类似的电影里也能窥之一二，郝斯嘉单恋的爱情故事更不是什么希世珍品。只有白瑞德迷人的小胡子和性感的声音还算特别。不过就算再加上费雯·丽的绝世容颜，单凭这些也不会让我在这么多年里一直念念不忘。

我忘不了的，是电影里南北战争时郝斯嘉带着梅兰妮顶着炮火纷飞一路出逃，白瑞德与郝斯嘉在橙红色的冲天火光里深深亲吻的剪影；我忘不了的，是郝斯嘉从容的扯下绿色天鹅绒的窗帘围到身上，眼珠一转计上心来的小聪明小得意；我忘不了的，是郝斯嘉重回塔拉庄园发现田地荒芜家业衰败，她在紫红色的夕阳照耀下从田地里拔出来一个萝卜，连泥土都未擦去就狠狠的咬了一口。这个倔强的女人面对夕阳，双手握拳高举双臂用尽全身的力气向苍天呐喊：“我以后绝不挨饿！”悲壮又舒缓的音乐这时候突然响了起来，郝斯嘉纤细的背影在夕阳下投下长长的影子。

很难说这部电影，还有后来读的《飘》究竟给我的人生以什么启示。可是郝斯嘉绝不挨饿的宣言，还有她在紫红云霞里的背影却永远永远的留在了我的心里。这部电影我一共看了五次，这个片断竟让我五次落泪。不管我是否喜欢郝斯嘉的个性，不管我是否容忍郝斯嘉的缺点，这样的坚定与勇气，这样连战乱都打不夸的女人，生命力顽强的如同春天的野草。看到她，生活就总有希望，不管面对什么样的困难。 
"""

y1291828="""
《天堂电影院》，这次看的是导演剪辑版，长达2小时53分钟。Giuseppe Tornatore这“时空三部曲”中，我还是最喜欢《天堂电影院》。《西西里的美丽传说》像个春宵一刻的梦，它只能成为记忆中的闪光；而《海上钢琴师》，正如它的名字，是一个Legend，1900不是一个人，更像是一个影子，一个躲在世俗背后单纯的影子，一个无法脱离海洋无法适应陆地的影子。上岸，他不是偏执，而是害怕；《天堂电影院》是每个人的童年，每个人的家乡，每个人的初恋，是最后绵绵长长一直伴随到死，渗透到了血液里灵魂里的记忆和感觉。当老Toto30年后重新踏上这片熟悉的土地的时候，那感觉丝毫未变，但周遭的人，物，景却早已天翻地覆，阴阳两隔，回天无术。我最喜欢的也是头发发白，功成名就的老Toto返乡的那段，他只有回到这里，才回到自己的心里。

Alfredo
Alfredo和Toto之间亦父亦友的爱成为贯穿全剧的一条线。Alfredo帮拿了买牛奶钱看电影，被妈妈发现打的Toto解围，Toto帮参加资格考试不会答题的Alfredo作弊，对于电影和放映机的共同爱好，让这两人成了忘年之交。但是Alfredo不希望Toto跟他一样，局限在这个几平米的放映室里，耗上一生的时光。这就是他执意让Toto离开，甚至不惜牺牲了Toto的初恋的原因。他像一个父亲一样希望自己的儿子可以在更大的空间里施展拳脚，因为他知道这个小镇的恬淡和平静最终会锁住这个孩子的潜力。Alfredo说，不准回来，不准想起我们，不准回头，不准写信。如此深沉的爱，大致Toto老了之后，成功了之后才会明白的。

Elena和母亲
和Elena的旧爱重逢是长版和短版的最重要区别。显然，作为一部电影，短版恰到好处，长版就画蛇添足了。但是之所以有个导演剪辑版，大概是为了给刨根问底的人一个交代，当然，也是给自己的青春一个完整的祭奠。那一段，虽然看着动人，但是因为它的不可能，它的挽歌性质，让我觉得无甚于有。毕竟逝者已矣，越追究越无奈，越追究越无法释怀。还有，Toto和妈妈的亲情戏也是一个看点，刚开始的时候，觉得妈妈对Toto很苛刻，甚至有点野蛮和不讲道理，但是慢慢地，尤其是在取了父亲的阵亡书回家的路上，妈妈拉着Toto的手，走着，后来搂了搂他的肩，我才看见这个母亲的坚强。长版中有一段Toto和母亲的促膝谈心，颇为煽情。母亲说每次她都要等到他放映回来，看到他睡了才偷偷下去锁上门，自从他走后，她已经30年没锁过门了，她干脆把锁拿了下来。最后母亲还对Toto轻轻说了一句话，忘了她吧。那个她，就是Elena。母亲终究是母亲，无论相距多远，相隔多少年，还是能看到心里头的那个人。

士兵的故事
Toto刚爱上Elena的时候，Alfredo给他讲过一个士兵的故事：从前，有一个国王为他的公主举办宴会，有个卫兵看见公主走过，她实在太美了，他立刻坠入情网，爱上了她。但是卑微的士兵哪配的上公主？后来，他终于有机会告诉她他不能没有她，公主深深地受感动，她告诉士兵：你如果连续100个昼夜守在我的阳台下，我就以身相许。于是士兵等了1天，2天，10天……公主每晚都可以看见他，刮风下雨，他都不走，但是到了第99夜，士兵起立，搬起椅子，走了。后来，Elena和Toto分开，在海边，Toto告诉Alfredo他知道了士兵为什么要放弃了，因为要是等到100天，公主却毁约，士兵会心碎而死，所以他在前一晚离开，好让公主永远记得他。我是早就知道这个答案了，在很多年前看《东京爱情故事》，赤名莉香登上早一班火车开始就知道了，她也怕等到最后一刻，她的完子还是不来。她和完子注定只是两条只有一个交点的直线，完成了短暂的相遇就要离开。因为缺憾，所以美好。 

"""



from app.models import Movie
from app import db
# y1=Movie(movieid=1292052,bigComment=y1292052,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y2=Movie(movieid=1291546,bigComment=y1291546,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y3=Movie(movieid=1295644,bigComment=y1295644,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y4=Movie(movieid=1292720,bigComment=y1292720,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y5=Movie(movieid=1292063,bigComment=y1292063,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y6=Movie(movieid=1291561,bigComment=y1291561,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y7=Movie(movieid=1295124,bigComment=y1295124,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y8=Movie(movieid=1292722,bigComment=y1292722,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y9=Movie(movieid=3541415,bigComment=y3541415,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y10=Movie(movieid=2131459,bigComment=y2131459,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y11=Movie(movieid=1292001,bigComment=y1292001,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y12=Movie(movieid=3793023,bigComment=y3793023,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y13=Movie(movieid=3011091,bigComment=y3011091,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y14=Movie(movieid=1291549,bigComment=y1291549,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y15=Movie(movieid=1292213,bigComment=y1292213,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y16=Movie(movieid=1291841,bigComment=y1291841,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y17=Movie(movieid=1291560,bigComment=y1291560,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y18=Movie(movieid=1292064,bigComment=y1292064,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y19=Movie(movieid=1300267,bigComment=y1300267,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# y20=Movie(movieid=1291828,bigComment=y1291828,rate1=0.0,rate2=0.0,rate3=0.0,rate4=0.0)
# db.session.add_all([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,
#                     y11,y12,y13,y14,y15,y16,y17,y18,y19,y20])
db.session.commit()