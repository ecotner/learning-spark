# Learning Spark
Learning how to use Apache Spark and pyspark for processing of big data.

## Background
Apache spark is a computing framework that is used to process big data in both real-time and batch scenarios.
It uses a distributed computation model to split work over a cluster of machines so that workloads can be scaled horizontally.
It is written in Scala (which itself is written in Java and compiled using the JVM), but there are API's for many languages (including Python and R).

## Installation
### Regular Spark
Go to Spark's [download site](https://spark.apache.org/downloads.html), download and unpack the tarball, and move to `/opt/spark`.
You can also add `/opt/spark/bin` and `/opt/spark/sbin` to your `$PATH` and set `SPARK_HOME=/opt/spark` in your env variables.

### PySpark
To install pyspark (which comes with its own self-contained spark installation), simply run `pip install pyspark`.
For more details, follow [this guide](https://spark.apache.org/docs/latest/api/python/getting_started/install.html).