"""
Spark Job Template for EMR Serverless
Reads RAW data and writes to Iceberg tables.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
