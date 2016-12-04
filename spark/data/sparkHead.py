from pyspark import SparkContext
import itertools
sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

#1. Read data in as pairs of (user_id, item_id clicked on by the user)
pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
#2. Group data into (user_id, list of item ids they clicked on)
two = pairs.groupByKey()

#3. Transform into (user_id, (item1, item2) where item1 and item2 are pairs of items the user clicked on
itertools.product('ab', 'cd'))
#pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
#count = pages.reduceByKey(lambda x,y: x+y)        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for page_id, count in output:
    print ("page_id %s count %d" % (page_id, count))
print ("Popular items done")

sc.stop()