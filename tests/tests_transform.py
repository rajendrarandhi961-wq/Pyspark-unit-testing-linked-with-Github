from src.transform import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()

input_path = "/Volumes/dev/practice/unit_testing_pyspark_dataset/employees_test.csv"

df = spark.read.csv(input_path,header=True)

#validate count
result_count = transform_func(df)
assert result_count.count() == 1