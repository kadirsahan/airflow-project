from pyspark.sql import SparkSession

def init_spark():
  spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
  sc = spark.sparkContext
  return spark,sc

def main():
  spark,sc = init_spark()
  print("Hello World spark")


if __name__ == '__main__':
  main()
