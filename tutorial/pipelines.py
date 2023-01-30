# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os
PATH = 'output'


from .redis_settings import *
import redis

class RedisWriterPipeline(object):
    """
    写入redis数据库的pipline
    """

    def __init__(self):
        self.file = None
        if not os.path.exists(PATH):
            os.mkdir(PATH)

    def process_item(self, item, spider):
        """
        处理item
        """
        r = redis.StrictRedis(host='localhost', port=REDIS_PORT, db=DATABASE)
        topic_url = item['url']
        topic_id = topic_url.split('/')[-2]
        topic_title = item['title']
        topic_content = item['content']
        topic_comments = item['comments']
        topic_author = item['author']
        topic_author_link = item['author_link']
        topic_created_time = item['create-time']
        topic_created_ip = item['create-ip']
        r.sadd(redis_douban_group_all_groups, item['group'])
        r.sadd(redis_douban_group_all_topics.format(groupid=item['group']), topic_id)
        r.set(redis_douban_group_topic_author.format(topicid=topic_id), topic_author)
        r.set(redis_douban_group_topic_author_link.format(topicid=topic_id), topic_author_link)
        r.set(redis_douban_group_topic_created_time.format(topicid=topic_id), topic_created_time)
        r.set(redis_douban_group_topic_created_ip.format(topicid=topic_id), topic_created_ip or '')
        r.set(redis_douban_group_topic_url.format(topicid=topic_id), topic_url)
        old_topic_content = r.get(redis_douban_group_topic_content.format(topicid=topic_id))
        # 原本没有内容时，添加内容
        if old_topic_content == None:
            r.set(redis_douban_group_topic_content.format(topicid=topic_id), topic_content)
        # HACK: 当新内容长度大于旧内容时才更新
        elif len(topic_content) > len(old_topic_content):
            r.set(redis_douban_group_topic_content.format(topicid=topic_id), topic_content)
        r.set(redis_douban_group_topic_title.format(topicid=topic_id), topic_title)
        # HACK: 如果评论内容修改了，会新增加一条
        for topic_comment in topic_comments:
            r.sadd(redis_douban_group_topic_comments.format(topicid=topic_id), topic_comment)
        r.save()
        return item

