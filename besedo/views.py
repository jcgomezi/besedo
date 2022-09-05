from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
import dbmanage as db
import json


class main(TemplateView):
    template_name='main.html'
    
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

class get_table(TemplateView):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        try:
            if 'all' in request.GET.keys():
                df = db.get_db_data_into_df('SELECT * FROM contacts')
                print(df)
                return JsonResponse(df.to_dict(orient='records'),safe=False)
            elif 'id' in request.GET.keys():
                df = db.get_db_data_into_df(f"SELECT * FROM contacts where id = '{request.GET['id']}'")
                print(df)
                return JsonResponse(df.to_dict(orient='records'),safe=False)
            else:
                return JsonResponse({'error':'no data requested'},safe=False)
        except:
            return JsonResponse({'error':'please verify'},safe=False)

            
class insert_new_value(TemplateView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        try:
            db.insert_new_value_into_table( table='contacts',
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'],
                                        phone=data['phone'],
                                        age=data['age']
                                        )
            return JsonResponse({'result':'saved_correclty'},safe=False)
        except:
            return JsonResponse({'error':'please verify'},safe=False)

class update_register(TemplateView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        try:
            db.update_register(table='contacts',
                        id = data['id'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        phone=data['phone'],
                        age=data['age']
                        )
            return JsonResponse({'result':'saved_correclty'},safe=False)
        except:
            return JsonResponse({'error':'please verify'},safe=False)

class delete_register(TemplateView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        try:
            db.delete_register(table='contacts',
                            id = data['id'],
                            )
            return JsonResponse({'result':'deleted_correclty'},safe=False)
        except:
            return JsonResponse({'error':'please verify'},safe=False)