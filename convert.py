import os
from datetime import datetime

print datetime.fromtimestamp(float(os.environ['POPCLIP_TEXT'][:10]))
