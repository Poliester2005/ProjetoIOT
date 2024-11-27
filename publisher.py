import tkinter as tk
from tkinter import colorchooser
import paho.mqtt.client as mqtt

BROKER = "3.91.141.102"
PORT = 1883
TOPIC = "lampada"

def publish_color(color_hex):
    client.publish(TOPIC, color_hex)
    print(f"Enviado: {color_hex}")

def choose_color():
    color_code = colorchooser.askcolor(title="Escolha uma cor")[1]
    if color_code:
        canvas.config(bg=color_code)
        publish_color(color_code)

client = mqtt.Client()

def connect_to_broker():
    try:
        client.connect(BROKER, PORT, 60)
        client.loop_start()
        print(f"Conectado ao broker MQTT: {BROKER}:{PORT}")
    except Exception as e:
        print(f"Erro ao conectar ao broker: {e}")

root = tk.Tk()
root.title("Controlador de Cores MQTT")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

choose_color_btn = tk.Button(frame, text="Escolher Cor", command=choose_color)
choose_color_btn.pack(pady=10)

canvas = tk.Canvas(frame, width=100, height=100, bg="white", highlightthickness=1, highlightbackground="black")
canvas.pack(pady=10)

connect_to_broker()

root.mainloop()

client.loop_stop()
client.disconnect()
