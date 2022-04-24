import os
import wget
# base url: https://archive.org/download/reddit-place-2022-datasets

url = "https://archive.org/download/reddit-place-2022-datasets/2022_place_canvas_history-00000000000{num}.csv.gzip"

file_name = "2022_place_canvas_history-00000000000{num}.csv.gzip"
                

for i in range(79):
    format_url = url.format(num=i)
    format_name = file_name.format(num=i)
    if os.path.exists(format_name):
        print("skipping " + format_name)
        continue
    print("downloading" + format_name)
    wget.download(format_url, format_name)
