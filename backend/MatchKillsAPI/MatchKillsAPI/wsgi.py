"""
WSGI config for MatchKillsAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MatchKillsAPI.settings')

application = get_wsgi_application()


# ML registry
import inspect
from ml.registry import MLRegistry
from api.views import MatchKillsLR, MatchKillsDTR, MatchKillsILR

try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    LR = MatchKillsLR()
    DTR = MatchKillsDTR()
    ILR=MatchKillsILR()
    # add to ML registry
    registry.add_algorithm(endpoint_name="Match Kills Linear Regression",
                            algorithm_object=LR,
                            algorithm_name="Linear Regression",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Jose Caro",
                            algorithm_description="Simple Linear Regression with preprocessing",
                            algorithm_code=inspect.getsource(MatchKillsLR))
    registry.add_algorithm(endpoint_name="Match Kills Decision Tree",
                            algorithm_object=DTR,
                            algorithm_name="Decision Tree Regressor",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Jose Caro",
                            algorithm_description="Simple Decision Tree with preprocessing",
                            algorithm_code=inspect.getsource(MatchKillsDTR))
    registry.add_algorithm(endpoint_name="Match Kills Improved Linear Regressor",
                            algorithm_object=ILR,
                            algorithm_name="Improved Linear Regression",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Jose Caro",
                            algorithm_description="Linear Regression with boosting and preprocessing",
                            algorithm_code=inspect.getsource(MatchKillsILR))
    registry.add_algorithm(endpoint_name="Match Kills K Nearest Neighbors",
                            algorithm_object=ILR,
                            algorithm_name="K Nearest Neighbors",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Oscar Quezada",
                            algorithm_description="KNN with preprocessing",
                            algorithm_code=inspect.getsource(MatchKillsILR))


except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))