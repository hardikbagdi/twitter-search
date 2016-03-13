import oauth2
import urllib
import json
import sys
#insert you key and secret below
#this is application only authentication
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
consumer = oauth2.Consumer(key=consumer_key, 
	    secret=consumer_secret)
request_token_url = "https://api.twitter.com/oauth/request_token"
search_tweet_url = "https://api.twitter.com/1.1/search/tweets.json"
#init oauth client, used in subsequet queries

def searchtwitter(search_query):	
	try:
		client = oauth2.Client(consumer)
		resp, content = client.request(request_token_url, "GET")
		data = {'q': search_query,'count' : 1}
		body = urllib.urlencode(data)
		query_url = search_tweet_url+ '?' + body
		resp,content = client.request(query_url, method="GET")
		json_response = json.loads(content)
		statuses = json_response['statuses']
		if (len(statuses) == 1):
			print '@'+urllib.unquote(statuses[0]['user']['screen_name'])+':'+urllib.unquote(statuses[0]['text'])
			if( 'media' in statuses[0]['entities'] and len(statuses[0]['entities']['media']) >=1):
				print 'media:'
				print urllib.unquote(statuses[0]['entities']['media'][0]['media_url'])
		else:
			print 'No tweet found for the keyword.'
	except Exception,e:
		print 'Exception'
		print str(e)
	return

if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print 'Please provide keyword to search.'
		print 'Usage: python script.py <keyword>'
		sys.exit()
	else:
		searchtwitter(sys.argv[1])