# Informe
Para el laboratorio se pidió desarrollar un programa que permita construya un índice invertido y permita la recuperación de documentos a través de consultas. El resultado fue implementado en Python.
## Preprocesamiento
Para asegurar la obtención de palabras significativas es necesario primero filtrar las palabras con el menor valor, para esto se usó la lista de palabras "stoplist.txt" como referencia, además de unas adiciones de símbolos que se vieron como necesarias. Se ha usado la librería _nltk_ para poder dividir todas las palabras del texto en palabras singulares para aplicar un formato estándar. Dentro del formato estándar todas las palabras deben encontrarse en minúsculas además de ser solo la raíz de la palabra, que se encuentra con la ayuda _SnowballStemmer_. La lectura de todas las palabra es guardada en una lista junto con las incidencias de la palabra en los archivos y el nombre de los archivos donde incide. La lista tiene el nombre _listaRecurrente_.
## Construcción del índice invertido
Para delimitar la _listaRecurrente_ es necesario primero ordenar de manera descendiente la lista a partir del número de incidencias, esto con el fin de asegurarnos de usar las palabras más relevantes. Una vez delimitada la lista la volvemos a ordenar en orden alfabético ya que facilita la búsqueda de una consulta. Todos los elementos de la lista (menos el número de incidencia) se guardan en el archivo del índice con el formato preestablecido.
## Consultas booleanas
- L(word): Le da el formato estándar a la palabra que recibe por parámetro y  la itera línea por línea del índice hasta encontrar la palabra respectiva, llegar al fin del archivo o encontrar una palabra alfabéticamente mayor. Si encuentra la palabra en el índice devuelve una lista con el nombre de todos los archivos donde se encuentra.
- AND(List,List): Python facilita las operaciones lineares entre listas así que se aplica y devuelve una lista con los nombres de documentos en los cuales aparezcan ambas listas de las palabras.
- OR(List,List): Mismo caso pero con la operación OR.
- AND-OR(List,List): Mismo caso pero con la operación AND-OR.
## Resultados
- AND_NOT( L(viejo) , L(voluntad) ):
Resultado: ['libro1.txt']
- AND_NOT(AND(L(acaba),L(asiste)),L(ayuda)):
Resultado: ['libro4.txt']
- AND(OR(L(acaba),L(asiste)),L(ayuda)):
Resultado: ['libro3.txt', 'libro5.txt', 'libro6.txt', 'libro4.txt', 'libro1.txt']
