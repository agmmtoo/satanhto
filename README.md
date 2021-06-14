# Satanhto

Video streamming website with user, admin upload features.

## Getting Start

### Clone the repo

```git
git clone https://github.com/agmyintmyatoo/satanhto.git
```

Virtual enviroment is recommended.

### Create and activate virtual environment

> Unix
>
>> ```bash
>> python3 -m venv env
>> source env/bin/activate
>> ```
>
> Windows
>
>> ```bash
>> py -m venv env
>> env/Scripts/activate
>> ```
>

```bash
cd satanhto
```

### Install requirements

You'll need Python runtime 3.9.5 or higher.

Install django and all dependicies stated in requirements file.

```python
python3 -m pip install -r requirements.txt
```

### Run migration commands

```python
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Create admin user

```python
python3 manage.py createsuperuser
```

### Finally, test in local server

```python
python3 manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
