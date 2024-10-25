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
date_end DATETIME NOT NULL,
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
date_work DATETIME NOT NULL,
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
(10, 'Магазин "СтройГрад"', 'г. Москва, ул. Тихая, д. 5');

-- 2
INSERT INTO architect (service_number, fio, work_exp, contacts) VALUES
(1, 'Ким Кирилл Сергеевич', 2, 'noobmaster6969@ya.ru'),
(2, 'Чистяков Тимофей Александрович', 4, 'qwerty123@example.com'),
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
(10, 'ИП "Лес и Дерево"');

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
(4, 'Кровельные материалы', 2.0, 1.0, 25.0),
(5, 'Изоляция', 1.0, 0.5, 5.0),
(6, 'Окна пластиковые', 1.2, 1.5, 10.0),
(7, 'Двери деревянные', 2.0, 0.8, 12.0),
(8, 'Системы отопления', 1.5, 1.5, 8.0),
(9, 'Трубы пластиковые', 6.0, 0.1, 2.0),
(10, 'Кровельные системы', 3.0, 2.0, 35.0);

-- 7
INSERT INTO project (id_project, date_end, square, price, draw_id_draw, architect_service_number) VALUES 
(1, '2023-12-01 00:00:00', 50, 300000.00, 1, 1),
(2, '2024-01-15 00:00:00', 70, 450000.00, 2, 2),
(3, '2024-02-20 00:00:00', 100, 600000.00, 3, 3),
(4, '2024-03-25 00:00:00', 80, 500000.00, 4, 4),
(5, '2024-04-30 00:00:00', 90, 550000.00, 5, 5),
(6, '2024-05-15 00:00:00', 60, 350000.00, 6, 6),
(7, '2024-06-20 00:00:00', 75, 400000.00, 7, 7),
(8, '2024-07-25 00:00:00', 85, 480000.00, 8, 8),
(9, '2024-08-30 00:00:00', 95, 620000.00, 9, 9),
(10, '2024-09-10 00:00:00', 55, 320000.00, 10, 10);

-- 8
INSERT INTO banya (id, owner, address, start_date_construction, project_id) VALUES 
(1, 'Сидоров Сидор Сидорович', 'г. Москва, ул. Садовая, д. 10', '2023-10-01 00:00:00', 1),
(2, 'Кузнецов Кузьма Кузьмич', 'г. Москва, ул. Цветочная, д. 5', '2023-11-01 00:00:00', 2),
(3, 'Петрова Анна Петровна', 'г. Москва, ул. Набережная, д. 15', '2023-09-15 00:00:00', 3),
(4, 'Смирнов Сергей Сергеевич', 'г. Москва, ул. Зелёная, д. 20', '2023-08-10 00:00:00', 4),
(5, 'Федоров Федор Федорович', 'г. Москва, ул. Осенняя, д. 25', '2023-07-05 00:00:00', 5),
(6, 'Григорьев Григорий Григорьевич', 'г. Москва, ул. Летняя, д. 30', '2023-06-01 00:00:00', 6),
(7, 'Тихонов Тимофей Тимофеевич', 'г. Москва, ул. Зимняя, д. 35', '2023-05-15 00:00:00', 7),
(8, 'Марков Марк Маркович', 'г. Москва, ул. Весенняя, д. 40', '2023-04-20 00:00:00', 8),
(9, 'Алексеев Алексей Алексеевич', 'г. Москва, ул. Природная, д. 45', '2023-03-25 00:00:00', 9),
(10, 'Иванова Ирина Ивановна', 'г. Москва, ул. Небесная, д.50', '2023-02-28 00:00:00', 10);

-- 9
INSERT INTO materials (id_mater, name_mater, type, price_per_piece, specifications_id, manufacturers_id) VALUES 
(1, 'Доска обрезная', 'Дерево', 150.00, 1, 1),
(2, 'Брус клееный', 'Дерево', 500.00, 2, 2),
(3, 'Фундаментный блок', 'Бетон', 1000.00, 3, 3),
(4, 'Кровельный материал', 'Металл', 2000.00, 4, 4),
(5, 'Изоляция минеральная', 'Минеральные материалы', 3000.00, 5, 5),
(6, 'Окно пластиковое', 'Пластик', 1500, 6, 6),
(7, 'Дверь деревянная', 'Дерево', 2000, 7, 7),
(8, 'Труба пластиковая', 'Пластик', 500, 8, 8),
(9, 'Система отопления', 'Металл', 10000, 9, 9),
(10, 'Кровельные системы', 'Металл', 1500, 10, 10);

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
(4, 1), 
(4, 2), 
(5, 3), 
(5, 4), 
(6, 5), 
(7, 6), 
(7, 7), 
(8, 8), 
(9, 9), 
(10, 10);

