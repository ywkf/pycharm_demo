import pytest
import requests


class TestWeather:

    url = "http://wthrcdn.etouch.cn/weather_mini"

    data_list = [
        {"city": 1},
        {"city": 2},
        {"city": 3},
    ]

    @pytest.mark.parametrize("data1", data_list)
    def test_city(self, data1):


        # data = {
        #     "city": data1.get("city")
        # }

        response = requests.get(self.url, data=data1).json()
        print("response: ", response)
        status = response.get("status")
        assert status == 1002

