
## **Quick guide**

</br>

### Requirements

- python 3.10.6 (should work with most versions above 3.9)
- pyenv
- poetry

</br>

### How to setup

1. Install poetry:
   [Link](https://python-poetry.org/docs/#installation)

2. Install pyenv:
   [Link](https://github.com/pyenv/pyenv#installation)

3. Install python 3.10.6:

```bash
pyenv install 3.10.6
```

4. Clone the repository:

```bash
git clone git@github.com:MatheusFBBueno/inaturalist-bot.git
```

5. Enter the project folder:

```bash
cd inaturalist-bot
```

6. Change default python version in current local:

```bash
pyenv local 3.10.6
```

7. Activate virtualenv for the python installed version:

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

8. Install dependencies:

```bash
poetry install
```
### To specify what species and licenses to search for
Simply edit the config.ini file located in the config folder, for example:
<code>
SPECIES_NAME=Lonomia obliqua  #Moth species

LICENSE=CC-BY-NC  #Non-commercial license

FILTER_LARVAE=False  #Set to True if you only want images of larvae
</code>



### To run Bot
```bash
poetry run main
```