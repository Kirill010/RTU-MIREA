# Часть №1 ---------------------------------------------------------------------
# Задание №1 -----------

x <- 2
y <- 4

tmp <- x
x <- y
y <- tmp

print(x)
print(y)

# Задание №2 -----------

x <- 3.5
y <- "2,6"
z <- 1.78
h <- TRUE

class(x)
class(y)
class(z)
class(h)

as.numeric(h)
y <- sub(",",".", y)
as.numeric(y)
as.character(x)

# Задание №3 -----------

dohod <- 1573
dohod <- log(dohod)

# Задание №4 -----------

var_poem <- readLines(con = "text.txt", n = 1, encoding = "UTF-8")
var_poem <- as.numeric(var_poem)
print(var_poem)
print(2 * var_poem - 1)

# Часть №2 ---------------------------------------------------------------------
# Задание №1 -----------

vect <- c(1, 0, 2, 3, 6, 8, 12, 15, 0, NA, NA, 9, 4, 16, 2, 0)

vect[1]
vect[length(vect)]
vect[c(3:5)]
vect[vect == 2]
vect[vect > 4]
vect[vect%% 3 == 0]
vect[vect > 4 & vect%% 3 == 0]
vect[vect < 1 | vect > 5]
which(vect == 0)
which(vect > 2 & vect < 8)
order(vect[vect != 2], decreasing = FALSE)

# Задание №2 -----------

vect[length(vect)] <- NA
vect

# Задание №3 -----------

which(is.na(vect))

# Задание №4 -----------

length(vect) - sum(table(vect))

# Задание №5 -----------

id <- seq(1, 100)
id

# Задание №6 -----------

country <- c("France", "Italy", "Spain")
year <- c(2019, 2020, 2018, 2017)
country
year
length(year)

# Задание №7 -----------

income <- c(10000, 32000, 28000, 150000, 65000, 1573)
s <- sum(income) / length(income)
s
which(income < s)
income_class <- rep(1, length(income))
income_class
income_class[1] = 0
income_class[2] = 0
income_class[3] = 0
income_class[6] = 0
income_class

# Задание №8 -----------

norm <- readLines(con = "coords.txt", n = 11, encoding = "UTF-8")
norm <- as.numeric(norm)
N <- 9
P <- 4.29
print(norm)
p = sum(abs(norm)^P)^(1 / P)
p
write(x = p, file = "result.txt")

# Задание №9 -----------

X <- readLines(con = "coords.txt", n = 11, encoding = "UTF-8")
print(X)
Q <- as.numeric(X)
X1 <- diff(Q)
print(X1)
write(X1, "diff_vectors.txt")
I <- as.numeric(X1)
X2 <- diff(I)
print(X2)
write(X2, "diff_vectors.txt", append = TRUE)

