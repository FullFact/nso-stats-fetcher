# nso-stats-fetcher
Fetches and cleans data from NSO websites and publishes them as tidy data

## Installation 
- Had to install Java to get Tabula working to read PDFs
- 

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