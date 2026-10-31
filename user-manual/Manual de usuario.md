# Manual de usuario

[Ejemplos de instrucciones](<user-instructions/Ejemplos de instrucciones.md>) · [Ejemplo de declaración de asistencia de IA](ai-disclosure-example.md) · [Ejemplo de página de publicación](publication-example.md) · [Ejemplos de repositorios](https://github.com/vtejdn/acme/discussions/1)

## ACME: Autonomous and Collaborative Mathematical Exploration

ACME es un marco ligero para la investigación matemática autónoma y colaborativa.
Combina reglas en Markdown para [agentes de IA](#notion-agent) con scripts auxiliares para apoyar la exploración sostenida y conservar investigaciones que puedan examinarse, reutilizarse y continuarse.
Tiene dos objetivos principales: permitir que agentes de IA autónomos realicen investigación matemática bajo la orientación de matemáticos humanos y facilitar la colaboración entre autores humanos.

### Matemáticos humanos

Los matemáticos humanos son responsables de:

1. Definir las preguntas de investigación, su alcance autorizado y los criterios de finalización para iniciar [tareas de investigación (Task)](#material-task).
2. Orientar el desarrollo de [estrategias de investigación (Strategy)](#material-strategy) junto con los [agentes](#notion-agent).
3. Aportar ideas, aclarar la intención matemática, establecer prioridades científicas, cuestionar argumentos, precisar preguntas y reorientar las investigaciones.
4. Comprender los resultados de la investigación y explorar las fronteras del conocimiento matemático.
5. Asumir la responsabilidad de los resultados matemáticos.

### Agentes basados en [LLM](#notion-llm)

Dentro del alcance autorizado, los [agentes](#notion-agent) autónomos son responsables de:

1. Estudiar la literatura y verificar los resultados necesarios para la investigación.
2. Desarrollar y evaluar [estrategias de investigación](#material-strategy), identificar lagunas y tomar de forma autónoma decisiones metodológicas habituales dentro del encargo.
3. Explorar preguntas abiertas y aclarar el alcance y las limitaciones de los resultados que van surgiendo.
4. Buscar demostraciones y contraejemplos para preguntas concretas y ejecutar cálculos reproducibles para obtener observaciones, evidencia e ideas.
5. Conservar hipótesis, argumentos, evidencia, dependencias, enfoques fallidos útiles, preguntas sin resolver y la historia sustancial de la investigación en los materiales adecuados, incluidos los [Claims](#material-claim) y los [Ledgers](#material-ledger).
6. Organizar [revisiones](#material-review) independientes cuando sea necesario y registrar su alcance, hallazgos y limitaciones.
7. Preparar y revisar manuscritos de acuerdo con los criterios generales de redacción matemática y las preferencias del autor responsable.

### Colaboración

Los matemáticos pueden [colaborar](#joint-task) mediante un [repositorio Git](git-repository.md#notion-git-repository) compartido, intercambiar materiales de investigación y reutilizar los resultados de los demás.
El repositorio puede alojarse en una plataforma como [GitHub](git-repository.md#notion-github), de modo que los colaboradores trabajen en sus propios equipos y sincronicen los cambios.
Véase el [diagrama de colaboración mediante un repositorio Git](git-repo.png).

Distintos matemáticos o equipos también pueden colaborar entre repositorios recibiendo materiales seleccionados mediante [Intake](#notion-intake); véase el [diagrama de colaboración entre repositorios](collaboration.jpg).

### Flujo de trabajo

La investigación comienza con un [Task](#material-task) definido por una persona y con criterios de finalización explícitos.
Los [agentes](#notion-agent) primero consultan y reutilizan los materiales de investigación y la literatura locales pertinentes, y después buscan fuentes adicionales en la Web cuando es necesario.
Comprueban la aplicabilidad de los resultados, desarrollan [estrategias](#material-strategy) e iteran entre intentos de demostración, cálculos y búsquedas de contraejemplos.
Cada intento informa el siguiente: los hallazgos útiles, los fracasos y las preguntas sin resolver se conservan en los materiales de investigación adecuados, incluidos los [Claims](#material-claim) y los [Ledgers](#material-ledger).
Las estrategias se adaptan dentro del objetivo autorizado.
Los resultados propuestos se someten a [revisión](#material-review) matemática y la finalización del Task se evalúa según los criterios originales.

Véase el [diagrama del flujo de trabajo](workflow.jpg).

## <a id="setup"></a>Configuración

Para un nuevo proyecto de investigación, siga los pasos I–III que se indican a continuación.
Si se incorpora a una colaboración existente, [prepare su espacio de trabajo](#setup-workplace) y después siga los [pasos para incorporarse a la colaboración](#setup-collaboration).

### Paso I. Elegir [LLM](#notion-llm) con capacidad suficiente

Compare el rendimiento de los LLM en tareas matemáticas de nivel de investigación.
Utilice [FrontierMath Tier 4](https://epoch.ai/frontiermath/tiers-1-4?tier=Tier+4+%28v2%29&view=graph&tab=leaderboard), [MathArena](https://matharena.ai/models), [Riemann-bench](https://surgehq.ai/benchmarks/riemann-bench) y otras evaluaciones pertinentes como puntos de referencia.
Elija modelos para la investigación matemática y las tareas administrativas teniendo en cuenta si son de código abierto, su accesibilidad y su coste.

### <a id="setup-workplace"></a>Paso II. Preparar el espacio de trabajo

Para la investigación individual en un solo equipo, utilice un [entorno de ejecución de agentes](agent-harness.md) adecuado con acceso a un [LLM](#notion-llm) con capacidad suficiente.

1. Instale un entorno de ejecución de agentes, como aplicación independiente o dentro de un [IDE](agent-harness.md#notion-ide), e inicie sesión si es necesario o lo desea.
2. Elija una carpeta en su equipo para guardar el marco y los futuros materiales de investigación.
3. Seleccione el modelo y el proveedor en la configuración o en el selector de modelos.

Sin [Git](git-repository.md#notion-git), la opción predeterminada es la investigación personal en su propio equipo.
Para sincronizar el trabajo entre equipos o colaborar mediante un [repositorio Git](git-repository.md#notion-git-repository) compartido, puede elegir una plataforma de alojamiento como [GitHub](git-repository.md#notion-github).
Subir los registros de investigación y hacer público un repositorio son decisiones distintas.

4. (Opcional) Instale Git en su equipo o pida a un [agente](#notion-agent) del entorno elegido que lo haga.
5. (Opcional) Cree una cuenta de alojamiento de repositorios o inicie sesión y, a continuación, conéctese a un repositorio existente o cree uno nuevo.

- Véanse también las [instrucciones de configuración](<user-instructions/Ejemplos de instrucciones.md#setup>).

### Paso III. Instalar e inicializar el marco

Si se incorpora a un repositorio de investigación existente que ya contiene ACME, siga los pasos de la sección siguiente.

1. Pida a un [agente](#notion-agent) que descargue el [marco ACME](https://github.com/vtejdn/acme) en la carpeta de su proyecto o que [clone](#notion-clone) su repositorio si utiliza [Git](git-repository.md#notion-git).
2. Elija una clave de autor única, como `Alice` o `Ali`, y elija de forma independiente el nombre que figurará en la atribución de `LICENSE`.
   Pida a un agente que le registre como autor y añada esa atribución.
   En un espacio de trabajo Git, pida al agente que asocie esta copia de trabajo con su clave de autor para que los nuevos registros tengan la autoría correcta.
3. (Si utiliza Git) Configure el nombre y el correo electrónico asociados a sus [commits](#notion-commit), o pida a un agente que lo haga.
4. (Si utiliza Git) Elija o confirme un nombre corto para su [repositorio](git-repository.md#notion-git-repository) de investigación y pida a un agente que compruebe que está registrado correctamente en el marco.
5. (Opcional) Cuando resulte apropiado, recomendamos encarecidamente compartir sus registros de investigación mediante un repositorio público.

- Véanse también las [instrucciones de configuración](<user-instructions/Ejemplos de instrucciones.md#setup>).

### <a id="setup-collaboration"></a>Incorporarse a un [repositorio Git](git-repository.md#notion-git-repository) existente como colaborador

1. Inicie sesión en la plataforma de alojamiento del repositorio y acepte la invitación de su coautor.
2. Pida a un [agente](#notion-agent) que le ayude a configurar el acceso al repositorio compartido.
3. Proporcione la dirección del repositorio a un agente y pídale que lo [clone](#notion-clone) en una nueva carpeta local.
   Abra esa carpeta en su entorno de ejecución de agentes.
4. Si aún no está registrado en el repositorio de investigación, elija una clave de autor distinta de las de sus colaboradores y elija de forma independiente el nombre que figurará en la atribución de `LICENSE`,
   y después pida a un agente que le registre y añada esa atribución.
   Pida al agente que asocie esta copia de trabajo con su clave de autor en ACME.
5. Configure el nombre y el correo electrónico utilizados en sus [commits](#notion-commit) de [Git](git-repository.md#notion-git), o pida a un agente que lo haga.

- Véanse también las [instrucciones de configuración](<user-instructions/Ejemplos de instrucciones.md#setup>).

## Primeros pasos

### Iniciar un [Task](#material-task)

1. (Opcional) Proporcione literatura pertinente o pida a un [agente](#notion-agent) que la busque.
   Pida al agente que guarde los archivos fuente en [el directorio local de literatura](../mathematics/literature/pdf) y revise las partes indicadas de los artículos pertinentes con la profundidad solicitada.
2. Establezca un Task mediante la discusión con los agentes, especificando las preguntas, restricciones y criterios de finalización.
   Puede elegir una [letra de línea de investigación](#notion-research-line-letter) para organizar el Task y sus materiales relacionados.
3. Para el trabajo autónomo sostenido, especifique o adopte límites de ejecución y condiciones de parada.
4. Autorice las acciones necesarias de las herramientas cuando se le solicite y responda a las preguntas de los agentes.
5. Reflexione sobre los materiales matemáticos producidos por los agentes y compréndalos; ningún agente puede hacerlo por usted.
   Discuta las matemáticas con los agentes para profundizar y acelerar su comprensión.
   Pida referencias pertinentes y cuestione de forma socrática las fuentes de los argumentos y las ideas, especialmente cuando un argumento se base en el conocimiento del modelo sin respaldo explícito de fuentes.
6. (Opcional, si utiliza [Git](git-repository.md#notion-git)) Cree [commits](#notion-commit) de los cambios que desee conservar; deshaga las ediciones locales o revierta commits cuando corresponda.

- Véanse también los [ejemplos de instrucciones de investigación](<user-instructions/Ejemplos de instrucciones.md#research-instructions>).

### <a id="joint-task"></a>Iniciar un [Task](#material-task) conjunto

Los colaboradores de un mismo repositorio pueden establecer un Task conjunto para un objetivo matemático común, definiendo la pregunta compartida, las hipótesis, el alcance y los criterios de finalización; cada participante avanza en su investigación mediante su propio Task.

1. Pida a un [agente](#notion-agent) que establezca un Task conjunto; si un colaborador ya ha establecido uno adecuado, puede pasar directamente al siguiente paso.
2. Pida al agente que establezca o reutilice su Task individual, lo vincule al Task conjunto que usted y sus colaboradores hayan acordado adoptar y precise su alcance de participación y sus criterios personales de finalización.
   El Task individual puede abarcar toda la pregunta común o parte de ella; sus criterios de finalización pueden coincidir con los del Task conjunto o determinarse según el alcance de su participación.
   Los participantes también pueden repartirse el trabajo sobre la misma pregunta: una persona intenta encontrar una demostración y otra busca un contraejemplo.
   Se recomienda elegir, de acuerdo con los colaboradores, distintas [estrategias de investigación (Strategy)](#material-strategy) para reducir la repetición del trabajo matemático y aprovechar mejor los recursos computacionales de IA.
   Para la verificación independiente, la replicación o la comprobación cruzada, también se puede adoptar deliberadamente el mismo enfoque de investigación.
3. Durante la investigación conjunta, el [agente principal de investigación](#notion-main-research-agent) sincroniza las actualizaciones de los colaboradores antes de cada ronda mediante operaciones como [pulls](#notion-pull) y [fusiones](#notion-merge);
   en el momento oportuno, realiza [commits](#notion-commit) y [pushes](#notion-push) de los avances de investigación que se pueden compartir.
   El agente resuelve los conflictos administrativos dentro del alcance de su autoridad; ante discrepancias matemáticas sustanciales, explica el problema y realiza una revisión conforme a la autorización existente o tras obtener la autorización necesaria.
   También puede solicitar expresamente operaciones de sincronización como pushes, pulls y fusiones.

### Precauciones

- Los [agentes](#notion-agent) intentarán descargar la literatura de acceso público en [el directorio local de literatura](../mathematics/literature/pdf).
  [Git](git-repository.md#notion-git) ignora este directorio de forma predeterminada.
  Si guarda allí sus propios materiales privados, asegúrese de que Git ignore el directorio y de que este no se suba a un repositorio público.
- Si varios colaboradores fueran a utilizar la misma clave de autor, acuerden claves distintas, como `Wang1` y `Wang2`.
- Utilice [letras de línea de investigación](#notion-research-line-letter) distintas para los [Tasks](#material-task) que vayan a avanzar en paralelo mediante agentes principales de investigación separados.
  Elija las letras al configurar los Tasks para separar la numeración de los materiales y reducir los conflictos de escritura.
  Pida a los agentes que coordinen los cambios en los archivos compartidos, incluidos los índices, la bibliografía y los registros de identidad del repositorio.
  No se recomiendan worktrees adicionales para la investigación en paralelo; el marco no define un procedimiento para gestionarlos.
- ACME orienta a los agentes mediante reglas escritas y herramientas auxiliares.
  Si un agente se aparta de sus instrucciones o de las reglas del marco, pídale que explique la discrepancia y corrija el trabajo afectado.
- Las reglas del marco pueden contener ambigüedades, incoherencias o lagunas.
  Puede pedir a un agente que revise las reglas del marco si lo considera oportuno.
  También puede informar al [autor](https://github.com/vtejdn) del marco ACME.

### Hábitos útiles

- Pregunte a un [agente](#notion-agent) siempre que tenga dudas sobre el marco.
- Si conserva la literatura en un directorio local sincronizado mediante un servicio en la nube, pida a un agente que conecte [el directorio local de literatura](../mathematics/literature/pdf) con él mediante una unión de directorios (directory junction).
  Conceda al agente los permisos necesarios para leer y gestionar los archivos de ese directorio.
- Cuando los agentes automaticen tareas relacionadas que utilicen credenciales, guarde los secretos de forma adecuada y exclúyalos de [Git](git-repository.md#notion-git).

### Redactar un manuscrito

En elaboración.

### Formalización en Lean

En elaboración.

## Información útil

### Versión del marco

La versión actual del marco es 0.8.0.

Cuando las comprobaciones automáticas estén activadas y se permita el acceso a la red,
el [agente](#notion-agent) comprobará al comenzar el trabajo si hay una versión más reciente del [marco ACME oficial](https://github.com/vtejdn/acme), como máximo una vez por día UTC.
Si la hay, le indicará la versión instalada y la disponible, y preguntará si desea organizar una actualización; puede continuar con el trabajo actual mientras decide.
Un aviso no instala ni actualiza nada, y puede aplazarlo.
Puede pedir que se desactiven o activen las comprobaciones automáticas de este repositorio, que se compruebe de nuevo ahora o que se realice una actualización explícitamente.

### Ejemplos de instrucciones

Los [ejemplos de instrucciones](<user-instructions/Ejemplos de instrucciones.md>) ilustran instrucciones habituales y explican qué resultados cabe esperar.

### Directorios y archivos de la raíz

Las tablas siguientes describen los principales archivos y directorios de la raíz del repositorio.
Algunos directorios se crean solo cuando son necesarios.

| Ruta | Finalidad |
| --- | --- |
| `.tmp/` | Guarda las entradas temporales y los archivos derivados que crean los [agentes](#notion-agent) y que se eliminan después de su uso. |
| `execution/` | Registra el estado actual de ejecución, los límites y las condiciones de parada de los [Tasks](#material-task) de investigación individuales. |
| [`framework/`](../framework/readme.md) | Contiene las reglas del marco, las plantillas de materiales, las especificaciones de formato y la información sobre versiones. |
| `intake/` | Registra qué materiales se recibieron de otros [repositorios](git-repository.md#notion-git-repository), sus fuentes y el alcance de cada adquisición. |
| [`mathematics/`](../mathematics/readme.md) | Contiene los materiales de investigación, los registros de literatura, los cálculos, los manuscritos y las presentaciones. |
| `profiles/` | Guarda las políticas personales de investigación, las preferencias de ejecución y las decisiones de redacción matemática. |
| [`repository/`](../repository/readme.md) | Guarda la configuración del repositorio, los registros de autores y las correspondencias con repositorios y autores externos. |
| [`scripts/`](../scripts/readme.md) | Ofrece herramientas opcionales de línea de comandos para la configuración, la gestión de materiales, la navegación y las comprobaciones. |
| [`user-manual/`](./) | Contiene las guías de usuario, las explicaciones de configuración y los ejemplos de instrucciones. |
| `.gitattributes` | Configura cómo [Git](git-repository.md#notion-git) trata los archivos de texto y binarios, incluidos los finales de línea. |
| `.gitignore` | Especifica los archivos y directorios sin seguimiento que Git debe ignorar. |
| `AGENTS.md` | Proporciona instrucciones de entrada que orientan a los agentes hacia las reglas y los materiales aplicables del marco. |
| `LICENSE` | Contiene las condiciones de licencia y los avisos del repositorio. |
| `readme.md` | Presenta el repositorio y enlaza el manual de usuario, las reglas del marco y los materiales de investigación. |

Según sus herramientas y su configuración, también pueden aparecer los directorios siguientes.

| Ruta | Finalidad |
| --- | --- |
| `.agents/` | Guarda las habilidades de agentes propias del repositorio. |
| `.claude/` | Guarda la configuración local de Claude Code para este espacio de trabajo. |
| `.codex/` | Guarda la configuración local de Codex para este espacio de trabajo. |
| `.git/` | Guarda el historial de Git, las referencias, la configuración y otros metadatos de control de versiones. |
| `.venv/` | Guarda el entorno virtual local de Python y sus dependencias instaladas. |
| `.vscode/` | Guarda la configuración del espacio de trabajo de VS Code y las recomendaciones de extensiones. |

### Categorías de materiales de investigación

| Abreviatura | Material | Ubicación | Finalidad |
| --- | --- | --- | --- |
| T | [Tarea de investigación (Task)](#material-task) | [`mathematics/tasks/`](../mathematics/tasks/index.md) | Define una pregunta de investigación, su alcance autorizado y los criterios de finalización, y registra las decisiones sobre su ciclo de vida. |
| S | [Estrategia de investigación (Strategy)](#material-strategy) | [`mathematics/strategies/`](../mathematics/strategies/index.md) | Desarrolla y evalúa una vía de investigación, organiza las prioridades e identifica los obstáculos y los pasos siguientes. |
| C | [Enunciado matemático (Claim)](#material-claim) | [`mathematics/claims/`](../mathematics/claims/index.md) | Formula enunciados matemáticos precisos, conserva sus argumentos y dependencias, y registra sus evaluaciones matemáticas y de revisión. |
| R | [Registro de revisión (Review)](#material-review) | [`mathematics/audits/reviews/`](../mathematics/audits/reviews/readme.md) | Registra revisiones matemáticas de argumentos concretos del proyecto, incluidos los elementos examinados, los hallazgos, la organización de la revisión y sus limitaciones. |
| D | Borrador (Draft) | [`mathematics/drafts/`](../mathematics/drafts/readme.md) | Proporciona un espacio de trabajo para desarrollar argumentos matemáticos, cálculos y alternativas que aún se están explorando. |
| L | [Registro de exploración (Ledger)](#material-ledger) | [`mathematics/ledger/`](../mathematics/ledger/readme.md) | Conserva exploraciones, comparaciones, síntesis y enfoques fallidos útiles, junto con las razones y los resultados de los cambios matemáticos sustanciales. |
| J | Cálculo (Computation) | [`mathematics/computations/programs/`](../mathematics/computations/readme.md) | Organiza los programas y las entradas necesarias para realizar cálculos reproducibles y registra el estado de ejecución, los resultados y las limitaciones. |
| U | Unidad de revisión de literatura (Literature audit unit) | [`mathematics/audits/literature/`](../mathematics/audits/literature/readme.md) | Permite reutilizar la literatura examinada registrando la edición y los pasajes de la fuente, el contenido matemático, la aplicabilidad y los límites de la inspección. |
| — | Manuscrito (Manuscript) | [`mathematics/manuscripts/`](../mathematics/manuscripts/index.md) | Permite elaborar artículos y documentos matemáticos relacionados, con su exposición, citas, decisiones de redacción y registros de compilación. |
| — | Presentación (Presentation) | [`mathematics/presentations/`](../mathematics/presentations/readme.md) | Permite preparar charlas y diapositivas para un público determinado, con sus archivos fuente, decisiones de redacción, información de compilación y registros de revisión. |

- Cada cálculo tiene un directorio J numerado que contiene sus programas, las entradas necesarias y un archivo `readme.md`.
  Los resultados generados se guardan por separado en la ruta local `mathematics/computations/outputs/<J>/`, ignorada por [Git](git-repository.md#notion-git).
- Las unidades de revisión de literatura se agrupan por clave de cita en `mathematics/audits/literature/`.
- El [índice de definiciones](../mathematics/definitions/index.md) organiza las definiciones, la terminología y los símbolos por concepto, con enlaces a sus formulaciones completas en los materiales C, L o U responsables.
- La [bibliografía](../mathematics/literature/references.bib) canónica registra la identidad de las publicaciones y sus claves de cita.
  La adquisición de fuentes, las versiones de los archivos y su disponibilidad se registran por separado en el registro de literatura (`mathematics/literature/registry.md`).

### Conceptos básicos

| Término | Significado |
| --- | --- |
| <a id="notion-llm"></a>LLM (modelo de lenguaje de gran tamaño) | Modelo de IA entrenado con grandes cantidades de texto para procesar y generar lenguaje, incluidas las explicaciones matemáticas y el código informático. |
| <a id="notion-agent"></a>Agente (Agent) | Sistema de IA basado en un [LLM](#notion-llm) que puede planificar y ejecutar tareas, utilizar herramientas y adaptar sus acciones a los resultados. Funciona mediante un [entorno de ejecución de agentes](agent-harness.md), dentro del alcance y los límites autorizados por el usuario humano. Aún no ha evolucionado hasta convertirse en un [Agente](https://es.wikipedia.org/wiki/Matrix#Argumento). |
| <a id="notion-context"></a>Contexto (Context) | Información disponible para un LLM durante una llamada al modelo, incluidas las instrucciones, el historial de conversación, los materiales proporcionados y los resultados de las herramientas. El contexto actual puede contener solo una selección o un resumen del historial completo de la [sesión](#notion-session). |
| <a id="notion-context-length"></a>Longitud del contexto (Context length) | Longitud máxima combinada de entrada y salida que un LLM puede procesar de una vez, normalmente medida en tokens, pequeñas unidades de texto. Incluye las instrucciones, el historial de conversación, los materiales proporcionados y la respuesta generada. |
| <a id="notion-session"></a>Sesión (Session) | Interacción continuada con un [agente](#notion-agent), gestionada por un [entorno de ejecución de agentes](agent-harness.md). Puede contener varios turnos de conversación, cada uno de los cuales suele comenzar con un mensaje del usuario e incluir las respuestas del agente y las operaciones de las herramientas. El entorno conserva el historial de conversación y prepara el [contexto](#notion-context) de cada llamada al modelo; para respetar la [longitud del contexto](#notion-context-length) del modelo, puede seleccionar o resumir partes anteriores del historial. |
| Identificador de material | Referencia estructurada que identifica un material y, cuando corresponde, su versión. Por ejemplo, `Alice_C_F0007_v1.md` identifica un [Claim](#material-claim) por autor, tipo, línea de investigación, número de serie y versión. |
| <a id="notion-research-line-letter"></a>Letra de línea de investigación | Letra, como la `F` de `Alice_C_F0007_v1.md`, que se utiliza para organizar materiales de investigación numerados. Los materiales derivados de un Task heredan su letra, pero reciben sus propios números de serie. La letra predeterminada es `A` cuando no se especifica ninguna línea. |
| Clave de autor | Clave estable registrada para un autor humano, como `Alice`, utilizada en los identificadores de materiales y los registros de autoría. |
| Familia de materiales | Versiones conservadas de un mismo material, como `Alice_C_F0007_v1.md` y `Alice_C_F0007_v2.md`. |
| Versión de material | Revisión concreta conservada de un material, como la versión `v1` o `v2` de un Claim. |
| <a id="notion-main-research-agent"></a>Agente principal de investigación | Agente que dirige el trabajo sobre un [Task](#material-task), coordina los subagentes que participen y mantiene la coherencia de los registros de investigación. |
| Ronda de trabajo de un Task | Periodo de trabajo sobre un Task que termina con un registro de los avances, las preguntas sin resolver y el punto de continuación. |
| <a id="notion-git-branch"></a>Rama Git (Branch) | Línea de desarrollo con nombre dentro de un [repositorio Git](git-repository.md#notion-git-repository) que permite desarrollar cambios por separado de otras líneas de trabajo. |
| <a id="notion-clone"></a>Clonación (Clone) | Copia de un repositorio Git existente en una nueva carpeta local, incluidos sus archivos y su historial de versiones. |
| <a id="notion-commit"></a>Commit | Versión guardada en el historial local de [Git](git-repository.md#notion-git) que registra cambios seleccionados con un mensaje que los describe. |
| <a id="notion-push"></a>Push | Envío de commits locales a un repositorio Git remoto para que el trabajo registrado esté disponible allí. |
| <a id="notion-pull"></a>Pull | Obtención de los cambios de un repositorio Git remoto e incorporación de estos al trabajo local. |
| <a id="notion-merge"></a>Fusión (Merge) | Integración de los cambios de otra [rama](#notion-git-branch) en la rama Git actual, resolviendo las ediciones en conflicto cuando sea necesario. |
| <a id="notion-intake"></a>Recepción (Intake) | Incorporación a su propio repositorio de materiales de investigación seleccionados de otro repositorio ACME público, conservando su autoría, procedencia y limitaciones de revisión. |
| Clave de cita | Identificador corto de una obra en la bibliografía que permite citarla de forma coherente en los registros de investigación y los manuscritos. |

### <a id="material-task"></a>Tarea de investigación (Task)

Un Task organiza la investigación en torno a un objetivo matemático preciso, su alcance autorizado y los criterios de finalización acordados.

| Estado del Task | Significado para el lector |
| --- | --- |
| `proposed` | Se ha planteado una pregunta de investigación, pero aún no se ha convertido en un objetivo de investigación activo. |
| `active` | La investigación está autorizada y sigue en curso. |
| `paused` | La investigación está detenida deliberadamente, con intención de retomarla y una base explícita para hacerlo. |
| `blocked` | Una entrada concreta que falta o un requisito previo incumplido impide el siguiente paso necesario. El registro explica qué se necesita para reanudar el avance. |
| `completed` | Se han cumplido los criterios de finalización acordados, con evidencia matemática de apoyo y la revisión necesaria. |
| `retired` | La investigación se ha abandonado. Sus razones, hallazgos útiles y partes pendientes siguen registrados. |

- Un Task puede seguir activo aunque ningún [agente](#notion-agent) esté trabajando en él en ese momento.
- Un Task reúne los materiales de investigación que sustentan su estudio.
  Los manuscritos relacionados, los informes de progreso y los demás documentos que solicite pueden reunirse en un proyecto como `mathematics/manuscripts/Alice_T_A0007/`.
- Puede pedir que se reactive un Task completado para continuar trabajando sobre el objetivo de investigación correspondiente.
  Explique qué desea investigar a continuación y qué cambios hay en el alcance o los límites.
  Un objetivo de investigación sustancialmente distinto debe establecerse como un nuevo Task.

### <a id="material-strategy"></a>Estrategia de investigación (Strategy)

Una estrategia describe una vía concreta hacia un objetivo de investigación, incluidos su mecanismo, los obstáculos restantes y los siguientes pasos útiles.

| Estado de la estrategia | Significado para el lector |
| --- | --- |
| `proposed` | Se ha identificado un enfoque posible, pero aún no se ha seleccionado para la investigación actual. |
| `active` | La vía está seleccionada actualmente para investigar el objetivo del Task. |
| `paused` | La vía se ha apartado temporalmente por motivos de prioridad, orden de trabajo o recursos disponibles. No implica un fracaso matemático. |
| `blocked` | Un requisito previo concreto incumplido impide el siguiente paso previsto. El registro identifica el obstáculo y lo que permitiría continuar la vía. |
| `completed` | La vía ha producido el resultado o la contribución que se proponía, con la evidencia de apoyo necesaria. Puede ser necesario realizar otros trabajos para completar el Task. |
| `refuted` | La evidencia matemática comprobada descarta el mecanismo registrado o una afirmación auxiliar que este necesita, bajo las hipótesis indicadas. |
| `superseded` | La vía ha sido sustituida por estrategias sucesoras identificadas o incorporada a otra vía. Su historia y sus hallazgos útiles siguen disponibles. |

- Un [Task](#material-task) puede tener varias estrategias, como alternativas o como partes de un enfoque combinado.
  Completar, pausar o descartar una estrategia no determina por sí solo el estado de todo el Task.
- Puede sugerir enfoques, pedir al [agente](#notion-agent) que compare alternativas o especificar prioridades.
  Indique explícitamente si una prioridad o un orden debe permanecer fijo; de lo contrario, el agente puede adaptar su elección de vías dentro del alcance acordado.
- Dentro del alcance autorizado, los agentes autónomos pueden añadir, revisar, cambiar de prioridad, dividir, fusionar, pausar o retomar estrategias a medida que cambien los hallazgos y los recursos.
- Una vía fallida puede seguir siendo informativa.
  Puede revelar un obstáculo, descartar un enfoque o identificar dónde haría falta una hipótesis adicional.

### <a id="material-claim"></a>Enunciado matemático (Claim)

Un Claim registra un enunciado matemático importante y preciso, y lo que se conoce actualmente sobre su validez.

| Estado matemático | Significado para el lector |
| --- | --- |
| `open` | El enunciado exacto sigue sin resolverse. Puede haber resultados parciales, reducciones o un argumento propuesto, pero aún no se cumplen las condiciones de `proved` o `refuted`. |
| `proved` | Una demostración completa establece el enunciado exacto bajo las hipótesis indicadas. Todos los resultados de apoyo necesarios están establecidos y son aplicables, y una [revisión](#material-review) matemática registrada no encontró ninguna laguna pendiente. |
| `refuted` | Un contraejemplo o argumento comprobado refuta el enunciado exacto dentro del alcance indicado. Todos los resultados de apoyo necesarios están establecidos y son aplicables, y una revisión matemática registrada no encontró ninguna laguna pendiente. |

### <a id="material-review"></a>Registro de revisión (Review)

Un Review registra el examen de un enunciado o argumento matemático por parte de un [agente](#notion-agent), incluidos los elementos y el alcance exactos del examen, los hallazgos y las limitaciones pendientes.

| Relación de revisión | Significado para el lector |
| --- | --- |
| `self-reviewed` | La demostración ha sido comprobada por un agente que participó en su desarrollo o conoce la discusión matemática de la que surgió. |
| `independently reviewed` | Un agente distinto comprobó la demostración sin participar en su desarrollo ni recibir la discusión correspondiente como su propio [contexto](#notion-context). |
| `unknown` | La relación de una revisión antigua o procedente de una fuente no está establecida; esto no implica un error ni una inspección independiente. |

- Estas etiquetas describen la relación de los agentes revisores con la demostración, no si la demostración es correcta.
  La ausencia de una declaración de esa relación es distinta de `unknown`; si no se ha seleccionado una revisión, el Claim no selecciona ninguna evidencia de revisión.
- La revisión de otro agente sigue siendo una autorrevisión si este hereda discusiones sobre el desarrollo de la demostración, resúmenes matemáticos, explicaciones del autor o conclusiones de revisiones anteriores.
  Una [sesión](#notion-session) o un modelo distinto no establece por sí solo la independencia.
- El [agente principal de investigación](#notion-main-research-agent) organiza revisiones independientes en los puntos clave de la demostración y, después de completar el [Task](#material-task), de toda la cadena lógica.
  También puede pedir la revisión de un resultado concreto o de un paso de una demostración.

### <a id="material-ledger"></a>Registro de exploración (Ledger)

Un Ledger conserva exploraciones matemáticas útiles, incluidas las comparaciones, los enfoques fallidos y las razones de los cambios de dirección.
Una entrada puede explicar qué se investigó, bajo qué hipótesis, qué se intentó, qué mostraron el razonamiento o la evidencia y qué sigue sin resolverse.

Un Ledger puede conservar argumentos parciales e ideas útiles aunque la investigación aún no haya producido un [Claim](#material-claim) separado.
Por ejemplo, los intentos fallidos o no concluyentes pueden revelar obstáculos, distinguir enfoques o ayudar a evitar repetir trabajo.

- Puede pedir a un [agente](#notion-agent) que compare [estrategias](#material-strategy), explique un intento fallido, sintetice hallazgos de varias fuentes o conserve una línea de razonamiento útil para trabajos posteriores.
- También puede pedir a un agente que registre cualquier contenido que considere matemáticamente sustancial y digno de conservarse.
