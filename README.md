# PIoT Assignment 1
## s3801950 Oyvind Samueslen / s3703700 Zaed Ahmed

##### Some useful commands

Copy __all__ files to Pi:

```scp -r * pi@10.0.0.77:/home/pi/a1```

Copy one file:

```scp working_file.py pi@10.0.0.77:/home/pi/a1```

where 'pi' is the Raspberry Pi's user name, 10.0.0.77 ip address of pi. 

## Tasks

#### b) monitor_and_display.py

Display temperature in 10 second intervals. Load temp levels from config.json, or user provided file. 

```$ python3 task_b/monitor_and_display.py [custon_config_file.json]```

Defaults to 'config.json' in working dir. 


### c) 
#### 1) electronic_die.py
Shake Pi to display random number (1-6) for 3 seconds.

``` $ python3 task_c/electronic_die.py ```


#### 2) game.py
Play a game of dice! Default is 2 players, first to 10.

```python3 task_c/game.py [goal] [player1] [player2]...```

Where goal is an int, playerX str.