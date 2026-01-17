# Named Entity Recognition – Azure Function

## 📌 Project Overview
This project is a **serverless Named Entity Recognition (NER) microservice**
built using **Azure Functions** and **Python**.

The service exposes an **HTTP API** that accepts text input and returns
recognized named entities (such as PERSON, ORG, LOCATION, DATE, etc.).
The project is designed as a lightweight, cloud-ready ML microservice.

> This repository is part of a technical assignment and demonstrates
> real-world backend + ML service design.

---

## 🏗️ Architecture (High Level)


Client (Postman / Browser)
|
| HTTP Request
v
Azure Function (Python)
|
| NER Processing
v
JSON Response


*(Architecture will be expanded with Azure Blob Storage in later steps)*


---

## 🛠️ Tech Stack
- **Python 3.10**
- **Azure Functions (HTTP Trigger)**
- **spaCy** (for Named Entity Recognition) *(to be added)*
- **Azure Blob Storage** *(to be added)*

---

## 🚀 API Details

### Endpoint

POST /api/ner_http
GET /api/ner_http


### Sample Response (Current)
```json
{
  "message": "NER function is running"
}
