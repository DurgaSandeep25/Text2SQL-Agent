import os
import logging
import datetime
from from_root import from_root

root_dir = from_root()
logfile_name = f"{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}"

logfile_path = os.path.join(root_dir, 'logs', logfile_name)
os.makedirs(name=logfile_path, exist_ok=True)

logging.basicConfig(
    filename=logfile_path,
    format="%(asctime)s - %(name)s -%(levelname)s - %(message)s",
    level=logging.DEBUG
)
