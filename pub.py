# coding=utf8

import paho.mqtt.client as paho

def on_connect(mqttc, obj, rc):
    mqttc.subscribe("$SYS/#", 0)
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_log(mqttc, obj, level, string):
    print(string)

if __name__ == '__main__':
    mqttc = paho.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish

    mqttc.connect("192.168.33.11", 1883, 60)

    mqttc.publish("my/topic/string", "hello world", 1)
