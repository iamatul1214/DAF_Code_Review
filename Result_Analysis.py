import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import json
import os
from datetime import datetime

with open('config.json','r') as config:
    params=json.load(config)["Params"]


class Result_Analysis:
    def __init__(self):
        self.time = datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")
        self.Data_Analysis_Source_DIR=params["Reviewed_Files_Folder"]
        self.review_plots=params["Review_Plots_Folder"]
        self.suggestions_plots=params["Suggestions_Plots_Folder"]

    def read_Excel(self):
        try:
            file = os.listdir(self.Data_Analysis_Source_DIR)
            paths = [os.path.join(self.Data_Analysis_Source_DIR, basename) for basename in file]
            file=max(paths, key=os.path.getctime)
            data=pd.read_excel(file)
            return data

        except Exception as e:
            print("Error occured while fetching and converting the data analaysis file to dataframe \t",str(e))

    def create_Count_Plot(self,dataframe):
        try:
            plt.figure(figsize=(15, 10))
            sns.countplot(x='Auto Code Review', data=dataframe)
            count_plot_image=self.time+"_"+"Auto_Code_Review CountPlot"
  #          plt.savefig(self.review_plots+"\/"+count_plot_image)
            return count_plot_image
        except Exception as e:
            print("Error occured while creating count plots \t", str(e))

    def create_Pie_plot(self,dataframe):
        try:
            plt.figure(figsize=(15, 15))
            plt.rcParams.update({'font.size': 20, 'font.weight': 'bold'})
            pie_chart = dataframe["Auto Code Review"].value_counts().plot(kind='pie', autopct='%1.1f%%')
            pie_chart.set_title("Auto code review distribution")
            pie_chart_image = self.time + "_" + "Auto_Code_Review piePlot"
            plt.savefig(self.review_plots+"\/"+pie_chart_image)

            plt.figure(figsize=(15, 15))
            plt.rcParams.update({'font.size': 20, 'font.weight': 'bold'})
            pie_chart = dataframe["Review Suggestions"].value_counts().plot(kind='pie', autopct='%1.1f%%')
            pie_chart.set_title("Review Suggestions Distribution")
            pie_chart_RS_image = self.time + "_" + "Review_Suggestions piePlot"
            plt.savefig(self.suggestions_plots+ "\/" + pie_chart_RS_image)
            return pie_chart_image, pie_chart_RS_image
        except Exception as e:
            print("Error occured while creating count plots \t", str(e))