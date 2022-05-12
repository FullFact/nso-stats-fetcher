# National statistics data on inflation

This is a graph of inflation in a number of countries over time.

![Inflation in different countries over time](./data/inflation_stats.png)

However, making this graph was not simple. It took time, plenty of searching and some programming skills to create. 

This shouldn't be the case. As these are national statistics, everyone should be able to easily find, view and analyse this data. 

## Where did this data come from? 

Probably a few questions raised in your head when you looked at this graph. 





Inflation is a measure of the rate at which the value of all goods and services in a country increases. It is measured in percentage points per year. 

The fragility, especially of PDFs, means whenever this data is updated the scripts to pull the data will also break. Perhaps we need some way of checking for these and not pulling data if so. 

## Argentina
- Monthly year-on-year inflation retrieved from [this page](https://datos.gob.ar/series/api/series/?ids=148.3_INIVELNAL_DICI_M_26&collapse=month&collapse_aggregation=avg&representation_mode=percent_change_a_year_ago&start_date=2021-05-01&end_date=2021-06-01).


## South Africa Data
### Inflation 
- There are two types of inflation available on the Statistics South Africa page. 
  - Consumer Price Index
  - Producer Price Index 

#### Consumer Price Index
- The [CPI info page is here](http://www.statssa.gov.za/?page_id=1854&PPN=P0141). 
- The actual table we want is in the CPI History document. 
  - [Document is here](http://www.statssa.gov.za/publications/P0141/CPIHistory.pdf)
  - This in PDF format. 
  - Needs to be individually parsed. 

#### Producer Price Index
- [South Africa producer price index](http://www.statssa.gov.za/?page_id=1854&PPN=P0142.1)
- [PDF of history of PPI in South Africa](http://www.statssa.gov.za/publications/P01421/Final_manufactured_goods.pdf)
  - Notable here that the table contains sub-rows which make it even harder to parse data from

## United Kingdom Data
### Inflation
- Types
  - CPI

#### Consumer Price Index
- [Consumer price inflation including housing](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l55o/mm23)
  - [Has a downloadable .xls file](https://www.ons.gov.uk/generator?format=xls&uri=/economy/inflationandpriceindices/timeseries/l55o/mm23)
  - Does offer a way to filter the Excel file and get the info that you need
