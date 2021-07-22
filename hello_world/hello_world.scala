// this script runs the "hello world" of spark, which is counting words in a document
// run the script with the command `spark-shell -i hello_world.scala`
// this sets up the spark context automatically in the scala REPL
// going forward I'm going to try and do everything in python/pyspark, but it is good to know this works in scala too

val textFile = sc.textFile("file:///opt/spark/README.md")
val tokenizedFileData = textFile.flatMap(line=>line.split(" "))
val countPrep = tokenizedFileData.map(word=>(word, 1))
val counts = countPrep.reduceByKey((accumValue, newValue)=>accumValue + newValue)
val sortedCounts = counts.sortBy(kvPair=>kvPair._2, false)
sortedCounts.saveAsTextFile("readmeWordCount")
System.exit(0)