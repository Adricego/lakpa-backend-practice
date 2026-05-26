# LAKPA Backend Practice

Ejercicios de práctica para entrevista técnica junior fullstack/backend.

## Stack inicial

- Python
- Flask
- API REST básica

## Endpoints

### GET /health

Verifica que la API esté funcionando.

Respuesta esperada:

```json
{
  "status": "ok"
}
```
## Cómo ejecutar el proyecto

Crear entorno virtual:
```bash
python -m venv venv
```

Activar entorno virtual en Git Bash:
```bash
source venv/Scripts/activate
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

Ejecutar API:
```bash
flask --app app run --debug
```

