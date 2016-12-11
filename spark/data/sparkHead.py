from pyspark import SparkContext
import itertools

#generates user, coviews for step 3
def generateUserItemPair(userList):
	l = []
	for i, j in itertools.combinations(userList[1], 2):
		l.append((userList[0], (i,j)))
	return l


sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access2.log", 2)     # each worker loads a piece of the data file

#1. Read data in as pairs of (user_id, item_id clicked on by the user)
userItems = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition

#2. Group data into (user_id, list of item ids they clicked on)
userLists = userItems.groupByKey()
userLists = userLists.map(lambda x: (x[0],set(x[1])) )

#3. Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on
userItemPairs = userLists.flatMap(generateUserItemPair)

#4 Transform into ((item1, item2), list of user1, user2 etc) where users are all the ones who co-clicked (item1, item2)
itemPairUserList = userItemPairs.map(lambda x : (x[1],x[0]));

#pretty sure they're already distinct, check later
itemPairUserList = itemPairUserList.distinct();


# 5. Transform into ((item1, item2), count of distinct users who co-clicked (item1, item2)

itemPairNumber = itemPairUserList.map(lambda x: (x[0], 1) )
itemPairCount = itemPairNumber.reduceByKey(lambda x, y: x+y)


#6, Filter out any results where less than 3 users co-clicked the same pair of items
itemPairCount = itemPairCount.filter(lambda x: x[1] >= 3)


output = itemPairCount.collect() # bring the data back to the master node so we can print it out
for k in output:
    print (k)
print ("Popular items done")
sc.stop()

