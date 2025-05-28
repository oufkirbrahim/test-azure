import azure.functions as func
import sys
import pkg_resources

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Lister les packages installés
    installed_packages = [d.project_name + "==" + d.version 
                         for d in pkg_resources.working_set]
    
    return func.HttpResponse(
        f"Packages installés:\n" + "\n".join(sorted(installed_packages)),
        status_code=200
    )
