import requests

def download_zip_file(url, filename):
    r = requests.get(url, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            f.write(r.content)
            print('Zip File Downloading Completed')


url = 'https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip'

# filename = url.split('/')[-1]

SourceData = "submissions.zip"
download_zip_file(url, SourceData)
