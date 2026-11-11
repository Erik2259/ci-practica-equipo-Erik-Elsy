# ci-practica-equipo-Erik-Elsy

Proyecto en Python utilizado para practicar integración continua con GitHub Actions.
Equipo: Erik, Elsy, Alexis y Carlos.

## Contenido

- `calculadora.py`: suma, resta, multiplicación, división, potencia, raíz cuadrada y porcentaje.
- `estadisticas.py`: promedio, mediana, máximo, mínimo y rango de una lista.
- `test_calculadora.py` y `test_estadisticas.py`: pruebas automatizadas con pytest.

## Integración continua

El workflow `.github/workflows/ci.yml` se ejecuta con cada push y pull request:

1. Instala las dependencias (build).
2. Ejecuta el análisis estático con flake8.
3. Ejecuta las pruebas con pytest y mide la cobertura (mínimo 90 %).
4. Guarda el reporte de cobertura (`coverage.xml` y `htmlcov/`) como artefacto.

## Ejecutar en local

```bash
pip install -r requirements.txt
flake8 .
pytest --cov=calculadora --cov=estadisticas --cov-report=term-missing
```
