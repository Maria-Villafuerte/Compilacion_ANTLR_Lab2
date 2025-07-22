# SimpleLang Type Checker

Un verificador de tipos simple para un lenguaje de programación básico implementado con ANTLR4 y Python.

## Descripción

Este proyecto implementa un analizador de tipos para SimpleLang, un lenguaje que soporta:
- Tipos de datos: enteros, flotantes, cadenas y booleanos
- Operadores aritméticos: `+`, `-`, `*`, `/`
- Operadores lógicos: `&&`
- Operadores de comparación: `==`
- Expresiones con paréntesis

## Archivos del Proyecto

- `SimpleLang.g4` - Gramática ANTLR4 del lenguaje
- `custom_types.py` - Definición de tipos de datos
- `type_check_listener.py` - Verificador de tipos usando patrón Listener
- `type_check_visitor.py` - Verificador de tipos usando patrón Visitor
- `DriverListener.py` - Driver principal usando Listener
- `Driver.py` - Driver principal usando Visitor
- `program_test_pass.txt` - Ejemplos de código que pasa la verificación
- `program_test_no_pass.txt` - Ejemplos de código con errores de tipo

## Requisitos

- Python 3.x
- ANTLR4 Python runtime
```bash
pip install antlr4-python3-runtime
```

## Uso

### Usando el patrón Listener:
```bash
python DriverListener.py programa.txt
```

### Usando el patrón Visitor:
```bash
python Driver.py programa.txt
```

## Ejemplos

### Código válido (`program_test_pass.txt`):
```
5 == 3
true && false
"hello" == "world"
2.5 == 3.0
```

### Código con errores (`program_test_no_pass.txt`):
```
5 == "hello"      # Error: no se pueden comparar int y string
true && 3         # Error: && requiere operandos booleanos
"text" == 42      # Error: no se pueden comparar string e int
```

## Reglas de Tipos

- **Operaciones aritméticas** (`+`, `-`, `*`, `/`): Solo entre números (int/float)
- **Operador lógico** (`&&`): Solo entre booleanos
- **Comparaciones** (`==`): Entre tipos compatibles:
  - Números (int/float) pueden compararse entre sí
  - Tipos idénticos pueden compararse (string con string, bool con bool)

## Video Explicativo
[Laboratorio 2 Construcción de compiladores _ Verificador de tipos](https://youtu.be/eaOmnPHg7nQ)

## Estructura del Verificador

El proyecto implementa dos enfoques para la verificación de tipos:

1. **Listener Pattern**: Recorre el árbol sintáctico y acumula errores en una lista
2. **Visitor Pattern**: Propaga tipos hacia arriba y lanza excepciones en errores

Ambos enfoques producen el mismo resultado pero con diferentes estrategias de manejo de errores.