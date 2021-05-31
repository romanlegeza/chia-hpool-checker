import os, os.path
import logging
import socket
import yaml
import telegram_notifier

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f'{round(size, 2)} {power_labels[n]}B'

file_count = 0
file_sizes = 0

config_file = open("config.yaml")
config = yaml.load(config_file, Loader=yaml.FullLoader)

hpool_config = yaml.load(open(config["hpool_path"]+"config.yaml"), Loader=yaml.FullLoader)

for DIR in hpool_config["path"]:
    file_sizes += sum([os.path.getsize(os.path.join(DIR, f)) for f in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, f)) and f.endswith('.plot')])
    file_count += len([f for f in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, f)) and f.endswith('.plot')])


for line in reversed(list(open(config["hpool_miner_log"]))):
    lline = line.rstrip()
    if lline.find("new mining info"):
        hpool_capacity = lline.partition('capacity=')[1] + lline.partition('capacity=')[2].partition('file=')[0]
        break

message = f"Plots on disks: {file_count} files ({format_bytes(file_sizes)}). HPool {hpool_capacity}"

# Telegram notification:
msg = "<b>{hostname}: </b>\n<pre> {text} </pre>".format(separator=' -' * 10, text=message, hostname=socket.gethostname())
print(msg)
telegram_notifier.basic_notifier(logger_name='training_notifier',
                                 token_id=config["telegram_token_id"],
                                 chat_id=config["telegram_chat_id"],
                                 message=msg,
                                 level=logging.INFO)
