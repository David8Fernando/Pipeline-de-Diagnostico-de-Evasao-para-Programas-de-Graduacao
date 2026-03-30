import requests
import json
from datetime import datetime
import os 
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DATAMISSION_API_TOKEN")

if not token:
    raise ValueError("Token de API não encontrado. Verifique o arquivo .env e a variável DATAMISSION_API_TOKEN.")


# ===== CONFIG =====
project_id = "e21f7967-1182-44a9-b29e-6e8833f294e7"

url = f"https://api.datamission.com.br/projects/{project_id}/dataset?format=csv"
headers = {"Authorization": f"Bearer {token}"}

# ===== REQUEST =====
response = requests.get(url, headers=headers)
response.raise_for_status()

# ===== TIMESTAMP (pra versionamento) =====
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# ===== SALVAR CSV =====
csv_filename = f"dataset_{project_id}_{timestamp}.csv"

with open(csv_filename, "wb") as file:
    file.write(response.content)

# ===== CAPTURAR HEADERS =====
response_headers = dict(response.headers)

# ===== SALVAR METADADOS =====
metadata = {
    "project_id": project_id,
    "download_timestamp": timestamp,
    "url": url,
    "status_code": response.status_code,
    "headers": response_headers
}

metadata_filename = f"metadata_{project_id}_{timestamp}.json"

with open(metadata_filename, "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=4, ensure_ascii=False)

# ===== LOG =====
print(f"✅ CSV salvo em: {csv_filename}")
print(f"📄 Metadados salvos em: {metadata_filename}")