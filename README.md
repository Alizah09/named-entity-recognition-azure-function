---
# 🧠 Named Entity Recognition (NER) Microservice on Azure

A serverless **Named Entity Recognition (NER) microservice** built using **Python, spaCy, Azure Functions, and Azure Blob Storage**.  
This service exposes an HTTP API that extracts named entities from input text and securely logs results to Azure Blob Storage.
I developed and locally tested an Azure Function with spaCy, validated responses via Postman, and verified logs in Azure Blob Storage.

---

## 🚀 Features

- Named Entity Recognition using **spaCy**
- REST API using **Azure Functions (HTTP Trigger)**
- Automatic JSON logging to **Azure Blob Storage**
- Private blob container (enterprise-style security)
- Cloud-ready, scalable microservice

---

## 🛠️ Tech Stack

- **Language:** Python 3.10  
- **NLP Library:** spaCy  
- **Compute:** Azure Functions  
- **Storage:** Azure Blob Storage  

---

## 🔗 API Endpoint

**POST** `/api/ner_http`

---

## 📥 Request Body

```json
{
  "text": "Satya Nadella is the CEO of Microsoft in Seattle"
}
```
---
## 📤 Response
```
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
```
---

## ☁️ Blob Storage Logging

Each API request is stored as a JSON file in Azure Blob Storage.

Container Name: ner-logs

File Naming Convention:
ner_YYYYMMDD_HHMMSS.json

---

## 📄 Example Stored Log
```
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
```
- 🔒 Note: The Blob container is private by design to follow enterprise security standards.
---

## 📁 Project Structure
```
named-entity-recognition-azure-function/
│
├── ner_function/
│   ├── function_app.py          # Azure Function HTTP trigger with spaCy NER logic
│   ├── host.json                # Azure Functions host configuration
│   ├── local.settings.json      # Local environment variables (not committed)
│   ├── requirements.txt         # Python dependencies
│   └── venv/                    # Python virtual environment (local use)
│
├── screenshot/
│   ├── screenshots_function_running_locally.png    # Postman request & NER API response
│   ├── screenshots_api_request_response.png        # Azure Functions running locally (func start)
│   ├── screenshots_ner_output.png                  # Azure Blob Storage container (ner-logs)
│   ├── screenshots_blob_container.png              # Stored JSON log with entities & timestamp
│   └── github_repository.png                       # GitHub repository & README view
│
└── README.md                     # Project documentation

```
---

## ⚙️ Environment Configuration

Create local.settings.json (do not commit this to GitHub):

```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "BLOB_CONNECTION_STRING": "<your-storage-connection-string>"
  }
}
```
---

## ▶️ Run Locally

- Activate virtual environment
```
venv\Scripts\activate
```
- Start Azure Functions
```
func start
```
- Local endpoint:
```
Local endpoint: http://localhost:7071/api/ner_http
```
---

## ☁️ Deployment

Azure Functions (Python runtime)

Azure Blob Storage (Central India)

Azure for Students subscription

---

## 🧠 Design Decisions

Serverless architecture for scalability

Secure Blob Storage with private access

Environment variables for secrets

Structured JSON logging for observability

---

## 👨‍💻 Author

- Amajad Ali
- Aspiring AI / ML Engineer
- Azure • NLP • Cloud Microservices
