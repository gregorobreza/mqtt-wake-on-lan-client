import time
import yaml
import os

from send_on_off_command import SendOnOff


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    config_path = os.path.join(parent_dir, 'config.yaml')
    with open(config_path, mode="rt", encoding="utf-8") as file:
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
        config["subscribe_topic"],
        config["wake_topic"],
        config["command_topic"],
        config["mqtt_user"],
        config["mqtt_password"],
    )
    bla = neki.run()
    # while True:
    #     print("bla")
    #     time.sleep(2)

if __name__ == "__main__":
    main()
