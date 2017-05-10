library(xlsx)
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

sheet <- read.xlsx("excel_data.xlsx",1, header = FALSE)
sheet

A <- sheet[,1]
B <- sheet[,2]

intersect(A, B)

union(A, B)

setdiff(A, B)
setdiff(B, A)
