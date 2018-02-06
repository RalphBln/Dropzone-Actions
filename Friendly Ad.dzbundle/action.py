# Dropzone Action Info
# Name: Friendly Ad
# Description: Adds the dragged email's sender to the "Friendly Ads" mail rule.
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
import re
import sys
import subprocess

def dragged():
    dz.begin("Creating filter rule conditions...")

    dz.determinate(True)
    dz.percent(0)

    numberItems = len(items)
    percentStep = 100 / numberItems
    currentPercent = 0

    numberNewItems = 0

    for item in items:
        for line in open(item, 'r'):
            match = re.search("^Message-ID: <(.*)>$", line, re.IGNORECASE)
            if match:
                messageID = match.group(1)
                if subprocess.check_output(["/usr/bin/osascript", "AddSenderOfMailToFilter.applescript", messageID]).strip() == "1":
                    numberNewItems += 1
                break
        currentPercent += percentStep
        dz.percent(currentPercent)

    dz.finish("Added %(numberNewItems)d of %(numberItems)d mails' senders to friendly add rule." % locals())

    dz.url(False)

def clicked():
    dz.url(False)
