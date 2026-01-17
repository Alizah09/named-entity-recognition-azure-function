🧠 Named Entity Recognition (NER) Microservice on Azure

A production-style Named Entity Recognition (NER) microservice built using Python, spaCy, Azure Functions, and Azure Blob Storage.
This service exposes an HTTP API that extracts named entities from text and securely stores inference logs in Azure Blob Storage.

🚀 Features

🔍 Named Entity Recognition using spaCy

🌐 REST API built with Azure Functions (HTTP Trigger)

☁️ Secure logging to Azure Blob Storage

🔐 Private storage access (enterprise security best practices)

📦 Clean, modular, cloud-ready architecture

🛠️ Tech Stack
Component	Technology
Language	Python 3.10
NLP Engine	spaCy
Cloud Compute	Azure Functions
Storage	Azure Blob Storage
Auth	Connection strings via environment variables
🧩 Architecture Overview
Client (POST Request)
        |
        v
Azure Function (HTTP Trigger)
        |
        |-- spaCy NER Processing
        |
        |-- JSON Output
        |
        v
Azure Blob Storage (Private Container)

📌 API Endpoint
POST /api/ner_http
Request Body
{
  "text": "Satya Nadella is the CEO of Microsoft in Seattle"
}

Response
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

🗂️ Blob Storage Logging

Each request is logged as a JSON file in Azure Blob Storage:

Container: ner-logs

File format:

ner_YYYYMMDD_HHMMSS.json

Example Stored Log
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


🔒 The container is private by design to follow enterprise security standards.

📁 Project Structure
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

⚙️ Environment Variables

Set inside local.settings.json (not committed to Git):

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

# Start Azure Function
func start


Access API:

http://localhost:7071/api/ner_http

☁️ Deployment

Azure Functions

Azure Blob Storage (Central India)

Azure for Students subscription

🧠 Design Decisions

Private Blob container to ensure data security

Environment variables for secrets

Stateless HTTP API for scalability

Structured logging for observability

📌 Recruiter Notes

This project demonstrates real-world cloud architecture

Storage access is intentionally restricted

Evaluation is done via:

API behavior

Code quality

Architecture decisions

Sample outputs

Temporary access (SAS) can be provided if required.

🙌 Author

Amajad Ali
Aspiring AI / ML Engineer
Azure • NLP • Cloud Microservices
