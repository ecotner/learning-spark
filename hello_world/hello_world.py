from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("Word Counter")
sc = SparkContext(conf=conf)

text_file = sc.textFile("file:///opt/spark/README.md")
tokenized_file_data = text_file.flatMap(lambda line: line.split(" "))
count_prep = tokenized_file_data.map(lambda word: (word, 1))
counts = count_prep.reduceByKey(lambda accum_val, new_val: accum_val + new_val)
sorted_counts = counts.sortBy(lambda kv_pair: kv_pair[1], ascending=False)
sorted_counts.saveAsTextFile("readmeWordCount")