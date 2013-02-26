# Wattvision api client interface
import urllib
import time

_VERSION_ = 0.2
_WV_ELEC_URL_  = "http://www.wattvision.com/api/v0.2/elec/"

_WV_API_ID_  = 'YOUR ID'
_WV_API_KEY_ = 'YOUR KEY'
_SENSOR_ID_  = 'YOUR SENSOR ID'

class WVQuickClient(object):
    def __init__(self, api_key, api_key_secret):
        self._WV_API_ID_ = api_key
        self._WV_API_KEY_  = api_key_secret

    def QuickElectricityConsumptionPost(self, sensor_id, watthours):

        str_fmt = '{{"sensor_id": "{0}", "api_id": "{1}", "api_key": "{2}", "watthours": {3} }}'
        request_body = str_fmt.format(str(sensor_id),
                                      str(self._WV_API_ID_),
                                      str(self._WV_API_KEY_),                                   
                                      watthours)

        request_body_encoded = request_body.encode('utf-8')
        response = urllib.urlopen(url=_WV_ELEC_URL_,data=request_body_encoded)
        return response

    def QuickPowerPost(self, sensor_id, watts):

        str_fmt = '{{"sensor_id": "{0}", "api_id": "{1}", "api_key": "{2}", "watts": {3} }}'
        request_body = str_fmt.format(str(sensor_id),
                                      str(self._WV_API_ID_),
                                      str(self._WV_API_KEY_),
                                      watts)
        
        request_body_encoded = request_body.encode('utf-8')
        response = urllib.urlopen(url=_WV_ELEC_URL_,data=request_body_encoded)
        return response

def main():
    import random
    wvclient = WVQuickClient(_WV_API_ID_,_WV_API_KEY_)
    watthours = 0
    while True:
        watts = random.uniform(150,250)
        wvclient.QuickPowerPost(_SENSOR_ID_, watts)
        wvclient.QuickElectricityConsumptionPost(_SENSOR_ID_, watthours )
        watthours += 1
        print "Just uploaded %d watts, %d watthours" % (watts,watthours)
        time.sleep(3)


if __name__ == "__main__":
    main()
