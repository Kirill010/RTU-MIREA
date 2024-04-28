# Задание №1--------------
# Пункт №1------------ 

download.file('https://raw.githubusercontent.com/qwerty29544/RpracticeBook/master/2Data/01FlatTables/ECG_yurchenkov.txt', destfile = 'yurchenkov.txt')

# Пункт №2-------------

data_yurchenkov = readLines('ECG_yurchenkov.txt')

for (i in 1:length(data_yurchenkov)) {
  if (data_yurchenkov[i] == '0	-0,02875	-0,024375	0,3125	-1,44196	1,475') {
    break
  }
  print(data_yurchenkov[i])
}

# Пункт №3----------------

for (i in c(1:length(data_yurchenkov))){
  if (data_yurchenkov[i] == 'Время(мс)	0	1	2	3	4')
    break
  else {
    data_yurchenkov <- data_yurchenkov[-i]
  }
}

data = read.csv('ECG_yurchenkov.txt', sep='\t', skip = 46)

colnames(data) <- c('time', 'v1', 'v2', 'v3', 'v4', 'v5')
for (i in 1:ncol(data)){
  data[,i] <- gsub(',', '.', data[,i])
  data[,i] <- as.numeric(data[,i])
}
data = na.omit(data)

# Пункт №4------------------

stages = function(x){
  sum(x == 0)
}

stages(data[,1])

# Пункт №5-----------------

time = function(x) {
  result = c()
  for (i in 2:length(x)) {
    if (abs(x[i] - x[i - 1]) != 4) {
      result = c(result, x[i - 1])
    }
  }
  result = c(result, x[length(x)])
  return(result)
}

ms = time(data[,1])
print(ms)

cumsum(ms)


table(cut(x = as.integer(data[,1]), breaks = seq(1, length(data), (length(data) - 1)/ncol(data))))

# Пункт №6----------------

library(matrixStats)

# Статистика
colStats = function(x) {
  cbind(
    colSds = colSds(as.matrix(x)),
    colVars = colVars(as.matrix(x)),
    colSums = colSums(as.matrix(x)),
    colMeans = colMeans(as.matrix(x)),
    colMedians = colMedians(as.matrix(x))
  )}

colStats(data)
summary(data)

split_data = split(data, cumsum(data[,1] == '0'))

for (i in split_data){
  print(summary(i))
}

# Графики
library(ggplot2)
hist(data$v1, breaks = 100, col = 'red')
hist(data$v2, breaks = 100, col = 'orange')
hist(data$v3, breaks = 100, col = 'yellow')
hist(data$v4, breaks = 100, col = 'green')
hist(data$v5, breaks = 100, col = 'blue')


hist(split_data[[1]]$v5, breaks = 100, col = 'purple')

# Пункт №7------------------------

ggplot(data[1:10000,], aes(time, v5)) +
  geom_bar(stat="identity", position="dodge") +
  theme(axis.text.x = element_text(angle = 90))


source("D:\\practice1\\pr5.R")


v1 = c(data$v1) + 1

alt_arimf = alter_johns(out_of_trend(v1[1:5000],2,'Arifm'))
alt_geom = alter_johns(out_of_trend(v1[1:5000], 25, "Geom"))
alt_garm = alter_johns(out_of_trend(v1[1:5000], 100, "Garm"))
p1 = plot(alt_arimf, type = 'l', col='pink')
p2 = plot(alt_geom, type = 'l', col = 'grey')
p3 = plot(alt_garm, type = 'l', col = 'black')









