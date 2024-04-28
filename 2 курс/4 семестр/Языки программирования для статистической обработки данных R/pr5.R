# Часть №1--------------
# Задание №1------------ 

id <- 1:3
country <- c("Flatland", "Wonderland", "Sphereland")
craziness <- c(20, 15, 18)
region_type <- c("A", "B", "A")
author <- c("Abbot", "Carroll", "Burger")
size <- c(10, 100, 30)
m <- cbind(id, country, craziness, region_type, author, size)
df <- as.data.frame(m)
df
num <- 0
fac <- 0
ch <- 0
f <- function(df){
  for (i in c(1:length(df))){ 
    if (is.numeric(df[i,1]) == TRUE){
      num <- num + 1
    }
    else if (is.factor(df[i,1]) == TRUE){
      fac <- fac + 1
    }
    else if (is.character(df[i,1]) == TRUE){
      ch <- ch + 1
    }
  }
  return (c('numeric'=num, 'character'=ch, 'factor'=fac))
  
}
r <- f(df)
print(r)

# Задание №2----------

numeric_type_df <- function(db){
  new_df <- data.frame()
  for (i in colnames(db)){
    if (is.numeric(db$i)){
      new_df$num <- db[i]
    }
  }
  return (new_df)
}

# Задание №4----------

numeric_median <- function(vector){
  if (is.numeric(vector)){
    return (median(vector))
  }
  else{
    print('Vector is not numeric, cannot compute the median')
  }
}

numeric_median(c(1,2,3,4,5))
numeric_median(c('a', 'b', 'c'))

# Часть №2--------------------------

if ("quantmod" %in% rownames(installed.packages()) == FALSE) {
  install.packages("quantmod") }
library(quantmod)
library(stringr)
if ("ggpubr" %in% rownames(installed.packages()) == FALSE) {
  install.packages("ggpubr") }
library(ggpubr)

downloadable_stocks <- c("ATVIX", "^IXIC")

df <- getSymbols(Symbols = downloadable_stocks,
                 src = "yahoo",
                 from = as.Date.character("1900-01-01"))
df

df <- data.frame(get(downloadable_stocks[1]))
df
downloadable_stocks <- str_remove(downloadable_stocks, "[:punct:\\^]")

df <- data.frame(get(downloadable_stocks[1]))

rm(list = downloadable_stocks)

# Задание №1---------------------------
# Пункт №2----------------------------

out_of_trend <- function(x, dt, method='Arifm'){
  stopifnot(length(x) > 3 & dt <= (ceiling(length(x)/2)-1) & is.numeric(x) & is.numeric(dt))
  stopifnot(method %in% c('Arifm', 'Geom', 'Garm'))
  y <- vector()
  if (method == 'Arifm'){
    for (i in c((1+dt):(length(x)-dt))){
      y <- append(y,log((x[i-dt] + x[i+dt])/(2*x[i])))
    }
    return (y)
  }
  else if (method == 'Geom'){
    for (i in c((1+dt):(length(x)-dt))){
      y <- append(y,log((x[i-dt] * x[i+dt])/(x[i]^2)))
    }
    return (y)
  }
  else if (method == 'Garm'){
    for (i in c((1+dt):(length(x)-dt))){
      y <- append(y, log((2 * x[i-dt] * x[i+dt])/(x[i] * (x[i-dt] + x[i + dt]))))
    }
    return (y)
  }
}

# Пункт №3------------------

t = seq(0, 10, 0.1)
x = 2 * t + 3 + sin(2*t)
x_n <- out_of_trend(x, 2, 'Arifm')
mean(x_n)

# Пункт №4-------------------

alter_johns <- function(y){
  for (i in y){
    stopifnot(is.numeric(i))
  }
  a_t <- numeric(length(y)-1)
  for (i in (1:(length(y)-1))){
    a_t[i] <- sum((1/(length(y)-i)) * abs(y[(1+i) : length(y)] - y[1:(length(y)-i)]))
  }
  return (a_t)
}

# Пункт №5-------------------

alter_johns(x_n)

# Пункт №6------------------

result_of_alter_johns_1 <- alter_johns(out_of_trend(df$ATVIX.Open,2,'Arifm'))


result_of_alter_johns_2 <- alter_johns(out_of_trend(df$ATVIX.Adjusted, 400, "Garm"))

plot(alter_johns(x_n), type = 'l', col='purple', lwd=5, xlab = 'Индекс элемента', ylab='Значение функции Альтера-Джонса')
a <- lines(result_of_alter_johns_1,type = 'l', col='green', lwd=3)
b <- lines(result_of_alter_johns_2, type = 'l', col =  'red', lwd=2)



# Часть №3---------------------
# Задание №1---------------------

SIM <- function(A, u0, f, n_iter = 10e5, eps=10e-7){
  stopifnot(n_iter>=0 & class(n_iter)=='numeric')
  stopifnot(eps>=0 & is.numeric(eps))
  stopifnot(is.numeric(A))
  stopifnot(length(A)>2, sqrt(length(A)) %% 1 == 0)
  maxaf <- max(A, f)
  A <- A/maxaf
  f <- f/maxaf
  B_matrix <- diag(rep(1,ncol(A))) - A
  u1 <- as.vector(B_matrix%*%u0 + f)
  for (i in c(1:n_iter)){
    if (max(abs(u1 - u0)) >= eps){
      u0 <- u1
      u1 <- B_matrix%*%u0 + f
    }
    else break
  }
  return (as.vector(u1))
}


A <- diag(c(4, 9))
A
u0 <- c(0.2, -0.3)
f <- matrix(c(4, 2), nrow = 2, ncol = 1)

result <- SIM(A, u0, f)
result
