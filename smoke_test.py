import boto3, os, sys
client=boto3.client("ssm",region_name="eu-north-1")
params={
    os.path.basename(p["Name"],p["Value"])
    for p in client.get_parameters_by_path(
        path="/application/banking",
        WithDecryption=True) ["Parameters"]
}

required=["DB_HOST","DB_NAME","DB_PASSWORD","DB_PORT"]
missing=[]

for k 


if missing:
    print(f"Failed: {missing}")
    sys.exit