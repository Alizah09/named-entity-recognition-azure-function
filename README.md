# 🧠 Named Entity Recognition (NER) Microservice on Azure

A serverless **Named Entity Recognition (NER) microservice** built using **Python, spaCy, Azure Functions, and Azure Blob Storage**.  
This service exposes an HTTP API that extracts named entities from input text and securely logs results to Azure Blob Storage.

---

## 🚀 Features

- Named Entity Recognition using **spaCy**
- REST API powered by **Azure Functions (HTTP Trigger)**
- Automatic logging to **Azure Blob Storage**
- Secure, private storage container
- Production-style cloud architecture

---

## 🛠️ Tech Stack

- **Language:** Python 3.10  
- **NLP Library:** spaCy  
- **Compute:** Azure Functions  
- **Storage:** Azure Blob Storage  

---

## 🔗 API Endpoint

### **POST** `/api/ner_http`

### 📥 Request Body
```json
{
  "text": "Satya Nadella is the CEO of Microsoft in Seattle"
}
📤 Response
json
{
  "entities": [
    {
      "entity_text": "Satya Nadella",
      "entity_label": "PERSON",
      "start_char": 0,
      "end_char": 13
    },
    {
      "entity_text": "Microsoft",
      "entity_label": "ORG",
      "start_char": 28,
      "end_char": 37
    },
    {
      "entity_text": "Seattle",
      "entity_label": "GPE",
      "start_char": 41,
      "end_char": 48
    }
  ]
}
☁️ Blob Storage Logging
Each request is stored as a JSON file in Azure Blob Storage.

Container Name: ner-logs
File Naming Convention:
pgsql
ner_YYYYMMDD_HHMMSS.json

📄 Example Stored Log
json
{
  "input_text": "Satya Nadella is the CEO of Microsoft in Seattle.",
  "entities": [
    {
      "entity_text": "Satya Nadella",
      "entity_label": "PERSON",
      "start_char": 0,
      "end_char": 13
    },
    {
      "entity_text": "Microsoft",
      "entity_label": "ORG",
      "start_char": 28,
      "end_char": 37
    },
    {
      "entity_text": "Seattle",
      "entity_label": "GPE",
      "start_char": 41,
      "end_char": 48
    }
  ],
  "timestamp": "2026-01-17T12:22:09.173432"
}
🔒 Note: The Blob container is private by design to follow enterprise security standards.

📁 Project Structure
pgsql
ner-project/
│
├── ner_function/
│   ├── function_app.py
│   ├── host.json
│   ├── local.settings.json
│   ├── requirements.txt
│   └── venv/
│
└── README.md
⚙️ Environment Configuration
Create local.settings.json (not committed to GitHub):

json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "BLOB_CONNECTION_STRING": "<your-storage-connection-string>"
  }
}
▶️ Run Locally
# Activate virtual environment
venv\Scripts\activate

# Start Azure Functions
func start
Local endpoint:
http://localhost:7071/api/ner_http

☁️ Deployment
Azure Functions (Python runtime)

Azure Blob Storage (Central India)

Azure for Students subscription

🧠 Design Decisions
Serverless architecture for scalability

Secure Blob Storage with private access

Environment variables for secrets

Structured JSON logging for observability

👨‍💻 Author
Amajad Ali
Aspiring AI / ML Engineer
Azure • NLP • Cloud Microservices
