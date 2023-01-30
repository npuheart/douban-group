# 数据库设置

REDIS_PORT = 6379
DATABASE = 1



# url
# title
# time
# content
# comments
redis_douban_group_all_topics     = 'douban:group:all:topics:groupid:{groupid:s}'
redis_douban_group_topic_url      = 'douban:group:topicid:{topicid:s}:url'
redis_douban_group_topic_title    = 'douban:group:topicid:{topicid:s}:title'
redis_douban_group_topic_time     = 'douban:group:topicid:{topicid:s}:time'
redis_douban_group_topic_content  = 'douban:group:topicid:{topicid:s}:content'
redis_douban_group_topic_comments = 'douban:group:topicid:{topicid:s}:comments'
redis_douban_group_topic_author      = 'douban:group:topicid:{topicid:s}:author:name'
redis_douban_group_topic_author_link      = 'douban:group:topicid:{topicid:s}:author:link'
redis_douban_group_topic_created_time      = 'douban:group:topicid:{topicid:s}:created:time'
redis_douban_group_topic_created_ip     = 'douban:group:topicid:{topicid:s}:created:ip'
