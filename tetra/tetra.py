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

class tetra:
    def csprint(printtext, speed=0):
        """Print with styling! For example, use `csprint("[bright_cyan][i]hello there", 0.05)` and see the output!"""
        if speed==0:
            text = Text.from_markup(printtext)
            console = Console()
            for c in text:
                console.print(c)
                sleep(0.04)
        else:
            text = Text.from_markup(printtext)
            console = Console()
            for c in text:
                console.print(c)
                sleep(speed)
    def z(optional_time="2"):
        """Make the program sleep for 2 seconds, or specify a time to make it sleep for."""
        sleep(optional_time)
    def asktext(text):
      """Ask the user for an input of plain text."""
      answer=questionary.text(text).ask()
      return answer
    def askpassword(text):
      """Ask the user to enter a password."""
      answer=questionary.password(text).ask()
      return answer
    def askfilepath(text):
      """Ask the user to enter a filepath with autoprompting."""
      answer=questionary.path(text).ask()
      return answer
    def askconfirmation(text):
      """Asks the user for confirmation with the only possible answers being yes or no."""
      answer=questionary.confirm(text).ask()
      return answer
    def askoneoption(text, listofoptions, usepointer=False):
      """Asks the user to choose one option out of many."""
      if usepointer==True:
        answer=questionary.select(
          text,
          choices=listofoptions,
          use_pointer=True
        ).ask()
        return answer
      else:

        answer=questionary.select(
          text,
          choices=listofoptions
        ).ask()
        return answer
    def askcheckbox(text, listofoptions, usepointer):
      """Asks the user to select one or more options."""
      if usepointer==True:
        answer=questionary.checkbox(
          text,
          choices=listofoptions
          ,
          use_pointer=True
        ).ask()
        return answer
      else:
        answer=questionary.checkbox(
          text,
          choices=listofoptions,
          use_pointer=False
        ).ask()
        return answer
    def askautocomplete(text, listofoptions):
      """Asks the user to enter an answer, but with autocompletion for answers."""
      answer=questionary.autocomplete(
        text,
        choices=listofoptions,
        ignore_case=True
      ).ask()
      return answer
    def raiseError(error, message):
      """Raise any error you want."""
      raise error(message)

    


