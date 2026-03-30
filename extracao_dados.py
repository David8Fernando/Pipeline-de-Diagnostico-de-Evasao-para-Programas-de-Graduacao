import requests

project_id = "e21f7967-1182-44a9-b29e-6e8833f294e7"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkYXZpZHBlcmVpcmEiLCJ0eXBlIjoiYXBpX2tleSIsImV4cCI6MTc3NzQ2ODEyOX0.LYI12VZj4Cq4rXAZAuE0OzE1gRe3WkjvTTeNvz3JXN0"
url = f"https://api.datamission.com.br/projects/{project_id}/dataset?format=parquet"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)
response.raise_for_status()

# Salva o arquivo localmente
with open(f"dataset_{project_id}.parquet", "wb") as file:
    file.write(response.content)

print("Download concluído com sucesso!")