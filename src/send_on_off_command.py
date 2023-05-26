import json
from wakeonlan import send_magic_packet
from mqtt_client import PowerOn


class SendOnOff(PowerOn):
    def __init__(self, *args, **kwargs):
        super(SendOnOff, self).__init__(*args, **kwargs)

    def on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        var_name = "devices"
        if msg.topic == self.wake_topic:
            message = json.loads(msg.payload)
            if message[var_name] == "all":
                self.wake_up_all_devices()
            elif type(message[var_name]) == str:
                self.wake_up_device(message[var_name])
            elif type(message[var_name]) == list and len(message[var_name]) > 0:
                for device in message[var_name]:
                    self.wake_up_device(device)

    def wake_up_all_devices(self):
        send_magic_packet(
            *[device["mac"] for device in self.devices], interface=self.interface
        )
        print("sent for all devices")

    def wake_up_device(self, deviceName: list):
        device = next((dev for dev in self.devices if dev["name"] == deviceName), False)
        if device:
            send_magic_packet(device["mac"], interface=self.interface)
            print(f'sent for {device["name"]} device')
