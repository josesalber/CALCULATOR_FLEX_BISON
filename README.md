# Calculadora Científica con Flex, Bison y Python

Este repositorio contiene una calculadora científica implementada utilizando **Flex** y **Bison** para el análisis léxico y sintáctico, junto con una interfaz gráfica desarrollada en **Python** usando **Tkinter**.

## Características

- **Flex y Bison**: Implementan el núcleo de la calculadora para analizar y evaluar expresiones matemáticas.
- **Interfaz Gráfica con Tkinter**: Ofrece una experiencia de usuario amigable para ingresar y evaluar expresiones.
- Soporte para operaciones matemáticas básicas y avanzadas, incluyendo:
  - Suma, resta, multiplicación y división.
  - Funciones trigonométricas, logarítmicas y exponenciales.
  - Paréntesis para agrupación de operaciones.

## Requisitos del Sistema

- **Flex** y **Bison** instalados en el sistema.
- Compilador **GCC**.
- **Python 3.6+** instalado.
- Biblioteca estándar de **Tkinter** (incluida en la mayoría de las distribuciones de Python).

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/calculadora-flex-bison-python.git
   cd calculadora-flex-bison-python
   ```

2. Compila los archivos de Flex y Bison:
   ```bash
   bison -d calc.y
   flex calc.l
   gcc calc.tab.c lex.yy.c -o calculadora -lm
   ```

3. Ejecuta la interfaz gráfica:
   ```bash
   python interfaz.py
   ```

## Uso

1. Abre la interfaz ejecutando `interfaz.py`.
2. Ingresa expresiones matemáticas en el cuadro de texto.
3. Presiona el botón "Calcular" para obtener el resultado.

## Estructura del Repositorio

- `calc.l`: Archivo Flex para definir el análisis léxico.
- `calc.y`: Archivo Bison para definir la gramática y el análisis sintáctico.
- `interfaz.py`: Interfaz gráfica en Python utilizando Tkinter.
- `calc.tab.c`, `calc.tab.h`, `lex.yy.c`: Archivos generados por Bison y Flex tras la compilación.
- `README.md`: Documentación del proyecto.

## Ejemplo de Compilación

```bash
bison -d calc.y
flex calc.l
gcc calc.tab.c lex.yy.c -o calculadora -lm
python interfaz.py
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, por favor abre un issue o envía un pull request.

## Licencia
Desarrollado por Jose Salirrosas como parte del curso Teoría de Lenguajes de Programación y Métodos de Traducción II.

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
