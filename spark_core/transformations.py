import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("read xml") \
    .master("local") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

df = spark.read.format("com.databricks.spark.xml") \
    .option("rowTag", "page") \
    .load("Wikipedia-20210724001848.xml")

df.filter(df.id == 5625591).select("revision").foreach(lambda x: print(x))