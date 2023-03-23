from google.cloud import bigquery
import yaml

## Import config data
try:
    print("Obtaining config data")
    with open('../config.yaml', "r") as f:
        config = yaml.safe_load(f)

    project_name = config['BIGQUERY']['PROJECT']
    dataset = config['BIGQUERY']['DATASET']
except:
     raise Exception("config.yaml failed to load")

# Connecting to the correct project in BQ
client = bigquery.Client(project=project_name)

# Query to find country which has the largest number of ports with a cargo wharf
query_for_country_with_most_cargo_wharf_ports = ("""
SELECT country, count(*) as port_count
FROM `bigquery-public-data.geo_international_ports.world_port_index`
WHERE cargo_wharf = TRUE
GROUP BY country
ORDER BY port_count DESC
LIMIT 1
""")

# Create a BigQuery table with the query result
table_id = f"{project_name}.{dataset}.country_with_most_cargo_wharf_ports"
job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")
query_job = client.query(query_for_country_with_most_cargo_wharf_ports, job_config=job_config)
print("Processing query")
query_job.result()
print("Completed")
