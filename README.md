# Groundhog

- **Binary Name:** groundhog
- **Language:** everything working on "the dump"
- **Compilation:** via Makefile, including re, clean, and fclean rules

## Project Description

The Groundhog project involves extracting relevant information from real-time temperature data received on standard input. The goal is to detect weather tendencies and aberrations (droughts, severe colds, hurricanes, or any extreme climatic condition) as soon as possible.

### Tendency Detection

Given a number of days (period) as an argument, the program:

1. Waits for the next temperature value on standard input.
2. Outputs indicators once enough data is gathered:
   - The temperature increase average (g) observed on the last period (decreases not considered).
   - The relative temperature evolution (r) between the last given temperature and the temperature observed n-days ago.
   - The standard deviation (s) of the temperatures observed during the last period.
   - Alerts when it detects a switch in global tendency.

3. Repeats the process until the STOP keyword is read.

### Program Termination

Once the STOP keyword is entered, the program must output:
1. The total number of tendency switches observed on the whole time-series.
2. The list of the five biggest aberrations observed on the whole time-series (sorted by decreasing weirdness).

## Usage

```bash
./groundhog period
```
Exemple
```bash
./groundhog 7
27.7
g=nan r=nan% s=nan
31.0
g=nan r=nan% s=nan
32.7
g=nan r=nan% s=nan
34.7
g=nan r=nan% s=nan
35.9
g=nan r=nan% s=nan
37.4
g=nan r=nan% s=nan
38.2
g=nan r=nan% s=3.46
39.5
g=1.69 r=43% s=2.82
40.3
g=1.33 r=30% s=2.50
42.2
g=1.36 r=29% s=2.40
41.3
g=1.07 r=19% s=2.06
40.4
g=0.90 r=13% s=1.56
39.8
g=0.69 r=6% s=1.19
38.7
g=0.57 r=1% s=1.07
36.5
g=0.39 r=-8% s=1.72 a switch occurs
35.7
g=0.27 r=-11% s=2.24
33.4
g=0.00 r=-21% s=2.65
29.8
g=0.00 r=-28% s=3.50
27.5
g=0.00 r=-32% s=4.20
25.2
g=0.00 r=-37% s=4.64
24.7
g=0.00 r=-36% s=4.51
23.1
g=0.00 r=-37% s=4.36
22.8
g=0.00 r=-36% s=3.58
22.7
g=0.00 r=-32% s=2.48
23.6
g=0.13 r=-21% s=1.60
24.3
g=0.23 r=-12% s=0.91
24.5
g=0.26 r=-3% s=0.77
26.7
g=0.57 r=8% s=1.29 a switch occurs
27.0
g=0.61 r=17% s=1.61
27.4
g=0.67 r=20% s=1.71
29.8
g=1.01 r=31% s=2.02
29.4
g=0.89 r=25% s=1.98
31.5
g=1.09 r=30% s=2.16
29.6
g=1.06 r=21% s=1.64
29.8
g=0.77 r=12% s=1.43
28.9
g=0.73 r=7% s=1.13
28.7
g=0.67 r=5% s=0.84
27.2
g=0.33 r=-9% s=1.20 a switch occurs
25.7
g=0.33 r=-13% s=1.74
26.0
g=0.07 r=-17% s=1.56
25.2
g=0.07 r=-15% s=1.67
21.6
g=0.04 r=-28% s=2.30
20.3
g=0.04 r=-30% s=2.77
21.1
g=0.16 r=-26% s=2.57
20.4
g=0.16 r=-25% s=2.41
19.8
g=0.16 r=-23% s=2.31
19.1
g=0.11 r=-27% s=1.85
19.6
g=0.19 r=-22% s=0.80
21.2
g=0.41 r=-2% s=0.72
21.0
g=0.41 r=3% s=0.77 a switch occurs
21.4
g=0.36 r=1% s=0.82
24.0
g=0.73 r=18% s=1.52
25.5
g=0.94 r=29% s=2.13
25.5
g=0.94 r=34% s=2.20
26.4
g=1.00 r=35% s=2.16
29.4
g=1.20 r=39% s=2.71
32.1
g=1.59 r=53% s=3.25
31.4
g=1.53 r=47% s=2.95
32.3
g=1.29 r=35% s=2.87
35.2
g=1.49 r=38% s=3.20
38.3
g=1.93 r=50% s=3.55
36.6
g=1.80 r=39% s=2.93
38.4
g=1.63 r=31% s=2.77
39.9
g=1.46 r=24% s=2.98
40.5
g=1.54 r=29% s=2.65
39.4
g=1.41 r=22% s=1.74
39.0
g=1.00 r=11% s=1.18
40.5
g=0.77 r=6% s=1.27
42.1
g=1.00 r=15% s=1.12
38.7
g=0.74 r=1% s=1.07
37.5
g=0.53 r=-6% s=1.39 a switch occurs
38.1
g=0.53 r=-6% s=1.43
36.5
g=0.53 r=-7% s=1.74
35.4
g=0.53 r=-9% s=2.13
STOP
Global tendency switched 5 times
5 weirdest values are [26.7, 24.0, 21.6, 36.5, 42.1]
```

### Additional Notes

- Error messages are written to the error output, and the program exits with the 84 error code (0 if there is no error).
- Ensure that a Makefile is included for building the binary named `groundhog`.

## Bonus Features

Consider implementing the following bonus features:
- Graphical interface with charts, indicators, tendencies, etc.
- Forecast for the next X days.
- Evaluation of the difference between your forecast and the actual result.
- Different metrics for detecting switches and/or outliers.
- Benchmark of various methods.

Analysis relies on observation, and plotting the data should provide better insights.

## Disclaimer

There is not one unique method to define a trend or to forecast. As a consequence, the switches and aberrations detection may vary from one program to another. Keep calm and carry on coding: your program will be proved with reasonable tests, and the switches detection will only be evaluated to help you improve for the main project. They won't be taken into account for any grade.

You should find, in a more convenient format, the input/output of the example above along with this subject.

## Conclusion

**Groundhog** empowers you to contribute to more accurate weather forecasts. Embrace the challenge, stay thorough, and use your skills to create a reliable tool for detecting climatic tendencies.

