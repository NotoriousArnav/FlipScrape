# FlipScrape
Flipkart Product Scrapper Library Made in Python


# Installation
Well, Right Now no PyPI Package is made, but you run this Command:uonkart
```
pip3 install bs4 requests
curl https://raw.githubusercontent.com/NotoriousArnav/FlipScrape/main/flip_scrape.py >flip_scrape.py
```

To get the Current Version of Flip Scrape from the Main Branch

# Using
Well, It would be great if you Find Your own way around, but if you don't have time for R&D, so Here you go
  FlipkartProduct is the class, that is going to make your work done. Make sure that,
    - You Give a Correct URL
    - Have bs4 and requests installed in your System
  
  This Class uses Variables to store Product Info, like:
   - obj.prod_name for Product Name
   - obj.price for current price
   - obj.discount for a dictionary containing Discount Information (Currently Working on Adding Bank Offers to this Dictionary)
