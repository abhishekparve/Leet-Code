# https://leetcode.com/problems/design-twitter/solutions/6450077/designing-twitter-efficient-tweet-retrieval-using-heaps-and-hashmaps/
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # (count, tweetId)
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId):
        res = []
        maxHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append((count, tweetId, followeeId, index - 1))
        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, (count, tweetId, followeeId, index - 1))
        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


answer = Twitter()
answer.follow(1, 1)
answer.follow(1, 2)
answer.follow(1, 3)
# answer.unFollow(1, 3)

answer.postTweet(1, 65)
answer.postTweet(2, 66)
answer.postTweet(1, 67)
answer.postTweet(2, 68)
answer.postTweet(3, 69)
answer.postTweet(3, 70)
print(answer.getNewsFeed(1))
