import json
import azure.functions as func
import spacy

# Load spaCy model globally (best practice for serverless performance)
nlp = spacy.load("en_core_web_sm")

app = func.FunctionApp()

@app.function_name(name="ner_http")
@app.route(
    route="ner_http",
    methods=["POST"],
    auth_level=func.AuthLevel.ANONYMOUS
)
def ner_http(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Parse JSON body
        req_body = req.get_json()
        text = req_body.get("text")

        if not text:
            return func.HttpResponse(
                "Please provide 'text' in request body",
                status_code=400
            )

        # Run NER
        doc = nlp(text)

        entities = []
        for ent in doc.ents:
            entities.append({
                "entity_text": ent.text,
                "entity_label": ent.label_,
                "start_char": ent.start_char,
                "end_char": ent.end_char
            })

        response = {
            "input_text": text,
            "entities": entities
        }

        return func.HttpResponse(
            json.dumps(response),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )
