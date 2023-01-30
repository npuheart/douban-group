
# extract data and write it into a json file

import json
import os
PATH = 'output'
JSONFILE = 'data.json'

from tutorial.redis_settings import *
import redis


r = redis.StrictRedis(host='localhost', port=REDIS_PORT, db=DATABASE)

all_data = {}
for group in r.smembers(redis_douban_group_all_groups):
    group = group.decode('utf-8')
    data = []
    for i in r.smembers(redis_douban_group_all_topics.format(groupid=group)):
        topic_id = i.decode('utf-8')
        topic_content = r.get(redis_douban_group_topic_content.format(topicid=topic_id))
        topic_title = r.get(redis_douban_group_topic_title.format(topicid=topic_id))
        topic_url = r.get(redis_douban_group_topic_url.format(topicid=topic_id))
        topic_author = r.get(redis_douban_group_topic_author.format(topicid=topic_id))
        topic_author_link = r.get(redis_douban_group_topic_author_link.format(topicid=topic_id))
        topic_created_ip = r.get(redis_douban_group_topic_created_ip.format(topicid=topic_id))
        topic_created_time = r.get(redis_douban_group_topic_created_time.format(topicid=topic_id))
        print(topic_title,topic_id,topic_url,topic_content)
        topic_comments = []
        for comment in r.smembers(redis_douban_group_topic_comments.format(topicid=topic_id)):
            topic_comments.append((comment or b'').decode('utf-8'))
        topic_comments = sorted(topic_comments)
        topic = {}
        topic['id'] = topic_id
        topic['content'] = (topic_content or b'').decode('utf-8')
        topic['title']= (topic_title or b'').decode('utf-8')
        topic['url'] =  (topic_url or b'').decode('utf-8')
        topic['comments'] = topic_comments
        topic['author'] = (topic_author or b'').decode('utf-8')
        topic['author_link'] = (topic_author_link or b'').decode('utf-8')
        topic['create-time'] = (topic_created_time or b'').decode('utf-8')
        topic['create-ip'] = (topic_created_ip or b'').decode('utf-8')
        data.append(topic)
    data = sorted(data, key=lambda s: s['create-time'], reverse=True)
    all_data[group] = data
    

with open(JSONFILE, 'w' ,encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)
