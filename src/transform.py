from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def transform_func(df):
    return df.filter(col("dept")=="IT")