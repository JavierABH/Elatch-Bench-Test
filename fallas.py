import os
import re
import csv
from bs4 import BeautifulSoup

directory = 'Logfile'
serial_pattern = r'\[([^\]]+)\]'
headers = ['Serial',
           'Status',
           'PN',
           'falla',
           ]

serials = []
selectors = ['table.uutTable tr:nth-child(8) td:nth-child(2)',
             'table.uutTable tr:nth-child(9) td:nth-child(2)',
             'table.criticalFailureTable tr:nth-child(3) td:nth-child(1) a'
]

csv_file = 'data.csv'

def main():
    i = 0
    with open(csv_file, mode= 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
    print('Write header')

    for filename in os.listdir(directory):
        i += 1
        serial = ''
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            matches = re.findall(serial_pattern, filepath)
            if matches:
                serial = matches[0]

            with open(filepath, 'r', encoding='utf-8') as file:
                html = file.read()
                # print(html)

            soup = BeautifulSoup(html, 'html.parser')
            values = []

            status = soup.select_one(selectors[0]).text.strip()
            partnumber = soup.select_one(selectors[1]).text.strip()

            if status == 'Failed':
                    failure = soup.select_one(selectors[2]).text.strip()
                    values.extend([status, partnumber, failure])
            else:
                values.extend([status, partnumber])

            with open(csv_file, mode= 'a', newline= '') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([serial] + values)
            print(f'{i}.-{serial} write values')

    print('done')

if __name__ == '__main__':
    main()