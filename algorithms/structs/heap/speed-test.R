pdf("/home/wiki/School/NPRG062/algorithms/structs/heap/speed-test.pdf", width=10, height=10)

data <-read.csv("/home/wiki/School/NPRG062/algorithms/structs/heap/speed-test.csv")

data.lm <- lm(s ~ n, data=data)

plot(data)
abline(a = data.lm$coefficients[1], b = data.lm$coefficients[2])

dev.off()