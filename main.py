# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main


import tensorflow as tf
import tensorflow_datasets as tfds


# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)