import feedparser
from jinja2 import Template

my_author_name = 'Gineesh Madapparambath'
#rss_feed_url = 'https://www.techbeatly.com/feed/atom/?paged=3'
rss_feed_url = 'https://www.techbeatly.com/feed'
NewsFeed = feedparser.parse(rss_feed_url)

print('Number of RSS posts :', len(NewsFeed.entries))

entry = NewsFeed.entries[1]
# ['summary_detail', 'published_parsed', 'links', 'title', 'summary', 'guidislink', 'title_detail', 'link', 'published', 'id']
#print(entry)
print('Post Title :',entry.title)

for entry in NewsFeed.entries:
  print('Author:',entry.author,': Post Title :',entry.title)
  if entry.author == my_author_name:
    print('Take it')
    print(entry.link)
    print(entry.title)
    print(entry.published)
    print(entry)