
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import plotly.express as px
import pandas as pd
import numpy as np
import csv
from django.views import View


global df
df = pd.read_csv("../hack_raipur/Data/Crimes_HINDI.csv")




def hello_geek(request):

    return HttpResponse("Hello Geeks")
     


def main_page(request):
    print(df.head(), "...............")
   # this is main index page
    return render(request, "index.html")



class analysis(View):
    def get(self, request):
        return render(request, "visual.html")
        
    def post(self, request):
        pass


def map_page(request):
   # this is main index page
    return render(request, "map.html")










# class Test(View):
#     def get(self, request):

#         df_type=df["Where"].unique()[0:5]
#         df_new = df_type.tolist()
#         type_count=[]
#         for x in range(len(df["Where"].value_counts())):
  
#          type_count.append(int(df["Where"].value_counts()[x]))
#          if x==4:
#           break
  

#         plot12=px.bar( x=df_type, y=type_count, title="Where most of the crime occurred: ", color=type_count, color_continuous_scale=px.colors.sequential.Blues,labels=dict(x="Location", y="No. of crime"), template="plotly_dark")
#         #plot12.show()

#         plot13=px.bar( x=df_type, y=type_count, title="Where most of the crime occurred: ", color=type_count, color_continuous_scale=px.colors.sequential.Blues,labels=dict(x="Location", y="No. of crime"), template="plotly_dark")
#         #plot12.show()

#         chart1 = plot12.to_html()
#         chart2 = plot13.to_html()
#         context = {'chart1':chart1 , 'chart2':chart2}
#         return render(request, 'test.html', context)



        #  np.random.seed(42)
        #  plot11 = px.bar( x=np.random.randint(1, 101, 100), y=np.random.randint(1, 101, 100), title="No. of Crimes by Type of theft: ",
        #             width=800, height=480,
        #             color_continuous_scale=px.colors.sequential.Blues, template="plotly_dark", )
        #  plot12 = px.bar( x=np.random.randint(1, 101, 100), y=np.random.randint(1, 101, 100), title="No. of Crimes by Type of MURDER: ",
        #             color_continuous_scale=px.colors.sequential.Blues, template="plotly_dark")

        #  chart1 = plot11.to_html()
        #  chart2 = plot12.to_html()
        #  context = {'chart1':chart1, 'chart2':chart2}
        #  return render(request, 'test.html', context)
          
    # def post():
    #       pass
   
 


# class plot1:

#     def test_data1(request):
     


#       np.random.seed(42)
#       plot11 = px.bar( x=np.random.randint(1, 101, 100), y=np.random.randint(1, 101, 100), title="No. of Crimes by Type of MURDER: ",
#                      color_continuous_scale=px.colors.sequential.Blues, template="plotly_dark")
#       plot12 = px.bar( x=np.random.randint(1, 101, 100), y=np.random.randint(1, 101, 100), title="No. of Crimes by Type of MURDER: ",
#                      color_continuous_scale=px.colors.sequential.Blues, template="plotly_dark")

#       chart1 = plot11.to_html()
#       chart2 = plot12.to_html()
#       context = {'chart1':chart1, 'chart2':chart2}
#       return render(request, 'test.html', context)

    


       
#     def test_data2(request):

    

#      df_type=df["Where"].unique()[0:5]
#      df_new = df_type.tolist()
#      type_count=[]
#      for x in range(len(df["Where"].value_counts())):
  
#       type_count.append(int(df["Where"].value_counts()[x]))
#       if x==4:
#        break
  

#      plot12=px.bar( x=df_type, y=type_count, title="Where most of the crime occurred: ", color=type_count, color_continuous_scale=px.colors.sequential.Blues,labels=dict(x="Location", y="No. of crime"), template="plotly_dark")
#      #plot12.show()

#      chart2 = plot12.to_html()
#      context = {'chart2':chart2}
#      return render(request, 'test.html', context)




