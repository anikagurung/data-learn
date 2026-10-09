from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


def users_name(spark: SparkSession) -> None:
    structureData = [
        (("James", "", "Smith"), "36636", "M", 3100),
        (("Michael", "Rose", ""), "40288", "M", 4300),
        (("Robert", "", "Williams"), "42114", "M", 1400),
        (("Maria", "Anne", "Jones"), "39192", "F", 5500),
        (("Jen", "Mary", "Brown"), "", "F", -1)
    ]

    structureSchema = StructType([
        StructField("name", StructType([
            StructField("firstname", StringType(), True),
            StructField("middlename", StringType(), True),
            StructField("lastname", StringType(), True)
        ])),
        StructField("id", StringType(), True),
        StructField("gender", StringType(), True),
        StructField("salary", IntegerType(), True)
    ])

    df = spark.createDataFrame(structureData, structureSchema)

    # Register dataframe as view named Users
    df.createOrReplaceTempView("Users")

    # Return firstname when lastname is Rose
    result = spark.sql("""
        SELECT name.firstname
        FROM Users
        WHERE name.middlename = 'Rose'
    """)

    result.show()


if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder \
        .master("local[1]") \
        .appName("Users Name") \
        .enableHiveSupport() \
        .getOrCreate()

    users_name(spark)



