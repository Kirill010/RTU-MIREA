-- 1
CREATE TABLE draw (
id_draw INT(10) AUTO_INCREMENT,
link_sketch VARCHAR(2550) NOT NULL,
PRIMARY KEY (id_draw)
);

-- 2
CREATE TABLE architect (
service_number INT(10) AUTO_INCREMENT,
fio VARCHAR(255) NOT NULL,
work_exp INT(10) NOT NULL,
contacts TEXT NOT NULL,
PRIMARY KEY (service_number)
);

-- 3
CREATE TABLE profession (
id_prof INT(10) AUTO_INCREMENT,
name_prof VARCHAR(255) NOT NULL,
PRIMARY KEY (id_prof)
);

-- 4
CREATE TABLE shops (
id_store INT(10) AUTO_INCREMENT,
name_shop VARCHAR(255) NOT NULL,
address TEXT NOT NULL,
PRIMARY KEY (id_store)
);

-- 5
CREATE TABLE manufacturers (
id_manufacturers INT(10) AUTO_INCREMENT,
name_manuf VARCHAR(255) NOT NULL,
PRIMARY KEY (id_manufacturers)
);

-- 6
CREATE TABLE specifications (
id_specifications INT(10) AUTO_INCREMENT,
name_spec VARCHAR(255) NOT NULL,
size_a_metr FLOAT(10) NOT NULL,
size_b_metr FLOAT(10) NOT NULL,
weight_kilo FLOAT(10) NOT NULL,
PRIMARY KEY (id_specifications)
);

-- 7
CREATE TABLE project (
id_project INT(10) AUTO_INCREMENT,
plan_start_date DATETIME NOT NULL,
plan_end_date DATETIME NOT NULL,
square INT(10) NOT NULL,
price FLOAT(10) NOT NULL,
draw_id_draw INT(10) NOT NULL,
architect_service_number INT(10) NOT NULL,
PRIMARY KEY (id_project),
FOREIGN KEY (draw_id_draw) REFERENCES draw (id_draw),
FOREIGN KEY (architect_service_number) REFERENCES architect (service_number)
);

-- 8
CREATE TABLE banya (
id INT(10) AUTO_INCREMENT,
owner VARCHAR(255) NOT NULL,
address TEXT NOT NULL,
start_date_construction DATETIME NOT NULL,
end_date_construction DATETIME NOT NULL,
project_id INT(10) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (project_id) REFERENCES project (id_project)
);

-- 9
CREATE TABLE materials (
id_mater INT(10) AUTO_INCREMENT,
name_mater VARCHAR(255) NOT NULL,
type VARCHAR(255) NOT NULL,
price_per_piece FLOAT(10) NOT NULL,
specifications_id INT(10) NOT NULL,
manufacturers_id INT(10) NOT NULL,
PRIMARY KEY (id_mater),
FOREIGN KEY (specifications_id) REFERENCES specifications (id_specifications),
FOREIGN KEY (manufacturers_id) REFERENCES manufacturers (id_manufacturers)
);

-- 10
CREATE TABLE list (
store_id INT(10),
mater_id INT(10),
PRIMARY KEY (store_id, mater_id),
FOREIGN KEY (store_id) REFERENCES shops(id_store),
FOREIGN KEY (mater_id) REFERENCES materials(id_mater)
);

-- 11
CREATE TABLE checks (
banya_id INT(10),
materials_id INT(10),
date_purchase DATETIME NOT NULL,
quantity INT(10) NOT NULL,
PRIMARY KEY (banya_id, materials_id),
FOREIGN KEY (banya_id) REFERENCES banya (id),
FOREIGN KEY (materials_id) REFERENCES materials (id_mater)
);

-- 12
CREATE TABLE builders (
service_number INT(10) AUTO_INCREMENT,
fio VARCHAR(255) NOT NULL,
work_exp INT(10) NOT NULL,
contacts TEXT NOT NULL,
revenue INT(10) NOT NULL,
profession_id INT(10) NOT NULL,
PRIMARY KEY (service_number),
FOREIGN KEY (profession_id) REFERENCES profession (id_prof)
);

-- 13
CREATE TABLE contract (
ban_id INT(10),
service_number INT(10),
link_if VARCHAR(2550) NOT NULL,
date_work_start TIME NOT NULL,
date_work_end TIME NOT NULL,
PRIMARY KEY (ban_id, service_number),
FOREIGN KEY (ban_id) REFERENCES banya (id),
FOREIGN KEY (service_number) REFERENCES builders (service_number)
);

/*
DROP TABLE IF EXISTS contract;
DROP TABLE IF EXISTS builders;
DROP TABLE IF EXISTS checks;
DROP TABLE IF EXISTS list;
DROP TABLE IF EXISTS materials;
DROP TABLE IF EXISTS banya;
DROP TABLE IF EXISTS project;
DROP TABLE IF EXISTS specifications;
DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS shops;
DROP TABLE IF EXISTS profession;
DROP TABLE IF EXISTS architect;
DROP TABLE IF EXISTS draw;


describe draw;
describe architect;
describe profession;
describe shops;
describe manufacturers;
describe specifications;
describe project;
describe banya;
describe materials;
describe list;
describe checks;
describe builders;
describe contract;
*/
-- Вставляем атрибуты в таблицах

