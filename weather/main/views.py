from django.shortcuts import render
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


# Create your views here.
def index(request):
    config_dict = get_default_config()
    config_dict['connection']['use_ssl'] = False
    config_dict['connection']["verify_ssl_certs"] = False
    config_dict['language'] = 'ru'

    owm = OWM('561d1f02a74d821c9e723ed6710c432a', config_dict)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Москва')
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    status = w.detailed_status
    return render(request, 'main/index.html', context={'temp': temp, 'status': status,})
