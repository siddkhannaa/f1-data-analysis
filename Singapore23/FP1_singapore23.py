import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd

ff1.plotting.setup_mpl(misc_mpl_mods=False)

# get session
session = ff1.get_session(2023, 15, 'FP1')
session.load()

print(session.event)