-- shops, architect, profession, manufacturers,
-- 1
INSERT INTO shops (id_store, name_shop, address) VALUES
(1, 'Петрович', 'рабочий посёлок Боброво, с67Ю'),
(2, 'Лемана Про', 'МКАД, 24-й километр, 1А'),
(3, 'Благовар', 'МКАД, 25-й километр, вл1'),
(4, 'Империя Печей', 'Московская улица 10, Чехов'),
(5, 'Магазин "ЭкоСтрой"', 'г. Москва, ул. Природная, д. 6'),
(6, 'Магазин "Качественные материалы"', 'г. Москва, ул. Качества, д. 7'),
(7, 'Магазин "Баня плюс"', 'г. Москва, ул. Солнечная, д. 8'),
(8, 'Магазин "Все для ремонта"', 'г. Москва, ул. Ремонтная, д. 9'),
(9, 'Магазин "СтройПартнер"', 'г. Москва, ул. Партнерская, д. 10'),
(10, 'Магазин "СтройГрад"', 'г. Москва, ул. Тихая, д. 5'),
(11, 'Магазин стройматериалов "Стройка"', 'г. Москва, ул. Ленина, д. 1'),
(12, 'Магазин "Все для бани"', 'г. Москва, ул. Пушкина, д. 2'),
(13, 'Магазин "Баня и Сауна"', 'г. Москва, ул. Цветочная, д. 3'),
(14, 'Магазин "Дерево и Сталь"', 'г. Москва, ул. Фруктовая, д. 4');

-- 2
INSERT INTO architect (service_number, fio, work_exp, contacts) VALUES
(1, 'Ким Кирилл Сергеевич', 2, 'noobmaster6969@ya.ru'),
(2, 'Чистяков Тимофей Александрович', 4, 'qwerty123@mail.ru'),
(3, 'Сидоров Сидор Сидорович', 8, 'sidorov@example.com'),
(4, 'Кузнецов Кузьма Кузьмич', 12, 'kuznetsov@example.com'),
(5, 'Алексеев Алексей Алексеевич', 7, 'alekseev@example.com'),
(6, 'Марков Марк Маркович', 9, 'markov@example.com'),
(7, 'Федоров Федор Федорович', 6, 'fedorov@example.com'),
(8, 'Григорьев Григорий Григорьевич', 4, 'grigorev@example.com'),
(9, 'Смирнов Сергей Сергеевич', 11, 'smirnov@example.com'),
(10, 'Тихонов Тимофей Тимофеевич', 3, 'tikhonov@example.com');

-- 3
INSERT INTO manufacturers (id_manufacturers, name_manuf) VALUES
(1, 'БетонСтрой'),
(2, 'ЛесПродукт'),
(3, 'МеталлДекор'),
(4, 'ТехноНИКОЛЬ'),
(5, 'ДеревоТорг'),
(6, 'ОкнаПлюс'),
(7, 'ДвериМир'),
(8, 'ООО "Качественные материалы"'),
(9, 'ЗАО "Надежные поставки"'),
(10, 'ИП "Лес и Дерево"'),
(11, 'ЗАО "Баня"'),
(12, 'ООО "СтройМастер"'),
(13, 'ИП "Деревянные конструкции"'),
(14, 'ЗАО "ЭкоСтрой"'),
(15, 'ООО "Баня и Сауна"'),
(16, 'ЗАО "СтройГрад"'),
(17, 'ИП "Ремонт и Стройка"');

-- 4
INSERT INTO profession (id_prof, name_prof) VALUES
(1, 'Плотник'),
(2, 'Каменщик'),
(3, 'Сантехник'),
(4, 'Электрик'),
(5, 'Архитектор'),
(6, 'Печник'),
(7, 'Строитель'),
(8, 'Дизайнер'),
(9, 'Монтажник'),
(10, 'Инженер');

-- 5
INSERT INTO draw (id_draw, link_sketch) VALUES 
(1, 'https://example.com/sketch1.jpg'),
(2, 'https://example.com/sketch2.jpg'),
(3, 'https://example.com/sketch3.jpg'),
(4, 'https://example.com/sketch4.jpg'),
(5, 'https://example.com/sketch5.jpg'),
(6, 'https://example.com/sketch6.jpg'),
(7, 'https://example.com/sketch7.jpg'),
(8, 'https://example.com/sketch8.jpg'),
(9, 'https://example.com/sketch9.jpg'),
(10, 'https://example.com/sketch10.jpg');

-- 6
INSERT INTO specifications (id_specifications, name_spec, size_a_metr, size_b_metr, weight_kilo) VALUES 
(1, 'Доска обрезная', 6.0, 0.15, 20.0),
(2, 'Брус клееный', 3.0, 0.1, 15.0),
(3, 'Фундаментный блок', 0.4, 0.2, 30.0),
(4, 'Профнастил', 3.0, 1.0, 25.0),
(5, 'Изоляция', 1.0, 0.5, 5.0),
(6, 'Окно пластиковое', 1.2, 1.5, 25.0),
(7, 'Дверь деревянная', 2.0, 0.8, 40.0),
(8, 'Система отопления', 1.5, 1.5, 8.0),
(9, 'Труба пластиковая', 6.0, 0.1, 2.0),
(10, 'Кровельные системы', 3.0, 2.0, 35.0),
(11, 'Деревянное бревно', 6.0, 0.3, 50.0),
(12, 'Кирпич', 0.25, 0.12, 3.5),
(13, 'Плита фундаментная', 2.0, 1.0, 150.0),
(14, 'Крыша металлочерепица', 1.2, 2.5, 10.0),
(15, 'Утеплитель', 1.2, 0.6, 5.0),
(16, 'Сайдинг', 3.0, 0.2, 8.0);

