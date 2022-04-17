import trafilatura


## get text from website
def get_text_page(url):
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.bare_extraction(downloaded)
