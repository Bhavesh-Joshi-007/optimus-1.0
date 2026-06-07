from openwakeword.model import Model
import sounddevice as sd
import numpy as np
import time
from engine import state

from engine.command import takeCommand
from engine.command import allCommands
from engine.command import speak


model = Model(
    inference_framework="onnx"
)

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280


def startWakeWordDetection():
    print("\nOPTIMUS Wake Word Engine Started...\n")
    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype=np.int16,
        blocksize=CHUNK_SIZE
    )

    stream.start()



    while True:
        if not state.WAKEWORD_ACTIVE:

            time.sleep(0.2)

            continue
        try:
            audio, overflowed = stream.read(
                CHUNK_SIZE
            )
            prediction = model.predict(
                audio.flatten()
            )
            print(
    prediction["hey_jarvis"]
)
            score = prediction.get(
                "hey_jarvis",
                0
            )
            if score > 0.5:
                print(
                    "Wake Word Detected!"
                )
                speak(
                    "Yes Sir"
                )
                query = takeCommand()
                if query:
                    print(
                        "COMMAND:",
                        query
                    )
                    allCommands(query)
                time.sleep(2)
        except Exception as e:
            print(
                "Wake Word Error:",
                e
            )