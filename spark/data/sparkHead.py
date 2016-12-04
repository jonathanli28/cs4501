from pyspark import SparkContext
import itertools

def generateUserItemPair(userList):
	l = []
	for i, j in itertools.product(userList[1], userList[1]):
		if i is not j:
			l.append((userList[0], (i,j)))
	return l

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

#1. Read data in as pairs of (user_id, item_id clicked on by the user)
userItems = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition

#2. Group data into (user_id, list of item ids they clicked on)
userLists = userItems.groupByKey()
userLists = userLists.map(lambda x: (x[0],set(x[1])) )

"""('chineeztakeout', <pyspark.resultiterable.ResultIterable object at 0x7f0327676550>)
('virginiabeach', <pyspark.resultiterable.ResultIterable object at 0x7f0327676dd8>)
('gloriousleader', <pyspark.resultiterable.ResultIterable object at 0x7f0327676e48>)
"""
#3. Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on
userItemPairs = userLists.flatMap(generateUserItemPair)
#for i, j in itertools.product(a, b):
output = userItemPairs.collect()
for x in output:
    print (x)
#pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
#count = pages.reduceByKey(lambda x,y: x+y)        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

#output = count.collect()                          # bring the data back to the master node so we can print it out
#for page_id, count in output:
#    print ("page_id %s count %d" % (page_id, count))
#print ("Popular items done")
sc.stop()

