import os
import pandas as pd
import numpy as np
import requests
import json


brands = pd.read_csv("data_brands.csv").to_numpy().flatten()


url_base =  "https://github.com/goodvibes-org/cosas_publicas/raw/feature/deteccion_producto_unico_api_keyword_reducida/data_ocr_ocr/{}.jpg"
url_base = "https://goodvives.ml/goodvibes/api/assets/data_ocr_ocr/{}.jpg"

base_docker = 'http://localhost:8082/name_match?url_data={}'
uq_brands = pd.unique(brands)
data_tr =  {brand : {} for brand in uq_brands}
data_te =  {brand : {} for brand in uq_brands}
for n, brand in enumerate(brands): 
    url = base_docker.format(url_base.format(n))
    rsp = requests.get(url).json()
    if n % 3 == 0:
        data_tr[brand][n] = rsp[-1]
    else:
        data_te[brand][n] = rsp[-1]

with open("tr_dataset.json", "w") as file:
    json.dump(data_tr,file)

with open("te_dataset.json", "w") as file:
    json.dump(data_te,file)


print("Job is done")


