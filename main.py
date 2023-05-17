import time
import yaml

from src.send_on_off_command import SendOnOff


def main():
    with open("config.yaml", mode="rt", encoding="utf-8") as file:
        # print(yaml.safe_load(file))
        config = yaml.safe_load(file)
    print(config)
    neki = SendOnOff(
        config["devices"],
        config["lan_interface"],
        config["mqtt_broker_url"],
        config["port"],
        config["mqtt_user"],
        config["mqtt_password"],
        config["topic"],
        config["mqtt_user"],
        config["mqtt_password"],
    )
    # neki = PowerOn()
    bla = neki.run()


if __name__ == "__main__":
    main()
