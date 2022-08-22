from django.shortcuts import render
import json
def my_cv(request):

    f = open('cv_app/static/cv_app/json/mydata.json','r')
    json_data = json.load(f)

    name = json_data.get('personal_data').get('name')
    surname = json_data.get('personal_data').get('surname')
    birthday = json_data.get('personal_data').get('birthday')
    adress = json_data.get('personal_data').get('adress')
    email = json_data.get('personal_data').get('email')
    phonenumber = json_data.get('personal_data').get('phonenumber')
    gith= json_data.get('personal_data').get('gith')
    linkd = json_data.get('personal_data').get('linkd')

    context = {'name':name,'surname':surname,'birthday':birthday,'adress':adress,'email':email,'phonenumber':phonenumber, 'gith':gith, 'linkd':linkd}

    return render(request,"cv_app/index.html",context)
