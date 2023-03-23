from google.cloud import bigquery


client = bigquery.Client(project='de-take-home')

# Query to find 5 nearest ports to Jurong Island
QUERY = ("""
-- Obtaining coordinates for Jurong Island port in SG
WITH jurong_port AS (
    SELECT port_geom AS jurong_port_geom
    FROM `bigquery-public-data.geo_international_ports.world_port_index`
    WHERE port_name = 'JURONG ISLAND' AND country = 'SG'),
-- Obtaining distance of ports to Jurong Island port
combined_data AS (
    SELECT wpi.port_name, ST_DISTANCE(jp.jurong_port_geom, wpi.port_geom, TRUE) as distance
    FROM jurong_port jp
    CROSS JOIN  `bigquery-public-data.geo_international_ports.world_port_index` wpi)
-- Obtaining 5 nearest ports to jurong port
SELECT * FROM combined_data
WHERE distance != 0 -- Removes Jurong Port from output
ORDER BY distance
LIMIT 5
""")

# Create a BigQuery table with the query result
table_id = "de-take-home.task_answers.nearest_ports_jurong_island"
job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")
query_job = client.query(QUERY, job_config=job_config)
print("Processing query")
query_job.result()
print("Completed")
