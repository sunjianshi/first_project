import redis
from redis import Redis
import time
from IPython import embed
from collections import Counter
from random import randint

# res = redis.StrictRedis(host='127.0.0.1', port=6379)
res = Redis(host='127.0.0.1', port=6379, db=11)
res.set('name', 'sunjianshi')
print(res.get('name'))

res.zincrby('name', 23)
# res.zadd('article_click', 1, 123)
# res.zadd('article_click', 2, 456)
# res.zadd('article_click', 3, 321)
# res.zadd('article_click', 4, 351)
# res.zadd('article_click', 5, 371)
# res.zadd('article_click', 6, 311)
# res.zadd('name',)

s = res.zrevrange('article_click',0,3,withscores=True)
print(s)
