import requests
import time

def get_single_site(url):
    with requests.get(url) as response:
        print ('Read {} from {}'.format(len(response.content)), url)

def get_all_sites(sites):
    for url in sites:
        get_single_site(url)

if __name__ == '__main__':
    start_time = time.time()
    urls = [
        'https://www.google.com',
        'https://www.amazon.com'
    ]

    get_all_sites(urls)
    end_time = time.time() - start_time

    print ('Downloaded {} in {} seconds'.format(len(urls), end_time))