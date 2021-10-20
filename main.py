# Importere library til at forbinde til adafruit.io
import umqtt_robust2
from machine import Pin
import dht
from time import sleep_ms, sleep
lib = umqtt_robust2
sensor = dht.DHT11(Pin(14))

while True:
    sleep_ms(500)
    besked = lib.besked
    # haandtere fejl i forbindelsen og hvor ofte den skal forbinde igen
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            # hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
            lib.c.reconnect()
        else:
            lib.c.resubscribe()
    try:
        # Det er primært herinde at i skal tilfoeje kode
        if besked == "fortæl en joke jarvis":
            print("modtaget")
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="""Hvorfor bliver zooligsk have aldrig solgt? fordi den er for dyr :D""")
            lib.besked = ""
        if besked == "hvad er temperaturen jarvis?":
            sensor.measure()
            temp = sensor.temperature()
            print(temp)
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="temperaturen er "+str(temp)+" C")
            lib.besked = ""
        if besked == "hvad er fugtigheden jarvis?":
            print ("modtaget")
            sensor.measure()
            hum = sensor.humidity()
            print(hum)
            lib.c.publish(topic=lib.mqtt_pub_feedname, msg="fugtigheden er "+str(hum)+" %")
            lib.besked = ""

    except OSError as e:
        print("Failed to read sensor.")
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    lib.c.check_msg() # needed when publish(qos=1), ping(), subscribe()
    lib.c.send_queue()  # needed when using the caching capabilities for unsent messages
lib.c.disconnect()



