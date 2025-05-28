import logging
import azure.functions as func
import os
import json


def main_func(req: func.HttpRequest) -> func.HttpResponse:
    try:
        test  = os.environ.get('TEST_KEY')
        return func.HttpResponse(json.dumps(test, ensure_ascii=False), mimetype="application/json")

    except Exception as e:
        logging.exception("Erreur lors du traitement.")
        return func.HttpResponse(str(e), status_code=500)
