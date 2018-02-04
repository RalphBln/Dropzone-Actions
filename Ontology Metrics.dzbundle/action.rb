# Dropzone Action Info
# Name: Ontology Metrics
# Description: Displays some ontology metrics if an ontology file is dragged.
# Handles: Files
# Creator: Ralph Schäfermeier
# URL: http://yoursite.com
# Events: Clicked, Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.0

def dragged
  puts $items.inspect

  $dz.begin("Analyzing file...")

  $dz.determinate(true)

  $dz.percent(10)

  result = `java -jar onto-metrics-0.0.1-SNAPSHOT-jar-with-dependencies.jar "#{$items[0]}"`

  $dz.finish(result)

  $dz.url(false)
end
