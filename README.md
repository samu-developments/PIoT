# PIoT Assignment 1
## s3801950 Oyvind Samueslen / s3703700 Zaed Ahmed

##### Some useful commands

Copy __all__ files to Pi:

```scp -r * pi@10.0.0.77:/home/pi/a1```

Copy one file:

```scp working_file.py pi@10.0.0.77:/home/pi/a1```

where 'pi' is the Rasberry Pi's user name, 10.0.0.77 ip address of pi. 

## Tasks

### b) monitor_and_display.py

Display temperature in 10 second intervals. Load temp levels from config.json, or user provided file. 

```$ python3 task_b/monitor_and_display.py [custon_config_file.json]```

Defaults to 'config.json' in task_b/