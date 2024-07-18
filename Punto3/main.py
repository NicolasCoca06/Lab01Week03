import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

few_shot_promt = """Contexto: Necesitamos identificar el tono de los siguientes correos electrónicos.

Ejemplo 1:
Correo: "Querido cliente, lamentamos informarle que su pedido ha sido retrasado."
Tono: Formal

Ejemplo 2:
Correo: "¡Hola! Solo quería decirte que tu pedido ya está en camino."
Tono: Informal

Correo a clasificar: "Estimado señor, le informamos que su solicitud ha sido procesada con éxito."
Tono: """

CoT_promt = """Pregunta: Si tienes 3 manzanas y luego compras 4 más, ¿cuántas manzanas tienes en total?

Razonamiento:
Primero, tienes 3 manzanas.
Luego, compras 4 manzanas adicionales.
Para encontrar el total, sumamos las manzanas iniciales y las compradas: 3 + 4.
Respuesta: """

Chain_Promt = """Prompt 1: Describe los ingredientes necesarios para hacer una pizza margarita.
Respuesta 1: Masa de pizza, salsa de tomate, queso mozzarella, albahaca, aceite de oliva.

Prompt 2: Describe el proceso para hacer la masa de pizza.
Respuesta 2: Mezclar harina, agua, levadura, y sal. Amasar la mezcla hasta obtener una masa homogénea. Dejar reposar hasta que duplique su tamaño.

Prompt 3: Describe cómo preparar la pizza margarita utilizando los ingredientes y la masa."""

Self_Consistency_Prompt = """"Pregunta: ¿Qué es la fotosíntesis?

Generación 1: La fotosíntesis es el proceso por el cual las plantas utilizan la luz solar para convertir el dióxido de carbono y el agua en glucosa y oxígeno.

Generación 2: La fotosíntesis es un proceso en el cual las plantas, utilizando luz solar, convierten el dióxido de carbono y el agua en alimentos y oxígeno.

Generación 3: La fotosíntesis es el proceso mediante el cual las plantas transforman el dióxido de carbono y el agua en glucosa y oxígeno, usando la energía de la luz solar.

Selección de la respuesta final: La fotosíntesis es el proceso por el cual las plantas utilizan la luz solar para convertir el dióxido de carbono y el agua en glucosa y oxígeno."""


promts_dictionary = {
    "few_shot": few_shot_promt,
    "CoT": CoT_promt,
    "Chain": Chain_Promt,
    "Self_Consistency": Self_Consistency_Prompt
}	
for promt in promts_dictionary:
    print("Tipo de promt: ", promt)
    print("El Promt es: ", promts_dictionary[promt])
    response = model.generate_content(promts_dictionary[promt])
    print("La respuesta es: ", response.text)


