# Databricks notebook source
display(dbutils.fs.ls("/"))

# COMMAND ----------

display(
    spark.read.csv("/FileStore/circuits.csv", header=True)
)

# COMMAND ----------


