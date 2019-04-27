# Understat xG

### Season xG data

To get xG values for every match in a season pass the league ID and year as args.
```
python season.py EPL 2015
```
League IDs are EPL, La_Liga, Bundesliga, Serie_A, Ligue_1 and RFPL.  
Available seasons are from 2014 to present.



### Match xG data
To get xG values for a single match pass its ID from the URL as an arg.  
```
# for https://understat.com/match/9901
python match.py 9091
```

### Heatmaps
To produce heatmaps as shown below pass a CSV as an arg
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