-- 7
INSERT INTO project (id_project, plan_start_date, plan_end_date, square, price, draw_id_draw, architect_service_number) VALUES
(1, '2023-12-01 07:00:00', '2024-01-11 17:00:00', 50, 3000000.0, 1, 1),
(2, '2024-01-15 10:00:00', '2024-02-20 10:00:00', 70, 4500000.0, 2, 1),
(3, '2024-02-20 08:30:00', '2024-03-31 20:00:00', 100, 6000000.0, 3, 2),
(4, '2024-03-25 09:00:00', '2024-04-26 09:00:00', 80, 5000000.0, 4, 2),
(5, '2024-04-30 10:00:00', '2024-05-30 10:00:00', 90, 5500000.0, 5, 3),
(6, '2024-04-30 09:30:00', '2024-06-30 09:30:00', 60, 3500000.0, 5, 4),
(7, '2024-06-20 11:00:00', '2024-07-24 11:00:00', 75, 4000000.0, 6, 5),
(8, '2024-07-25 12:00:00', '2024-08-25 14:00:00', 85, 4800000.0, 8, 5),
(9, '2024-08-30 08:20:00', '2024-10-30 10:00:00', 95, 6200000.0, 7, 6),
(10, '2024-09-10 09:00:00', '2024-10-10 09:00:00', 55, 3200000.0, 6, 6),
(11, '2024-01-15 09:00:00', '2024-03-15 17:00:00', 50, 1200000.0, 8, 7),
(12, '2024-02-01 10:00:00', '2024-04-01 18:00:00', 75, 1500000.0, 5, 8),
(13, '2024-03-10 08:30:00', '2024-05-10 16:30:00', 100, 2000000.0, 2, 8),
(14, '2024-04-05 11:00:00', '2024-06-05 15:00:00', 60, 1300000.0, 3, 9),
(15, '2024-05-20 09:30:00', '2024-07-20 17:30:00', 80, 1600000.0, 1, 9),
(16, '2024-06-15 10:15:00', '2024-08-15 14:15:00', 90, 1800000.0, 9, 10),
(17, '2024-07-01 08:45:00', '2024-09-01 16:45:00', 70, 1400000.0, 10, 10),
(18, '2024-08-10 09:30:00', '2024-10-10 15:30:00', 55, 1250000.0, 10, 2),
(19, '2024-09-05 11:15:00', '2024-11-05 17:15:00', 85, 1700000.0, 1, 4),
(20, '2024-10-20 10:30:00', '2024-12-20 14:30:00', 65, 1350000.0, 2, 6);

-- 8
INSERT INTO banya (id, owner, address, start_date_construction, end_date_construction, project_id) VALUES 
(1, 'Сидоров Сидор Сидорович', 'г. Москва, ул. Садовая, д. 10', '2023-12-01 07:00:00', '2024-01-11 17:00:00', 1),
(2, 'Кузнецов Кузьма Кузьмич', 'г. Москва, ул. Цветочная, д. 5', '2024-01-15 10:00:00', '2024-02-20 10:00:00', 2),
(3, 'Петрова Анна Петровна', 'г. Москва, ул. Набережная, д. 15', '2024-02-20 08:30:00', '2024-03-31 20:00:00', 3),
(4, 'Смирнов Сергей Сергеевич', 'г. Москва, ул. Зелёная, д. 20', '2024-03-25 09:00:00', '2024-04-26 09:00:00', 4),
(5, 'Федоров Федор Федорович', 'г. Москва, ул. Осенняя, д. 25', '2024-04-30 10:00:00', '2024-05-30 10:00:00', 5),
(6, 'Григорьев Григорий Григорьевич', 'г. Москва, ул. Летняя, д. 30', '2024-04-30 09:30:00', '2024-06-30 09:30:00', 6),
(7, 'Тихонов Тимофей Тимофеевич', 'г. Москва, ул. Зимняя, д. 35', '2024-06-20 11:00:00', '2024-07-24 11:00:00', 7),
(8, 'Марков Марк Маркович', 'г. Москва, ул. Весенняя, д. 40', '2024-07-25 12:00:00', '2024-08-25 14:00:00', 8),
(9, 'Алексеев Алексей Алексеевич', 'г. Москва, ул. Природная, д. 45', '2024-08-30 08:20:00', '2024-10-30 10:00:00', 9),
(10, 'Иванова Ирина Ивановна', 'г. Москва, ул. Небесная, д.50', '2024-09-10 09:00:00', '2024-10-10 09:00:00', 10),
(11, 'Быков Алексей Смирнов', 'Московская область, д. Лесная, 15', '2024-01-05 08:00:00', '2024-02-15 17:00:00', 11),
(12, 'Егорова Екатерина Петрова', 'Ленинградская область, г. Сосновый Бор, ул. Озерная, 22', '2024-02-01 09:00:00', '2024-03-01 18:00:00', 12),
(13, 'Петров Сергей Кузнецов', 'Тульская область, д. Лесная Поляна, 5', '2024-03-10 10:30:00', '2024-04-20 16:30:00', 13),
(14, 'Ключникова Марина Иванова', 'Калужская область, с. Речное, ул. Центральная, 12', '2024-04-15 11:00:00', '2024-05-30 15:00:00', 14),
(15, 'Питерский Дмитрий Васильев', 'Рязанская область, г. Рязань, пр. Победы, 30', '2024-05-20 09:30:00', '2024-06-25 14:30:00', 15),
(16, 'Рыгина Ольга Сидорова', 'Владимирская область, д. Зеленая Роща, ул. Солнечная, 8', '2024-06-16 08:45:00', '2024-08-10 17:15:00', 16),
(17, 'Степанов Игорь Федоров', 'Нижегородская область, с. Березовка, ул. Школьная, 3', '2024-07-05 10:00:00', '2024-08-15 19:00:00', 17),
(18, 'Аршинова Татьяна Орлова', 'Смоленская область, г. Смоленск, ул. Ленина, 45', '2024-08-10 09:30:00', '2024-10-20 16:30:00', 18),
(19, 'Виноградов Анатолий Григорьев', 'Ярославская область, д. Кострома, ул. Природная, 18', '2024-09-15 11:15:00', '2024-10-25 18:45:00', 19),
(20, 'Жукова Наталья Коваленко', 'Тверская область, г. Тверь, ул. Набережная, 5', '2024-10-21 10:30:00', '2024-12-15 15:30:00', 20);

