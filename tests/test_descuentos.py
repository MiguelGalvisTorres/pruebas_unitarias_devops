from src.descuentos import (
    aplicar_descuento, calcular_descuento, calcular_precio_final,
    descuento_por_volumen, descuento_cumulativo, descuento_apilado
)

def test_aplicar_descuento_valido():
    # Arrange
    precio, porcentaje = 100, 20
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 80.0

def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -50, 10
    # Act & Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        aplicar_descuento(precio, porcentaje)

def test_aplicar_descuento_porcentaje_invalido_lanza_error():
    # Arrange
    precio, porcentaje = 100, 110
    # Act & Assert
    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        aplicar_descuento(precio, porcentaje)

def test_calcular_descuento_valido():
    # Arrange
    precio, porcentaje = 200, 15
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 30.0

def test_calcular_descuento_precio_negativo_lanza_error():
    # Arrange
    precio, porcentaje = -10, 15
    # Act & Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        calcular_descuento(precio, porcentaje)

def test_calcular_descuento_porcentaje_invalido_lanza_error():
    # Arrange
    precio, porcentaje = 100, -5
    # Act & Assert
    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        calcular_descuento(precio, porcentaje)

def test_calcular_precio_final_impuesto_sobre_precio_descontado():
    """Revela BUG 1 de descuentos: el impuesto se calcula sobre el precio original y no sobre el descontado."""
    # Arrange
    precio, impuesto, descuento = 100, 19, 10
    # Precio con descuento = 90. Impuesto (19% de 90) = 17.1. Total esperado = 107.1
    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    # Assert
    assert resultado == pytest.approx(107.1)

def test_calcular_precio_final_precio_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = -100, 19, 10
    # Act & Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        calcular_precio_final(precio, impuesto, descuento)

def test_calcular_precio_final_impuesto_negativo_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, -5, 10
    # Act & Assert
    with pytest.raises(ValueError, match="El impuesto no puede ser negativo"):
        calcular_precio_final(precio, impuesto, descuento)

def test_calcular_precio_final_descuento_invalido_lanza_error():
    # Arrange
    precio, impuesto, descuento = 100, 19, 120
    # Act & Assert
    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio_final(precio, impuesto, descuento)

def test_descuento_por_volumen_sin_descuento():
    # Arrange
    cantidad, precio_unitario = 5, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 50.0

def test_descuento_por_volumen_10_unidades():
    # Arrange
    cantidad, precio_unitario = 10, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 95.0

def test_descuento_por_volumen_20_unidades():
    # Arrange
    cantidad, precio_unitario = 20, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 180.0

def test_descuento_por_volumen_50_unidades():
    # Arrange
    cantidad, precio_unitario = 50, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 425.0

def test_descuento_por_volumen_100_unidades():
    # Arrange
    cantidad, precio_unitario = 100, 10
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 800.0

def test_descuento_por_volumen_cantidad_negativa_lanza_error():
    # Arrange
    cantidad, precio_unitario = -1, 10
    # Act & Assert
    with pytest.raises(ValueError, match="La cantidad no puede ser negativa"):
        descuento_por_volumen(cantidad, precio_unitario)

def test_descuento_por_volumen_precio_negativo_lanza_error():
    # Arrange
    cantidad, precio_unitario = 10, -5
    # Act & Assert
    with pytest.raises(ValueError, match="El precio unitario no puede ser negativo"):
        descuento_por_volumen(cantidad, precio_unitario)

def test_descuento_cumulativo_valido():
    # Arrange
    precio, descuentos = 100, [10, 20]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 72.0

def test_descuento_cumulativo_lista_vacia():
    # Arrange
    precio, descuentos = 100, []
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 100

def test_descuento_cumulativo_error_validaciones():
    # Arrange
    precio_negativo = -50
    descuentos_invalidos = [10, 150]
    # Act & Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(precio_negativo, [10])
    with pytest.raises(ValueError):
        descuento_cumulativo(100, descuentos_invalidos)

def test_descuento_apilado_excede_100_se_limita_a_cero():
    """Revela BUG 2 de descuentos: cuando la suma de descuentos supera 100%, lanza ValueError en vez de topar en 100% (precio 0)."""
    # Arrange
    precio, descuentos = 100, [60, 50]
    # Act
    resultado = descuento_apilado(precio, descuentos)
    # Assert
    assert resultado == 0.0

def test_descuento_apilado_casos_borde():
    # Arrange
    precio = 100
    # Act & Assert
    assert descuento_apilado(precio, []) == 100
    assert descuento_apilado(precio, [20, 30]) == 50.0
    with pytest.raises(ValueError):
        descuento_apilado(-10, [10])