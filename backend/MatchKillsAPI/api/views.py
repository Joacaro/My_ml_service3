import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class MatchKillsLR(APIView):
    def post(self, request):
        data = request.data
        MatchFlankKills = data['MatchFlankKills'] 
        MatchAssists = data['MatchAssists'] 
        MatchHeadshots= data['MatchHeadshots']
        lin_reg_model = ApiConfig.modelLR
        predicted_MatchKills = lin_reg_model.predict([[MatchFlankKills, MatchAssists, MatchHeadshots]])
        predicted_MatchKills = np.round(predicted_MatchKills, 0)
        response_dict = {"Predicted MatchKills": predicted_MatchKills}
        return Response(response_dict, status=200)

class MatchKillsDTR(APIView):
    def post(self, request):
        data = request.data
        MatchFlankKills = data['MatchFlankKills'] 
        MatchAssists = data['MatchAssists'] 
        MatchHeadshots= data['MatchHeadshots']
        dtr_model = ApiConfig.modelDTR
        predicted_MatchKills = dtr_model.predict([[MatchFlankKills, MatchAssists, MatchHeadshots]])
        predicted_MatchKills = np.round(predicted_MatchKills, 0)
        response_dict = {"Predicted MatchKills": predicted_MatchKills}
        return Response(response_dict, status=200)

class MatchKillsILR(APIView):
    def post(self, request):
        data = request.data
        MatchFlankKills = data['MatchFlankKills'] 
        MatchAssists = data['MatchAssists'] 
        MatchHeadshots= data['MatchHeadshots']
        impr_lin_reg_model = ApiConfig.modelILR
        predicted_MatchKills = impr_lin_reg_model.predict([[MatchFlankKills, MatchAssists, MatchHeadshots]])
        predicted_MatchKills = np.round(predicted_MatchKills, 0)
        response_dict = {"Predicted MatchKills": predicted_MatchKills}
        return Response(response_dict, status=200)