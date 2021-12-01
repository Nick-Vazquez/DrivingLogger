import logging
import logging.config
import pathlib

if 'logs' not in [path.name for path in pathlib.Path.cwd().iterdir()]:
    pathlib.Path.mkdir(pathlib.Path.cwd().joinpath('logs'))

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')