-- 11
INSERT INTO checks (banya_id, materials_id, date_purchase, quantity) VALUES 
(1, 1, '2023-10-02', 20), 
(1, 2, '2023-10-03', 15), 
(1, 3, '2023-10-04', 10), 
(2, 4, '2023-11-04', 25), 
(2, 5, '2023-11-05', 30), 
(3, 6, '2023-09-21', 12), 
(3, 7, '2023-09-22', 8), 
(4, 8, '2023-08-11', 20), 
(5, 9, '2023-07-06', 18), 
(6, 10, '2023-06-02', 22);

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
(10, 'Петрова Анна Петровна', 3, 'petrova@example.com', 35000, 3);


-- 13
INSERT INTO contract (ban_id, service_number, link_if, date_work) VALUES 
(1, 1, 'https://example.com/contract1.pdf', '2023-10-05'), 
(2, 2, 'https://example.com/contract2.pdf', '2023-11-10'), 
(3, 3, 'https://example.com/contract3.pdf', '2023-09-25'), 
(4, 4, 'https://example.com/contract4.pdf', '2023-08-15'), 
(5, 5, 'https://example.com/contract5.pdf', '2023-07-20'), 
(6, 6, 'https://example.com/contract6.pdf', '2023-06-18'), 
(7, 7, 'https://example.com/contract7.pdf', '2023-05-14'), 
(8, 8, 'https://example.com/contract8.pdf', '2023-04-22'), 
(9, 9, 'https://example.com/contract9.pdf', '2023-03-30'), 
(10, 10, 'https://example.com/contract10.pdf', '2023-02-28');


SELECT * FROM architect;

-- Практическая работа №2

SELECT fio FROM architect;

SELECT fio, contacts FROM builders;

SELECT * FROM materials ORDER BY price_per_piece; -- DESC

SELECT * FROM architect WHERE work_exp=4;

SELECT * FROM architect WHERE work_exp>4;

SELECT * FROM architect WHERE work_exp<4;

SELECT * FROM architect WHERE work_exp>=4;

SELECT * FROM architect WHERE work_exp<=4;

SELECT * FROM architect WHERE work_exp!=4;

SELECT * FROM architect WHERE service_number IS NOT NULL;

SELECT * FROM architect WHERE service_number IS NULL;

SELECT * FROM builders WHERE work_exp BETWEEN 4 AND 8;

SELECT * FROM builders WHERE service_number IN (1, 4);

SELECT * FROM builders WHERE service_number NOT IN (1, 4);

SELECT * FROM shops WHERE address LIKE 'МКАД%';

SELECT * FROM shops WHERE address NOT LIKE 'МКАД%';

SELECT * FROM shops WHERE address LIKE '%Москва%';

ALTER TABLE builders ADD COLUMN rating FLOAT(10) AFTER work_exp; -- от 0 до 5

UPDATE builders SET rating=3.4
WHERE service_number=1;

UPDATE builders SET rating=4.7
WHERE service_number=2;

UPDATE builders SET rating=2.7
WHERE service_number=3;

UPDATE builders SET rating=1.0
WHERE service_number=4;

UPDATE builders SET rating=5.0
WHERE service_number=5;

UPDATE builders SET rating=4.6
WHERE service_number=6;

UPDATE builders SET rating=5.0
WHERE service_number=7;

UPDATE builders SET rating=0.8
WHERE service_number=8;

UPDATE builders SET rating=4.1
WHERE service_number=9;

UPDATE builders SET rating=3.8
WHERE service_number=10;

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

-- Операция пересечения +
SELECT 
    s.name_shop AS shop_name,
    s.address AS shop_address,
    m.name_mater AS material_name,
    m.price_per_piece AS material_price
FROM 
    shops s
JOIN 
    list l ON s.id_store = l.store_id
JOIN 
    materials m ON l.mater_id = m.id_mater
WHERE 
    m.type = 'Дерево' -- ищем строительные материалы
ORDER BY 
    s.name_shop;  -- Сортировка по имени магазина


-- Операция разности +
SELECT builders.FIO, builders.work_exp FROM builders
WHERE NOT EXISTS
(SELECT architect.FIO, architect.work_exp FROM architect
WHERE architect.FIO=builders.FIO AND architect.work_exp=builders.work_exp);


-- Операция группировки +
SELECT type, COUNT(*) as cnt FROM builders
WHERE type = 'Пластик' 
GROUP BY type;

