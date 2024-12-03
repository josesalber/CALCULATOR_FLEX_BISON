import tkinter as tk
from tkinter import messagebox
import subprocess

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica Avanzada")
        self.root.state("zoomed")  # Maximizar la ventana
        self.root.configure(bg="#ecf0f1")  # Fondo claro

        # Fuentes modernas
        self.font = ("Roboto", 12)
        self.title_font = ("Roboto", 18, "bold")

        # Título llamativo
        self.titulo = tk.Label(
                self.root,
                text="🧮 Calculadora Científica Avanzada 🧮",
                font=("Roboto", 24, "bold"),
                bg="#2c3e50",
                fg="#ecf0f1",
                pady=20,
            )
        self.titulo.pack(fill="x")


        # Contenedor principal
        self.container = tk.Frame(root, bg="#ecf0f1")
        self.container.pack(expand=True, fill="both")


        # Terminal
        self.terminal = tk.Text(
            self.container,
            font=("Courier", 12),
            bg="#2d3436",
            fg="white",
            height=8,
            width=100,
            wrap="word",
            state="normal",
            bd=0,
            padx=10,
            pady=10,
        )
        self.terminal.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # Entrada de comando
        self.entrada_comando = tk.Entry(
            self.container,
            font=("Roboto", 14),
            bg="#fff",
            width=60,
            justify="center",
            bd=0,
            relief="flat",
            highlightthickness=2,
            highlightbackground="#bdc3c7",
            highlightcolor="#3498db",
        )
        self.entrada_comando.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
        self.entrada_comando.bind("<Return>", self.enviar_comando)

        # Botones principales
        self.boton_limpiar = tk.Button(
            self.container,
            text="Limpiar",
            font=("Roboto", 12),
            bg="#e74c3c",
            fg="white",
            command=self.limpiar_terminal,
            width=20,
            relief="flat",
            bd=3,
            padx=10,
            pady=5,
        )
        self.boton_limpiar.grid(row=2, column=0, padx=20, pady=10)

        self.boton = tk.Button(
            self.container,
            text="Ejecutar",
            font=("Roboto", 12, "bold"),
            bg="#3498db",
            fg="white",
            width=20,
            relief="flat",
            bd=5,
            padx=10,
            pady=5,
            command=self.enviar_comando,
        )
        self.boton.grid(row=2, column=2, padx=20, pady=10)

        # Recuadro informativo
        self.recuadro_info = tk.LabelFrame(
            self.container,
            text="Teoría y Funciones Disponibles",
            font=self.title_font,
            fg="black",
            bg="#16a085",
            width=950,
            height=400,
            padx=10,
            pady=10,
            bd=5,
            relief="solid",
        )
        self.recuadro_info.grid(row=3, column=0, columnspan=3, padx=20, pady=20)

        # Información detallada
        self.info_text = tk.Text(
            self.recuadro_info,
            font=("Roboto", 10),
            height=8,
            width=130,
            wrap="word",
            bg="#ecf0f1",
            fg="black",
            state="normal",
            bd=0,
        )
        self.info_text.insert(
            tk.END,
            "-Teoría de Derivadas Numéricas-\n"
            "La derivada numérica aproxima la pendiente de una función en un punto específico. Método: diferencias centradas.\n\n"
            "-Teoría de Integrales Numéricas-\n"
            "La integración numérica aproxima el área bajo la curva de una función. Método: trapezoide.\n\n"
            "-Funciones Matemáticas Disponibles-\n"
            "1. Seno (sin)\n"
            "2. Coseno (cos)\n"
            "3. Exponencial (exp)\n"
            "4. Logaritmo Natural (log)\n"
            "5. Raíz Cuadrada (sqrt)\n"
            "6. Tangente (tan)\n"
            "7. Arcotangente (atan)\n"
            "8. Seno Hiperbólico (sinh)\n"
            "9. Logaritmo Personalizado (log_base)\n\n"
            "-Uso de la Calculadora-\n"
            "1. Derivada: derivada(función, punto)\n"
            "2. Integral: integral(a, b, función, n)\n"
            "3. Operaciones básicas: suma (+), resta (-), multiplicación (*), división (/).\n\n",
        )
        self.info_text.config(state=tk.DISABLED)
        self.info_text.grid(row=0, column=0, columnspan=5)

        # Recuadro de botones de funciones matemáticas
        self.funciones_container = tk.Frame(self.container, bg="#ecf0f1")
        self.funciones_container.grid(row=0, column=4, rowspan=4, padx=20, pady=20, sticky="n")

        funciones = [
            ("Seno", "sin(x)"),
            ("Coseno", "cos(x)"),
            ("Tangente", "tan(x)"),
            ("Exponencial", "exp(x)"),
            ("Logaritmo", "log(x)"),
            ("Raíz Cuadrada", "sqrt(x)"),
            ("Arcotangente", "atan(x)"),
            ("Seno Hiperbólico", "sinh(x)"),
            ("Log Base", "log_base(b, x)"),
            ("Derivada", "derivada(funcion, x)"),
            ("Integral", "integral(a, b, funcion, n)"),
        ]

        for i, (nombre, comando) in enumerate(funciones):
            boton = tk.Button(
                self.funciones_container,
                text=nombre,
                font=("Roboto", 12),
                bg="#16a085",
                fg="white",
                width=20,
                relief="flat",
                command=lambda c=comando: self.insertar_comando(c),
            )
            boton.grid(row=i, column=0, pady=5, padx=5)

    def insertar_comando(self, comando):
        self.entrada_comando.delete(0, tk.END)
        self.entrada_comando.insert(0, comando)

    def enviar_comando(self, event=None):
        comando = self.entrada_comando.get()
        self.mostrar_comando(comando)
        try:
            resultado = self.evaluar_expresion_flex_bison(comando)
            self.mostrar_resultado(resultado)
        except Exception as e:
            self.mostrar_resultado(f"Error: {str(e)}")
        self.entrada_comando.delete(0, tk.END)

    def mostrar_comando(self, comando):
        self.terminal.insert(tk.END, f"> {comando}\n")
        self.terminal.yview(tk.END)

    def mostrar_resultado(self, resultado):
        self.terminal.insert(tk.END, f"{resultado}\n")
        self.terminal.yview(tk.END)

    def limpiar_terminal(self):
        self.terminal.delete(1.0, tk.END)

    def evaluar_expresion_flex_bison(self, expresion):
        try:
            entrada = expresion.strip() + "\n"
            proceso = subprocess.run(
                ["./calculadora.exe"], input=entrada, text=True, capture_output=True, check=True
            )
            resultado = proceso.stdout.strip()
            if "syntax error" in resultado.lower():
                raise Exception("Error de sintaxis detectado.")
            return resultado
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error en el cálculo: {e.stderr.strip()}")
        except Exception as e:
            raise Exception(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
