import os
from pathlib import Path
import logging


ROOT = Path(Path.cwd())

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DOWNLOAD = Path(Path.cwd, 'Download')
