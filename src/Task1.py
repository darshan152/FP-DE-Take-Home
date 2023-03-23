from google.cloud import bigquery

# Connecting to the correct project in BQ
client = bigquery.Client(project='de-take-home')

# Query to obtain lat long of Jurong Island
query_for_jurong_island = ("""
    SELECT port_latitude, port_longitude
    FROM `bigquery-public-data.geo_international_ports.world_port_index`
    WHERE port_name = 'JURONG ISLAND' AND country = 'SG'
""")

# Running query
print("Obtaining Jurong Island Details")
result = client.query(query_for_jurong_island).result()

# Throws error is rows returned is more than expected
if result.total_rows != 1:
    raise Exception("More than 1 row was obtained when querying for location of Jurong Island")    

# Storing Jurong Island details
for i in result:
        jurong_lat, jurong_long = (i[0],i[1])

# Query to find 5 nearest ports to Jurong Island
query_for_nearest_ports = (f"""
SELECT wpi.port_name, ST_DISTANCE(ST_GEOGPOINT({jurong_long},{jurong_lat}), wpi.port_geom, TRUE) as distance
FROM `bigquery-public-data.geo_international_ports.world_port_index` wpi
WHERE port_name != 'JURONG ISLAND' -- Removes Jurong Port from output
ORDER BY distance
LIMIT 5
""")

# Create a BigQuery table with the query result
table_id = "de-take-home.task_answers.nearest_ports_jurong_island"
job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")
query_job = client.query(query_for_nearest_ports, job_config=job_config)
print("Processing query")
query_job.result()
print("Completed")



