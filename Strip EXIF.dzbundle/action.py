# Dropzone Action Info
# Name: Strip EXIF
# Description: Removes all EXIF data from an image for more privacy. Requires exiftool to be installed in the default location.
# Handles: Files
# Creator: Ralph Schaefermeier
# URL: ralph.schaefermeier.net
# Events: Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.5

import time
import subprocess

def dragged():
    dz.begin("Stripping EXIF data...")

    dz.determinate(True)
    dz.percent(0)
    percentStep = 100 / len(items)
    currentPercent = 0

    for item in items:
        subprocess.call(["/usr/local/bin/exiftool", "-all=", item])
        currentPercent += percentStep
        dz.percent(currentPercent)

    dz.percent(100)

    dz.finish("Your images are EXIF free.")
    dz.url(False)

def clicked():
    dz.url(False)
