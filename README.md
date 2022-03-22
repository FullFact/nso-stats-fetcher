# nso-stats-fetcher
Fetches and cleans data from NSO websites and publishes them as tidy data

## Installation 
- Had to install Java to get Tabula working to read PDFs
- 

The fragility, especially of PDFs, means whenever this data is updated the scripts to pull the data will also break. Perhaps we need some way of checking for these and not pulling data if so. 

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
- [Consumer price inflation tables](https://www.ons.gov.uk/economy/inflationandpriceindices/datasets/consumerpriceinflation)
  - [Has a downloadable .xls file](https://www.ons.gov.uk/file?uri=%2feconomy%2finflationandpriceindices%2fdatasets%2fconsumerpriceinflation%2fcurrent/consumerpriceinflationdetailedreferencetables15022022174940.xls)
  - Does offer a way to filter the Excel file and get the info that you need
