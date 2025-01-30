import tkinter as tk
import random
import time
from tkinter import font

class AdivinaNumeroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Número")
        self.root.configure(bg="#121212")  # Fondo oscuro moderno
        self.numero_secreto = random.randint(0, 100)
        self.intentos = 3
        self.bloqueado = False
        self.ultimo_fallo = None
        
        self.pixel_font = font.Font(family="Consolas", size=14, weight="bold")
        
        self.label = tk.Label(root, text="Adivina un número entre 0 y 100", fg="#00ffcc", bg="#121212", font=self.pixel_font)
        self.label.pack(pady=10)
        
        self.hint_label = tk.Label(root, text=self.generar_pista(), fg="#00ffcc", bg="#121212", font=self.pixel_font)
        self.hint_label.pack(pady=5)
        
        self.entry = tk.Entry(root, font=self.pixel_font, fg="#ffffff", bg="#1e1e1e", insertbackground="#00ffcc", relief=tk.FLAT, justify="center")
        self.entry.pack(pady=5, ipadx=5, ipady=5)
        
        self.button = tk.Button(root, text="Intentar", command=self.verificar_numero, font=self.pixel_font, fg="#121212", bg="#00ffcc", activebackground="#00ffaa", relief=tk.FLAT, cursor="hand2")
        self.button.pack(pady=5, ipadx=5, ipady=5)
        
        self.result_label = tk.Label(root, text="", fg="#ff4444", bg="#121212", font=self.pixel_font)
        self.result_label.pack(pady=5)
        
        self.restart_button = tk.Button(root, text="Reiniciar", command=self.reiniciar_juego, font=self.pixel_font, fg="#121212", bg="#ffcc00", activebackground="#ffaa00", relief=tk.FLAT, cursor="hand2")
        self.restart_button.pack(pady=10, ipadx=5, ipady=5)
    
    def generar_pista(self):
        return "Pista: El número es mayor a 50" if self.numero_secreto > 50 else "Pista: El número es menor o igual a 50"
    
    def verificar_numero(self):
        if self.bloqueado:
            if time.time() - self.ultimo_fallo < 180:
                self.result_label.config(text="Debes esperar 3 minutos antes de intentarlo de nuevo.")
                return
            else:
                self.bloqueado = False
                self.intentos = 3
                
        try:
            intento = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Por favor, ingresa un número válido.")
            return
        
        if intento == self.numero_secreto:
            self.result_label.config(text="¡Felicidades, lograste adivinar el número!", fg="#00ffaa")
            self.button.config(state=tk.DISABLED)
        else:
            self.intentos -= 1
            if self.intentos == 0:
                self.result_label.config(text="Fallaste. Debes esperar 3 minutos.")
                self.ultimo_fallo = time.time()
                self.bloqueado = True
            else:
                self.result_label.config(text=f"Fallaste, intenta de nuevo. Intentos restantes: {self.intentos}")
    
    def reiniciar_juego(self):
        self.numero_secreto = random.randint(0, 100)
        self.intentos = 3
        self.bloqueado = False
        self.result_label.config(text="")
        self.hint_label.config(text=self.generar_pista())
        self.button.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)

root = tk.Tk()
app = AdivinaNumeroApp(root)
root.mainloop()