
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import plotly.express as px
import pandas as pd
import numpy as np


datafile = settings.BASE_DIR /'Data'/ 'Crimes.csv'
with open("datafile" , 'r') as csvfile:
    df = pd.read_csv(csvfile)



def hello_geek(request):

    return HttpResponse("Hello Geeks")


def main_page(request):
   # this is main index page
    return render(request, "index.html")


def viaual_page(request):
   # this is main index page
    return render(request, "visual.html")


def map_page(request):
   # this is main index page
    return render(request, "map.html")




def test_data(request):

    # Which Type of Crime is more?
  df_type = list(df.Type.unique())[0:5]
  type_count = []
  for x in range(len(df.Type.value_counts())):

    type_count.append(int(df.Type.value_counts()[x]))
    if x == 4:
        break


  plot11 = px.bar(data_frame=df, x=df_type, y=type_count, title="No. of Crimes by Type of Crime: ",
                color=type_count, color_continuous_scale=px.colors.sequential.Blues, template="plotly_dark")

  chart = plot11.to_html()
  context = {'char':chart}
  return render(request, 'test.html', context)

