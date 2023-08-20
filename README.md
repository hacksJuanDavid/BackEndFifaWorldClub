/////////////////////////

## EndPoints API

### Get all clubs

```
GET /fifaWorldClub
```

### Get one club

```
GET /fifaWorldClub/{id}
```

### Create a club

```
POST /fifaWorldClub
```

### Update a club

```
PUT /fifaWorldClub/{id}
```

### Delete a club

```
DELETE /fifaWorldClub/{id}
```

## Description

```
This project is a simple CRUD using FastApi and MongoDB
```

## Install conda

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

```
bash Miniconda3-latest-Linux-x86_64.sh
```

```
source ~/.bashrc
```

```
conda --version
```

```
conda update conda
```

## Create environment using conda

```
1. Create environment

```

conda create -n env_python_mongo_crud python=3.10.9

```

2. Activate environment

```

conda activate env_python_mongo_crud

```

3. Deactivate environment

```

conda deactivate

```

4. List environments

```

conda env list

```

5. Remove environment

```

conda remove -n env_name --all

```

###

/////////////////////////

###

Commands using fast api and uvicorn server

###

###

1.Install fast api

```

pip install fastapi

```

2.Install uvicorn

```

pip install uvicorn

```

###

```

###

1.Run server using uvicorn

```

uvicorn app:app --reload

```

###

###

1. Intall models

```

pip install pydantic

```

```

conda install pydantic -c conda-forge

```

## Create Requirements

    ```
    pip freeze > requirements.txt
    ```

## Install Requirements

    ```
    pip install -r requirements.txt
    ```

## Estructura del proyecto

```
.
├── app.py
├── config
│   ├── db.py
│   └── __pycache__
│       └── db.cpython-310.pyc
├── Miniconda3-latest-Linux-x86_64.sh
├── models
│   ├── FifaworldClub.py
│   └── __pycache__
│       └── FifaworldClub.cpython-310.pyc
├── __pycache__
│   └── app.cpython-310.pyc
├── README.md
├── requirements.txt
├── routes
│   ├── FifaworldClub.py
│   └── __pycache__
│       ├── FifawordClub.cpython-310.pyc
│       └── FifaworldClub.cpython-310.pyc
└── schema
    ├── FifaworldClub.py
    └── __pycache__
        └── FifaworldClub.cpython-310.pyc

9 directories, 14 files
```
