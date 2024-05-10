# Часть №1--------------
# Задание №1------------ 

library(ggplot2)

data = read.csv("demography.csv")

# Задание №2------------ 

data$young_share <- data$young_total / data$popul_total
data$trud_share <- data$wa_total / data$popul_total
data$old_share <- (data$ret_total + data$X70_plus) / data$popul_total

# Задание №3------------ 

ggplot(data, aes(x = trud_share)) +
  geom_histogram(binwidth = 0.01, color = "black", fill = "blue", alpha =
                   0.5, bins=20) +
  geom_rug() +
  geom_vline(xintercept = median(data$trud_share), color = "red") +
  labs(x = "Процент (%)", y = "Доля") +
  scale_x_continuous(labels = scales::percent)

# Задание №4------------ 

ggplot(data, aes(x=trud_share, fill=region)) +
  geom_density(alpha=0.5) +
  facet_wrap(~region) +
  labs(x = "Процент (%)", y = "Доля") +
  scale_fill_manual(values = rainbow(length(unique(data$region))))

ggplot(data, aes(x = region, y = trud_share, fill = region)) +
  geom_violin(alpha = 0.7) +
  geom_boxplot(width = .2) +
  labs(y = "Процент (%)")

# Задание №5------------ 

ggplot(data, aes(x=young_share, y=old_share)) +
  geom_point(color="green", shape=17) +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(x = "Молодые (%)", y = "Пожилые (%)", title = paste("Корреляция: ", 
round(cor(data$young_share, data$old_share, use =
"complete.obs"), 2)))

# Задание №6------------ 

data$male_total = data$wa_male + data$ret_male + data$young_male
data$male_share = data$male_total / data$popul_total 
data$male = ifelse(data$male_share > 0.5, 1, 0)

# Задание №7------------ 

ggplot(data, aes(x=young_share, y=old_share, size=male_share, color=factor(male))) +
  geom_point(alpha=0.7) +
  labs(x = "Молодые (%)", y = "Пожилые (%)", size = "Доля мужчин (%)", color = "Преобладают нет|да") +
  scale_size_continuous(range=c(1,10)) +
  scale_color_manual(values = c("purple", "orange")) +
  theme_minimal()

# Столбиковая диаграмма

ggplot(data, aes(x = region, fill = region)) +
  geom_bar(position = "dodge") +
  labs(x = "Регион", y = "Районов") +
  theme_minimal() +
  scale_fill_manual(values = c("darkgreen", "blue"))


# Часть №2--------------
# Задание №1------------

View(mtcars)
ggplot(mtcars, aes(x = hp, y = wt, size = cyl, color = factor(am == 1))) +
  geom_point(alpha = 0.7) +
  labs(x = "Лошадиная сила", y = "Вес", size = "Cylinders", color = "Коробка 
передач") +
  scale_color_manual(values = c("red", "green"), labels = c("Механика", 
                                                            "Автоматика")) +
  ggtitle("Зависимости автомобильных компонентотв")

# Часть №2--------------
# Задание №2------------

ggplot(mtcars, aes(x = hp, fill = factor(am))) +
  geom_histogram(bins = 6, color = "black", fill = "brown") +
  labs(x = "Horsepower") +
  scale_fill_manual(values = c("brown", "black"), guide = FALSE) +
  facet_wrap(~ factor(am, labels = c("Automatic", "Mechanic")), nrow = 1) +
  ggtitle("Gross horsepower")+
  theme_bw()

# Часть №2--------------
# Задание №3------------

View(sleep)
ggplot(sleep, aes(x = group, y = extra)) +
  geom_boxplot(fill = c("orange", "darkgreen")) +
  labs(x = "Группа", y = "Extra", title = "Ящики с усами️",
       fill = "Transmission Type") +
  scale_fill_manual(values = c("blue", "green")) +
  theme(plot.title = element_text(color = "black", size = 14, face = "bold", hjust = 0.5))

        
# Часть №3--------------

covid_data = read.csv("data_output/output.csv")
covid_data
colnames(covid_data) = gsub('NA_','', colnames(covid_data))
ggplot(covid_data, aes(x = covid_data$Date,y = X.Armenia))+
  geom_point(col='orange', size=1)+
  labs(x='Время с начала пандемии', title = 'Динамика роста заболеваемости в 
Армении', subtitle = paste("Данные от", min(rownames(covid_data))))


ggplot(covid_data, aes(x = covid_data$Date,y = X.Belgium))+
  geom_point(size=1, col='darkred')+
  labs(x='Время с начала пандемии', title = 'Динамика роста заболеваемости в 
Бельгии', subtitle = paste("Данные от", min(rownames(covid_data))))


ggplot(covid_data, aes(x = covid_data$Date,y = X.Brazil))+
  geom_point(col='blue', size=1)+
  labs(x='Время с начала пандемии', title = 'Динамика роста заболеваемости в 
Бразилии', subtitle = paste("Данные от", min(rownames(covid_data))))


ggplot(data = covid_data, aes(X.Belarus)) +
  geom_histogram(aes(y = ..density..), bins = 30, color = "darkgreen", fill =
                   "red") +
  geom_density(fill="green", alpha = 0.1)+
  labs(x='Беларусь', y='Плотность')


ggplot(data = covid_data, aes(X.Latvia)) +
  geom_histogram(aes(y = ..density..), bins = 30, color = "white", fill =
                   "darkred") +
  geom_density(fill="black", alpha = 0.1)+
  labs(x='Латвия', y='Плотность')


ggplot(data = covid_data, aes(X.Russia)) +
  geom_histogram(aes(y = ..density..), bins = 30, color = "blue", fill =
                   "white") +
  geom_density(fill="red", alpha = 0.1)+
  labs(x='Россия', y='Плотность')

