"""
355. Design Twitter
https://leetcode.com/problems/design-twitter/description/

Medium

TC: 
SC: 
"""

"""
Optimizations:
  - use a set for following instead of list
  - tweets are a map for each user
  - only store last 10 tweets by each user
  - sort the list of following tweets before return
"""

import heapq


class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.tweet_number = 0

    def post_tweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            if len(self.tweets[userId]) > 9:
                self.tweets[userId].pop(0)
            self.tweets[userId].append([self.tweet_number, tweetId])
        else:
            self.tweets[userId] = [[self.tweet_number, tweetId]]

        self.tweet_number += 1
        return

    def get_news_feed(self, userId: int) -> List[int]:
        feed = []
        if userId in self.tweets:
            feed.extend(self.tweets[userId])

        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.tweets:
                    feed.extend(self.tweets[followeeId])

        feed.sort(key=lambda x: x[0], reverse=True)

        return [tweet[1] for tweet in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        else:
            self.follows[followerId].remove(followeeId)
        return


"""
Below is the initial implementation
The class is fully functional but unoptimized
"""


class TwitterUnoptimized:

    def __init__(self):
        self.tweets = []  # list of all tweets where each item is [userId, tweetId]
        self.follows = {}  # maps userId to list of following userId

    def post_tweet(self, userId, tweetId):
        self.tweets.append([userId, tweetId])
        return

    def get_news_feed(self, userId):
        following_list = [userId]
        if userId in self.follows:
            following_list += self.follows[userId]
        user_feed = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if len(user_feed) >= 10:
                return user_feed
            if self.tweets[i][0] in following_list:
                user_feed.append(self.tweets[i][1])
        return user_feed

    def follow(self, followerId, followeeId):
        if followerId in self.follows:
            self.follows[followerId].append(followeeId)
        else:
            self.follows[followerId] = [followeeId]
        return

    def unfollow(self, followerId, followeeId):
        if followerId not in self.follows:
            return
        else:
            for i, followee in enumerate(self.follows[followerId]):
                if followee == followeeId:
                    self.follows[followerId].pop(i)
        return
