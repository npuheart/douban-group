# douban-group
每天爬取豆瓣小组的内容

1. 在首页最近讨论的链接
<img width="477" alt="image" src="https://user-images.githubusercontent.com/115222128/215251954-011b798e-9941-4b04-8578-6f5b52763364.png">
2. 爬取每个讨论中的内容
<img width="721" alt="image" src="https://user-images.githubusercontent.com/115222128/215251940-990a9141-3636-411d-a6e1-fb3ffca1917a.png">
3. 将爬取的数据保存在redis数据库中
4. 将数据生成json文件
<img width="594" alt="image" src="https://user-images.githubusercontent.com/115222128/215252104-9f1e28d9-c03b-45a9-a779-80145c96f789.png">

## docker
1. 先为项目创建网桥 `sudo docker network create douban-group`
2. `cd docker && sudo docker-compose build`
3. `sudo docker-compose -d up`

如果修改了`docker/conf`文件夹下的文件，则需要重新构建镜像。

## 从数据库生成json文件
1. 启动数据库 `redis-server --port 13849`
2. `python3 convert.py`

