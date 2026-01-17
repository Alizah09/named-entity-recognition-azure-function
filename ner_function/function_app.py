import azure.functions as func
import json

app = func.FunctionApp()

@app.function_name(name="ner_http")
@app.route(route="ner_http", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS)
def ner_http(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"message": "NER function is running"}),
        mimetype="application/json",
        status_code=200
    )
