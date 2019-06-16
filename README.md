Project adapt from https://github.com/rafikahmed/web-scraping-course. More detail, tutorial and information you can find his course (Modern Web Scrapping with Python) on Udemy. 

In this project you will:

### Scrape this website: http://quotes.toscrape.com/js/

### From each page you have to scrape:

The quote

The author

The tags

### Project requirements
Initiate a new Scrapy project and call it: sixth_assignment

Create a new spider class called 
```diff
+ QuotesToScrapeJsSpider
```

Your spider should be named: 
```diff
+ quotesjs
```

Build the parse method, just a regular one and yield all the fields

Follow the links in pagination

Install and add Splash to your 
```diff
+ settings.py

```

Execute your spider and save the items in a JSON file

The target website does use Javascript to render the content so using Splash in this case is a must. 

### HELPFUL TRICK

How do we know if the website is using JavaScript beside testing it with Scrapy Shell ?

Well if you are using Chrome you can head over to settings -> Content settings -> JavaScript -> toggle allowed

If we disable JavaScript the website content won't be rendered.

## Questions for this project

In opinion what 'endpoint' do we need to use in this case with the SplashRequest ? Please justify your response

Please post in your start_requests method implementation

In your opinion what are the two factors the 'wait' argument depends on ?
