# Python Daily Event Bot
This repository contains a Python bot that parses through all the events that happened on a given day and selects the most important one. The bot generates a short essay on the selected event and automatically posts it to your Telegram channel.

## Features
- Automatic parsing of daily events
- Selection of the most important event of the day
- Generation of a short essay on the event
- Automatic posting of the essay to your Telegram channel

## Getting Started

### Prerequisites
- Python 3
- Python libraries: requests, beautifulsoup4, datetime

### Installation
1. Clone this repository to your local machine.
2. Install the necessary libraries listed above using pip or another package manager.
3. Set up a Telegram bot and obtain an API key.
4. Configure telegram-send to use your Telegram API key.
5. Run the main.py script.

## Usage
The bot will automatically run every day and select an important event to write about. The generated essay will be posted to your Telegram channel. You can customize the bot to select events from specific news sources or topics by modifying the code.

## Contributing
Contributions to this repository are welcome! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.