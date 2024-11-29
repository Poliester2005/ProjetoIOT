import turtle
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

def update_bgcolor(hex_code):
    try:
        screen.bgcolor(hex_code)
        print(f"Cor de fundo atualizada para: {hex_code}")
    except turtle.TurtleScreen._root.TclError:
        print(f"Erro: Código hexadecimal inválido recebido: {hex_code}")

def on_message(client, userdata, message):
    color = message.payload.decode()
    update_bgcolor(color)

def create_mqtt_client():
    client = mqtt.Client()
    return client

def main():
    global screen

    screen = turtle.Screen()
    t = turtle.Turtle()

    load_dotenv()


    mqtt_broker = os.getenv("BROKER")
    mqtt_port = int(os.getenv("PORT"))
    mqtt_topic = os.getenv("TOPIC")


    client = mqtt.Client()
    client.on_message = on_message
    client.connect(mqtt_broker, mqtt_port, 20000)
    client.subscribe(mqtt_topic)
    print(f"Inscrito no tópico '{mqtt_topic}' para receber cores de fundo...")
    client.loop_forever()

    turtle.done()

if __name__ == "__main__":
    main()
