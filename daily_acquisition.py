import os
import json
import urllib.request
import time


def make_request():
    offset = 1
    json_num = 0
    count = 2
    while offset < count:
        url_n = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-12-01&enddate=2018-12-31&limit=1000&offset=' + str(offset)
        key='NOAA_TOKEN'
        token=os.getenv(key)
        header = {'token': token}
        req = urllib.request.Request(url=url_n, headers=header)
        data = urllib.request.urlopen(req)
        final_resp = data.read()
        form = json.loads(final_resp)
        json_file = './data/daily_summaries/daily_summaries_FIP10003_dec_2018_' + str(json_num) + '.json'
        with open(json_file, 'w') as outfile:
            json.dump(form, outfile, sort_keys=True, indent=4)
        count = form['metadata']['resultset']['count']
        offset += 1000
        print("Complete " + str(json_num))
        json_num +=1
        time.sleep(1)

if __name__ == '__main__':
    make_request()

