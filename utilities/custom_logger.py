import logging


class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\logs\\mylog.log', mode='a')
        formatter = logging.Formatter(
            '%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
