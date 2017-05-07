"""
Julia and Nisarg worked on the collecting tweets and API recall.
"""

import twitter, sys, json
from pattern.en import positive
import random

reload(sys)
sys.setdefaultencoding("utf-8")

myApi=twitter.Api(consumer_key='ZWk455L3W3KdK3k1W8bjUxFer', \
                  consumer_secret='76cPwbWZ88hDA4lhBrMy4mFXqfaK6FPqWxns7hKlxkIWthF8VF', \
                  access_token_key='3087724435-e0zd5WxOJgkivEhkTotjiY4AbTtQwudX2GVBMIy', \
                  access_token_secret='r1xpWHTRGPYjEH14FY1tCG6wbXPRFFZUOSt6UihN24Be6')

def print_info(tweet):
    print '***************************'
    print 'Tweet ID: ', tweet['id']
    print 'Post Time: ', tweet['created_at']
    print 'User Name: ', tweet['user']['screen_name']
    try:
	    print 'Tweet Text: ', tweet['text']
    except:
		pass

def rest_query_ex1():
	
    geo = ('41.3833', '2.1833', '750mi') # City of Barcelona
    f=open('r.txt',"w")
    MAX_ID = None
    for it in range(5): # Retrieve up to 200 tweets
        tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                in myApi.GetSearch(None, geo, count = 100, max_id = MAX_ID, result_type='recent')]
    	for raw in tweets:
    		f.write(str(raw['text'])+",False,"+str(reset())+ '\n')
    		#file.write(str(raw)+ '\n')
    	if tweets:
			MAX_ID = tweets[-1]['id']
			print MAX_ID, len(tweets)

def rest_query_ex2():
    query = '(congestion OR jam OR block) AND \
             (road OR highway OR street OR lane OR traffic OR car OR vehicle OR bus)'
    geo = ('42.6525', '-73.7572', '9mi') # City of Albany
    raw_tweets = myApi.GetSearch(query, geo)
    for raw_tweet in raw_tweets:
        tweet = json.loads(str(raw_tweet))
        print_info(tweet)
         
def rest_query_ex3():
	
    query = ' fcb OR messi OR xavi OR espana OR barca OR barcelona OR football OR soccer OR campnou OR forca barca OR barcafans OR neymar OR iniesta OR fcbarcelona OR laliga OR suarez '
    geo = ('41.3833', '2.1833', '500mi') # City of Barcelona
    f=open('results.txt',"w")
    MAX_ID = None
    for it in range(5): # Retrieve up to 200 tweets
        tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                in myApi.GetSearch(query, geo, count = 100, max_id = MAX_ID, result_type='recent')]
    	for raw in tweets:
    		f.write(str(raw['text'])+",True,"+str(reset())+'\n')
    		#file.write(str(raw)+ '\n')
    	if tweets:
			MAX_ID = tweets[-1]['id']
			print MAX_ID, len(tweets)

    #f=open('results.txt',"w")
    #file3= open('results.txt',"r")
    

   
           
	# f.close()       
def neel():
	

    F = open('F.txt', 'w')
    I = open('I.txt', 'w')
    G = open('G.txt', 'w')
    J = open('J.txt', 'w')
    
    with open('r.txt') as f1:
        lineset = set(f1)
    with open('results.txt') as f2:
        lineset.difference_update(f2)

    for line in f1.readlines():
        word = line.split(',')
        if word[1].strip() == 'True':
            if word[2].strip() == 'True':
                F.write(line)
            else:
                I.write(line)
        else:
            if word[2].strip() == 'True':
                G.write(line)
            else:
                J.write(line)
    

def main():
    #for i in range(10):
    rest_query_ex1()
    rest_query_ex3()
    
    
    
    #rest_query_ex3()
    pass

if __name__ == '__main__':
    main()
    
