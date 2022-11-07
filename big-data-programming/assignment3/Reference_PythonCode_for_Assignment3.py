from tokenize import String
import pyspark
from pyspark.context import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession, SQLContext, Row
from pyspark.sql.functions import *
import json
import os


conf = SparkConf()
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")


spark = (
    SparkSession.builder.appName("Phone Book - Country Look up")
    .config("spark.some.config.option", "some-value")
    .config("spark.sql.caseSensitive", "false")
    .getOrCreate()
)
spark.conf.set("spark.sql.caseSensitive", False)


DF2 = spark.read.json("cityStateMap.json")
DF1 = spark.read.json("tweets.json")

DF1.show()
DF2.show()


# 1) print only tweets from atlanta
# used filter here, to verify it geo is atlanta and
# then used select function for displaying only tweet.
DF3 = DF1.filter("geo == 'Atlanta'").select(["tweet", "geo"]).show()


# 2) print only tweets that contain the word "today"

# as we have case sensitive words here. use filter twice
DF5 = DF1.filter((DF1.tweet.contains("today")) | (DF1.tweet.contains("Today"))).show()

# other way of doing it is
# changing column values to lower case and then filtering to get the word = 'today'
columnName = "tweet"
DF = DF1.withColumn(columnName, lower(col(columnName)))
DF.filter(DF.tweet.contains("today")).show()
# DF6 = DF1.filter(DF1.tweet.toLowerCase().contains('today')).show()

# 3) Print only tweets from california

# first join is used, as state is in DF2.
# and then as geo and city are same, dropped a column,
# and now used filter to check if state is california and then displayed only tweet column
DF1.join(DF2, DF1.geo == DF2.city, "inner").drop(DF2.city).show()
DF6 = DF1.join(DF2, DF1.geo == DF2.city, "inner").drop(DF2.city)
DF6.filter("state == 'California'").select(["tweet", "state"]).show()


# 4) Count the number of tweets published in each state.

# it is required to count the tweets, so we need to groub by state to get count
DF8 = DF6.groupBy("state").count().show()
