1、老师账号
1303845892@qq.com   nmb_python
2、学生账号
408848063@qq.com    nmb_python
3、老师登陆接口信息
url:https://www.ketangpai.com/UserApi/login
request:email=1303845892%40qq.com&password=nmb_python&remember=0
4、创建课程接口信息
url:https://www.ketangpai.com/CourseApi/createCourse
request:coursename=webauto&relation=0&teachClassid=&neednatureclass=0&needgrade=0&needentrance=0&coid=&canview=0&classname=yss&semester=2020-2021&term=1
response:{"status":1,"info":"success","state":0,"data":{"id":"MDAwMDAwMDAwMLSsqd6IubNr","coursename":"webauto","code":"828M2B",
"username":"IDO","minpic":"\/\/assets.ketangpai.com\/theme\/min\/08.jpg","bannercolor":"#318eeb","total":"0","hlist":[],"role":1,"tips":"success"}}
5、删除课程接口信息
url:https://www.ketangpai.com/CourseApi/delCourse
request:courseid=MDAwMDAwMDAwMLSsqd6IubNr&password=nmb_python
response:{"status":1,"info":"\u5220\u9664\u6210\u529f"}