-- или

SELECT profession_id, AVG(revenue) as cnt FROM builders
WHERE profession_id = 1
GROUP BY profession_id;

-- Операция сортировки +
SELECT * FROM builders 
INNER JOIN profession on builders.service_number = profession.id_prof
WHERE builders.rating > 0.5 OR builders.work_exp > 2
GROUP BY builders.service_number ORDER BY builders.rating;

-- Операция деления +
-- DROP VIEW IF EXISTS T1;
-- DROP VIEW IF EXISTS T2;
-- DROP VIEW IF EXISTS TT;

SELECT m.name_mater FROM materials m
WHERE NOT EXISTS (
    SELECT * 
    FROM shops s
    WHERE NOT EXISTS (
        SELECT * FROM list l
        WHERE l.store_id = s.id_store AND l.mater_id = m.id_mater
        )
    );

-- Хранимые процедуры, функции и триггеры

-- Процедуры

-- 1. Добавление нового архитектора
CREATE PROCEDURE AddArchitect (
    IN p_fio VARCHAR(255),
    IN p_work_exp INT,
    IN p_contacts TEXT
)
BEGIN
    INSERT INTO architect (fio, work_exp, contacts) VALUES (p_fio, p_work_exp, p_contacts);
END;
   
-- 2. Получение информации о проекте по ID
CREATE PROCEDURE GetProjectById (
    IN p_project_id INT
)
BEGIN
    SELECT * FROM project WHERE id_project = p_project_id;
END;
   
-- 3. Добавление нового материала в магазин
CREATE PROCEDURE AddMaterialToShop (
    IN p_name_mater VARCHAR(255),
    IN p_type VARCHAR(255),
    IN p_price_per_piece FLOAT,
    IN p_specifications_id INT,
    IN p_manufacturers_id INT
)
BEGIN
    INSERT INTO materials (name_mater, type, price_per_piece, specifications_id, manufacturers_id)
    VALUES (p_name_mater, p_type, p_price_per_piece, p_specifications_id, p_manufacturers_id);
END;
   
-- 4. Обновление статуса строительства бани
CREATE PROCEDURE UpdateBanyaConstructionStatus (
    IN p_banya_id INT,
    IN p_new_status VARCHAR(255)
)
BEGIN
    UPDATE banya SET status = p_new_status WHERE id = p_banya_id;
END;
   
-- 5. Добавление новой записи о покупке материалов
CREATE PROCEDURE AddMaterialPurchase (
    IN p_banya_id INT,
    IN p_materials_id INT,
    IN p_date_purchase DATETIME,
    IN p_quantity INT
)
BEGIN
    INSERT INTO checks (banya_id, materials_id, date_purchase, quantity)
    VALUES (p_banya_id, p_materials_id, p_date_purchase, p_quantity);
END;
   
-- Функции

-- 1. Получение стоимости строительства бани по проекту
CREATE FUNCTION GetConstructionCost (p_project_id INT) RETURNS FLOAT
BEGIN
    DECLARE total_cost FLOAT;
    SELECT SUM(price) INTO total_cost FROM materials 
    JOIN checks ON materials.id_mater = checks.materials_id 
    JOIN banya ON checks.banya_id = banya.id 
    WHERE banya.project_id = p_project_id;
       
    RETURN total_cost;
END;
   


-- 2. Подсчет количества материалов по типу
CREATE FUNCTION CountMaterialsByType (p_type VARCHAR(255)) RETURNS INT
BEGIN
    DECLARE material_count INT;
    SELECT COUNT(*) INTO material_count FROM materials WHERE type = p_type;
       
    RETURN material_count;
END;
   


-- 3. Получение списка всех архитекторов с опытом работы более N лет
CREATE FUNCTION GetArchitectsWithExperience (p_years INT) RETURNS TABLE
BEGIN
    RETURN (SELECT * FROM architect WHERE work_exp > p_years);
END;
   


-- 4. Получение информации о магазине по ID
CREATE FUNCTION GetShopById (p_shop_id INT) RETURNS TABLE
BEGIN
    RETURN (SELECT * FROM shops WHERE id_store = p_shop_id);
END;
   


-- 5. Проверка наличия материала в магазине
CREATE FUNCTION IsMaterialAvailable (p_material_id INT) RETURNS BOOLEAN
BEGIN
    DECLARE available BOOLEAN;
    SELECT COUNT(*) > 0 INTO available FROM list WHERE mater_id = p_material_id;
       
    RETURN available;
END;
   


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
   

-- Практическая работа №4





