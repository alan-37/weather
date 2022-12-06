from django.shortcuts import render
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from .forms import MyForm


# Create your views here.
def index(request):
    config_dict = get_default_config()
    config_dict['connection']['use_ssl'] = False
    config_dict['connection']["verify_ssl_certs"] = False
    config_dict['language'] = 'ru'

    owm = OWM('561d1f02a74d821c9e723ed6710c432a', config_dict)
    mgr = owm.weather_manager()
    form = MyForm(request.POST or None)
    temp = None
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            city = data.get('city')
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temp = round(w.temperature('celsius')["temp"])
            status = w.detailed_status
            return render(request, 'main/index.html', context={'temp': temp, 'status': status, 'form': form, 'city': city})

    return render(request, 'main/index.html', context={'form': form, 'temp': temp})
