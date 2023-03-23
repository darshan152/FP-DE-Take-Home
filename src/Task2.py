from google.cloud import bigquery

# Connecting to the correct project in BQ
client = bigquery.Client(project='de-take-home')

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
table_id = "de-take-home.task_answers.country_with_most_cargo_wharf_ports"
job_config = bigquery.QueryJobConfig(destination=table_id, write_disposition="WRITE_TRUNCATE")
query_job = client.query(query_for_country_with_most_cargo_wharf_ports, job_config=job_config)
print("Processing query")
query_job.result()
print("Completed")
