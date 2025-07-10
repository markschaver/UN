library(tidyverse)
library(rmarkdown)
library(knitr)

setwd("/Users/markschaver/Library/CloudStorage/OneDrive-Personal/Archive/Code/UN")

un <- read.csv("un-coincidence-2023.csv")

most_similar <- filter(un, un["COINCIDENCE"] == max(un["COINCIDENCE"]))
kable(most_similar)

closest <- filter(un, un["COINCIDENCE"] > .75)
kable(arrange(closest, desc(COINCIDENCE)))

farthest <- filter(un, un["COINCIDENCE"] < .2)
kable(arrange(farthest, COINCIDENCE))
