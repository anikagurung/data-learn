from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

#Question1
def partition_rdd() -> None:
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rdd = spark.sparkContext.parallelize(data, 5)
    print("Number of partitions:", rdd.getNumPartitions())

#question2
def count_records(spark):
    #rdd = spark.sparkContext.textFile("/user/takeo/date_data.txt")
    rdd = spark.sparkContext.textFile(
        "file:///home/takeo/pycharmprojects/sparkproject/date_data.txt"
    )

    print("Number of records:", rdd.count())

#question3
def word_count(spark: SparkSession) -> None:
    rdd = spark.sparkContext.textFile(
        "file:///home/takeo/pycharmprojects/sparkproject/paragraph.txt"
    )

    words = rdd.flatMap(lambda line: line.split())

    word_pairs = words.map(lambda word: (word, 1))

    word_count = word_pairs.reduceByKey(lambda x, y: x + y)

    for item in word_count.collect():
        print(item)



#question4
def users_salary(spark: SparkSession) -> None:
    data = [
        ("James", "", "Smith", "36636", "M", 3000),
        ("Michael", "Rose", "", "40288", "M", 4000),
        ("Robert", "", "Williams", "42114", "M", 4000),
        ("Maria", "Anne", "Jones", "39192", "F", 4000),
        ("Jen", "Mary", "Brown", "", "F", -1)
    ]

    schema = StructType([
        StructField("firstname", StringType(), True),
        StructField("middlename", StringType(), True),
        StructField("lastname", StringType(), True),
        StructField("id", StringType(), True),
        StructField("gender", StringType(), True),
        StructField("salary", IntegerType(), True)
    ])

    df = spark.createDataFrame(data, schema)

    df.createOrReplaceTempView("Users")

    result = spark.sql("""
        SELECT *
        FROM Users
        WHERE salary > 3000
    """)

    result.show()

if __name__ == '__main__':
    spark: SparkSession = SparkSession.builder.master("local[1]").appName(
            "bootcamp.com").enableHiveSupport().getOrCreate()
    partition_rdd()
    count_records(spark)
    word_count(spark)
    users_salary(spark)


