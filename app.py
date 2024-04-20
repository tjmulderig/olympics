import config
import csv

dfile = 'olympics_athlete_events.csv'

# Establish database connections
r = config.get_redis_connection()

# Clear db
r.flushall()

with open(dfile, mode='r') as f:
    data = csv.DictReader(f)
    for record in data:
        row_idx = record.pop('ID')
        r.hmset(f"row:{row_idx}", record)
        print(f"{row_idx} added to db")

r.close()