For price tracker to run you will need to:

 1.  	Create a new virtual env 
 
 2.  	Install the following libraries for python by entering the following on your commandline (without the quotation marks):
 	"pip install wheels requests selenium "beautiful soup 4",
  	 
  
3.	Place the geckodriver into the virtual enviroment's bin folder. An updated version may be needed. This project is intended to be used with Firefox browser. 
 
 
 OVERVIEW-------------------------------------------------------------------------------
    This document is an overview of a web scraping price tracker. The goal of the project is to build a tool that tracks the listings and prices of items on multiple websites, starting with Guitar center. 

   The first step is to lay out the mechanism to grab/strip data from the html of various websites for storing in a database table. Guitar center has two types of listings: new gear and used gear. Used gear listings are posted and removed in an irregular fashion. The data structure of the listings are identical so parsing shouldn't be an issue. 
   
   After the data stripping section is working, I will work on a function that accepts keywords to pass as search terms into the search bar on the guitar center website. This way, the user can add and remove keywords, and specify which keywords should be used on which sites. 
   
   With new listings frequently being created, I want to implement an alerting system to notify me when a new listing is found. A function that compares the number of results from a keyword search and compares it to previous results should work. 
   
   I am still going through possible uses for the stored data. A few of the obvious uses would be creating alerts for price drops, value assessment on new items based on other similarly named items, and determining which sites tend to give the best deals.
