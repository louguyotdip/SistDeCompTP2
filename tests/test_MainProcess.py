from MainProcess import value_get,get_country,filter_and_fill,get_values_po, button_position

# Testea si se pudieron obtener los datos o si hubo algun error. 200 es si anduvo bien
def test_value_get():
    assert value_get().status_code == 200

# Testea si el pais elegido para ver los indices GINI es argentina
def test_get_country():
    assert get_country() == "Argentina"

# Testea si la posicion que se calcula del boton es un numero mayor a 0
def test_button_position():
    assert button_position() > 0

# Testea si el tamaño de la lista de indice GINI es mayor a 0
def test_pre_post_c_function():
    assert len(get_values_po()) > 0 
