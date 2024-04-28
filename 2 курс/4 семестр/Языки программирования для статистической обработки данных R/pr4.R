# Часть №1--------------
# Задание №1------------ 
# Пункт №1------------ 

#install.packages('readxl')
library('readxl')

dfd <- read_excel(
                "D:/practice1/GAZ.xlsx",
                col_types = c('date', 'numeric', 'numeric', 'numeric', 'numeric', 'numeric', 'text', 'text', 'text')
)

colnames(dfd) <- c('date', 'p', 'temp', 'gas', 'condensate', 'water', 'ID', 'tree', 'group') 
dfd
# Пункт №2------------ 

dfd <- na.omit(dfd)
dfd

# Пункт №3------------ 

dfd$kelvins <- as.numeric(dfd$temp) + 273.15
dfd <- dfd[,-3]   
dfd

# Пункт №4----------- 

dfd$id <- as.integer(factor(dfd$ID, levels = unique(dfd$ID)))
dfd$Куст <- as.integer(factor(dfd$tree, levels = unique(dfd$tree)))
dfd$Группа <- as.integer(factor(dfd$group, levels = unique(dfd$group)))
dfd

# Пункт №5------------ 

dfd$gas_con <- dfd[3] / dfd[4]
dfd$gas_water <- dfd[3] / dfd[5]
dfd$water_con <- dfd[5] / dfd[4] 
dfd

# Пункт №6------------ 

dfd_2018 <- subset(dfd, substring(date, 1,4) == '2018')
dfd_2018

# Пункт №7------------ 

dfd_111 <- subset(dfd, ID == '111')

# Пункт №8------------ 

library(dplyr)
unique_ids = dfd %>%
  group_by(ID) %>%
  summarize(max_water = max(water)) %>%
  filter(max_water < 2) %>%
  pull(ID)

unique_ids

# Пункт №9------------ 

id_well = dfd %>%
  group_by(ID) %>%
  filter(all(water + gas + condensate >= 1000)) %>%
  pull(ID)

unique(id_well)

# Пункт №10------------ 

dfd_2018$sum <- dfd_2018$gas + dfd_2018$condensate + dfd_2018$water
print(subset(dfd_2018, sum == max(sum))$tree)

# Пункт №11------------ 

print(subset(dfd_2018, water == max(water))$tree)
dfd
# Пункт №12------------ 

mean_gas_water <- dfd %>%
  subset(gas_water$gas != Inf) %>%
  group_by(tree) %>%
  summarise(mean_gas_water = mean(gas_water$gas, na.rm = TRUE))

print(mean_gas_water)

max_mean_row <- mean_gas_water %>%
  filter(mean_gas_water == max(mean_gas_water, na.rm = TRUE))

print(max_mean_row)