-- 9
INSERT INTO materials (id_mater, name_mater, type, price_per_piece, specifications_id, manufacturers_id) VALUES 
(1, 'Доска обрезная', 'Дерево', 150.0, 1, 1),
(2, 'Брус клееный', 'Дерево', 500.0, 2, 2),
(3, 'Фундаментный блок', 'Бетон', 1000.0, 3, 3),
(4, 'Кровельный материал', 'Металл', 2000.0, 4, 5),
(5, 'Изоляция минеральная', 'Минеральные материалы', 3000.0, 5, 15),
(6, 'Окно пластиковое', 'Пластик', 1500.0, 6, 16),
(7, 'Дверь деревянная', 'Дерево', 2000.0, 7, 17),
(8, 'Труба пластиковая', 'Пластик', 500.0, 8, 8),
(9, 'Система отопления', 'Металл', 10000.0, 9, 9),
(10, 'Кровельные системы', 'Металл', 1500.0, 10, 10),
(11, 'Доска обрезная', 'Дерево', 500.0, 1, 11),
(12, 'Брус клееный', 'Дерево', 1200.0, 2, 12),
(13, 'Кирпич', 'Кирпич', 15.0, 12, 13),
(14, 'Фундаментный блок', 'Бетон', 800.0, 3, 11),
(15, 'Металлочерепица', 'Металл', 350.0, 10, 10),
(16, 'Утеплитель', 'Изоляция', 200.0, 15, 8),
(17, 'Пластиковое окно', 'Окно', 2500.0, 6, 5),
(18, 'Дверь деревянная', 'Дерево', 3000.0, 7, 4),
(19, 'Труба пластиковая', 'Пластик', 100.0, 9, 3),
(20, 'Сайдинг', 'Металл', 200.0, 16, 6),
(21, 'Цемент', 'Строительные материалы', 500.0, 13, 4),
(22, 'Песок', 'Строительные материалы', 1000.0, 13, 6),
(23, 'Щебень', 'Строительные материалы', 800.0, 13, 2),
(24, 'Гидроизоляция', 'Изоляция', 1500.0, 5, 6),
(25, 'Кровельная пленка', 'Изоляция', 250.0, 5, 3),
(26, 'Линолеум', 'Полы', 700.0, 14, 5),
(27, 'Керамическая плитка', 'Отделка', 1200.0, 15, 3),
(28, 'Светодиодные лампы', 'Электрика', 300.0, 8, 1),
(29, 'Электропроводка', 'Электрика', 50.0, 8, 2),
(30, 'Краска для наружных работ', 'Отделка', 1200.0, 8, 9),
(31, 'Доска обрезная', 'Деревянные материалы', 1200.0, 1, 11),
(32, 'Брус', 'Деревянные материалы', 1500.0, 2, 10),
(33, 'Плита ОСБ', 'Строительные материалы', 800.0, 13, 12),
(34, 'Минеральная вата', 'Изоляция', 900.0, 5, 17),
(35, 'Пенопласт', 'Изоляция', 700.0, 5, 16),
(36, 'Стекловата', 'Изоляция', 850.0, 5, 15),
(37, 'Кровельные материалы (профнастил)', 'Кровля', 1800.0, 4, 8),
(38, 'Цементно-стружечная плита (ЦСП)', 'Строительные материалы', 1100.0, 13, 8),
(39, 'Теплоизоляционные плиты', 'Изоляция', 1300.0, 13, 9),
(40, 'Системы отопления (котел)', 'Отопление', 25000.0, 12, 4),
(41, 'Кирпич лицевой', 'Кирпичные материалы', 15.0, 12, 3),
(42, 'Бетонные блоки', 'Бетонные материалы', 50.0, 3, 1),
(43, 'Гидроизоляция', 'Изоляция', 1200.0, 4, 5),
(44, 'Сайдинг', 'Отделочные материалы', 900.0, 16, 10),
(45, 'Кровельная черепица', 'Кровля', 250.0, 16, 8),
(46, 'Арматура', 'Металлические материалы', 80.0, 9, 5),
(47, 'Лист фанеры', 'Деревянные материалы', 600.0, 14, 1),
(48, 'Штукатурка', 'Отделочные материалы', 500.0, 14, 2),
(49, 'Лак для дерева', 'Отделочные материалы', 300.0, 4, 3),
(50, 'Электропроводка', 'Электрика', 2000.0, 3, 17);

