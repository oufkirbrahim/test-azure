import azure.functions as func
import sys
from functions import test_function

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Lister les packages installés
    installed_packages = test_function()
    
    return func.HttpResponse(
        f"Packages installés:\n" + "\n".join(sorted(installed_packages)),
        status_code=200
    )
