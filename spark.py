from pyspark.sql import (SparkSession)
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from classProject import classProject
from enforce_schema import enforce_schema, nested_schema
from pyspark.sql.functions import expr
from pyspark.sql.functions import col
def distinct_func():
    data = [("James", "Sales", 3000),
            ("Michael", "Sales", 4600),
            ("Robert", "Sales", 4100),
            ("Maria", "Finance", 3000),
            ("James", "Sales", 3000),
            ("Scott", "Finance", 3300),
            ("Jen", "Finance", 3900),
            ("Jeff", "Marketing", 3000),
            ("Kumar", "Marketing", 2000),
            ("Saif", "Sales", 4100)
            ]
    columns = ["employee_name", "department", "salary"]

    df = spark.createDataFrame(data=data, schema=columns)
    df.printSchema()
    df.show(truncate=False)
    distinctDF = df.distinct()
    print("Distinct count: " + str(distinctDF.count()))
    distinctDF.show(truncate=False)


def number_rdd():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rdd = spark.sparkContext.parallelize(data)
    print(rdd.collect())
    print('Hello')

simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]

columns= ["employee_name","department","state","salary","age","bonus"]
#df = spark.createDataFrame(data = simpleData, schema = columns)
#df.printSchema()
#df.show(truncate=False)

if __name__ == '__main__':

    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()
   
    nested_schema(spark)
   
    distinct_func()
    
