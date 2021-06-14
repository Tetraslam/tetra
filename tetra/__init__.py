from typing import final
from questionary import question
from rich.console import Console
from rich.text import Text
from rich.progress import Progress
import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import mixer
from time import sleep
import questionary
from cryptography.fernet import Fernet
from questionary import Style
