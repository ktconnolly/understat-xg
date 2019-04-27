# Understat xG

### Season xG Data

To get xG values for every match in a season pass the league ID folowed by season year as arguments.
```
python season.py EPL 2015
```
League IDs are EPL, La_Liga, Bundesliga, Serie_A, Ligue_1 and RFPL.  
Available seasons are 2014 to present.

### Match Shot Data
To get data for all shots in a single match pass its ID as an argument.  
```
# for https://understat.com/match/9901
python match.py 9091
```
Be aware that shots in first half injury time will show as 46, 47 etc rather than 45.

### Heatmaps
To create heatmaps pass a CSV produced by match.py as an argument.  
Penalties and own goals will be excluded.
```
python heatmap.py match_data.csv
```

Below are heatmaps using 250,000 attempts on goal.

![](figures/all_shots.png)
![](figures/head.png)
![](figures/right_foot.png)
![](figures/left_foot.png)
![](figures/freekicks.png)
![](figures/freekicks_right.png)
![](figures/freekicks_left.png)
