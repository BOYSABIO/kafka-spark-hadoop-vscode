from pyspark.sql import SparkSession

def get_spark_session():
    spark = SparkSession.builder.appName("LocalVSCode-Spark").master("spark://localhost:7077").config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000").getOrCreate()
    
    return spark