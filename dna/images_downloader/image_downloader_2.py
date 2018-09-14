import requests
import shutil
import os

in_filename = 'aircraft_urls.txt'
out_filename = 'aircraft_urls_clean_2.txt'
folder = 'aircraft_named'
downloading = True
file_names = {}
with open(in_filename, 'r') as file:
    while downloading:
        current = file.readline().split(',')
        if not current or current == ['']:
            downloading = False
        try:
            print(f'fetching {current[1].strip()}', end=' ')
            data = requests.get(current[1], stream=True, timeout=30)
        except requests.exceptions.ConnectionError:
            print('connection error... skipping!')
            continue
        except requests.exceptions.TooManyRedirects:
            print('too many redirects... skipping!')
            continue
        except Exception as e:
            print(f'{e}... skipping!')
            continue
        print(f"status: {data.status_code} content:{data.headers.get('Content-Type')}")

        if data.status_code == 200 and data.headers.get('Content-Type', 'filetype')[:5] == 'image':
            file_type = data.headers.get('Content-Type').split('/')[-1]
            if file_type.lower() not in ['jpeg', 'jpg', 'png', 'gif']:
                file_type = 'jpg'
            output_name = current[0].replace('"','').replace(' ','_').replace('/','-').replace('\\','-')
            if file_names.get(output_name):
                file_names[output_name] += 1
            else:
                file_names[output_name] =1
            output_filename = os.path.join(folder, output_name + '_' + str(file_names[output_name]).zfill(4) + '.' + file_type)
            print(f'saving {output_filename}')
            with open(output_filename, 'wb') as outfile:
                shutil.copyfileobj(data.raw, outfile)
            with open(out_filename, 'a') as outfile_2:
                outfile_2.write(current[0] + ',' + current[1])
