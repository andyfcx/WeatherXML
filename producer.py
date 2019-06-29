from tasks import job
import csv
# Read dates
with open('date2018') as f:
    dates = f.read().split('\n')
# Read sites
with open('sites_all.csv') as f:
    sites = [{k: v for k, v in row.items()}
             for row in csv.DictReader(f, skipinitialspace=True)]

for site in sites:
    for date in dates:
        job.delay(site, date)
