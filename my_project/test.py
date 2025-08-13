import os

if "DATABRICKS_RUNTIME_VERSION" in os.environ:
    print("✅ Running on Databricks cluster")
else:
    print("💻 Running locally")
