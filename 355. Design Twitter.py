class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = {}
        self.f = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.t:
            self.t[userId] = []

        self.t[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.t and userId not in self.f:
            return []

        res = []
        if userId in self.t:
            for tw in self.t[userId]:
                res.append(tw)

        if userId in self.f:
            for user in self.f[userId]:
                if user in self.t:
                    for tw in self.t[user]:
                        res.append(tw)

        res = sorted(res, key=lambda x: x[0], reverse=True)
        answer = []

        for i in range(10):
            if i == len(res):
                break
            answer.append(res[i][1])

        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.f:
            self.f[followerId] = []

        if followerId != followeeId and followeeId not in self.f[followerId]:
            self.f[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.f:
            self.f[followerId] = []
            return

        if followeeId in self.f[followerId]:
            self.f[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)