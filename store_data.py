import json
import pymysql

# Open the JSON file and read its contents
with open('jsondata.json') as f:
    json_data = f.read()

# Decode JSON
data = json.loads(json_data)


# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='', database='data_visualization')
cursor = conn.cursor()

# Insert data into table
for row in data:
     # Check if intensity is available, otherwise insert NULL
    intensity = row['intensity'] if row['intensity'] != '' else None
    likelihood = row['likelihood'] if row['likelihood'] != '' else None
    relevance = row['relevance'] if row['relevance'] != '' else None

    sql = """INSERT INTO EnergyForecasts 
    (end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, source, title, likelihood) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
        row['end_year'], intensity, row['sector'], row['topic'], row['insight'], row['url'], row['region'],
        row['start_year'], row['impact'], row['added'], row['published'], row['country'], relevance,
        row['pestle'], row['source'], row['title'], likelihood
    )
    cursor.execute(sql, values)
    conn.commit()

# Close connection
cursor.close()
conn.close()
