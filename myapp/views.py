from django.shortcuts import render
import pandas as pd
from pandas.io import json

from myapp.models import Data

# Create your views here.
def hello(request):
    # print(request.POST.get('name'))
    # print(request.FILES['file'])
    # delete previous data
    previous_data = Data.objects.all()
    previous_data.delete()

    if request.FILES:
        file = request.FILES['file']
        # excel like rows n columns is called dataframe ie, here df
        df = pd.read_csv(file)
        print(df)
        print('-------------------------')
        # df to json so that it can be converted into object to save it
        json_records = df.reset_index().to_json(orient='records')
        print(json_records)
        print('-------------------------')
        data = json.loads(json_records)
        print(data)
        print('-------------------------')
        for d in data:
            print(d)
            name = d['property_name']
            price = d['property_price']
            rent = d['property_rent']
            emi = d['emi']
            tax = d['tax']
            exp = d['other_exp']
            expenses_monthly = emi + tax + exp
            income_monthly = rent - expenses_monthly

            # django ORM 
            dt = Data(name=name, price=price, rent=rent, emi=emi, tax=tax, exp=exp, expenses_monthly=expenses_monthly, income_monthly=income_monthly)
            dt.save()
        
        # access data 
        data_objects = Data.objects.all()
        context = {'data_objects': data_objects}
        return render(request, 'myapp/index.html', context)

    return render(request, 'myapp/index.html')
    