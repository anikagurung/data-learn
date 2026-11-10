# q1_kafka_producer.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, trim
spark = ( SparkSession.builder.appName("ApplicationLogKafkaProducer").getOrCreate() )
# Read the text file: one log entry per row.

lines_df = spark.read.text("application.log")

# Split at the first colon. The second split field retains any later colons.

parts_df = lines_df.select(
    trim(split(col("value"), ":", 2).getItem(0)).alias("LogLevel"),
    trim(split(col("value"), ":", 2).getItem(1)).alias("LogMessage") )

# Keep only valid rows with both fields present.

log_df = parts_df.filter(
    col("LogLevel").isNotNull() &
    col("LogMessage").isNotNull() &
    (col("LogLevel") != "") &
    (col("LogMessage") != "")
)
# Publish LogLevel as key and LogMessage as value.

kafka_df = log_df.selectExpr("CAST(LogLevel AS STRING) AS key","CAST(LogMessage AS STRING) AS value")
(
    kafka_df.write.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("topic", "applog").save() )
log_df.show(truncate=False)
spark.stop()

# q2_kafka_consumer.py


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, size

spark = (

    SparkSession.builder.appName("ApplicationLogKafkaConsumer") .getOrCreate()

)

# Subscribe to the applog topic.

kafka_stream_df = (spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "applog").option("startingOffsets", "earliest").load()
)

# Kafka value is the LogMessage; key contains the LogLevel.

messages_df = kafka_stream_df.select(col("key").cast("string").alias("LogLevel"),col("value").cast("string").alias("LogMessage"))

# Count words in each message and retain the original message.
result_df = messages_df.select("LogLevel","LogMessage",size(split(col("LogMessage"), r"\\s+")).alias("WordCount"))

query = (result_df.writeStream.format("console").outputMode("append").option("truncate", "false").start() )

query.awaitTermination()