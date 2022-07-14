
import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "linear_regression.joblib")
    modelLR = joblib.load(MODEL_FILE)
    MODEL_FILE = os.path.join(settings.MODELS, "decision_tree_regressor.joblib")
    modelDTR = joblib.load(MODEL_FILE)
    MODEL_FILE = os.path.join(settings.MODELS, "improved_linear_regression.joblib")
    modelILR = joblib.load(MODEL_FILE)
    MODEL_FILE = os.path.join(settings.MODELS, "KNN.joblib")
    modelKNN = joblib.load(MODEL_FILE)
