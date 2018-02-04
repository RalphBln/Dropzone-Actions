# Dropzone-Actions
A set of custom actions for the Mac utility "Dropzone" from http://aptonic.com

## Friendly Ad.dzbundle

I wrote this in order to help me move the masses of advertisement that is not spam (i.e. that I might want to look at at some point in time but which I do not want to clog my inbox) out of my inbox in Mail.app into a dedicated folder. The moving of mails is taken care of by a filter rule, but adding all the addresses of the hundreds of companies I receive ads from manually has become cumbersome, so I wrote this action. Drag an email onto the Friendly Ad Dropzone action, and the sender's address is added to the filter rule.

## Ontology Metrics.dzbundle

Drag an OWL ontology file onto this Dropzone action. An analysis of the ontology is performed and the results (including expressiveness (OWL profile/DL family) and metrics like module cohesion are stored in the clipboard (one line separated with tabs, so that it can be pasted into a Numbers/Excel table).

Uses https://github.com/RalphBln/onto-module-metrics

## Strip EXIF.dzbundle

Drag an image file onto the action, and all EXIF data of the image will be removed.
