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

# Setting the coordinates
distress_latitude = 32.610982
distress_longitude = -38.706256

# Query to find the nearest port with provisions, water, fuel oil, and diesel
query_for_nearest_ports = (f"""
SELECT country, port_name, port_latitude, port_longitude
FROM `bigquery-public-data.geo_international_ports.world_port_index`
WHERE provisions = TRUE AND water = TRUE AND fuel_oil = TRUE AND diesel = TRUE
ORDER BY ST_DISTANCE(ST_GEOGPOINT({distress_longitude},{distress_latitude}),port_geom, TRUE) ASC
LIMIT 1
""")

# Create a BigQuery table with the query result
table_id = f"{project_name}.{dataset}.nearest_provision_ports"
job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")
query_job = client.query(query_for_nearest_ports, job_config=job_config)
print("Processing query")
query_job.result()
print("Completed")
