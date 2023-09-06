# Context
This data was taken from an actual production line near Detroit, Michigan. The goal is to predict certain properties of the line's output from the various input data. The line is a high-speed, continuous manufacturing process with parallel and series stages.

# Content
The data comes from one production run spanning several hours. Liveline Technologies has a large quantity of this type of data from multiple production lines in various locations.

# Challenge
The data comes from a multi-stage continuous flow manufacturing process. In the first stage, Machines 1, 2, and 3 operate in parallel, and feed their outputs into a step that combines the flows. Output from the combiner is measured in 15 locations surrounding the outer surface of the material exiting the combiner.

```
Primary Goal: Predict measurements of output from first stage.
```
Next, the output flows into a second stage, where Machines 4 and 5 process in series. After Machine 5, measurements are made again in the same 15 locations surrounding the outer surface of the material exiting Machine 5.
```
Secondary Goal: Predict measurements of output from second stage.
```
