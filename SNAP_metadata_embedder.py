# Author: Ramine Tinati - raminetinati@gmail.com
# Purpose: To embed Web Observatory metadata into SNAP
import glob
import os
import time
import sys
import json
from lxml import html
import requests
from datetime import datetime