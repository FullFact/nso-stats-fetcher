
# import requests
import tabula

def fetch_za_inflation():
    url = 'http://www.statssa.gov.za/publications/P0141/CPIHistory.pdf'
    # response = requests.get(url)
    
    # tmp_pdf_filepath = '/tmp/ZA_CPIHistory.pdf'
    # with open(tmp_pdf_filepath, 'wb') as f:
    #     f.write(response.content)

    # tables = camelot.read_pdf(tmp_pdf_filepath)
    tables = tabula.read_pdf(url, pages="all", multiple_tables=True)

    a = 1



if __name__ == '__main__':
    fetch_za_inflation()
    # ons_scraper = create_ons_scraper(production_eventing.NoopEventer())
    # print(ons_scraper.get_datasets())
    # ons_scraper.close()
