#!/bin/bash

# Определить переменные
results=./results
rep_history=./final-report/history
report=./final-report

# Удалить старые результаты
rm -rf $results

# Запустить тесты
pytest --alluredir=$results

# Перенести историю в результаты
mv $rep_history $results/history

# Удалить старый отчет
rm -rf $report

# Сгенерировать отчет с сохранением истории
allure generate $results -o $report --history $results/history

# Открыть отчет
allure open $report