from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time

client = AWSIoTMQTTClient("SmartLampClient")
client.configureEndpoint("ayuovu9l1arx0-ats.iot.eu-north-1.amazonaws.com", 8883)
client.configureCredentials("AmazonRootCA1.pem", "2fc4c5a335ae3fc0d8f6c2aa8e50b27429123a920104e0e82c16fec8bebf7713-private.pem.key", "2fc4c5a335ae3fc0d8f6c2aa8e50b27429123a920104e0e82c16fec8bebf7713-certificate.pem.crt")
client.connect()

topic = "smartLamp001/topic"

for i in range(3):
    # payload = {
    #         "device_id": "SmartLamp_001",
    #         "light_level": 320,
    #         "motion": True
    # }

    import random
    payload = {
        "device_id": "SmartLamp_001",
        "light_level": random.randint(0, 100),  # 0-100 arasında rasgele sayı
        "motion": random.choice([True, False])  # True veya False rastgele
    }
    client.publish(topic, json.dumps(payload), 1)
    print(f"Published: {payload}")
    time.sleep(5)



# import random
# import time
# import json
# from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# ENDPOINT = "ayuovu9l1arx0-ats.iot.eu-north-1.amazonaws.com"
# CLIENT_ID = "virtual_device_1"
# TOPIC = "smartLamp001/topic"

# mqtt_client = AWSIoTMQTTClient(CLIENT_ID)
# mqtt_client.configureEndpoint(ENDPOINT, 8883)
# mqtt_client.configureCredentials("2fc4c5a335ae3fc0d8f6c2aa8e50b27429123a920104e0e82c16fec8bebf7713-public.pem", "2fc4c5a335ae3fc0d8f6c2aa8e50b27429123a920104e0e82c16fec8bebf7713-private.pem", "2fc4c5a335ae3fc0d8f6c2aa8e50b27429123a920104e0e82c16fec8bebf7713-certificate.pem")
# mqtt_client.connect()

# while True:
#     payload = {
#         "device_id": CLIENT_ID,
#         "motion": random.choice([True, False]),
#         "light": random.randint(0, 100),
#         "timestamp": int(time.time())
#     }
    
#     mqtt_client.publish(TOPIC, json.dumps(payload), 1)
#     print(f"Gönderilen Veri: {payload}")
#     time.sleep(5)