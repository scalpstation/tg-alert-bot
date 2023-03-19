from parser.station_parser import StationParser
from receiver.telegram_receiver import TelegramReceiver
from router.default_roter import Router
from sender.default_sender import DefaultSender

Router(TelegramReceiver(), StationParser(), DefaultSender()).run()

