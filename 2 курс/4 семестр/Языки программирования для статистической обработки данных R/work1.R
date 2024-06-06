# Установка и загрузка необходимых библиотек
install.packages("forecast")
install.packages("dplyr")
install.packages("ggplot2")
install.packages("seasonalview")
install.packages("tidyverse")
install.packages("gridExtra")
install.packages("outliers")
install.packages("readr")


library(outliers)
library(stats)
library(quantmod)
library(forecast)
library(ggplot2)
library(dplyr)
library(readr)
library(seasonalview)
library(tidyverse)
library(gridExtra)

# Загрузка данных
data1 <- read.csv('D:\\practice1\\archive\\Combined_Flights_2018.csv')
data2 <- read.csv('D:\\practice1\\archive\\Combined_Flights_2019.csv')
data3 <- read.csv('D:\\practice1\\archive\\Combined_Flights_2020.csv')

# Выбрали столбцы FlightDate и DepDelayMinutes
data11 <- select(data1, FlightDate, DepDelayMinutes)
data22 <- select(data2, FlightDate, DepDelayMinutes)
data33 <- select(data3, FlightDate, DepDelayMinutes)

# Объединили таблицы
data111 <- full_join(data11, data22, by = "FlightDate")
data222 <- full_join(data111, data33, by = "FlightDate")
data222 <- data222[1:2]
data2222 <- na.omit(data222)

flight_delays <- data2222 %>%
  group_by(FlightDate) %>%
  summarise(total_delay = DepDelayMinutes.x)

flight_delays1 <- na.omit(flight_delays)

# Нашли мин макс и икслючили
min_value <- min(flight_delays1$total_delay)
max_value <- max(flight_delays1$total_delay)

flight_delays12345 <- subset(flight_delays1, total_delay > min_value & total_delay < max_value)
print(flight_delays12345)

# Временной ряд
flight_delays_ts <- ts(flight_delays12345$total_delay, start = c(2018, 1), end = c(2020, 12), frequency = 12)


(acf(flight_delays_ts, main=""))

plot(stl(flight_delays_ts, s.window="periodic")$time.series, main="")

ggtsdisplay(flight_delays_ts)
ggtsdisplay(diff(flight_delays_ts))
mean(diff(flight_delays_ts))
ggtsdisplay(diff(diff(flight_delays_ts, 12)))
ggtsdisplay(diff(diff(flight_delays_ts)))
mean(diff(diff(flight_delays_ts)))
plot(decompose(flight_delays_ts))
flightDecomposed <- decompose(flight_delays_ts)
plot(flightDecomposed$x,
     main = "Обзор характеристик временного ряда",
     xlab = "Время наблюдения",
     ylab = "Значения")
lines(flightDecomposed$trend, col = "red")

PP.test(flightDecomposed$x)

# ARIMA модель прогноза ---------------------------------------------------
fit <- auto.arima(flightDecomposed$x)
summary(fit)
arimaorder(fit)

arima1.model <- auto.arima(flightDecomposed$x)
arima2.model <- arima(flightDecomposed$x, order = c(2,3,1))
arima3.model <- arima(flightDecomposed$x, order = c(3,0,1))
arima4.model <- arima(flightDecomposed$x, order = c(1,4,3))
arima5.model <- arima(flightDecomposed$x, order =  c(1,2,1))

AIC(arima1.model,arima2.model, arima3.model, arima4.model, arima5.model)


summary(arima5.model)
arimaorder(arima5.model)

future1 <- forecast(arima5.model, h = 12)
print(future1)
autoplot(future1)


# ARIMA для тренда --------------------------------------------------------
arima6.model <- auto.arima(flightDecomposed$trend)
future5 <- forecast(arima5.model, h = 12)


plot(future5)
print(future5)
str(future5)
summary(future5)

round(predict(arima5.model,
              n.ahead=12,
              se.fit=TRUE)$se) + 
  predict(arima5.model,
          n.ahead=12,
          se.fit=TRUE)$pred

round(-predict(arima5.model,
               n.ahead=12,
               se.fit=TRUE)$se) + 
  predict(arima5.model,
          n.ahead=12,
          se.fit=TRUE)$pred

#Оценка-------------
data4 <- read.csv('D:\\practice1\\archive\\Combined_Flights_2021.csv')

f44 <- select(data4, FlightDate, DepDelayMinutes)

f444 <- na.omit(f44)
f444

min_value1 <- min(f444$DepDelayMinutes)
max_value1 <- max(f444$DepDelayMinutes)
f33312345 <- subset(f444, DepDelayMinutes > min_value1 & DepDelayMinutes < max_value1)
print(f33312345)

f33312345 <- f33312345 %>%
  group_by(FlightDate) %>%
  summarise(DepDelayMinutes = mean(DepDelayMinutes))

forecast_df <- data.frame(forecast=future1$mean)

f33312345$FlightDate <- as.Date(f33312345$FlightDate)

flight_date <- as.Date(c("2021-01-01", "2021-02-01", "2021-03-01", 
                         "2021-04-01", "2021-05-01", "2021-06-01", 
                         "2021-07-01", "2021-08-01", "2021-09-01", 
                         "2021-10-01", "2021-11-01", "2021-12-01"))

fdata <- data.frame(flight_date, forecast_df)


# Создание первого графика
plot(fdata$flight_date, fdata$forecast, type = "l", col = "blue", xlab = "Date", ylab = "Forecast")

# Установка параметров для второго графика
par(new = TRUE)

# Создание второго графика
plot(f33312345$FlightDate, f33312345$DepDelayMinutes, type = "l", col = "red", xlab = "", ylab = "", axes = FALSE)

# Добавление осей координат для второго графика
axis(side = 4, col = "red")

# Добавление легенды
legend("topleft", legend = c("Forecast", "DepDelayMinutes"), col = c("blue", "red"), lty = 1)


library(ggplot2)

# Создание графиков с ggplot2
ggplot() +
  geom_line(data = fdata, aes(x = flight_date, y = forecast), color = "blue") +
  geom_line(data = f33312345, aes(x = FlightDate, y = DepDelayMinutes), color = "red") +
  labs(x = "Date", y = "Value") +
  scale_color_manual(values = c("blue", "red"))

