import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, promedio, maximo, minimo,
    calcular_area_rectangulo, calcular_perimetro_rectangulo
)

def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_restar_numeros():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 6

def test_multiplicar_numeros():
    # Arrange
    a, b = 6, 7
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 42

def test_dividir_numeros_validos():
    # Arrange
    a, b = 10, 2
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 5.0

def test_dividir_por_cero_lanza_error():
    # Arrange
    a, b = 10, 0
    # Act & Assert
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(a, b)

def test_potencia_enteros():
    # Arrange
    base, exponente = 2, 3
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 8

def test_raiz_cuadrada_positiva():
    # Arrange
    numero = 16
    # Act
    resultado = raiz_cuadrada(numero)
    # Assert
    assert resultado == 4.0

def test_raiz_cuadrada_negativa_lanza_error():
    """Revela BUG 1 de calculadora: no lanza ValueError con números negativos."""
    # Arrange
    numero = -9
    # Act & Assert
    with pytest.raises(ValueError, match="No se puede calcular la raíz cuadrada de un número negativo"):
        raiz_cuadrada(numero)

def test_promedio_lista_valida():
    # Arrange
    lista = [10, 20, 30]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 20.0

def test_promedio_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        promedio(lista)

def test_maximo_lista_valida():
    # Arrange
    lista = [3, 15, 7, 2]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 15

def test_maximo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        maximo(lista)

def test_minimo_lista_positivos():
    """Revela BUG 2 de calculadora: min_val inicia en 0 en vez de lista[0]."""
    # Arrange
    lista = [5, 8, 12, 3]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 3

def test_minimo_lista_con_negativos():
    # Arrange
    lista = [4, -2, 9, -7]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == -7

def test_minimo_lista_vacia_lanza_error():
    # Arrange
    lista = []
    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        minimo(lista)

def test_calcular_area_rectangulo_valido():
    # Arrange
    base, altura = 5, 4
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 20

def test_calcular_area_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = -5, 4
    # Act & Assert
    with pytest.raises(ValueError, match="La base y altura deben ser positivas"):
        calcular_area_rectangulo(base, altura)

def test_calcular_perimetro_rectangulo_valido():
    # Arrange
    base, altura = 5, 4
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 18

def test_calcular_perimetro_rectangulo_negativo_lanza_error():
    # Arrange
    base, altura = 5, -4
    # Act & Assert
    with pytest.raises(ValueError, match="La base y altura deben ser positivas"):
        calcular_perimetro_rectangulo(base, altura)