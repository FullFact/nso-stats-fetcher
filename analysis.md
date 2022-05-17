# Better national statistics data publishing

## Comparing inflation across countries

This is a graph of inflation over time in Argentina, Nigeria, the UK and South Africa (also online as [an interactive plot](https://rawcdn.githack.com/FullFact/nso-stats-fetcher/35d695071faf97930960102da860cf83e73f1c5e/data/inflation_stats.html)). It shows the monthly consumer price index, year-on-year. Simply put, it's how much a basket of regular household goods has changed in price from, say, April one year, to the following one.    

![Inflation in different countries over time](./data/inflation_stats.png)￼

What's really obvious here is the big difference in information about inflation between the different countries. South Africa's stretches all the way back to the 1920s while data on Argentina only starts in the late 2010s.     

This is a sign that something is going on with the data sources. They're not standardised or the making and publishing of these statistics differs a lot. 

And indeed, making this graph was not at all simple. It took a lot of time, plenty of searching and some programming skills to create. 

This shouldn't be the case. These are very important national statistics data, and they should be be easy for anyone find, view and analyse. 

In this piece, I'll show the differences in how this information was published. And then say how it can be published better. 

## Why are you doing this?

Two reasons, really.

Full Fact are developing a robo-checking tool, which automates parts of fact checking. To say whether a claim or true or not, it needs a standardised, reliable dataset. One of the topics it is used on is inflation. So, we created code which fetches and standardises this data and puts it all in [one location within a Github repo](https://github.com/FullFact/nso-stats-fetcher/tree/main/data).

More broadly, at the Open Data Institute, we want a world where data works for everyone. National statistics are really important open data. And we hope with better-published national statistics, it means more people using them to for more insights and better decisions. We hope this article helps the cause!

## What are national statistics

There are many organisations in a country that can publish national statistics data. These include government departments, research institutes, health services, survey companies or international groups. All the statistics published by these creates the [**national statistical system**](https://stats.oecd.org/glossary/detail.asp?ID=1726).

One organisation usually operates as the main hub for national statistical data in a country. These are known as [National Statistical Offices](https://stats.oecd.org/glossary/detail.asp?ID=4344) (NSOs):

NSOs publish statistical data on topics like health, the economy, education and housing. People in the public and private sectors use this data to observe what is happening in the country and to plan ahead. There are NSOs in almost every country on earth. Nearly every country has one main NSO, but in some, such as the USA, the job is split across multiple organisations.

They're statistics produced within countries about how that country is doing. They can come from many sources including goverment departments, health services, academics or national . These all make up what is known as the [national statistical system](https://stats.oecd.org/glossary/detail.asp?ID=1726). 

## A brief note on inflation

There's other places much [more qualified than here to define inflation](https://www.oecd-ilibrary.org/economics/producer-price-indices-ppi/indicator/english_a24f6fa9-en). But, in short, there are a few types. Consumer Price Index, CPI, is the weighted average of a typical basket of goods. CPIH is another which includes housing. There's Producer Price Index, which measures how much domestic producers pay. And there's also Retail Price Index which measures retail goods and services.

When you see "inflation" in the news, they're usually talking about CPI. And therefore, this is most important for fact checking.  So we focus on how we got the CPI for each country. 

Also, we're not here to judge how these measures are calculated or which measure is the best. We're focused on how these numbers appear on NSO websites, and are they easy to use, share and analyse. 

## Getting the inflation data for each country

These are some points about collecting the data from each country. The details might be a bit boring, but the main thing is just how varied, challenging and often needing special insider knowledge it is to get, what should, headline data from these NSOs. 

### Argentina

- [Instituto Nacional de Estadística y Censos](https://www.indec.gob.ar) (INDEC), is the country's main NSO. It has [different pages](https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-5-31) with [reports](https://www.indec.gob.ar/uploads/informesdeprensa/ipc_05_2224DC1A5434.pdf) and some [datasets](https://www.indec.gob.ar/ftp/cuadros/economia/sh_ipc_aperturas.xls) (.XLS file) related to inflation (or "*Índice de precios al consumidor*" as is the translation of "consumer price index"). 
- This was quite a difficult page for me to find though. A large part of this is definitely my lack of Spanish skills. I tried using an in-browser translation service but couldn't find exactly what I wanted. Then I asked two Spanish-speaking people in the ODI to help me out, but neither could find the CPI numbers. 
- Luckily, on this project we have Chequeado as partners. So I have quite a long message thread on Slack with Ignacio Ferreiro and Francisco Pensa who helped me ifnd the page for monthly year-on-year CPI on its [own dedicated page](https://datos.gob.ar/series/api/series/?ids=148.3_INIVELNAL_DICI_M_26&collapse=month&collapse_aggregation=avg&representation_mode=percent_change_a_year_ago). 
- And the data was available in CSV and JSON. Fantastic! However, there was one slight odd thing whether it showed the rate as percentages on the graph but the data is in ratios between 0 and 1. 
- Overall, the data is well-formed, and very easy to work with. However, it's not ideal that I needed to find experienced users of these national statistics to find where this data is stored.  

### South Africa

- [Statistics South Africa](https://www.statssa.gov.za) is the NSO for South Africa. 
- Finding monthly CPI involved navigating through: Find Statistics -> [By theme](https://www.statssa.gov.za/?page_id=595) -> The economy -> [Inflation](https://www.statssa.gov.za/?page_id=735&id=3) -> Consumer Price Index. 
- On that page there's a standard report in PDF with the supporting tables also available to download. 
- The actual table we want is in the [CPI History document](http://www.statssa.gov.za/publications/P0141/CPIHistory.pdf) in a PDF format. 
- This PDF makes it much harder to read using a programme, unlike the JSON files from Argentina and UK. 
- However, it goes back nearly 100 years!

### Nigeria

* [Nigeria Bureau of Statistics](https://nigerianstat.gov.ng)
* The hompage has graphs of CPI but no link to the underlying datasets
* Maybe not the clearest structure but easy enough to find the table. [E-library](https://nigerianstat.gov.ng/elibrary) -> [CPI and Inflation Report April 2022](https://nigerianstat.gov.ng/elibrary/read/1241170) -> [Download Tables](https://nigerianstat.gov.ng/resource/cpi_1NewAPR2022.xlsx) (Excel file). 
* However, the format of the table though was quite tricky to parse programatically. The year isn't filled in for each month so have to interpret it based on last entered year. Month names also switch from shortened 3-letter to full names. 

### United Kingdom

* The ONS make it extremely easy to find inflation data. The link to [CPIH (housing included) data](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l55o/mm23) is right there clearly marked on the homepage.  
* However, we're looking for just the regular Consumer Price Index data. The search didn't show exactly what we needed. 
* So I just relied on Full Fact to point me to where the [dataset for CPI history is](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/d7g7/mm23). I'm still not sure how you directly navigate to it. 
* ALSO, I learned from Full Fact the one magical trick where if you type `/data` on an ONS dataset page, it'll show it in JSON! Mind blown. I'm not entirely sure if this is documented anywhere but it's extremely useful.  



## Improving national statistics publishing

This shouldn’t be as difficult to do this. Not that each individual site is particularly bad. It’s just that adding them up and combining them takes a lot of work of understanding the individual knowledge of each NSO.  

All NSOs publish statistical data about their country. But the quantity and quality of data varies greatly between them. This is very understandable as every country has different finances, resources and society.

However, there exist good practices and standards in open data publishing that every NSO, no matter the size of budget, can aim to achieve. We’re not saying every NSO needs to build large data platforms, but simple, achievable techniques exist which can really help users of data.

Open principles for data publishing are partly about following open standards and partly about thinking about how the data can best be designed for other people to be able to reuse.

The Office of National Statistics in the UK produced a [set of principles for what this can practically mean](https://digitalblog.ons.gov.uk/2017/01/06/some-open-data-publishing-principles/). In these they outline a need to consider publishing information so that it performs well on other sites and services. This is similar in many ways to the use of the [Claim Review format](https://schema.org/ClaimReview) in the fact checking world. For statistics this might be about how well it displays in the [Google dataset explorer](https://www.google.com/publicdata/directory) or in search results. This wider theme of making data part of the web is a key component of making data available in ways that support the processes of fact checking. By making access easier to the data, always presenting it in context and designing systems with reuse at the core.

The ODI has also undertaken a range of work around the idea of [data as infrastructure](https://theodi.org/topic/data-infrastructure/) and has a short eLearning course [What is open data?](https://data.europa.eu/elearning/en/module1/#/id/co-01) Both of these offer further useful guidance on this topic.



