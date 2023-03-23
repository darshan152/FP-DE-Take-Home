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
client = bigquery.Client(project = project_name)

# Set parameters for dataset creation
dataset_id = "{}.{}".format(project_name,dataset)
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"

 # Make an API request to create dataset
dataset = client.create_dataset(dataset, timeout=30) 
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))