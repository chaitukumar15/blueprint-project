import requests as req 

import pandas as pd 



res=req.get("https://fakestoreapi.com/products")

data=res.json()

dataaa=pd.array([1,2,3,4,5])
print(dataaa)