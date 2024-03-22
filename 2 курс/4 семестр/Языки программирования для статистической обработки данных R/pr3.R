# Часть №1--------------
# Задание №1------------ 

names <- c("Jane", "Michael", "Mary", "George")
ages <- c(8, 6, 28, 45)
gender <- c(0, 1, 0, 1)

info <- list(names, ages, gender) # Создайте из векторов из задачи 3 список (list) и назовите его info
info

info[[1]][2] # Выведите на экран имя Michael


info[[3]] # Выведите на экран вектор gender

names(info) <- c("Names", "Age", "Gender") # Назовите векторы в списке name, age, gender. Выведите на экран элементы вектора name.
info

info$drinks <- c("juice", "tea", "rum", "coffee") # Добавьте в список вектор drinks, в котором сохранен значения: juice, tea, rum, coffee
info

info$Names[5] <- "John"
info$Age[5] <- 2
info$Gender[5] <- 1
info$drinks[5] <- "milk"
info

# Задание №2---------------

index1 <- "0,72;0,38;0,99;0,81;0,15;0,22;0,16;0,4;0,24"
let1 <- strsplit(index1, ";")
class(let1)
let1 <- unlist(let1)
let2 <- gsub(",", ".", let1) # заменили , на .
let2
I <- as.numeric(let2) # Сделайте переменную y числовой (обратите внимание на запятую!).
I

# Часть №2---------
# Задание №1---------
#install.packages("randomNames")
library(randomNames)

# Задание №2-------

set.seed(1234) # чтобы у всех получались одинаковые результаты
names <- randomNames(100, which.names = "first", ethnicity = 4)
names

# Задание №3----

ages <- sample(16:75, 100, replace = TRUE) # replace = TRUE – с повторяющимися значениями
views <- c("right", "left", "moderate", "indifferent")
polit <- sample(views, 100, replace = TRUE)
fr <- data.frame(names, ages, polit)
fr

# Задание №4----

fr$id <- 1:100
fr

# Задание №5----

from25_to_30 <- nrow(fr[fr$ages >= 25 & fr$ages <= 30, ])
print(from25_to_30)

num_rows <- nrow(fr)
rate <- from25_to_30 / num_rows
print(rate)

print(round(rate * 100, 1))

# Задание №6-----

polit_views <- factor(fr$polit)
print(polit_views)
print(length(levels(polit_views)))
fr$polit_views <- polit_views
print(fr)

# Часть №3-------
# Задание №1-----

library(dplyr)
if ("car" %in% installed.packages() == FALSE) {
  install.packages("car", dependencies = TRUE)
}
library(car)

Firms <- Ornstein
Firms

# Задание №2-------

nrow(Firms)
ncol(Firms)
colnames(Firms)

# Задание №3-------

filter(Firms, is.na(assets) | is.na(sector) | is.na(nation) | is.na(interlocks))

# Задание №4-------

filter(Firms, assets>=10000 & assets<=20000)
filter(Firms, interlocks<=30)
filter(Firms, sector=="TRN" & nation=="CAN")

# Задание №5-------

log_assets <- log(Firms$assets)
log_assets
Firms <- mutate(Firms, log_assets )
Firms

# Задание №6-------

#install.packages("foreign")
library(foreign)

write.dta(Firms, "Firms.dta")

# Задание №7-------

if(!require("VIM")) install.packages("VIM")
library(VIM)

plot(Firms$assets,Firms$interlocks, col=c('blue'), numbers=TRUE)


# Часть №4------
#install.packages(c("dplyr", "readr", "stringi", "stringr"), dependencies = TRUE)
#install.packages("tidyr", dependencies = TRUE)
library(dplyr)
library(readr)
library(stringr)
library(tidyr)

# Задание №1-------
covid_data <- read.csv(
  "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
)

# Задание №2-------

print(dim(covid_data))
print(names(covid_data))
print(sapply(covid_data, class))

# Задание №3-------

covid_data <- unite(covid_data, Province.State, Country.Region, col="Place", sep=" ")

numbers <- select(covid_data, -c("Place", "Lat", "Long"))

sum_r <- apply(numbers, MARGIN = 1, FUN=sum)
mean_r <- apply(numbers, MARGIN = 1, FUN=mean)
sd_r <- apply(numbers, MARGIN = 1, FUN=sd)

aggr <- data.frame(
        select(covid_data, c("Place", "Lat", "Long")),
        sum_r,
        mean_r,
        sd_r
)

names(aggr) <- c(
              "Страна/Регион",
              "Широта",
              "Долгота",
              "Сумма заболевших",
              "Среднее число заболевших",
              "Среднее отклонение числа заболевщих"
)

aggr

covid_data <- covid_data %>%
  pivot_longer(
    cols = -c(Place, Lat, Long),
    names_to = "Date",
    values_to = "Count"
  ) %>%
  mutate(Date = as.Date(gsub("X", "", Date), format = "%m.%d.%y"))

print(sapply(covid_data, class))

# Задание №6-------

if (!file.exists("data_output")){
  dir.create("data_output")
}

#install.packages("VIM", dependencies = TRUE)
#install.packages("openxlsx", dependencies = TRUE)
library(openxlsx)

head(covid_data)
approved_data <- select(covid_data, c("Place", "Count", "Date")) %>%
  pivot_wider(
    names_from = Place,
    values_from = Count,
    values_fn = sum
  ) %>% mutate(Date = strftime(Date , "%Y-%m-%d"))


head(approved_data)

write.table(approved_data, file = "data_output/output.txt")
write.csv(approved_data, file = "data_output/output.csv")
write.xlsx(approved_data, file = "data_output/output.xlsx")