-- 10
INSERT INTO list (store_id, mater_id) VALUES 
(1, 1), 
(1, 2), 
(1, 3), 
(2, 4), 
(2, 5), 
(2, 6), 
(3, 7), 
(3, 8), 
(3, 9), 
(4, 10),
(4, 11), 
(4, 12), 
(5, 13), 
(5, 14), 
(6, 15), 
(7, 16), 
(7, 17), 
(8, 18), 
(9, 19), 
(10, 20),
(10, 21),
(11, 21), 
(12, 22), 
(12, 23), 
(12, 24), 
(13, 25), 
(13, 26), 
(14, 27), 
(14, 28), 
(14, 29), 
(14, 30),
(11, 31), 
(13, 32), 
(1, 33), 
(12, 34), 
(1, 35), 
(10, 36), 
(9, 37), 
(2, 38), 
(4, 39), 
(4, 40),
(6, 41), 
(6, 42), 
(6, 43), 
(7, 44), 
(1, 45), 
(1, 46), 
(8, 47), 
(8, 48), 
(5, 49), 
(10, 50);

-- 11
INSERT INTO checks (banya_id, materials_id, date_purchase, quantity) VALUES 
(1, 1, '2023-11-29', 20), 
(1, 2, '2023-11-28', 15), 
(1, 3, '2023-11-29', 10), 
(2, 4, '2024-01-14', 25), 
(2, 5, '2024-01-15', 30), 
(3, 6, '2024-02-21', 12), 
(3, 7, '2024-02-19', 8), 
(4, 8, '2024-03-23', 20), 
(5, 9, '2024-04-29', 18), 
(6, 10, '2024-04-30', 22),
(7, 22, '2024-06-20', 56),
(8, 13, '2024-07-25', 65),
(9, 15, '2024-08-30', 76),
(10, 20, '2024-09-10', 33),
(11, 23, '2024-01-15', 11),
(12, 47, '2024-02-01', 8),
(13, 32, '2024-03-10', 1),
(14, 50, '2024-04-05', 30),
(15, 34, '2024-05-20', 23),
(16, 21, '2024-06-15', 32),
(17, 18, '2024-07-01', 89),
(18, 20, '2024-08-10', 101),
(19, 19, '2024-09-05', 66),
(20, 1, '2024-10-20', 58);

-- 12
INSERT INTO builders (service_number, fio, work_exp, contacts, revenue, profession_id) VALUES 
(1, 'Смирнов Сергей Сергеевич', 8, 'smirnov@example.com', 60000, 1), 
(2, 'Федоров Федор Федорович', 4, 'fedorov@example.com', 40000, 1), 
(3, 'Григорьев Григорий Григорьевич', 6, 'grigorev@example.com', 50000, 2), 
(4, 'Тихонов Тимофей Тимофеевич', 5, 'tikhonov@example.com', 45000, 6), 
(5, 'Марков Марк Маркович', 7, 'markov@example.com', 70000, 4), 
(6, 'Алексеев Алексей Алексеевич', 9,'alekseev@example.com', 80000, 6), 
(7, 'Ким Кирилл Сергеевич', 2, 'noobmaster6969@ya.ru', 25000, 5),
(8, 'Кузнецов Кузьма Кузьмич', 11, 'kuznetsov@example.com', 100000, 1), 
(9, 'Иванова Ирина Ивановна', 2, 'ivanova@example.com', 30000, 3), 
(10, 'Петрова Анна Петровна', 3, 'petrova@example.com', 35000, 3),
(11, 'Иванов Иван Иванович', 5, '8-999-111-22-33', 60000, 2),
(12, 'Петров Петр Петрович', 5, '8-999-222-33-44', 80000, 7),
(13, 'Сидоров Сидор Сидорович', 5, '8-999-333-44-55', 50000, 5),
(14, 'Смирнова Анна Сергеевна', 5, '8-999-444-55-66', 75000, 2),
(15, 'Кузнецов Алексей Викторович', 5, '8-999-555-66-77', 90000, 8),
(16, 'Васильев Сергей Николаевич', 5, '8-999-666-77-88', 55000, 10),
(17, 'Федорова Ольга Владимировна', 5, '8-999-777-88-99', 70000, 9),
(18, 'Морозов Дмитрий Андреевич', 5, '8-999-888-99-00', 65000, 9),
(19, 'Лебедева Екатерина Игоревна', 5, '8-999-999-00-11', 72000, 6),
(20, 'Григорьев Артем Валерьевич', 5, '8-999-000-11-22', 85000, 1);

-- 13
INSERT INTO contract (ban_id, service_number, link_if, date_work_start, date_work_end) VALUES -- пропуск (студенческий билет)
(1, 1, 'https://example.com/contract1.pdf', '08:00:00', '17:00:00'), 
(2, 2, 'https://example.com/contract2.pdf', '09:00:00', '18:00:00'), 
(3, 3, 'https://example.com/contract3.pdf', '10:00:00', '16:00:00'), 
(4, 4, 'https://example.com/contract4.pdf', '08:30:00', '17:30:00'), 
(5, 5, 'https://example.com/contract5.pdf', '09:15:00', '18:15:00'), 
(6, 6, 'https://example.com/contract6.pdf', '10:45:00', '19:00:00'), 
(7, 7, 'https://example.com/contract7.pdf', '11:00:00', '20:00:00'), 
(8, 8, 'https://example.com/contract8.pdf', '09:30:00', '18:30:00'), 
(9, 9, 'https://example.com/contract9.pdf', '08:15:00', '17:45:00'), 
(10, 10, 'https://example.com/contract10.pdf', '10:30:00', '19:15:00'),
(11, 1, 'https://example.com/contract11.pdf', '08:00:00', '17:00:00'), 
(12, 2, 'https://example.com/contract12.pdf', '09:00:00', '18:00:00'), 
(13, 3, 'https://example.com/contract13.pdf', '10:00:00', '16:00:00'), 
(14, 4, 'https://example.com/contract14.pdf', '01:30:00', '17:30:00'), 
(15, 5, 'https://example.com/contract15.pdf', '09:00:00', '18:15:00'), 
(16, 6, 'https://example.com/contract16.pdf', '10:00:00', '19:00:00'), 
(17, 7, 'https://example.com/contract17.pdf', '11:00:00', '21:00:00'), 
(18, 8, 'https://example.com/contract18.pdf', '10:30:00', '22:00:00'), 
(19, 9, 'https://example.com/contract19.pdf', '09:15:00', '22:45:00'), 
(20, 10, 'https://example.com/contract20.pdf', '10:00:00', '20:15:00');


