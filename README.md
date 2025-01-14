
# Discord-Server-Leaver

A Python script that allows you to leave Discord servers where the bot is not the owner or leave a specific server by ID.

## Features

- **Leave All Non-Owned Servers**: Automatically leave all servers where the bot is not the owner.
- **Leave Specific Server**: Leave a specific server by providing its ID.
- **Rate Limit Handling**: Advanced handling of rate limits to avoid hitting Discord's API limits.
- **Interactive Menu**: User-friendly console menu for easy navigation and execution of commands.
- **Colorful Output**: Enhanced console output with colors for better readability.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/potatobyme/Discord-Server-Leaver.git
    ```
2. Go To The Directory
   ```bash
   cd Discord-Server-Leaver
   ```
   

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

   ```

## Usage

1. Run the script:
   ```bash
   python Leaver.py
   ```

2. Follow the on-screen instructions:
   - Enter your Discord account token when prompted.
   - Choose an option from the menu:
     1. Leave all servers where the bot is not the owner.
     2. Leave a specific server by ID.
     3. Exit the script.

### Options Explained

- **Leave All Servers**: This option will make the bot leave all servers where it is not the owner. It handles rate limits by waiting the required amount of time before retrying.
- **Leave a Specific Server**: This option allows you to leave a specific server by providing its ID. The bot checks if it is not the owner before attempting to leave.

## Example

When you run the script, it will look something like this:

```plaintext
  _____                                  _                                 
 / ____|                                | |                                
| (___    ___  _ __ __   __  ___  _ __  | |  ___   __ _ __   __  ___  _ __ 
 \___ \  / _ \| '__|\ \ / / / _ \| '__| | | / _ \ / _` |\ \ / / / _ \| '__|
 ____) ||  __/| |    \ V / |  __/| |    | ||  __/| (_| | \ V / |  __/| |   
|_____/  \___||_|     \_/   \___||_|    |_| \___| \__,_|  \_/   \___||_|   
                                                                           
                                                                           made by Potato

[INFO] Logged in as: YourName#1234

FAAR Server Leaver
===================
1. Leave all servers where the bot is not the owner
2. Leave a specific server by ID
3. Exit
===================
Enter your choice (1, 2, or 3):
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

Made by FAAR
