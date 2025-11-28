# ohtuvarasto
[![CI](https://github.com/cameocami/ohtuvarasto/actions/workflows/main.yml/badge.svg)](https://github.com/cameocami/ohtuvarasto/actions/workflows/main.yml)

[![codecov](https://codecov.io/github/cameocami/ohtuvarasto/graph/badge.svg?token=J1D1W6OWSN)](https://codecov.io/github/cameocami/ohtuvarasto)

Ohjelmistotuotannon tehtävät 2-13

## Web-käyttöliittymä

Varastosovellus sisältää web-käyttöliittymän, joka mahdollistaa varastojen hallinnan selaimen kautta.

### Asennus

1. Varmista, että sinulla on Python 3.12+ asennettuna
2. Asenna Poetry (jos ei ole jo asennettu):
   ```bash
   pip install poetry
   ```
3. Kloonaa repositorio ja siirry projektikansioon:
   ```bash
   git clone https://github.com/cameocami/ohtuvarasto.git
   cd ohtuvarasto
   ```
4. Asenna riippuvuudet:
   ```bash
   poetry install
   ```

### Käynnistys

Käynnistä web-sovellus:

#### Linux / macOS

```bash
cd src
poetry run python app.py
```

Kehitystilassa:

```bash
cd src
FLASK_DEBUG=true poetry run python app.py
```

#### Windows (PowerShell)

```powershell
cd src
poetry run python app.py
```

Kehitystilassa:

```powershell
cd src
$env:FLASK_DEBUG="true"; poetry run python app.py
```

#### Windows (Command Prompt)

```cmd
cd src
poetry run python app.py
```

Kehitystilassa:

```cmd
cd src
set FLASK_DEBUG=true && poetry run python app.py
```

Sovellus käynnistyy osoitteessa `http://localhost:5000`

### Käynnistys

Käynnistä web-sovellus komennolla:

```bash
cd src
poetry run python app.py
```

Sovellus käynnistyy osoitteessa `http://localhost:5000`

### Käyttö

- Klikkaa **+** -painiketta luodaksesi uuden varaston
- Syötä tilavuus ja alkusaldo pop-up-ikkunassa ja paina **Luo**
- Varastot näkyvät etusivulla säiliöelementteinä
- Klikkaa varastoa avataksesi toimintokuplan:
  - Syötä määrä ja paina **Lisää** lisätäksesi varastoon
  - Syötä määrä ja paina **Ota** ottaaksesi varastosta
- Kaksoisklikkaa varastoa muokataksesi tai poistaaksesi sen
