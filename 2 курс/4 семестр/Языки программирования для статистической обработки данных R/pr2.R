# Часть №1----------------
# Задание №1--------------

M <- matrix(3, nrow = 3, ncol = 4)
M[1,3] = 4
M[2,1] = 1 
M[3,2] = NA
M[3,4] = 1
M

# Задание №2--------------

A <- c(1, 3, 4, 9, NA)
B <- c(5, 6, 7, 0, 2)
C <- c(9, 10, 13, 1, 20)
cols <- cbind(A, B, C)
print(cols)
rows <- rbind(A, B, C)
print(rows)

# Задание №3----------

names <- c("Jane", "Michael", "Mary", "George")
ages <- c(8, 6, 28, 45)
gender <- c(0, 1, 0, 1)

q <- cbind(names, ages, gender)
age_sq <- ages ** 2
q1 <- cbind(q, age_sq)
q1

# Задание №4----------
info <- list(names, ages, gender)
info

info[[1]][2]


info[[3]]

names(info) <- c("Names", "Age", "Gender")
info

info$drinks <- c("juice", "tea", "rum", "coffee")
info

info$Names[5] <- "John"
info$Age[5] <- 2
info$Gender[5] <- 1
info$drinks[5] <- "milk"
info

# Задание №5----------

index1 <- "0,72;0,38;0,99;0,81;0,15;0,22;0,16;0,4;0,24"
let1 <- strsplit(index1, ";")
class(let1)
let1 <- unlist(let1)
let2 <- gsub(",", ".", let1)
let2
I <- as.numeric(let2)
I

# часть №2----------------
# Задание №1--------------

A <- diag(c(4,9))
colnames(A) <- c('x1','x2')
rownames(A) <- c('eq1','eq2')
print(A)

# Задание №2---------------

A <- diag(c(4,9))
e <- eigen(A)
e$values # собственные значения

# Задание №3--------------

I <- diag(as.numeric(c(1,1)))
A <- diag(c(4,9)) / 9 # нормируем
B <- I - A
print(B)

# Задание №4-------------- 
f <- matrix(c(4, 2), nrow = 2, ncol = 1)
f

# Задание №5---------------

u_result <- solve(A) %*% f
u_result

# Задание №6---------------

u <- matrix(c(0.2, -0.3), nrow = 2, ncol = 1)
f <- f / 9
u1 <- B %*% u + f
u2 <- B %*% u1 + f
u3 <- B %*% u2 + f
u4 <- B %*% u3 + f
u5 <- B %*% u4 + f
u6 <- B %*% u5 + f
u7 <- B %*% u6 + f
print(u7-u_result)

# Задание №7------------

u7
u_result
dev <- u_result - u7
dev

# Задание №8-------------

max_A <- max(A)
A <- A / max_A
f <- f / max_A

A8 <- A
f8 <- f

A8
f8

# Задание №9-------------

eigen(A)$values

B <- diag(1, nrow = 2, ncol = 2) - A / 9
B

u_result <- solve(A) %*% f
u_result

u0 <- matrix(c(0.2, -0.3), nrow = 2, ncol = 1)
f <- f / 9
u1 <- B %*% u0 + f
u2 <- B %*% u1 + f
u3 <- B %*% u2 + f
u4 <- B %*% u3 + f
u5 <- B %*% u4 + f
u6 <- B %*% u5 + f
u6
u7 <- B %*% u6 + f
u7

u7
u_result
dev <- u_result - u7
dev

max_A <- max(A)
A <- A / max_A
f <- f / max_A

A10 <- A
f10 <- f

# Задание №10--------------
cat("Разница между A8 и A10: ", A8 - A10)
cat("Разница между f8 и f10: ", f8 - f10)

# Часть №3---------------------------------------------------------------------

step <- 1 # Шаг сетки
dekart_begin <- -5 # Начало сетки
dekart_end <- 5 # Конец сетки

# Задание сеточной поверхности
x <- seq(from = dekart_begin, to = dekart_end, by = step)
y <- x

# Задание двумерной функции на координатной сетке
surface_matrix <- outer(
  X = x,
  Y = y,
  FUN = function(x,y) Re(exp(-1i * 0.5 * x * y))
)
dimnames(surface_matrix) <- list(x, y)
surface_matrix

# Задание №1---------

M <- matrix(3, nrow = 4, ncol = 4)
M[1,3] = 4
M[2,1] = 2 
M[3,2] = 5
M[3,4] = 1
M
d <- nrow(M) * ncol(M)
X1 <- paste("number of matrix elements:", d)
write(X1, "summary.txt")

X2 <- paste("number of rows:", nrow(M))
write(X2, "summary.txt", append=TRUE)

X3 <- paste("number of cols:", ncol(M))
write(X3, "summary.txt", append=TRUE)

X4 <- paste("sum of main diag elements:", sum(diag(as.matrix(M))))
write(X4, "summary.txt", append=TRUE)

X5 <- paste("sum of middle row elements:", sum(M[nrow(M) %/% 2, ]))
write(X5, "summary.txt", append=TRUE)

X6 <- paste("sum of middle column elements:", sum(M[, ncol(M) %/% 2]))
write(X6, "summary.txt", append=TRUE)

X7 <- paste("row sums:", rowSums(M), collapse = ", ")
write(X7, "summary.txt", append=TRUE)

X8 <- paste("col sums:", colSums(M), collapse = ", ")
write(X8, "summary.txt", append=TRUE)



# Часть №4------------
# Задание №1-----------
# Пункт №1-----------
cars_matrix <- as.matrix(cars)
cars_matrix
cars_speed <- cbind(as.numeric(cars_matrix[,1]),rep(1, nrow(cars_matrix)))
cars_speed

# Пункт №2-----------

cars_dist <- cars_matrix[,2]
cars_dist

# Пункт №3-----------

alpha <- t(cars_speed)%*%cars_speed
alpha <- solve(alpha) %*% t(cars_speed) %*% cars_dist
alpha

# Пункт №4----------

print(class(alpha))
as.vector(alpha)

# Пункт №5---------

alpha_c <- alpha[1]
alpha_x <- alpha[2]
print(paste("alpha_c =", alpha_c))
print(paste("alpha_x =", alpha_x))

# Пункт №6---------

cars_speed_lm <- cars_matrix[,1]
cars_speed_lm

# Пункт №7--------

cars_dist_lm <- alpha_c + cars_speed_lm * alpha_x
cars_dist_lm

# Пункт №8-------

dist_residuals <- cars_dist_lm - cars_dist
dist_residuals

# Пункт №9-------

avg <- mean(dist_residuals)
std <- sd(dist_residuals)

# Пункт №10------

print(cars_dist_lm)

# Пункт №11------

print(avg)
print(std)
print(dist_residuals)