SELECT * FROM architect;
SELECT * FROM draw;
SELECT * FROM profession;
SELECT * FROM shops;
SELECT * FROM manufacturers;
SELECT * FROM specifications;
SELECT * FROM project;
SELECT * FROM banya;
SELECT * FROM materials;
SELECT * FROM list;
SELECT * FROM checks;
SELECT * FROM builders;
SELECT * FROM contract;


-- Практическая работа №2

SELECT fio FROM architect;

SELECT fio, contacts FROM builders;

SELECT * FROM materials ORDER BY price_per_piece DESC;

SELECT * FROM project ORDER BY plan_start_date ASC;

SELECT * FROM architect WHERE work_exp=4;

SELECT * FROM architect WHERE work_exp>4;

SELECT * FROM architect WHERE work_exp<4;

SELECT * FROM architect WHERE work_exp>=4;

SELECT * FROM architect WHERE work_exp<=4;

SELECT * FROM architect WHERE work_exp!=4;

SELECT * FROM architect WHERE service_number IS NULL;

SELECT * FROM architect WHERE service_number IS NOT NULL;

SELECT * FROM builders WHERE work_exp BETWEEN 4 AND 8;

SELECT * FROM builders WHERE service_number IN (1, 4);

SELECT * FROM builders WHERE service_number NOT IN (1, 4);

SELECT * FROM shops WHERE address LIKE 'МКАД%';

SELECT * FROM shops WHERE address NOT LIKE 'МКАД%';

SELECT * FROM shops WHERE address LIKE '%Москва%';

ALTER TABLE builders ADD rep FLOAT(10) AFTER work_exp; -- от 0 до 5

UPDATE builders SET rep=3.4
WHERE service_number=1;

UPDATE builders SET rep=4.7
WHERE service_number=2;

UPDATE builders SET rep=2.7
WHERE service_number=3;

UPDATE builders SET rep=1.0
WHERE service_number=4;

UPDATE builders SET rep=5.0
WHERE service_number=5;

UPDATE builders SET rep=4.6
WHERE service_number=6;

UPDATE builders SET rep=5.0
WHERE service_number=7;

UPDATE builders SET rep=0.8
WHERE service_number=8;

UPDATE builders SET rep=4.1
WHERE service_number=9;

UPDATE builders SET rep=3.8
WHERE service_number=10;

UPDATE builders SET rep=2.3
WHERE service_number=11;

UPDATE builders SET rep=0.6
WHERE service_number=12;

UPDATE builders SET rep=0.5
WHERE service_number=13;

UPDATE builders SET rep=3.0
WHERE service_number=14;

UPDATE builders SET rep=4.9
WHERE service_number=15;

UPDATE builders SET rep=4.5
WHERE service_number=16;

UPDATE builders SET rep=3.4
WHERE service_number=17;

UPDATE builders SET rep=3.3
WHERE service_number=18;

UPDATE builders SET rep=4.5
WHERE service_number=19;

UPDATE builders SET rep=4.8
WHERE service_number=20;

ALTER TABLE builders CHANGE COLUMN rep rating FLOAT(10);

DELETE FROM builders
WHERE work_exp = 0;

SELECT * FROM builders;

-- Практическая работа №3

-- Операция соединения +
SELECT name_mater, name_manuf FROM materials, manufacturers 
WHERE materials.type='Металл' AND 
materials.manufacturers_id=manufacturers.id_manufacturers;

-- Операция объединения +
SELECT name_mater, price_per_piece FROM materials
INNER JOIN shops ON materials.id_mater = shops.id_store
WHERE materials.price_per_piece > 1000;

-- Операция пересечения + -- ищем строительные материалы
SELECT shops.name_shop, shops.address, materials.name_mater, materials.price_per_piece FROM shops
JOIN list ON shops.id_store = list.store_id
JOIN materials ON list.mater_id = materials.id_mater
WHERE materials.type = 'Дерево'
ORDER BY shops.name_shop;

-- Операция разности +
SELECT builders.FIO, builders.work_exp FROM builders
WHERE NOT EXISTS
(SELECT architect.FIO, architect.work_exp FROM architect
WHERE architect.FIO=builders.FIO AND architect.work_exp=builders.work_exp);

-- Операция группировки +
SELECT type, COUNT(*) as cnt FROM materials
WHERE type = 'Пластик' 
GROUP BY type;

-- Операция сортировки + Запрос для получения списка материалов, отсортированных по цене за единицу:
SELECT materials.name_mater, materials.price_per_piece, shops.name_shop FROM materials
JOIN list ON materials.id_mater = list.mater_id
JOIN shops ON list.store_id = shops.id_store
ORDER BY materials.price_per_piece ASC;

