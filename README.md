# Understat xG

### Season xG Data

To get xG values for every match in a season pass the league ID folowed by season year as args.
```
python season.py EPL 2015
```
League IDs are EPL, La_Liga, Bundesliga, Serie_A, Ligue_1 and RFPL.  
Available seasons are from 2014 to present.



### Match Shot Data
To get data for every shot in a single match pass its ID as an arg.  
```
# for https://understat.com/match/9901
python match.py 9091
```

### Heatmaps
To produce heatmaps as shown below pass a CSV (such as one produced by match.py) as an arg
```
python match.py match_data.csv
```

Matplotlib heatmaps for 250,000 attempts on goal (excluding penalties).

![](figures/all_shots.png)
![](figures/head.png)
![](figures/right_foot.png)
![](figures/left_foot.png)
![](figures/freekicks.png)
![](figures/freekicks_right.png)
![](figures/freekicks_left.png)
