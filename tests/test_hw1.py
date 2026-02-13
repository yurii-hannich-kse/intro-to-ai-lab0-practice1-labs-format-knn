import pytest
import numpy as np
from grader_utils import load_notebook_functions

# Шлях до ноутбука, який завантажуємо
hw = load_notebook_functions("homework1.ipynb")

def test_data_processing():
    """Тест завдання 1: Спліт даних (2 бали)"""
    assert hasattr(hw, 'data_processing'), "Функція data_processing не знайдена!"
    # Викликаємо функцію студента
    res = hw.data_processing(test_size=0.2, val_size=0.2)
    assert len(res) == 6, "Функція має повертати 6 об'єктів (X_train, X_val, ...)"
    # Перевірка розмірності тест-сету для Iris (150 * 0.2 = 30)
    assert len(res[2]) == 30, "Неправильний розмір X_test"

def test_find_best_k():
    """Тест завдання 2: Пошук K (3 бали)"""
    assert hasattr(hw, 'find_best_k'), "Функція find_best_k не знайдена!"
    # Тест на простих даних
    X = np.array([[1], [2], [10], [11]])
    y = np.array([0, 0, 1, 1])
    k = hw.find_best_k(X, y, X, y, 3)
    assert k == 1, f"Для ідентичних даних k має бути 1, отримано {k}"