import pkg_resources

def test_function():
  # Lister les packages installés
  installed_packages = [d.project_name + "==" + d.version 
                         for d in pkg_resources.working_set]
  return installed_packages 
