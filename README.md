# Welcome to Mars
Welcome crew member. You have been assigned to the software engineering team.
There is no time to waste, Mars is a dangrous place and ressources are sparse.
We need your exprtise -- **right now**!

## Background
Six months ago, the first mission to Mars successfully landed and built the
base you just entered. An fleet of automous vehicles and building bots
commenced their work immedately and built this station as well as
several measurement, monitoring, and maintenance infrastructure.

Atmospheric assistance systems were deployed and operating for the last
6 months in order to create a sustainable habitat for humans. The fact that
you are still reading this message is proof that the systems are fully
operational.

In order for the atmospheric assistance systems to work, the station needs
to be exposed to solar power. This leves the station, however, vulnerable to
extreme weather and other potential dangers. The station can be secured into
a hibernation mode that will protect all life inside the station from any
dangers for at least 3 consequtive days -- bevore athmospheric assistance breaks
down and life suffocates. Our simulation data showed that this is sufficient to
guarantee a 99.98% change of survival until the next mission arrives in 5 years.

Good luck!

## Task
The AI's automated surveillance systems detected a malfunction with the early
strom warning system two days ago. Self healing procedures failed to restore
an operational state.

Your first task is to implement an early warning system so that the station
can enter hibernation in case of incoming storms.

### Resources
There are 8 weather data stations located at the surrounding of the station.
The stations's coordinates are `x=0, y=0`. The data from the weather stations
is collected and you can query it at:

https://masr-strom.herokuapp.com/data

All coordinates are expressed in km relative to the main station.

### Criteria for Success
Set up a system that warns the crew of the station in case of an incoming
storm. A warning should be issued when a strom reaches wind velocities above
50 km/h. Any signs of a storm stronger than 90 km/h is considered critical.

Hibernation is costly and not free of danger. You should only issue warnings
if the storm is actually (potentially) approaching the station. You should
differ between dangrous situations (wind speed of more than 50 km/h)
and critical situations (wind speed of more than 90 km/h). If possible, you
should give an estimate of the expected time left before the storm hits the
station.

### Technical Hints
In the folders `node`, `python`, and `spring` you can find a skeleton of
a working application set-up in JavaScript, Python 3, and Java respectiveley.
You are free to use any language, framework or other resource that might help
you achieve your target. If you want to use any of the skeletons provided,
please follow the instructions you find in the folders.

This exercise is meant to be playful. Feel free to alter the task. You can
focus on an alarming system that will push messages somehow. Or, you could
rather work on a visualization of the station and the weather at the surrounding
weather outposts. Maybe you have another great idea what to do with the data!

You can work on this together as a group, or alone. It's up to you.
There is only _one_ hard rule: **If you don't have fun, you're doing
it wrong**