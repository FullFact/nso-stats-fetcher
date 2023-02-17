[![fetch-stats](https://github.com/FullFact/nso-stats-fetcher/actions/workflows/fetch_stats.yml/badge.svg)](https://github.com/FullFact/nso-stats-fetcher/actions/workflows/fetch_stats.yml)

# National Statistical Offices Statistics Fetcher
Fetches and cleans data from NSO websites and publishes them as in a standardised [tidy data](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html) format. 

This work has two goals
- Provide a database of well-formatted data that can be used in [Full Fact’s Stats Checking tools](https://fullfact.org/blog/2021/jul/how-does-automated-fact-checking-work/). 
- To highlight how much work is involved to collect and compare national statistics data across countries, [as discussed in the write-up](https://fullfact.github.io/nso-stats-fetcher/analysis.html).

The data files follows a simple `timescale,observation` format. Time is YYYY-MM, and observation is percentage change. For example:

```
month,observation
1996-01,47.56
1996-02,43.645
1996-03,41.9048
...
```

These are the statistics that are fetched, reformatted and stored in the `./data` directory:
- Argentina
  - [Consumer price index – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/ar_inflation_cpi.csv) ([source](https://datos.gob.ar/series/api/series/?ids=148.3_INIVELNAL_DICI_M_26&collapse=month&collapse_aggregation=avg&representation_mode=percent_change_a_year_ago))
- Ireland
  - [Consumer price index – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/ie_inflation_cpi.csv) ([source](https://data.cso.ie/product/CPIM))
- Japan
  - [Consumer price index – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/jp_inflation_cpi.csv) ([source](https://www.stat.go.jp/english/data/cpi/1581-z.html))
- Mexico
  - [Consumer price index – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/mx_inflation_cpi.csv) ([source](https://www.stat.go.jp/english/data/cpi/1581-z.html))
- Nigeria
  - [Consumer price index – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/ng_inflation_cpi.csv) ([source](https://nigerianstat.gov.ng/elibrary/read/1241157))
- Philippines
  - [Consumer price index – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/ph_inflation_cpi.csv) ([source](https://psa.gov.ph/statistics/survey/price/summary-inflation-report-consumer-price-index-2018100-may-2022))
- UK
  - [Consumer price inflation (excl. housing) – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/uk_inflation_cpi.csv) ([source](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/d7g7/mm23))
  - [Consumer price inflation (inc. housing) – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/uk_inflation_cpih.csv) ([source](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l55o/mm23/data))
  - [Retail price inflation – monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/uk_inflation_rpi.csv) ([source](https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/czbh/mm23/data))
- South Africa
  - [Consumer price index - monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/za_inflation_cpi.csv) ([source](https://www.statssa.gov.za/?page_id=1854&PPN=P0141))
  - [Producer price index - monthly year-on-year](https://fullfact.github.io/nso-stats-fetcher/data/za_inflation_ppi.csv) ([source](https://www.statssa.gov.za/?page_id=1854&PPN=P0142.1))

In almost all cases the data file is downloaded and read in (except for Philippines where the numbers were hard-coded). Preferably the files would be JSON or a CSV, but some countries have PDFs or XLS files. The location of all these files online and other metadata is in the [data/nso_stats_metadata.json](https://fullfact.github.io/nso-stats-fetcher/data/nso_stats_metadata.json) file.

It is also deployed as a Github action which runs several times between 6am and 10am UTC. So some of the statistics should stay up-to-date. You can view this Github action in `.github/workflow/fetch_stats.yaml`. However, given the variability of these statistics data, it wouldn't be surprising if the action breaks at some point if the published format changes.

# Dependenices 
- Java 8+ (for [Tabula to read PDFs](https://tabula-py.readthedocs.io/en/latest/getting_started.html#requirements))
- Python 3.10+
  - It likely works for older versions of Python, but it hasn't been tested

# Setup
Clone this repo
```
git clone https://github.com/FullFact/nso-stats-fetcher.git
```

Install required libraries 

Either
```
poetry install
```
or
```
pip install -r requirements.txt
```

To run the scripts and fetch updated versions of all the statistics data, run:

```
python src/nsofetch/fetch_all.py
```

Or just run each country's individual script individually. We use [ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) for standardised country names.
