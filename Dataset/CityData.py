# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:13:53 2016

@author: Nisarg
"""
from pattern.en import sentiment,positive
import twitter, sys, json,random

reload(sys)
sys.setdefaultencoding("utf-8")

myApi=twitter.Api(consumer_key='1o3v5Pr1hGaLUHqqGL6TFKRrT', \
                  consumer_secret='tKCogd7AcGtE7COcKn2i3b3M5FZ6RMYgFn0ai7JUnmzCaIxfiA', \
                  access_token_key='700554121225441280-tXHu522OXBgrK5571QBlIAJOxEHUnpL', \
                  access_token_secret='2CIBJFtcznr1emzvV1PtdXICqk3gduyyO2zyvFEuaE0Du')

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
    geo = ('34.0201812','-118.6919205', '500mi') # City of Los Angeles
    f=open('losangelesdata.txt','w')   
    MAX_ID = None

    for it in range(10):
        raw_tweets = myApi.GetSearch(None, geo, count=100, max_id = MAX_ID)
        tweets = [json.loads(str(raw_tweet)) for raw_tweet in raw_tweets]
        MAX_ID = tweets[-1]['id']
        
        for raw_tweet in raw_tweets:
            tweet = json.loads(str(raw_tweet))
            f.write(tweet['text']+"\n")
        if tweets:
            MAX_ID = tweets[-1]['id']

def rest_query_ex2():
    query = 'Bernie OR Sanders OR President OR Election 2016 OR Democrat OR Vote OR Campaign OR feelthebern OR bernie OR politics OR debate OR poll OR delegate OR voters OR campaign OR caucus OR candidate OR Presidential OR BernieSanders'
    geo = ('43.61656', '-116.2008349','150mi') # City of Los Angeles
    f=open('BERNIE_BOISE_DATA.txt','w')   
    MAX_ID = None

    for it in range(20):
        raw_tweets = myApi.GetSearch(query, geo, count=200, max_id = MAX_ID,result_type='recent')
        tweets = [json.loads(str(raw_tweet)) for raw_tweet in raw_tweets]
        MAX_ID = tweets[-1]['id']
        
        for raw_tweet in raw_tweets:
            tweet = json.loads(str(raw_tweet))
            f.write(tweet['text']+"\n")

        
         
def rest_query_ex3():
    query = 'election2016 OR trump OR clinton OR republican OR democratic'
    geo = ('34.0201812','-118.6919205', '500mi') # City of Los Angeles
    MAX_ID = None
    f=open("LA_DATA_RECENT.txt",'w')
    for it in range(10): # Retrieve up to 500 tweets
        tweets = [json.loads(str(raw_tweet)) for raw_tweet \
                  in myApi.GetSearch(query, geo, count = 1000, max_id = MAX_ID, result_type='recent')]
        f.write(str(tweets)+'\n')
        if tweets:
            MAX_ID = tweets[-1]['id']
            print MAX_ID, len(tweets)



'''
def rwithoutm():

    with open('randomdata.txt') as f1:
        lineset = set(f1)
    with open('data.txt') as f2:
        lineset.difference_update(f2)
    with open('rwithoutm.txt', 'w') as out:
        for line in lineset:
            out.write(line)
    
def files():
    F = open('F.txt', 'w')
    I = open('I.txt', 'w')
    G = open('G.txt', 'w')
    J = open('J.txt', 'w')

   

    f1 = open('rwithoutm.txt')
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




'''

def main():
    #for i in range(10):
       # rest_query_ex1()
        rest_query_ex2()
        #rest_query_ex3()
        #rwithoutm()
        #files()
        pass
    
        
        

if __name__ == '__main__':
    main()
    
"""
Without filtering on location, retrieve tweets that contain the phrase 'road accident'. 
Note that if the query is 'road accident' instead of '"road accident"', then the 
returned queries will match both 'road' and 'accident' but not the phase "road accident"
"""
"""
Retrieve tweets that are related to traffic congestions in the city of Albany 
"""