-- Операция деления +
-- DROP VIEW IF EXISTS T1;
-- DROP VIEW IF EXISTS T2;
-- DROP VIEW IF EXISTS TT;

SELECT materials.name_mater FROM materials
    WHERE NOT EXISTS (SELECT * FROM shops
        WHERE NOT EXISTS (SELECT * FROM list
            WHERE list.store_id = shops.id_store AND list.mater_id = materials.id_mater));

-- Выборка данных (DQL)

-- Операция проекции + 
select * from materials;

-- Операция селекции + 
select * from builders
where rating > 4;

-- Операция соединения + 
SELECT banya.owner, banya.address, project.plan_start_date, project.plan_end_date
FROM banya
JOIN project ON banya.project_id = project.id_project;

-- Операция объединения +
SELECT fio FROM architect
WHERE service_number = 1
UNION
SELECT fio FROM builders
WHERE service_number = 2;

-- Операция пересечения +
SELECT materials.name_mater, materials.type
FROM materials
INNER JOIN list ON materials.id_mater = list.mater_id
ORDER BY materials.type;

-- Операция разности +
SELECT builders.FIO, builders.work_exp FROM builders
WHERE NOT EXISTS
(SELECT architect.FIO, architect.work_exp FROM architect
WHERE architect.FIO=builders.FIO AND architect.work_exp=builders.work_exp);

-- Операция группировки + Посчитаем количество бань, построенных каждым архитектором.
SELECT architect.fio, COUNT(banya.id) AS count_banya
FROM architect
JOIN project ON architect.service_number = project.architect_service_number
JOIN banya ON project.id_project = banya.project_id
GROUP BY architect.fio;

-- Операция сортировки +
SELECT * FROM shops
ORDER BY name_shop ASC;

-- Операция деления


-- Хранимые процедуры, функции и триггеры

-- Процедуры

-- DROP PROCEDURE имя_процедуры

-- 1. Добавление нового архитектора
CREATE PROCEDURE AddArchitect (IN p_fio VARCHAR(255), IN p_work_exp INT, IN p_contacts TEXT)
BEGIN
    INSERT INTO architect (fio, work_exp, contacts) VALUES (p_fio, p_work_exp, p_contacts);
END;

CALL AddArchitect('Пушкин Александр Сергеевич', 7, 'onegin@mail.com');
   
-- 2. Получите список материалов, используемых в конкретной бане.
CREATE PROCEDURE get_materials_by_banya(
    IN p_banya_id INT
)
BEGIN
    SELECT materials.name_mater, checks.quantity
    FROM banya
    JOIN checks ON banya.id = checks.banya_id
    JOIN materials ON checks.materials_id = materials.id_mater
    WHERE banya.id = p_banya_id;
END;

CALL get_materials_by_banya(1);
   
-- 3. Получение список строителей, сколько они работали.
CREATE PROCEDURE get_builders_by_banya(
    IN p_banya_id INT
)
BEGIN
    SELECT builders.fio, DATEDIFF(contract.date_work_end,contract.date_work_start)
    FROM banya
    JOIN contract ON banya.id = contract.ban_id
    JOIN builders ON contract.service_number = builders.service_number
    WHERE banya.id = p_banya_id;
END;

call get_builders_by_banya(2);

-- 4. Обновления даты окончания строительства бани
CREATE PROCEDURE UpdateDate(IN id_p INT, IN end_date DATETIME)
BEGIN
    UPDATE banya
    SET end_date_construction = end_date
    WHERE id = id_p;
END;

call UpdateDate(20, '2024-12-19 10:00:00');
   
-- 5. Посчитать площадь
CREATE PROCEDURE calculate_material_area(IN p_type VARCHAR(255))
BEGIN
    SELECT name_spec, size_a_metr * size_b_metr FROM specifications
    JOIN materials ON materials.specifications_id = specifications.id_specifications
    WHERE materials.type = p_type;
END;

call calculate_material_area('Металл');

-- Функции

-- DROP FUNCTION [ IF EXISTS ] function_name;

-- 1. Получение всей стоимости строительства бани
CREATE FUNCTION GetConstructionCost (p_project_id INT) 
RETURNS FLOAT 
DETERMINISTIC
BEGIN
    DECLARE total_cost FLOAT;

    SELECT SUM(materials.price_per_piece * checks.quantity) + 
           (SELECT price FROM project WHERE id_project = p_project_id) INTO total_cost 
    FROM materials 
    JOIN checks ON materials.id_mater = checks.materials_id 
    JOIN banya ON checks.banya_id = banya.id 
    WHERE banya.project_id = p_project_id;

    RETURN total_cost;
END;

select banya.owner, project.price, (GetConstructionCost(2) - project.price) as cost_materials, GetConstructionCost(2) as all_sum from banya
JOIN project ON banya.project_id = project.id_project
where project.id_project = 2;

-- 2. Подсчет количества материалов по типу
CREATE FUNCTION CountMaterialsByType (p_type VARCHAR(255)) 
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE material_count INT;
   
    SELECT COUNT(*) INTO material_count FROM materials WHERE type = p_type;
       
    RETURN material_count;
END;

select CountMaterialsByType('Дерево');

-- 3. Проверка наличия материала в магазине
CREATE FUNCTION IsMaterialAvailable (p_material_id INT) RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    DECLARE available BOOLEAN;
    SELECT COUNT(*) > 0 INTO available FROM list WHERE mater_id = p_material_id;
       
    RETURN available;
