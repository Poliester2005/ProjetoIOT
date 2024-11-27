import turtle
import paho.mqtt.client as mqtt

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

    mqtt_broker = "3.91.141.102"
    mqtt_port = 1883
    mqtt_topic = "lampada"

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(mqtt_broker, mqtt_port, 20000)
    client.subscribe(mqtt_topic)
    print(f"Inscrito no tópico '{mqtt_topic}' para receber cores de fundo...")
    client.loop_forever()

    turtle.done()

if __name__ == "__main__":
    main()
