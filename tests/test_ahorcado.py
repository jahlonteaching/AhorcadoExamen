import inspect
import pytest

import ahorcado.modelo.ahorcado

from dataclasses import is_dataclass, fields

module_members = [item[0] for item in inspect.getmembers(ahorcado.modelo.ahorcado)]

palabra_defined = 'Palabra' in module_members
ahorcado_defined = 'Ahorcado' in module_members


if palabra_defined:
    from ahorcado.modelo.ahorcado import Palabra

if ahorcado_defined:
    from ahorcado.modelo.ahorcado import Ahorcado


ahorcado_is_dataclass = ahorcado_defined and is_dataclass(Ahorcado)


@pytest.fixture(scope="session")
def proveedor_palabras_mock():
    class ProveedorPalabrasMock:
        def proveer_palabra(self) -> str:
            return "palabra"

    return ProveedorPalabrasMock()


@pytest.fixture(scope="session")
def palabra_objetivo():
    return Palabra("palabra")


@pytest.fixture(scope="session")
def ahorcado(proveedor_palabras_mock, palabra_objetivo):
    return Ahorcado(proveedor_palabras=proveedor_palabras_mock, palabra_objetivo=palabra_objetivo)


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
@pytest.mark.parametrize("metodo", [
    "__init__", "contiene_letra", "posiciones_letra", "agregar_letra", "esta_completa", "__str__"
])
def test_clase_palabra_contiene_metodos_esperados(metodo):
    assert metodo in Palabra.__dict__


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
@pytest.mark.parametrize("metodo", [
    "generar_texto", "iniciar_juego", "letra_usada", "agregar_letra", "palabra_completa", "tiene_intentos_disponibles"
])
def test_clase_ahorcado_contiene_metodos_esperados(metodo):
    assert metodo in Ahorcado.__dict__


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_clase_ahorcado_es_dataclass():
    assert is_dataclass(Ahorcado)


@pytest.mark.xfail(not ahorcado_is_dataclass, reason="required class not defined")
@pytest.mark.parametrize("atributo", [
    "intentos", "letras_usadas", "proveedor_palabras", "palabra_objetivo"
])
def test_clase_ahorcado_define_atributos_de_dataclass(atributo):
    assert atributo in [f.name for f in fields(Ahorcado)]


@pytest.mark.xfail(not ahorcado_is_dataclass, reason="required class not defined")
@pytest.mark.parametrize("atributo", [
    "intentos", "letras_usadas"
])
def test_atributos_de_clase_ahorcado_no_se_inicializan_en_constructor(atributo):
    assert atributo in [f.name for f in fields(Ahorcado) if f.init is False]


@pytest.mark.xfail(not ahorcado_is_dataclass, reason="required class not defined")
@pytest.mark.parametrize("atributo", [
    "proveedor_palabras", "palabra_objetivo"
])
def test_atributo_de_clase_ahorcado_son_inicializados_en_constructor(atributo):
    assert atributo in [f.name for f in fields(Ahorcado) if f.init is True]


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
@pytest.mark.parametrize("atributo", [
    "texto", "letras"
])
def test_clase_palabra_contiene_atributos(palabra_objetivo, atributo):
    assert hasattr(palabra_objetivo, atributo)


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
def test_palabra_inicializa_letras_con_letra_vacia(palabra_objetivo):
    assert palabra_objetivo.letras == ['_' for _ in palabra_objetivo.texto]


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
def test_metodo_contiene_letra_devuelve_true_si_letra_esta_en_texto(palabra_objetivo):
    assert palabra_objetivo.contiene_letra('p') is True


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
def test_metodo_posiciones_letra_devuelve_lista_con_posiciones_de_letra_en_texto(palabra_objetivo):
    assert palabra_objetivo.posiciones_letra('a') == [1, 3, 6]


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
def test_metodo_agregar_letra_agrega_letra_en_posicion(palabra_objetivo):
    palabra_objetivo.agregar_letra('a', 1)
    assert palabra_objetivo.letras == ['_', 'a', '_', '_', '_', '_', '_']


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
def test_metodo_esta_completa_devuelve_true_si_todas_las_letras_estan_completas(palabra_objetivo):
    palabra_objetivo.letras = ['p', 'a', 'l', 'a', 'b', 'r', 'a']
    assert palabra_objetivo.esta_completa() is True


@pytest.mark.xfail(not palabra_defined, reason="required class not defined")
def test_metodo_str_devuelve_texto_con_letras_separadas_por_espacio(palabra_objetivo):
    palabra_objetivo.letras = ['p', 'a', 'l', 'a', 'b', 'r', 'a']
    assert str(palabra_objetivo) == 'p a l a b r a'


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_generar_texto_devuelve_texto(ahorcado):
    assert ahorcado.generar_texto() == "palabra"


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_iniciar_juego_reinicia_letras_usadas(ahorcado):
    ahorcado.letras_usadas = ['a', 'b', 'c']
    ahorcado.iniciar_juego()
    assert ahorcado.letras_usadas == []


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_iniciar_juego_reinicia_intentos(ahorcado):
    ahorcado.intentos = 3
    ahorcado.iniciar_juego()
    assert ahorcado.intentos == 0


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_iniciar_juego_genera_nueva_palabra_objetivo(ahorcado):
    ahorcado.iniciar_juego()
    assert ahorcado.palabra_objetivo.texto == "palabra"


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_letra_usada_devuelve_true_si_letra_esta_en_letras_usadas(ahorcado):
    ahorcado.letras_usadas = ['a', 'b', 'c']
    assert ahorcado.letra_usada('a') is True


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_agregar_letra_agregar_letras_en_posiciones_correctas(ahorcado):
    ahorcado.palabra_objetivo.letras = ['_', '_', '_', '_', '_', '_', '_']
    ahorcado.palabra_objetivo.texto = "palabra"
    ahorcado.agregar_letra('a')
    assert ahorcado.palabra_objetivo.letras == ['_', 'a', '_', 'a', '_', '_', 'a']


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_agregar_letra_retona_true_si_letra_esta_en_palabra_objetivo(ahorcado):
    assert ahorcado.agregar_letra('a') is True


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_agregar_letra_retorna_false_si_letra_no_esta_en_palabra_objetivo(ahorcado):
    assert ahorcado.agregar_letra('z') is False


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_agregar_letra_aumenta_intentos_si_letra_no_esta_en_palabra_objetivo(ahorcado):
    ahorcado.iniciar_juego()
    ahorcado.agregar_letra('z')
    assert ahorcado.intentos == 1


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_palabra_completa_devuelve_true_si_palabra_objetivo_esta_completa(ahorcado):
    ahorcado.palabra_objetivo.letras = ['p', 'a', 'l', 'a', 'b', 'r', 'a']
    assert ahorcado.palabra_completa() is True


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_palabra_completa_devuelve_false_si_palabra_objetivo_no_esta_completa(ahorcado):
    ahorcado.palabra_objetivo.letras = ['p', 'a', 'l', 'a', 'b', '_', 'a']
    assert ahorcado.palabra_completa() is False


@pytest.mark.xfail(not ahorcado_defined, reason="required class not defined")
def test_metodo_tiene_intentos_disponibles_devuelve_true_si_intentos_es_menor_a_7(ahorcado):
    ahorcado.intentos = 6
    assert ahorcado.tiene_intentos_disponibles() is True