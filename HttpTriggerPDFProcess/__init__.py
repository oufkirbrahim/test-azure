import logging
import azure.functions as func
import tempfile
import os
from dotenv import load_dotenv
import json

def save_uploaded_file(req_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(req_file.read())
        return tmp.name

def main_func(req: func.HttpRequest) -> func.HttpResponse:
    try:
        test  = os.getenv("TEST_KEY")
        return func.HttpResponse(json.dumps(test, ensure_ascii=False), mimetype="application/json")

    except Exception as e:
        logging.exception("Erreur lors du traitement.")
        return func.HttpResponse(str(e), status_code=500)
