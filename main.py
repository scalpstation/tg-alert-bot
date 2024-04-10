from parser.station_parser import StationParser
from receiver.telegram_receiver import TelegramReceiver
from router.default_roter import Router
from sender.default_sender import DefaultSender
from conf import read_config


if __name__ == '__main__':

    config = read_config()

    Router(TelegramReceiver(config['telegram']), StationParser(config['parser']), DefaultSender(config['sender'])).run()

