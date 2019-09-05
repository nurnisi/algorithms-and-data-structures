# 355. Design Twitter
import collections
class Twitter:
    def __init__(self):
        self.userFollows = collections.defaultdict(set)
        self.tweetFeed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetFeed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for i in range(len(self.tweetFeed)-1, -1, -1):
            uid, tid = self.tweetFeed[i]
            if uid == userId or uid in self.userFollows[userId]:
                feed.append(tid)
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)