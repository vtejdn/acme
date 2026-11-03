# Ejemplos de instrucciones

[Manual de usuario](<../Manual de usuario.md>)

Describa su objetivo en lenguaje natural.
Los ejemplos siguientes se agrupan en instrucciones de [configuración](#setup), [investigación](#research-instructions), [administración](#administration-instructions), [redacción de manuscritos](#writing-instructions) y [formalización en Lean](#lean-instructions).
Adapte la redacción a su pregunta, sus archivos y el alcance real del trabajo.

## <a id="setup"></a>Instrucciones de configuración

Utilice estos ejemplos para preparar su espacio de trabajo, registrar su identidad de autor y configurar los recursos locales.
Consulte la sección de [configuración](<../Manual de usuario.md#setup>) del manual para conocer el orden de los pasos de instalación y registro.

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Descargue e instale ACME (https://github.com/vtejdn/acme) en `D:\my-math-repository`. | Comprobar el contenido existente del directorio indicado e integrar los archivos del marco de la versión oficial seleccionada en la raíz real del proyecto, conservando el contenido existente y el historial de Git, sin incorporar los metadatos Git del repositorio oficial. Reutilizar la información existente del proyecto y del autor, completar la configuración necesaria, verificar la versión del marco y los puntos de entrada en la raíz del proyecto e informar de la ubicación real de la instalación, la versión y el trabajo pendiente. |
| Instale [Git](../git-repository.md#notion-git). | Comprobar si Git ya está instalado, instalarlo si es necesario e informar de la versión disponible y de los pasos de configuración pendientes. |
| Registre Ali como mi clave de autor; utilice Alice como nombre completo. | Tras comprobar la clave y los registros existentes, utilizar los valores proporcionados: `Ali` como clave de autor y `Alice` como nombre para la atribución de `LICENSE`. Registrarle, añadir la atribución conservando las identidades y los avisos existentes, y asociar esta copia de trabajo con `Ali` si utiliza Git. |
| Explíqueme cómo conectarme a [GitHub](../git-repository.md#notion-github). | Explicar cómo iniciar sesión, autenticarse y conectarse a un repositorio remoto, indicando los pasos que debe completar personalmente. |
| Ya he iniciado sesión en GitHub. Compruebe la conexión. | Comprobar la cuenta autenticada y realizar pruebas de conexión de solo lectura para GitHub y el repositorio de destino. Informar del resultado o del error concreto. |
| Establezca la clave del repositorio en `〈clave del repositorio〉`. | Validar la clave elegida, registrar un valor válido y actualizar las referencias actuales afectadas; pedirle otra elección si no es válida. La clave del repositorio es independiente de la abreviatura, el nombre completo y el título del README del proyecto; conservar el significado de las claves de autor, las identidades de los materiales y los datos históricos de procedencia. |
| Establezca la abreviatura y el nombre completo del repositorio en `〈abreviatura〉` y `〈nombre completo〉`. | Registrar la abreviatura y el nombre completo del proyecto elegidos por separado, comprobando que ambos sean texto no vacío de una sola línea. Utilizarlos para formar el encabezado principal del README «〈abreviatura〉: 〈nombre completo〉», mantener la coherencia entre la configuración y el título y conservar el resto del texto. La clave del repositorio se establece por separado. |
| Configure Git y conéctelo a mi repositorio <https://github.com/alice/acme>. | Inicializar Git solo si es necesario, completar los registros pendientes del nombre del repositorio o del autor según sus elecciones y asociar la copia de trabajo con su clave de autor. Comprobar o configurar la identidad de los commits para que coincida con su registro, conectar el repositorio remoto indicado y probar el acceso mediante la cuenta o el canal de autenticación pertinente. Conservar los commits existentes, la configuración ajena al encargo y los límites de los Tasks, e informar del destino configurado y de los pasos de configuración pendientes. |
| [Clone](<../Manual de usuario.md#notion-clone>) el repositorio de mi colaborador <https://github.com/alice/acme> y regístreme como Bob. | Clonar el repositorio compartido y comprobar la clave de autor `Bob`, su identidad real y los registros existentes. En un primer registro, preguntar antes por el nombre de atribución de `LICENSE` elegido de forma independiente y después registrar al autor y añadir el aviso necesario. Reutilizar una identidad existente aplicable, asociar la nueva copia de trabajo Git con la clave verificada, conservar los autores y materiales de investigación existentes y explicar la configuración de identidad de los commits de Git. |

## <a id="research-instructions"></a>Instrucciones de investigación

Utilice estos ejemplos para trabajar con la literatura y explorar preguntas matemáticas.

### Buscar, registrar o revisar literatura

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Examine la fuente local abc26, regístrela y revísela. | Identificar la obra, la edición y el original local de abc26, completar la bibliografía y mantener, cuando sea necesario, las notas de edición y ubicación del original. Si el original tiene un índice de contenidos, preparar una copia que permita realizar búsquedas. Revisar el contenido matemático y registrar el alcance examinado, las conclusiones y las cuestiones sin resolver. |
| Revise el teorema 1.7 de abc26. | Localizar el teorema 1.7 en el original, comprobar su enunciado completo, sus hipótesis, su demostración y la aplicabilidad de las dependencias necesarias, y registrar los hallazgos, las partes no examinadas y las lagunas concretas. |
| Busque *On the construction of S* e intente registrarlo y revisarlo. | Identificar la obra y la edición, consultar los materiales existentes e intentar obtener el original; completar la bibliografía y mantener, cuando sea necesario, notas sobre la edición obtenida y la ubicación de la fuente. Si el original tiene un índice de contenidos, preparar una copia que permita realizar búsquedas. Revisar el contenido obtenido e informar de los fallos de adquisición, las partes no disponibles y el alcance realmente examinado. |
| ¿Cómo se utiliza esta definición en la literatura pertinente? | Consultar los registros de definiciones existentes y las fuentes originales pertinentes, comparar los objetos, las hipótesis, la notación y los usos, aportar citas precisas y distinguir las definiciones de las fuentes de las reformulaciones o generalizaciones locales. |

### <a id="start-or-continue-research"></a>[Task](<../Manual de usuario.md#material-task>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Establezca un Task en la [línea W](<../Manual de usuario.md#notion-research-line-letter>) para la conjetura 1.3 de abc26. | Comprobar el enunciado original, las hipótesis y el alcance de la conjetura 1.3 y buscar primero un Task existente sobre la misma pregunta. Si hace falta uno nuevo, utilizar la línea W e indicar la fuente, la pregunta exacta y los criterios de finalización. |
| Establezca un Task en la línea F con el objetivo «si P, entonces Q». | Precisar los objetos, las hipótesis y los cuantificadores de P y Q, crear un Task en la línea F con «P implica Q» como objetivo completo y establecer los criterios de finalización. |
| Cree un nuevo Task para generalizar la proposición P del caso de dimensión finita al de dimensión infinita. | Comprobar la proposición original, precisar los nuevos objetos, las hipótesis y la conclusión buscada, crear el Task y conservar la proposición original como un caso particular que la generalización deba abarcar. |
| Establezca un Task para encontrar una fórmula general en el marco P que incluya la fórmula (1) de abc26. | Comprobar las hipótesis y la notación de la fórmula original, precisar el marco P y el alcance de la fórmula general, y crear un Task cuyos criterios de finalización incluyan una derivación correcta y una explicación de cómo abarca la fórmula original. |
| Comience a trabajar en el Task F0001 hasta que quede un 5 % de la cuota semanal. | Comprobar el estado actual del Task y sus condiciones de ejecución vigentes, y confirmar que pueda consultarse el uso semanal de la cuenta pertinente; de lo contrario, explicar la limitación y aplazar el avance. Avanzar cuando se cumplan las condiciones de ejecución, vigilar la cuota restante y detenerse en la primera observación de un resto igual o inferior al 5 % o de un fallo de seguimiento. Conservar los resultados útiles, las preguntas abiertas y un punto de continuación, y registrar las condiciones de parada vigentes. |
| Organice los resultados obtenidos hasta ahora y después haga una pausa. | Terminar la comprobación y la organización del trabajo de la ronda actual. Conservar los resultados útiles, los intentos fallidos, las preguntas pendientes y un punto de continuación utilizable; registrar la pausa y las condiciones que sigan vigentes, y después detener cualquier avance adicional. |
| Informe del progreso actual de F0001. | Comprobar el estado actual del Task, distinguir los resultados demostrados, los argumentos propuestos, las observaciones computacionales y las preguntas abiertas, enlazar los materiales pertinentes y explicar qué falta para alcanzar el objetivo original. |
| Continúe trabajando en el Task F0001. | Leer el objetivo actual, las estrategias, los resultados existentes y las condiciones de parada, y reanudar el trabajo dentro de la autorización actual y los límites que sigan vigentes. Si continúa aplicándose una condición de parada, explicar la razón concreta que impide continuar. |

### [Estrategias](<../Manual de usuario.md#material-strategy>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Considere construir un S mediante la teoría A; añada esta estrategia al [Task](<../Manual de usuario.md#material-task>) F0001. | Comprobar la aplicabilidad de la teoría A y registrar la construcción propuesta como estrategia de investigación para F0001. Indicar sus hipótesis, la función prevista, los pasos pendientes de verificación y la siguiente acción, y compararla con las estrategias existentes para evitar duplicaciones. |
| Incorpore la discusión anterior a las estrategias de F0001. | Identificar el enfoque discutido, actualizar una estrategia existente o crear una cuando sea necesario, conservar sus fundamentos, las preguntas abiertas y el siguiente paso, y asociarla con F0001. |
| Busque y analice enfoques para el Task G0001, proponga estrategias y establezca sus prioridades de forma autónoma. | Leer el objetivo de G0001, sus restricciones, las estrategias existentes y los materiales pertinentes, reutilizar primero los resultados locales y después buscar y revisar literatura según sea necesario. Comparar las condiciones de aplicación, los fundamentos, los obstáculos y los recursos necesarios de las vías candidatas, proponer estrategias y priorizarlas de forma autónoma; registrar los motivos del orden, los pasos sin resolver y la siguiente acción, conservando el objetivo original, los criterios de finalización y los límites de ejecución vigentes. |

### [Tasks conjuntos](<../Manual de usuario.md#material-task>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Examine primero las vías de la colaboradora Alice y después elija un enfoque útil para mi Task F0001. | Leer las vías pertinentes, los resultados reutilizables y los fracasos informativos, y elegir o adaptar su propia Strategy dentro del alcance de participación de F0001 y de las condiciones de ejecución existentes. Las vías distintas pueden reducir la repetición del trabajo; la verificación independiente, la replicación y la comprobación cruzada deliberadas siguen siendo apropiadas. |
| Establezca un Task conjunto para esta pregunta y vincúlelo al Task F0001. | Comprobar la pregunta compartida, las hipótesis, el alcance y los criterios de finalización, y establecer o reutilizar un Task conjunto adecuado; vincular su F0001 con la versión del contrato común que se haya adoptado realmente, precisar su alcance de participación y sus criterios individuales de finalización, y conservar las condiciones de ejecución existentes. La vinculación por sí sola no inicia la investigación. |

### [Enunciados matemáticos](<../Manual de usuario.md#material-claim>) y [Registros de exploración](<../Manual de usuario.md#material-ledger>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Organice y registre la discusión anterior según las reglas del marco. | Conservar los enunciados y argumentos reutilizables, los hallazgos de exploración y la demás evidencia necesaria en los materiales adecuados, con sus hipótesis, fuentes y partes sin resolver. Reutilizar los registros existentes y reparar las referencias. |

## <a id="administration-instructions"></a>Instrucciones de administración

Utilice estos ejemplos para las operaciones de [Git](../git-repository.md#notion-git), la configuración del entorno y el mantenimiento habitual.

### [Commit](<../Manual de usuario.md#notion-commit>) y [push](<../Manual de usuario.md#notion-push>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Cree un commit y haga push. | Determinar el alcance de la entrega prevista y conservar los cambios ajenos ya preparados en el área de staging. Comprobar la identidad del autor de los cambios, la rama y el repositorio remoto de destino; confirmar la conexión, crear el commit y hacer push, e informar del alcance incluido en el commit y del resultado remoto. |
| Cree un commit y haga push de los cambios del directorio del manuscrito de F0001. | Localizar el proyecto de manuscrito de F0001, incluir en el commit solo los cambios del directorio indicado que deban guardarse en Git y conservar el resto del trabajo. Confirmar la identidad, el destino y la conexión antes de hacer push, e informar del alcance real. |
| Cree un commit de todos los cambios del espacio de trabajo. | Comprobar todos los cambios del espacio de trabajo y su autoría, crear un commit local del contenido que deba guardarse en Git, conservar los archivos excluidos por las reglas de exclusión e informar del alcance del commit y de los cambios restantes. |
| Cree un commit y haga push sin ninguna comprobación. | Omitir la revisión del contenido, las comprobaciones de formato, las pruebas y las exploraciones adicionales. Realizar solo las comprobaciones de alcance, identidad, destino y conexión necesarias para la entrega mediante Git; después crear el commit, hacer push e informar del resultado. |

### [Pull](<../Manual de usuario.md#notion-pull>) y [fusión](<../Manual de usuario.md#notion-merge>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Obtenga los últimos cambios remotos y fusiónelos con la [rama local](<../Manual de usuario.md#notion-git-branch>). | Comprobar la rama actual y su repositorio remoto correspondiente, conservar el trabajo local, obtener y fusionar las actualizaciones remotas e informar del resultado. Ante conflictos que afecten al significado matemático, explicar las diferencias concretas y proponer cómo proceder. |

### Configuración del entorno

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Cree una unión de directorios (directory junction) desde [mathematics/literature/pdf](../../mathematics/literature/pdf) hacia `D:\MyLiterature`. | Comprobar la ruta del proyecto y el directorio de destino, conservar las fuentes existentes, crear la unión de directorios hacia la carpeta indicada y confirmar que los archivos fuente estén excluidos de Git. |
| Establezca en 512k la [longitud del contexto](<../Manual de usuario.md#notion-context-length>) predeterminada de `<nombre del entorno de ejecución>` para este proyecto. | Identificar la configuración del [entorno de ejecución](../agent-harness.md) de este proyecto, confirmar que el modelo y el entorno admitan la longitud solicitada y actualizar el valor predeterminado del proyecto. Explicar cómo entra en vigor el cambio y si se ha verificado su aplicación real; indicar el límite efectivo si la configuración solicitada no está admitida. |
| Establezca mi condición de parada predeterminada para los Tasks: hacer una pausa cuando quede un 5 % de la cuota semanal. | Registrar esta condición como preferencia personal de ejecución predeterminada, aplicable cuando no tenga prioridad una configuración más específica. Conservar las condiciones vigentes de los Tasks existentes y explicar cómo puede consultarse el uso semanal pertinente. |

### [Importación](<../Manual de usuario.md#notion-import>) y [recepción](<../Manual de usuario.md#notion-intake>)

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Importe el Task F0001 desde mi repositorio `〈URL del repositorio〉`. | Verificar el repositorio de origen y su identidad de autor, importar F0001 y sus dependencias matemáticas necesarias, y reutilizar los materiales locales existentes que sean adecuados; obtener las aportaciones necesarias de otros autores mediante Intake y conservar el vínculo al contrato conjunto o preparar un contrato autónomo completo, según corresponda. Conservar las condiciones de parada y las cuotas vigentes; la importación por sí sola no inicia la investigación. |
| Importe mis preferencias de redacción y el manuscrito F0001 desde mi repositorio `〈URL del repositorio〉`. | Importar las preferencias personales de redacción seleccionadas que sigan siendo aplicables, junto con los archivos fuente, las figuras, la bibliografía y el apoyo matemático necesario para el manuscrito F0001; conservar la autoría y el alcance de las preferencias, reutilizar los materiales locales existentes, reparar las referencias, realizar las comprobaciones de compilación necesarias e informar de las entradas que falten y de los problemas pendientes. |
| Reciba materiales relacionados con el Task A0001 de Alice desde `〈URL del repositorio〉`. | Verificar el repositorio de origen y la identidad de autor de Alice, seleccionar los resultados, argumentos, cálculos y revisiones relacionados con A0001 que sean necesarios para esta solicitud y reutilizar los materiales existentes adecuados; conservar la autoría original, las fuentes exactas, todo el contenido matemático necesario y las limitaciones reales de las revisiones, e informar de las entradas necesarias que no estén disponibles. Realizar la investigación posterior dentro de su propio Task y de su autorización. |

### Mantenimiento habitual

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |
| Active/desactive las comprobaciones automáticas de la versión del marco para este repositorio. | Actualizar la opción de este repositorio según su elección de activar o desactivar las comprobaciones, conservar el resto de la configuración e informar del ajuste actual; cuando estén activadas, aplicar las reglas de comprobación automática por día UTC. Una actualización sigue requiriendo una autorización explícita efectiva. |
| Actualice el marco a la última versión. | Comprobar la versión instalada y la última versión oficial; si hay una actualización, fijar la versión y el commit de destino, adaptar los archivos afectados según las notas de actualización y realizar las comprobaciones necesarias, conservando los cambios locales, los materiales de investigación, las preferencias personales y las condiciones de ejecución vigentes. Actualizar la versión instalada tras superar las comprobaciones; en un repositorio Git realmente compartido entre varios autores, crear el commit, hacer push y confirmar el resultado remoto con la autorización predeterminada, respetando las restricciones explícitas de trabajo local, sin conexión o sin push. Informar de las versiones anterior y posterior, del commit de destino, de las comprobaciones y la entrega, así como de la ausencia de actualizaciones o de tareas pendientes. |
| Resuelva los conflictos de fusión según las reglas del marco. | Examinar los cambios de ambas partes, la autoría y las facultades reales, y resolver directamente los conflictos administrativos cuya solución pueda determinarse, incluidas las correcciones de localización que conserven el objeto y el significado matemático. Ante desacuerdos matemáticos de fondo, conservar la evidencia de ambas partes, explicar las diferencias y efectuar una nueva comprobación delimitada con la autorización existente o tras obtener la necesaria; conservar las correcciones sustantivas del contenido de otro autor en los materiales propios de quien las realiza. Comprobar el resultado de la fusión y las referencias afectadas, e informar del resultado y de las cuestiones pendientes. |
| Examine los archivos de `.tmp` y elimine los que puedan borrarse sin riesgo. | Comprobar la finalidad de los archivos y si se están utilizando. Conservar primero cualquier contenido necesario que aún no esté guardado en los materiales de investigación y después eliminar los archivos que se hayan confirmado como prescindibles y que no utilicen otras sesiones activas. |
| Compruebe si los materiales matemáticos locales cumplen las reglas del marco. | Dentro del alcance solicitado, encargar a un agente aislado de las fases de reparación y aceptación que examine por lotes y en modo de solo lectura los materiales matemáticos locales y las entradas y referencias necesarias, comprobando autoría, versiones, evaluaciones, fuentes, correspondencias entre revisiones y materiales revisados, y demás requisitos aplicables. Registrar los problemas de conformidad en `maintenance` y los problemas matemáticos de fondo en `erratum`, e informar de la cobertura real, el alcance no examinado y las cuestiones pendientes. |
| Consulte maintenance y erratum y repare los problemas según las reglas del marco. | Leer los puntos pendientes de reparación dentro del alcance solicitado; un agente que cumpla el aislamiento entre fases verifica los problemas, repara dentro de las facultades reales sobre los materiales del autor, realiza autocomprobaciones y revisa los materiales dependientes necesarios. Someter las reparaciones de conformidad a aceptación independiente y aplicar a los errores matemáticos los requisitos reales de versión, evaluación y revisión matemática; conservar el problema original, sus fundamentos, los requisitos de aceptación y los puntos sin reparar o sin aceptar, e informar del alcance reparado y de las limitaciones restantes. |
| Acepte las reparaciones de materiales según las reglas del marco. | Encargar a un agente independiente que no haya participado en la inspección o reparación del mismo alcance ni heredado las discusiones sustantivas relacionadas que compruebe las reparaciones presentadas y los materiales dependientes necesarios frente a los problemas originales y las reglas actuales, e informe del alcance aceptado o rechazado. Retirar de las listas de pendientes solo las partes aceptadas dentro de las facultades reales de resolución del autor correspondiente o de la parte receptora, conservando los puntos fallidos, no aceptados, fuera del alcance y añadidos simultáneamente; durante la aceptación no se reparan materiales, y la aceptación de conformidad no equivale a revisión matemática independiente. |

## <a id="writing-instructions"></a>Redacción de manuscritos

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |

## <a id="lean-instructions"></a>Formalización en Lean

| Ejemplo de instrucción | Acciones esperadas del agente |
| --- | --- |

