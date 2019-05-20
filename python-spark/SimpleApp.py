''' SimpleApp.py'''
from pyspark.sql import  SparkSession

logFile = "/opt/spark/README.md"
spark = SparkSession.builder().appName(appName).master(master).getOrCreate()
logData = spark.read.text(logFile).cache()

numAs=logData.filter(logData.value.contains('a')).count()

numBs=logData.filter(logData.value.contains('b')).count()

print ("lines with a :%i ,lines with b: %i" %(numAs ,numBs))
spark.stop