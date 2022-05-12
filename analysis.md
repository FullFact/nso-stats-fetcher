# A journey into some national inflation data

## A graph of some country's inflation

* This is a graph
  * Well, abracadabra. Here’s a graph of it This is a plot of inflation over time in 4 different countries. You can also view it as [an interactive plot.](https://rawcdn.githack.com/FullFact/nso-stats-fetcher/35d695071faf97930960102da860cf83e73f1c5e/data/inflation_stats.html) 
* Picture of the graph
  * ![Inflation in different countries over time](./data/inflation_stats.png)￼
* However, making this graph was not simple. 
  * It took a lot of time, plenty of searching and some programming skills to create. This shouldn't be the case. 
* As these are national statistics, everyone should be able to easily find, view and analyse this data. 

* There’s some probably some questions you might be thinking. 
  * Where did the data for this come from? 
  * Why does South Africa have so many plot points?
  * Why does Argentina have so few?
* This work will talk about how this data came about

* **Why are you doing this?**
  * Provide a database of well-formatted data that can be used in [Full Fact’s Robo-checking](https://github.com/FullFact/Robo-checking). 
  * Show how varied and hard to collect national statistics data across countries can be
* **What are national statistics?** 
  * What are NSS
  * What are NSO
  * What is inflation?
    * It shows a type of inflation called the Consumer Price Index. This is how much a typical basket of goods has changed in price from year to year, and calculated every month. So how much did the price of goods cost in, say, this February versus last February.
    * There’s a few types
      * CPI
      * PPI
      * RPI
  * National statistics are data
* **Process for each country**
  * Argentina
    * - Monthly year-on-year inflation retrieved from [this page](https://datos.gob.ar/series/api/series/?ids=148.3_INIVELNAL_DICI_M_26&collapse=month&collapse_aggregation=avg&representation_mode=percent_change_a_year_ago&start_date=2021-05-01&end_date=2021-06-01).
    * Website is this. Looked through their page, using translate. Found some measure of inflation. 
    * Turned to our project partners in Chequeado. After much discussion found this. 
    * Luckily they have a JSON format. Which is structured this way. 
  * Nigeria
    * Nigeria statistics relatively easy to find the data I wanted. 
    * The format of the table though was quite tricky to parse. 
  * South Africa
    * The [CPI info page is here](http://www.statssa.gov.za/?page_id=1854&PPN=P0141). 
    * The actual table we want is in the CPI History document. 
    * [Document is here](http://www.statssa.gov.za/publications/P0141/CPIHistory.pdf)
    * This in PDF format. 
    * Needs to be individually parsed. 
    * Here is the page for South Africa. Here’s how I navigated to it. 
    * Then describe the PDF
  * United Kingdom
    * The ONS make it pretty easy to find this page
    * There is a CSV to download. 
    * However, there is this magical /data thing
* **Improving national statistics publishing**
  * This shouldn’t be as difficult to do this. Not that each individual site is particularly bad. It’s just that adding them up and combining them takes a lot of work of understanding the individual knowledge of each NSO.  
  * The more it takes to read these the more locked away this information becomes
  * If we have standards in data publishing by NSOs, and that they make data more easily machine readable. 
  * And then ultimately the point is to make it easier to gain insights and make better decisions in the world

