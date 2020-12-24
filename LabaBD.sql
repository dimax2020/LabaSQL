-- phpMyAdmin SQL Dump
-- version 4.9.7deb1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Дек 24 2020 г., 23:17
-- Версия сервера: 8.0.22
-- Версия PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Laba`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Вклады`
--

CREATE TABLE `Вклады` (
  `dep_id` int NOT NULL,
  `client_id` int NOT NULL,
  `Сумма вклада` int NOT NULL,
  `Процентная ставка` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `Вклады`
--

INSERT INTO `Вклады` (`dep_id`, `client_id`, `Сумма вклада`, `Процентная ставка`) VALUES
(5, 10, 1000, 6),
(6, 10, 10000, 14),
(7, 11, 5000, 10),
(8, 12, 9999, 14);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `Вклады`
--
ALTER TABLE `Вклады`
  ADD PRIMARY KEY (`dep_id`,`client_id`),
  ADD KEY `fk_table2_Клиенты_idx` (`client_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `Вклады`
--
ALTER TABLE `Вклады`
  MODIFY `dep_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `Вклады`
--
ALTER TABLE `Вклады`
  ADD CONSTRAINT `fk_table2_Клиенты` FOREIGN KEY (`client_id`) REFERENCES `Клиенты` (`client_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
