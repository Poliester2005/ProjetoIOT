# Projeto: Simulação de Lâmpada RGB Usando Broker MQTT

Este projeto é uma interface gráfica em Python que permite ao usuário selecionar cores e enviá-las para um broker MQTT. As cores são enviadas no formato hexadecimal para um tópico configurado. O projeto inclui também um script que simula uma lâmpada RGB, exibindo a cor recebida do broker.

---

## **Requisitos**

- Python 3.7 ou superior
- Broker MQTT configurado
- Bibliotecas Python:
  - `paho-mqtt`
  - `tkinter` (inclusa na maioria das instalações do Python)
  - `dotenv`

---

## **Como funciona**

1. O script `color_picker.py` permite que o usuário escolha uma cor através de uma interface gráfica.
2. A cor escolhida é publicada em um tópico MQTT.
3. O script `subscriber.py` simula uma lâmpada RGB que assina o tópico MQTT e exibe as cores recebidas.

---

## **Requisitos**

- Python 3.7 ou superior
- Broker MQTT configurado (Nesse caso, via Amazon Web Services EC2)
- Bibliotecas Python:
  - `paho-mqtt`
  - `tkinter` (inclusa na maioria das instalações do Python)
  - `dotenv`

---

## **Instalação**

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/mqtt-color-picker.git
   cd mqtt-color-picker
   ```


2. Crie um arquivo `.env` com as configurações do broker MQTT:
   ```
   BROKER=<endereço_do_broker>
   PORT=<porta_do_broker>
   TOPIC=<tópico_mqtt>
   ```
3. Faça a instação das bibliotecas necessárias:
   ```
   pip install paho-mqtt
   pip install dotenv
   ```

---

## **Uso**


### **1. Exemplo de `.env` para configuração da conexão do Broker**

```env
BROKER=mqtt.eclipseprojects.io
PORT=1883
TOPIC=lamp/color
```
### **2. Publicador: `publisher.py`**
1. Execute o script:
   ```bash
   python publishr.py
   ```

2. Na interface gráfica:
   - Clique no botão **"Escolher Cor"**.
   - Escolha uma cor no seletor.
   - A cor será exibida na interface e enviada ao broker MQTT.

### **3. Assinante: `subscriber.py`**
1. Em outro terminal, execute o script:
   ```bash
   python subscriber.py
   ```

2. O console exibirá a mensagem recebida com o código da cor, e uma janela gráfica simulará a lâmpada exibindo a cor recebida.


---

## **Contribuição**

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias para o projeto!

---

## Relatório
O relatório de toda a realização dessa atividade se encontra no arquivo `relatorio.md`.

---

## Nossa Equipe

Apresentamos nossa equipe, na qual contribuiu para esta atividade:

<table>
  <tr>
  <td align="center">
      <a href="https://github.com/brunocmartins11" title="Bruno Martins">
        <img src="https://avatars.githubusercontent.com/u/101012137?v=4" width="100px;" alt="Foto de Bruno Martins"/><br>
        <sub>
          <b>Bruno Martins</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Poliester2005" title="Eduardo Pielich">
        <img src="https://avatars.githubusercontent.com/u/107966984?v=4" width="100px;" alt="Foto de Eduardo Pielich"/><br>
        <sub>
          <b>Eduardo Pielich</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/RenatoAC2004" title="Renato Carvalho">
        <img src="https://avatars.githubusercontent.com/u/108144847?v=4" width="100px;" alt="Foto de Renato Carvalho"/><br>
        <sub>
          <b>Renato Carvalho</b>
        </sub>
