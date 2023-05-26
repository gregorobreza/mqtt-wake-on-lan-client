import paho.mqtt.client as mqtt


class PowerOn(mqtt.Client):
    def __init__(
        self,
        devices: list[dict],
        interface: str,
        mqtt_broker_url: str,
        port: int,
        mqtt_user: str,
        mqtt_password: str,
        subscribe_topic: str,
        wake_topic: str,
        command_topic: str,
        username: str,
        password: str,
        *args,
        **kwargs
    ):
        super(PowerOn, self).__init__(*args, **kwargs)
        self.devices = devices
        self.interface = interface
        self.mqtt_broker_url = mqtt_broker_url
        self.port = port
        self.mqtt_user = mqtt_user
        self.mqtt_password = mqtt_password
        self.subscribe_topic = subscribe_topic
        self.wake_topic = wake_topic
        self.command_topic = command_topic
        self._username = username
        self._password = password

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: " + str(rc))

    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")

    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        # self.connect("mqtt.eclipseprojects.io", 1883, 60)
        self.connect(self.mqtt_broker_url, self.port, 60)
        # self.subscribe("$SYS/#", 0)
        self.subscribe(self.subscribe_topic, 0)
        self.loop_forever()
