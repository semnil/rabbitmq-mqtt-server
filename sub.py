# coding=utf8

import paho.mqtt.client as paho
import sys

topic = "$SYS/#"

def on_connect(mqttc, obj, rc):
    # mqttc.subscribe(topic, 0)
    print("subscribe " + topic + " rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

if __name__ == '__main__':
    mqttc = paho.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe

    mqttc.username_pw_set("/subscriber:subscriber", "subscriber_pass")

    if len(sys.argv) > 1:
        topic = "topic/string/" + sys.argv[1]
    else:
        topic = "topic/string/#"

    mqttc.connect("192.168.33.12", 1883, 60)

    mqttc.subscribe(topic, 0)

    mqttc.loop_forever()
