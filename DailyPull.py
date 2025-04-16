import urllib.request
import json

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31"
tok = "pLPWsbxSowNQurrZleAiABCJGkuJepeg"
limit = 1000

def make_request (url, filename, headers):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode('utf-8'))
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Success")
            return data.get('metadata', {}).get('totalCount', 0)

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


if __name__ == "__main__":
    headers = {
        'token': tok
    }
    offset_increment = limit

    for i in range(40):
        offset = i * offset_increment
        api_url = f"{url}&limit={limit}&offset={offset}"
        filename = f"locations_{i}.json"
        make_request(api_url, filename, headers)
        print(f"Attempting to create file: {filename}")