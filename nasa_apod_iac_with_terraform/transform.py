from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.getOrCreate()

custom_schema = StructType([
    StructField("date", StringType(), nullable=True),
    StructField("explanation", StringType(), nullable=True),
    StructField("hdurl", StringType(), nullable=True),
    StructField("media_type", StringType(), nullable=True),
    StructField("service_version", StringType(), nullable=True),
    StructField("title", StringType(), nullable=True),
    StructField("url", StringType(), nullable=True)
])

json_file_path = "../nasa-apod-iac-with-terraform/data/apod_data.json"

df = spark.read.schema(custom_schema).json(json_file_path)

parquet_file_path = "../nasa-apod-iac-with-terraform/data/apod_data.parquet"
df_parquet = df.write \
    .mode("overwrite") \
    .parquet(parquet_file_path)

df = spark.read \
    .format("parquet") \
    .option("header", "true") \
    .load(parquet_file_path)

df.show(5)