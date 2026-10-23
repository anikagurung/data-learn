from pyspark.shell import spark
from pyspark.sql.functions import lit, col, avg, when
from pyspark.sql.types import StructField, StructType, StringType, IntegerType


def classProject(spark):
    data = [
        ("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150, 3761, "US"),
        ("BMW 2002", 113, 2234, "Europe"),
        ("Toyota Corolla", 90, 2430, "Asia"),
        ("Honda Civic", 115, 2200, "Asia"),
        ("Ford Mustang", 200, 3500, "US")
    ]

    schema = StructType([
        StructField("carr", StringType(), True),
        StructField("horsepower", IntegerType(), True),
        StructField("weight", IntegerType(), True),
        StructField("origin", StringType(), True)
    ])

    # Create DataFrame
    df = spark.createDataFrame(data, schema)

    # Rename column
    df = df.withColumnRenamed("carr", "car")

    # Add a calculated column
    df = df.withColumn(
        "power_to_weight",
        (col("horsepower") / col("weight")) * 1000
    )

    # Categorize cars by horsepower
    df = df.withColumn(
        "performance",
        when(col("horsepower") >= 150, "High")
        .otherwise("Standard")
    )

    # Display all cars
    print("All Cars:")
    df.show(truncate=False)

    # Filter high-horsepower cars
    print("Cars with at least 150 horsepower:")
    df.filter(col("horsepower") >= 150).show(truncate=False)

    # Group cars by origin and calculate average horsepower
    print("Average Horsepower by Origin:")
    df.groupBy("origin").agg(
        avg("horsepower").alias("average_horsepower")
    ).orderBy(col("average_horsepower").desc()).show()

    # Select specific columns and sort by weight
    print("Cars Sorted by Weight:")
    df.select("car", "horsepower", "weight").orderBy(
        col("weight").asc()
    ).show(truncate=False)

    # Count the total number of cars
    print("Total Cars:", df.count())


classProject(spark)