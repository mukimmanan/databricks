# Databricks notebook source
account_key = dbutils.secrets.get(scope="formula1-scope", key="formula1dl-account-key")

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula1dlpractise.dfs.core.windows.net", 
    account_key
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlpractise.dfs.core.windows.net"))

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls abfss://demo@formula1dlpractise.dfs.core.windows.net

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlpractise.dfs.core.windows.net", header=True))

# COMMAND ----------


