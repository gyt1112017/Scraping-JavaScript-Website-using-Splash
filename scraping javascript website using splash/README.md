# Note: Docker only supports 64bit

	1. Get docker toolbox (win10 Home 64bit) link https://docs.docker.com/toolbox/overview/
	2. During the install process. Make sure tick intall VirtualBox. 
	3. To push splash from Doceker Hub:
	docker pull scrapinghub/splash
	4. To luanch splash:
	docker run -p 8050:8050 scrapinghub/splash
	5. Get your virtual machine ip address:
	Open a new terminal, you ip address shows on the top/
	You can type docker-machine ip default
  6. Open chrome type address: your ip address:8050 (usually 192.168.99.100:8050/localhost:8050
  
## Initiate a request and splash a request
scrapy genspider -t basic 'spider name' 'website without http/https'
in this project, it gonna be 
scrapy genspider -t basic quotesjs quotes.toscrape.com/js/

## Note
whenever you want to use exceute a custom script always use the execute endpoint
run:
scrapy crawl quotesjs -o all_pages.json

adapt setting.py
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = 'YOUR SPLASH URL' 
In this case:
SPLASH_URL = '192.168.99.100:8050' 

FEED_EXPORT_ENCODING = 'UTF-8'
