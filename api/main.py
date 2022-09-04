from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.responses import StreamingResponse
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mclr
import io
import os


app = FastAPI()
origins = [
  'http://localhost',
  'http://localhost:8080',
  'http://192.168.1.15',
  'http://192.168.1.15:8080',
  'http://127.0.0.1',
  'http://127.0.0.1:8000'
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
  expose_headers=[]
)
settingImage = {
  "dbz": {
    "colors": ["#04cefa", "#004fff", "#008081",
          "#01e403", "#00b103", "#81cc01",
          "#ffe201", "#ffa004", "#fd3a05",
          "#e00002", "#b00001", "#ce0085",
          "#c700fe", "#9300fc"],
    "norm": plt.Normalize(vmin=5, vmax=75)
  },
  "qpe": {
    "colors": ['#eeeeee', '#00FF00', '#ffff00', '#FFA500',
      '#FF0000', '#800080', '#0000FF'],
    "norm": plt.Normalize(vmin=2.5, vmax=17.5)
  }
}

settingImage["dbz"]["cmap"] = mclr.LinearSegmentedColormap.from_list("", settingImage["dbz"]["colors"])
settingImage["qpe"]["cmap"] = mclr.LinearSegmentedColormap.from_list("", settingImage["qpe"]["colors"])

@app.get('/')
async def index():
  return {'data': 'Hello World'}

@app.get("/db")
async def db():
  radar=[
        {
          "id": 1,
          "jam": "17:10",
          "file": "santanu001_20211210_171011"
        },
        {
          "id": 2,
          "jam": "17:12",
          "file": "santanu001_20211210_171210"
        },
        {
          "id": 3,
          "jam": "12:14",
          "file": "santanu001_20211210_171412"
        },
        {
          "id": 4,
          "jam": "12:16",
          "file": "santanu001_20211210_171610"
        }
      ]
  return radar

@app.get("/status/{filename}")
async def status(filename:str):
  path = f"./datamat/{filename}.mat"
  if not os.path.exists(path):
    # raise HTTPException(status_code=404, detail="Item not found")
    return JSONResponse(status_code=404)
  # path = path.replace(r"/", "\\") # Dicomment apabila dijalankan di linux
  mat = sio.loadmat(path)
  data = mat['ZI']
  data = data / 10**4
  return data.max()


@app.get("/dbz/datamat/{filename}")
async def dbz(filename: str):
  path = f"./datamat/{filename}.mat"
  if not os.path.exists(path):
    # raise HTTPException(status_code=404, detail="Item not found")
    return JSONResponse(status_code=404)
  # path = path.replace(r"/", "\\") # Dicomment apabila dijalankan di linux
  mat = sio.loadmat(path)
  data = mat['ZI']
  data = data / 10**4
  data[data<0] = 0
  data[data == 0] = np.nan
  image = settingImage["dbz"]["cmap"](settingImage["dbz"]["norm"](np.flip(data.T, 0)))
  imgio = io.BytesIO()
  plt.imsave(imgio, image, format='PNG')
  imgio.seek(0)
  return StreamingResponse(imgio, media_type="image/png")
