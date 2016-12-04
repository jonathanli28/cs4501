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
"""
('chineeztakeout', ('1', '3'))
('chineeztakeout', ('3', '1'))
('virginiabeach', ('1', '5'))
('virginiabeach', ('1', '3'))
('virginiabeach', ('1', '2'))
('virginiabeach', ('5', '1'))
('virginiabeach', ('5', '3'))
('virginiabeach', ('5', '2'))
('virginiabeach', ('3', '1'))
('virginiabeach', ('3', '5'))
('virginiabeach', ('3', '2'))
('virginiabeach', ('2', '1'))
('virginiabeach', ('2', '5'))
('virginiabeach', ('2', '3'))
('gloriousleader', ('4', '1'))
('gloriousleader', ('4', '5'))
('gloriousleader', ('4', '3'))
('gloriousleader', ('4', '2'))
('gloriousleader', ('1', '4'))
('gloriousleader', ('1', '5'))
('gloriousleader', ('1', '3'))
('gloriousleader', ('1', '2'))
('gloriousleader', ('5', '4'))
('gloriousleader', ('5', '1'))
('gloriousleader', ('5', '3'))
('gloriousleader', ('5', '2'))
('gloriousleader', ('3', '4'))
('gloriousleader', ('3', '1'))
('gloriousleader', ('3', '5'))
('gloriousleader', ('3', '2'))
('gloriousleader', ('2', '4'))
('gloriousleader', ('2', '1'))
('gloriousleader', ('2', '5'))
('gloriousleader', ('2', '3'))
"""
#4 Transform into ((item1, item2), list of user1, user2 etc) where users are all the ones who co-clicked (item1, item2)
itemPairUserList = userItemPairs.map(lambda x : (x[1],x[0]));

#pretty sure they're already distinct, check later
itemPairUserList = itemPairUserList.distinct();
itemPairUserList = itemPairUserList.groupByKey();

#output = itemPairUserList.collect()
#for x in output:
#    print (x[0])
#    for item in x[1]:
#        print(str(item)) 

#pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
#count = pages.reduceByKey(lambda x,y: x+y)        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

#output = count.collect()                          # bring the data back to the master node so we can print it out
#for page_id, count in output:
#    print ("page_id %s count %d" % (page_id, count))
#print ("Popular items done")
sc.stop()

