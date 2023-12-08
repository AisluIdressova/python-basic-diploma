from config_data.config import SiteSettings
from utils.site_api_handler import SiteApiInterface


site = SiteSettings()


url = "https://" + site.host_api + "/airports/search"

querystring = {"query":"new york","locale":"ru_RU"}

headers = {
	"X-RapidAPI-Key": site.api_key.get_secret_value(),
	"X-RapidAPI-Host": site.host_api
}

site_api = SiteApiInterface()

if __name__ == '__main__':
	site_api()
