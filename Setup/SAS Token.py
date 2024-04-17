# Databricks notebook source
spark.conf.set("fs.azure.account.auth.type.formula1dlpractise.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dlpractise.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dlpractise.dfs.core.windows.net", "sp=rl&st=2024-04-13T10:00:47Z&se=2024-04-13T18:00:47Z&spr=https&sv=2022-11-02&sr=c&sig=KcsGOjHJozMuwRHbPmejmsEAzBlFDcUMJPB21adIdzE%3D")

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls abfss://demo@formula1dlpractise.dfs.core.windows.net

# COMMAND ----------


