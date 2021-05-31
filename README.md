# Chia HPool Checker
Simple script to compare your local Chia plots to HPool and send a notification to you Telegram chat via bot

![The view of the message](https://i.imgur.com/BD22yMP.png "View")

## Installation

The installation of this library is straightforward.

#### NOTE: If `python` does not work, please try `python3`.

1. Download and Install Python 3.7 or higher: https://www.python.org/
2. `git clone` this repo or download it.
3. Open CommandPrompt / PowerShell / Terminal and `cd` into the main library folder.
   * Example: `cd C:\Chia\chia-hpool-checker`
4. OPTIONAL: Create a virtual environment for Python. This is recommended if you use Python for other things.
	1. Create a new python environment: `python -m venv venv`
	   * The second `venv` can be renamed to whatever you want. I prefer `venv` because it's a standard.
	2. Activate the virtual environment. This must be done *every single time* you open a new window.
	   * Example Windows: `venv\Scripts\activate`
	   * Example Linux: `. ./venv/bin/activate` or `source ./venv/bin/activate`
	3. Confirm that it has activated by seeing the `(venv)` prefix. The prefix will change depending on what you named it.
5. Install the required modules: `pip install -r requirements.txt`
6. Copy `config.yaml.default` and name it as `config.yaml` in the same directory.
7. Edit and set up the config.yaml to your own personal settings. There is more help on this below.
	* You will need to add the `hpool_path` as well! This should point to your hpool miner executable.
9. Close the CommandPrompt and run the checker script: check.bat
   * This will start a process that will count your plots on a disks and send a notification to your Telegram chat every 60 minutes.
10. (OPTIONAL): You can add a shortcut to the check.bat to a startup

## Configuration

The configuration of this library is unique to every end-user. The `config.yaml` file is where the configuration will live. 

### telegram_token_id and telegram_chat_id

This is a variables that should contain the telegram bot id

* Example: `123124124:kfhklashdfklhaskldhklsad`

### hpool_path

This is a single variable that should contain the location of your HPool Miner folder.

* Example: `C:\Chia\HPool-Miner-chia\`

### hpool_miner_log

This is a single variable that should contain the location of your HPool Miner log file.

* Example: `C:\Chia\HPool-Miner-chia\log\miner.log.log`

## Telegram bot Set-up:

 1. Open Telegram and search "BotFather" in the search bar. This is the official bot that allows you to create other bots.  
 2. Create new bot: `/newbot`
 3. Choose a name for your bot: `ScriptNotifier`
 4. Choose a username for your bot that must end with "_bot": `script_notifier_bot`  
 5. Once the bot is created, you will have a long string: this is the TOKEN-ID
 6. The bot will send you messages on a specific chat that you need to create. Go to Telegram search bar, on your smartphone, and search your bot (e.g. ScriptNotifier). Then, start the bot: `/start` 
 7. Finally, search for your CHAT-ID by going to the bot webpage: https://api.telegram.org/bot[TOKEN-ID]/getUpdates
