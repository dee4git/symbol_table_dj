from django.shortcuts import render

# Create your views here.
from items import forms
from items.models import Symbol


def search(request):
    search_results = []
    symbols = Symbol.objects.all()
    if request.method == 'GET':  # If the form is submitted
        keyword = request.GET.get('search_box', None)
        key = get_custom_hash(str(keyword))
        print('key', key)
        for i in symbols:
            if i.index == key and i.name == keyword:
                search_results.append(i)

    return render(request, 'search_result.html', {
        "search_results": search_results
    })


def home(request):
    """views the home page"""
    symbols = Symbol.objects.order_by('index')
    return render(request, "home.html", {
        "symbols": symbols,
    })


def form_checker(request, instance):
    text = instance.name
    result = [x.strip() for x in text.split(',')]
    return result


types = ['int', 'id', 'num', 'function']


def custom_hash(key):
    # returns a value joining ascii values
    return ''.join(str(ord(c)) for c in key)


def get_custom_hash(key):
    key = int((custom_hash(key)))
    key = key % 9
    return key


def index_maker(i_name):
    # also deletes the one to be replaced
    index = (get_custom_hash(str(i_name)))
    symbols = Symbol.objects.all()
    # for i in symbols:
    #     if i.index == index:
    #         i.delete()
    return index


def delete_symbol(request, symbol_id):
    Symbol.objects.get(pk=symbol_id).delete()
    return home(request)


def update_symbol(request, symbol_id):
    symbol = Symbol.objects.get(pk=symbol_id)
    if request.method == "POST":
        form = forms.UpdateSymbolForm(request.POST, request.FILES, instance=symbol)
        if form.is_valid():
            instance = form.save(commit=False)
            result = form_checker(request, instance)
            if is_valid(result):
                i_name = result[0]
                i_type = result[1]
                print(i_type)
                if i_type in types:
                    # instance is valid so lets make its index and also remove duplicates
                    instance.index = index_maker(i_name)
                    instance.name = i_name
                    instance.type = i_type
                    if i_type == 'num':
                        instance.size = 4
                    elif i_type == 'id':
                        instance.size = 1
                    instance.save()
                else:
                    form = forms.AddSymbolForm()
                    msg = "Wrong Input"
                    return render(request, 'form.html',
                                  {
                                      "form": form,
                                      "msg": msg,
                                  },
                                  )
            else:
                form = forms.UpdateSymbolForm(instance=symbol)
                msg = "Wrong Input"
                return render(request, 'form.html',
                              {
                                  "form": form,
                                  "msg": msg,
                              },
                              )
            return home(request)
    else:
        form = forms.UpdateSymbolForm(instance=symbol)
    return render(request, 'form.html',
                  {"form": form,
                   },
                  )


def is_valid(result):
    if len(result) == 2:
        return True


def add_symbol(request):
    if request.method == "POST":
        form = forms.AddSymbolForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            result = form_checker(request, instance)
            if is_valid(result):
                i_name = result[0]
                i_type = result[1]
                print(i_type)
                if i_type in types:
                    # instance is valid so lets make its index and also remove duplicates
                    instance.index = index_maker(i_name)
                    instance.name = i_name
                    instance.type = i_type
                    if i_type == 'num':
                        instance.size = 4
                    elif i_type == 'id':
                        instance.size = 1
                    instance.save()
                else:
                    form = forms.AddSymbolForm()
                    msg = "Wrong Input"
                    return render(request, 'form.html',
                                  {
                                      "form": form,
                                      "msg": msg,
                                  },
                                  )
            else:
                form = forms.AddSymbolForm()
                msg = "Wrong Input"
                return render(request, 'form.html',
                              {
                                  "form": form,
                                  "msg": msg,
                              },
                              )
            return home(request)
    else:
        form = forms.AddSymbolForm()
    return render(request, 'form.html',
                  {"form": form,
                   },
                  )
