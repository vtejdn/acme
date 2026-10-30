# Ejemplos de instrucciones

[Manual de usuario](<../Manual de usuario.md>)

Describa su objetivo en lenguaje natural.
Los ejemplos siguientes se agrupan en instrucciones de [configuración](#setup), [investigación](#research-instructions) y [administración](#administration-instructions).
Adapte la redacción a su pregunta, sus archivos y el alcance real del trabajo.

## <a id="setup"></a>Instrucciones de configuración

Utilice estos ejemplos para preparar su espacio de trabajo, registrar su identidad de autor y configurar los recursos locales.
Consulte la sección de [configuración](<../Manual de usuario.md#setup>) del manual para conocer el orden de los pasos de instalación y registro.

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Descargue [ACME](https://github.com/vtejdn/acme) en `D:\acme`. | Comprobar que el destino sea adecuado para la instalación, descargar los archivos del marco ACME, conservar el contenido existente e informar de la versión y de los pasos de configuración pendientes. |
| Instale [Git](../git-repository.md#notion-git). | Comprobar si Git ya está instalado, instalarlo si es necesario e informar de la versión disponible y de los pasos de configuración pendientes. |
| Registre Ali como mi clave de autor; utilice Alice como nombre completo. | Tras comprobar la clave y los registros existentes, utilizar los valores proporcionados: `Ali` como clave de autor y `Alice` como nombre para la atribución de `LICENSE`. Registrarle, añadir la atribución conservando las identidades y los avisos existentes, y asociar esta copia de trabajo con `Ali` si utiliza Git. |
| Explíqueme cómo conectarme a [GitHub](../git-repository.md#notion-github). | Explicar cómo iniciar sesión, autenticarse y conectarse a un repositorio remoto, indicando los pasos que debe completar personalmente. |
| Ya he iniciado sesión en GitHub. Compruebe la conexión. | Comprobar la cuenta autenticada y realizar pruebas de conexión de solo lectura para GitHub y el repositorio de destino. Informar del resultado o del error concreto. |
| [Clone](<../Manual de usuario.md#notion-clone>) [ACME](https://github.com/vtejdn/acme) en `D:\acme`. | Comprobar que Git, los permisos de acceso y el destino estén preparados, clonar el repositorio ACME con su historial de versiones e informar de la rama, la versión y los pasos de inicialización pendientes. |
| Utilice `nombre del repositorio` como nombre del repositorio. | Validar el nombre elegido y pedirle que elija otro si no es válido, en lugar de modificarlo automáticamente. Registrar el nombre aceptado en el marco y actualizar la presentación actual del nombre del repositorio y las referencias afectadas, conservando las claves de autor, las identidades de los materiales y los datos históricos de procedencia. |
| Configure Git y conéctelo a mi repositorio <https://github.com/alice/acme>. | Inicializar Git solo si es necesario, completar los registros pendientes del nombre del repositorio o del autor según sus elecciones y asociar la copia de trabajo con su clave de autor. Comprobar o configurar la identidad de los commits para que coincida con su registro, conectar el repositorio remoto indicado y probar el acceso mediante la cuenta o el canal de autenticación pertinente. Conservar los commits existentes, la configuración ajena al encargo y los límites de los Tasks, e informar del destino configurado y de los pasos de configuración pendientes. |
| Clone el repositorio de mi colaborador <https://github.com/alice/acme> y regístreme como Bob. | Clonar el repositorio compartido, registrarle como Bob y asociar la nueva copia de trabajo Git con Bob. Conservar los autores y los materiales de investigación existentes e informar de la configuración de identidad de los commits de Git. |

## <a id="research-instructions"></a>Instrucciones de investigación

Utilice estos ejemplos para trabajar con la literatura y explorar preguntas matemáticas.

### Buscar, registrar o revisar literatura

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Examine la fuente local abc26, regístrela y revísela. | Identificar la obra, la edición y el original local de abc26, y completar el registro bibliográfico y el de los archivos. Si el original tiene un índice de contenidos, preparar una copia que permita realizar búsquedas. Revisar el contenido matemático y registrar el alcance examinado, las conclusiones y las cuestiones sin resolver. |
| Revise el teorema 1.7 de abc26. | Localizar el teorema 1.7 en el original, comprobar su enunciado completo, sus hipótesis, su demostración y la aplicabilidad de las dependencias necesarias, y registrar los hallazgos, las partes no examinadas y las lagunas concretas. |
| Busque *On the construction of S* e intente registrarlo y revisarlo. | Identificar la obra y la edición, comprobar los registros existentes e intentar obtener el original. Registrar los datos bibliográficos y lo que se haya obtenido realmente. Si el original tiene un índice de contenidos, preparar una copia que permita realizar búsquedas. Revisar el contenido disponible e indicar las partes no disponibles. |
| ¿Cómo se utiliza esta definición en la literatura pertinente? | Consultar los registros de definiciones existentes y las fuentes originales pertinentes, comparar los objetos, las hipótesis, la notación y los usos, aportar citas precisas y distinguir las definiciones de las fuentes de las reformulaciones o generalizaciones locales. |

### <a id="start-or-continue-research"></a>Iniciar o continuar un [Task](<../Manual de usuario.md#material-task>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Establezca un Task en la línea W para la conjetura 1.3 de abc26. | Comprobar el enunciado original, las hipótesis y el alcance de la conjetura 1.3 y buscar primero un Task existente sobre la misma pregunta. Si hace falta uno nuevo, utilizar la [línea W](<../Manual de usuario.md#notion-research-line-letter>) e indicar la fuente, la pregunta exacta y los criterios de finalización. |
| Establezca un Task en la línea F con el objetivo «si P, entonces Q». | Precisar los objetos, las hipótesis y los cuantificadores de P y Q, crear un Task en la línea F con «P implica Q» como objetivo completo y establecer los criterios de finalización. |
| Cree un nuevo Task para generalizar la proposición P del caso de dimensión finita al de dimensión infinita. | Comprobar la proposición original, precisar los nuevos objetos, las hipótesis y la conclusión buscada, crear el Task y conservar la proposición original como un caso particular que la generalización deba abarcar. |
| Establezca un Task para encontrar una fórmula general en el marco P que incluya la fórmula (1) de abc26. | Comprobar las hipótesis y la notación de la fórmula original, precisar el marco P y el alcance de la fórmula general, y crear un Task cuyos criterios de finalización incluyan una derivación correcta y una explicación de cómo abarca la fórmula original. |
| Comience a trabajar en el Task F0001 hasta que quede un 5 % de la cuota semanal; después organice los resultados y haga una pausa. | Comprobar el estado actual del Task y sus condiciones de ejecución, y confirmar que pueda consultarse el uso semanal pertinente antes de continuar. Vigilar la cuota restante y detener el avance en el umbral del 5 %, organizar los resultados, las preguntas abiertas y un punto de continuación, y después hacer una pausa. |
| Continúe trabajando en el Task F0001. | Leer el objetivo actual, las estrategias, los resultados existentes y las condiciones de parada, y reanudar el trabajo dentro de la autorización actual y los límites que sigan vigentes. Si continúa aplicándose una condición de parada, explicar la razón concreta que impide continuar. |

### Objetivos compartidos

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Examine primero las vías de los colaboradores y después elija un enfoque útil para mi Task F0001. | Leer las vías pertinentes, los resultados reutilizables y los fracasos informativos, y elegir o adaptar su propia Strategy dentro del alcance de participación de F0001 y de las condiciones de ejecución existentes. Las vías distintas pueden reducir la repetición del trabajo; la verificación independiente, la replicación y la comprobación cruzada deliberadas siguen siendo apropiadas. |
| Establezca un Task conjunto para esta pregunta y vincúlelo al Task F0001. | Comprobar la pregunta compartida, las hipótesis, el alcance y los criterios de finalización, y establecer o reutilizar un Task conjunto adecuado; vincular su F0001 con la versión del contrato común que se haya adoptado realmente, precisar su alcance de participación y sus criterios individuales de finalización, y conservar las condiciones de ejecución existentes. La vinculación por sí sola no inicia la investigación. |


### Importación de contenido

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Importe el Task F0001 desde mi repositorio `〈URL del repositorio〉`. | Verificar el repositorio de origen y su identidad de autor, importar F0001 y sus dependencias matemáticas necesarias, y reutilizar los materiales locales existentes que sean adecuados; obtener las aportaciones necesarias de otros autores mediante Intake y conservar el vínculo al contrato conjunto o preparar un contrato autónomo completo, según corresponda. Conservar las condiciones de parada y las cuotas vigentes; la importación por sí sola no inicia la investigación. |
| Importe mis preferencias de redacción y el manuscrito F0001 desde mi repositorio `〈URL del repositorio〉`. | Importar las preferencias personales de redacción seleccionadas que sigan siendo aplicables, junto con los archivos fuente, las figuras, la bibliografía y el apoyo matemático necesario para el manuscrito F0001; conservar la autoría y el alcance de las preferencias, reutilizar los materiales locales existentes, reparar las referencias, realizar las comprobaciones de compilación necesarias e informar de las entradas que falten y de los problemas pendientes. |
| Reciba materiales relacionados con el Task A0001 de Alice desde `〈URL del repositorio〉`. | Verificar el repositorio de origen y la identidad de autor de Alice, seleccionar los resultados, argumentos, cálculos y revisiones relacionados con A0001 que sean necesarios para esta solicitud y reutilizar los materiales existentes adecuados; conservar la autoría original, las fuentes exactas, todo el contenido matemático necesario y las limitaciones reales de las revisiones, e informar de las entradas necesarias que no estén disponibles. Realizar la investigación posterior dentro de su propio Task y de su autorización. |

### Otras instrucciones habituales

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Considere construir un S mediante la teoría A; añada esta [estrategia](<../Manual de usuario.md#material-strategy>) al Task F0001. | Comprobar la aplicabilidad de la teoría A y registrar la construcción propuesta como estrategia de investigación para F0001. Indicar sus hipótesis, la función prevista, los pasos pendientes de verificación y la siguiente acción, y compararla con las estrategias existentes para evitar duplicaciones. |
| Incorpore la discusión anterior a las estrategias de F0001. | Identificar el enfoque discutido, actualizar una estrategia existente o crear una cuando sea necesario, conservar sus fundamentos, las preguntas abiertas y el siguiente paso, y asociarla con F0001. |
| Organice y registre la discusión anterior según las reglas del marco. | Conservar los enunciados y argumentos reutilizables, los hallazgos de exploración y la demás evidencia necesaria en los materiales adecuados, con sus hipótesis, fuentes y partes sin resolver. Reutilizar los registros existentes y reparar las referencias. |
| Informe del progreso actual de F0001. | Comprobar el estado actual del Task, distinguir los resultados demostrados, los argumentos propuestos, las observaciones computacionales y las preguntas abiertas, enlazar los materiales pertinentes y explicar qué falta para alcanzar el objetivo original. |
| Organice los resultados obtenidos hasta ahora y después haga una pausa. | Terminar la comprobación y la organización del trabajo de la ronda actual. Conservar los resultados útiles, los intentos fallidos, las preguntas pendientes y un punto de continuación utilizable; registrar la pausa y las condiciones que sigan vigentes, y después detener cualquier avance adicional. |

## <a id="administration-instructions"></a>Instrucciones de administración

Utilice estos ejemplos para las operaciones de Git, la configuración del entorno y el mantenimiento habitual.

### Commit y push

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Cree un [commit](<../Manual de usuario.md#notion-commit>) y haga [push](<../Manual de usuario.md#notion-push>). | Determinar el alcance de la entrega prevista y conservar los cambios ajenos ya preparados en el área de staging. Comprobar la identidad del autor de los cambios, la rama y el repositorio remoto de destino; confirmar la conexión, crear el commit y hacer push, e informar del alcance incluido en el commit y del resultado remoto. |
| Cree un commit y haga push de los cambios del directorio del manuscrito de F0001. | Localizar el proyecto de manuscrito de F0001, incluir en el commit solo los cambios del directorio indicado que deban guardarse en Git y conservar el resto del trabajo. Confirmar la identidad, el destino y la conexión antes de hacer push, e informar del alcance real. |
| Cree un commit de todos los cambios del espacio de trabajo. | Comprobar todos los cambios del espacio de trabajo y su autoría, crear un commit local del contenido que deba guardarse en Git, conservar los archivos excluidos por las reglas de exclusión e informar del alcance del commit y de los cambios restantes. |
| Cree un commit y haga push sin ninguna comprobación. | Omitir la revisión del contenido, las comprobaciones de formato, las pruebas y las exploraciones adicionales. Realizar solo las comprobaciones de alcance, identidad, destino y conexión necesarias para la entrega mediante Git; después crear el commit, hacer push e informar del resultado. |

### Pull y fusión

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Haga [pull](<../Manual de usuario.md#notion-pull>) de los últimos cambios remotos y [fusiónelos](<../Manual de usuario.md#notion-merge>) con la [rama local](<../Manual de usuario.md#notion-git-branch>). | Comprobar la rama actual y su repositorio remoto correspondiente, conservar el trabajo local, obtener y fusionar las actualizaciones remotas e informar del resultado. Ante conflictos que afecten al significado matemático, explicar las diferencias concretas y proponer cómo proceder. |

### Configuración del entorno

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Cree una unión de directorios (directory junction) desde [mathematics/literature/pdf](../../mathematics/literature/pdf) hacia `D:\MyLiterature`. | Comprobar la ruta del proyecto y el directorio de destino, conservar las fuentes existentes, crear la unión de directorios hacia la carpeta indicada y confirmar que los archivos fuente estén excluidos de Git. |
| Establezca en 512k la [longitud del contexto](<../Manual de usuario.md#notion-context-length>) predeterminada de `<nombre del entorno de ejecución>` para este proyecto. | Identificar la configuración del [entorno de ejecución](../agent-harness.md) de este proyecto, confirmar que el modelo y el entorno admitan la longitud solicitada y actualizar el valor predeterminado del proyecto. Explicar cómo entra en vigor el cambio y si se ha verificado su aplicación real; indicar el límite efectivo si la configuración solicitada no está admitida. |
| Establezca mi condición de parada predeterminada para los Tasks: hacer una pausa cuando quede un 5 % de la cuota semanal. | Registrar esta condición como preferencia personal de ejecución predeterminada, aplicable cuando no tenga prioridad una configuración más específica. Conservar las condiciones vigentes de los Tasks existentes y explicar cómo puede consultarse el uso semanal pertinente. |

### Mantenimiento habitual

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Desactive las comprobaciones automáticas de la versión del marco para este repositorio. | Desactivar la comprobación diaria de metadatos de versión de este repositorio, conservando el marco actual y el trabajo de investigación. |
| Active las comprobaciones automáticas de la versión del marco para este repositorio. | Activar la comprobación diaria del repositorio; cualquier actualización posterior sigue requiriendo su solicitud explícita. |
| Actualice el marco a la última versión. | Comprobar la versión instalada y la última versión oficial, determinar la versión de destino y su fuente fijada, y seguir las notas de actualización para tratar los archivos afectados y las migraciones de materiales necesarias, conservando los cambios locales, los materiales de investigación, la configuración personal y las condiciones de ejecución vigentes de los Tasks. Actualizar la versión instalada después de completar las comprobaciones necesarias e informar de las versiones anterior y posterior, del commit de destino y de los problemas pendientes. |
| Resuelva los conflictos de fusión según las reglas del marco. | Examinar el contenido en conflicto, su autoría y los materiales afectados, y resolver directamente los conflictos administrativos dentro de las facultades existentes. Ante desacuerdos matemáticos de fondo, conservar la evidencia de ambas partes, explicar las diferencias y realizar una nueva comprobación de alcance delimitado con la autorización existente o tras obtener la autorización necesaria; conservar las correcciones del cuerpo del texto de otro autor en los materiales propios de quien realiza la corrección. Comprobar el resultado de la fusión y las referencias afectadas, e informar del resultado y de las cuestiones que aún requieran su decisión. |
| Examine los archivos de `.tmp` y elimine los que puedan borrarse sin riesgo. | Comprobar la finalidad de los archivos y si se están utilizando. Conservar primero cualquier contenido necesario que aún no esté guardado en los materiales de investigación y después eliminar los archivos que se hayan confirmado como prescindibles y que no utilicen otras sesiones activas. |

## Redacción de manuscritos

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |

## Formalización en Lean

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
