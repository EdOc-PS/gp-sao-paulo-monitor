
import json
import os
import random
from datetime import datetime
import time
import paho.mqtt.client as mqtt

broker = "mqtt"
port = 1883
id = os.getenv("CAR_ID")

client = mqtt.Client()
client.connect(broker, port, 60)
client.loop_start()

def gen_tire_data(compound="Macio"):
    return {
        "temperature": round(random.uniform(95, 105), 1),
        "pressure": round(random.uniform(18.5, 19.8), 1),
        "compound": compound,
        "wear": random.randint(40, 70)
    }

def gen_car(car_id=id, lap=1):
    tire_data = {
        "frontLeft": gen_tire_data(),
        "frontRight": gen_tire_data(),
        "rearLeft": gen_tire_data(),
        "rearRight": gen_tire_data(),
    }

    return {
        "carId": car_id,
        "lapNumber": lap,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "speed": round(random.uniform(200, 230), 1),
        "tireData": tire_data
    }

def send_to_isccp():
    isccp_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"]

    for isccp in isccp_list:
        car_data = gen_car() 
        car_data["sector"] = isccp 
        topic = f"/isccp/{isccp}/tires"
        payload = json.dumps(car_data)

        client.publish(topic, payload)
        print(f"[CAR] → Enviado para tópico {topic}")

def main(): 
    for lap in range(1, 72):
        print(f"\n=== CARRO {id} — Lap {lap}/71 ===")
        car_data = gen_car(id, lap)
        send_to_isccp(car_data)

        time.sleep(1)

    print(f"\n✅ Carro {id} finalizou 71 voltas")
    client.disconnect()

if __name__ == "__main__":
    main()
  
