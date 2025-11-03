# 📚 Validador de ISBN — Actividad V

**Alumnos:** Díaz Hernández Eduardo  
**Docente:** M.A. Raúl Iván Herrera González  
**Materia:** Integradora
**Universidad Tecnológica de Durango**

---

##  Descripción del Proyecto

Este repositorio contiene un módulo de validación de códigos ISBN-10 e ISBN-13, desarrollado como parte de la Actividad V. El objetivo es aplicar pruebas básicas (unitarias, caja negra/blanca, particiones de equivalencia, análisis de fronteras y propiedades) a un sistema realista, integrando herramientas TIC como control de versiones, CI y análisis de cobertura.

---

##  Estructura del Proyecto
enlace a Github:https://github.com/DiazEduardo19/ReadMe-Actividad-5
##  Ejemplos de pruebas

### test_isbn10.py

```python
def test_valid_isbn10_digits():
    assert is_valid_isbn10("0306406152") is True

def test_valid_isbn10_with_X():
    assert is_valid_isbn10("0-8044-2957-X") is True

```

### test_properties.py

```python
def test_idempotent_normalization():
    raw = "978-0-306-40615-7"
    once = normalize_isbn(raw)
    twice = normalize_isbn(once)
    assert once == twice
```

## ⚙️ Instalación y ejecución de pruebas

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/validador-isbn.git
cd validador-isbn