END;

select IsMaterialAvailable(112);


-- 4. Посчитать количество дней, когда началось строительство бани летом
CREATE FUNCTION count_summer_construction_days(table_name VARCHAR(255)) RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE summer_days INT;

    SET @query = CONCAT('SELECT COUNT(*) INTO summer_days FROM ', table_name, ' WHERE MONTH(start_date_construction) IN (6, 7, 8)');
    
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    RETURN summer_days;
END;


SELECT count_summer_construction_days('banya') AS summer_construction_days;


-- 5. 


-- Триггеры

-- 1. Триггер на обновление цены материала
CREATE TRIGGER UpdateMaterialPrice AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    INSERT INTO price_history (material_id, old_price, new_price, change_date)
    VALUES (NEW.id_mater, OLD.price_per_piece, NEW.price_per_piece, NOW());
END;
   


-- 2. Триггер на добавление новой бани для уведомления архитектора
CREATE TRIGGER NotifyArchitect AFTER INSERT ON banya
FOR EACH ROW
BEGIN
    INSERT INTO notifications (architect_service_number, message)
    VALUES (NEW.project_id.architect_service_number, CONCAT('Новая баня построена для ', NEW.owner));
END;
   


-- 3. Триггер на удаление материала из магазина
CREATE TRIGGER PreventMaterialDeletion BEFORE DELETE ON materials
FOR EACH ROW
BEGIN
    DECLARE material_count INT;
    SELECT COUNT(*) INTO material_count FROM list WHERE mater_id = OLD.id_mater;
       
    IF material_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Нельзя удалить материал, так как он используется в магазинах.';
    END IF;
END;
   


-- 4. Триггер на добавление новой записи о покупке материалов
CREATE TRIGGER LogMaterialPurchase AFTER INSERT ON checks
FOR EACH ROW
BEGIN
    INSERT INTO purchase_log (banya_id, materials_id, quantity, purchase_date)
    VALUES (NEW.banya_id, NEW.materials_id, NEW.quantity, NEW.date_purchase);
END;
   


-- 5. Триггер на изменение статуса бани
CREATE TRIGGER LogBanyaStatusChange BEFORE UPDATE ON banya
FOR EACH ROW
BEGIN
    IF OLD.status != NEW.status THEN
        INSERT INTO status_change_log (banya_id, old_status, new_status, change_date)
        VALUES (NEW.id, OLD.status, NEW.status, NOW());
    END IF;
END;
   
specifications.size_a * specifications.size_b > project.size

-- 1. Обновите общую стоимость бани при добавлении нового чека.
CREATE TRIGGER update_banya_cost_on_check_insertion
AFTER INSERT ON checks
FOR EACH ROW
BEGIN
    UPDATE banya
    SET total_cost = total_cost + (SELECT materials.price_per_piece * NEW.quantity FROM materials WHERE materials.id_mater = NEW.materials_id)
    WHERE id = NEW.banya_id;
END;

-- Практическая работа №4

-- Агрегатные функции

-- COUNT() +
SELECT architect.fio, COUNT(project.id_project) as CountProject 
FROM architect JOIN project ON project.architect_service_number = architect.service_number
GROUP BY architect.fio;

-- SUM() +
SELECT banya.owner, banya.start_date_construction, SUM(project.price) OVER (PARTITION BY banya.start_date_construction) as p
FROM banya JOIN project ON project.id_project = banya.project_id;

-- AVG() +
SELECT banya.owner, AVG(DATEDIFF(project.plan_end_date, project.plan_start_date)) OVER (PARTITION BY banya.owner) as avg_const_time 
FROM banya JOIN project ON project.id_project = banya.project_id;

-- MIN() +
SELECT materials.name_mater, specifications.name_spec, specifications.weight_kilo,
MIN(specifications.weight_kilo) OVER (PARTITION BY materials.name_mater) as min_weight
FROM materials JOIN specifications ON materials.specifications_id = specifications.id_specifications;

-- MAX() +
SELECT materials.name_mater, specifications.name_spec, materials.price_per_piece,
MAX(materials.price_per_piece) OVER (PARTITION BY materials.name_mater) as max_price
FROM materials JOIN specifications ON materials.specifications_id = specifications.id_specifications;

-- Ранжирующие функции

-- ROW_NUMBER()
-- RANK()
-- DENSE_RANK()
-- NTILE()

SELECT banya.owner, banya.address, banya.start_date_construction, banya.end_date_construction,
ROW_NUMBER() OVER (ORDER BY banya.end_date_construction) AS RowNumber,
RANK() OVER (ORDER BY banya.end_date_construction DESC) AS SalesRank,
DENSE_RANK() OVER (ORDER BY banya.end_date_construction DESC) AS DenseRank,
NTILE(4) OVER (ORDER BY banya.end_date_construction DESC) AS PriceGroup
FROM banya;

-- Функции смещения

-- LAG() и LEAD()
-- FIRST_VALUE() и LAST_VALUE()

SELECT banya.owner, project.plan_start_date, project.plan_end_date,
LAG(project.plan_start_date, 1) OVER (ORDER BY project.plan_start_date) AS prev_value,
LEAD(project.plan_start_date, 1) OVER (ORDER BY project.plan_start_date) AS next_value,
FIRST_VALUE(project.plan_start_date) OVER (ORDER BY project.plan_start_date) AS first_val,
LAST_VALUE(project.plan_start_date) OVER (ORDER BY project.plan_start_date) AS last_val
FROM banya JOIN project ON project.id_project = banya.project_id;
