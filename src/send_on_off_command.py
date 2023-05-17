from wakeonlan import send_magic_packet
from mqtt_client import PowerOn


class SendOnOff(PowerOn):
    def __init__(self, *args, **kwargs):
        super(SendOnOff, self).__init__(*args, **kwargs)

    def on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        self.wake_up_device("main")

    def wake_up_all_devices(self):
        send_magic_packet(
            *[device["mac"] for device in self.devices], interface=self.interface
        )
        print("sent for all devices")

    def wake_up_device(self, deviceName):
        device = next((dev for dev in self.devices if dev["name"] == deviceName), False)
        if device:
            send_magic_packet(device["mac"], interface=self.interface)
            print(f'sent for {device["name"]} device')
