"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df= df.dropna()

    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    # sexo (lower)
    # tipo_de_emprendimiento (lower)

    # idea_negocio
    df.idea_negocio= df.idea_negocio.str.replace("-"," ")
    df.idea_negocio= df.idea_negocio.str.replace("_"," ")

    # barrio
    df.barrio= df.barrio.str.replace("-"," ")
    df.barrio= df.barrio.str.replace("_"," ")

    # estrato
    df.estrato = df.estrato.astype(int)

    # comuna_ciudadano
    df.estrato = df.estrato.astype(int)

    # fecha_de_beneficio
    def fecha(texto):
        fecha= texto.split("/")
        if len(fecha[0])==4:
            texto= "/".join(reversed(fecha))
        return texto

    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(fecha)

    # monto_del_credito df.monto_del_credito = df.monto_del_credito.apply(lambda x: x.translate(str.maketrans('', '', ''.join(["$",","]))))
    df.monto_del_credito= df.monto_del_credito.str.replace("$","")
    df.monto_del_credito= df.monto_del_credito.str.replace(",","")
    df.monto_del_credito= df.monto_del_credito.str.replace(" ","")
    df.monto_del_credito= df.monto_del_credito.str.replace(".00","")

    # línea_credito
    df.línea_credito= df.línea_credito.str.replace("-"," ")
    df.línea_credito= df.línea_credito.str.replace("_"," ")

    df= df.drop_duplicates()
    df= df.drop_duplicates(subset=df.columns[1:])

    return df