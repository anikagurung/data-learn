from pyspark.shell import spark
from pyspark.sql.functions import lit, col
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


def classProject(spark):
    data = [
        ("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150, 3761, "US"),
        ("BMW 2002", 113, 2234, "Europe")
    ]

    schema = StructType([
        StructField("carr", StringType(), True),
        StructField("horsepower", IntegerType(), True),
        StructField("weight", IntegerType(), True),
        StructField("origin", StringType(), True)
    ])

    df = spark.createDataFrame(data, schema)

    df = df.withColumnRenamed("carr", "car")

    df.show()


classProject(spark)