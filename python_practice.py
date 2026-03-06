# 3-5-2026
# Certification Practice

import csv

states = [ {'state': 'California', 'capital': 'Sacramento', 'year_admitted': 1850},
           {'state': 'New York', 'capital': 'Albany', 'year_admitted': 1788},
           {'state': 'Texas', 'capital': 'Austin', 'year_admitted': 1845} ]

states[0]["capital"] = "Merced"
states.append({'state': 'Nevada', 'capital': 'Carson City', 'Year Admitted': 1864})


f = open("/Users/mike/Downloads/employees.csv")
rows = csv.DictReader(f)
max_sal = []
for row in rows:
    max_sal.append(row['Salary'])

print(max(max_sal))

f.close()
