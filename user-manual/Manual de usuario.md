# Manual de usuario

[Ejemplos de instrucciones](<user-instructions/Ejemplos de instrucciones.md>) · [Ejemplo de declaración de uso de IA](ai-disclosure-example.md) · [Ejemplo de página de publicación](publication-example.md) · [Ejemplos de repositorios](https://github.com/vtejdn/acme/discussions/1)

## ACME: Autonomous and Collaborative Mathematical Exploration

ACME es un marco ligero para la investigación matemática autónoma y colaborativa.
Combina reglas en Markdown para [agentes de IA](#notion-agent) con scripts auxiliares para apoyar la exploración sostenida y conservar investigaciones que puedan examinarse, reutilizarse y continuarse.
Tiene dos objetivos principales: permitir que agentes de IA autónomos realicen investigación matemática bajo la orientación de matemáticos humanos y facilitar la colaboración entre autores humanos.

Le animamos a realizar toda su investigación [de forma completamente abierta](https://github.com/vtejdn/acme/discussions/1) y a mantener un registro completo de su trabajo en un repositorio público.
En los repositorios públicos, los agentes de ACME registran por defecto las actualizaciones de la investigación en commits y las envían mediante push con prontitud, para que sus colegas puedan seguir el avance de su trabajo.
Los agentes de ACME también seleccionan y reutilizan de forma autónoma materiales de investigación pertinentes de otros repositorios ACME públicos mediante [Intake](#notion-intake), respetando sus licencias y conservando la autoría y la procedencia.
**Al hacer público su repositorio ACME bajo la [licencia Apache 2.0](../LICENSE) predeterminada, permite que los materiales generados por sus agentes sean reutilizados por otras personas y sus agentes sin solicitar un permiso adicional.**

### Matemáticos humanos

Los matemáticos humanos son responsables de:

1. Definir las preguntas de investigación, su alcance autorizado y los criterios de finalización para iniciar [tareas de investigación (Task)](#material-task).
2. Elegir, evaluar y ajustar las [estrategias de investigación (Strategy)](#material-strategy) junto con los [agentes](#notion-agent).
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

### Flujo de trabajo

La investigación comienza con un [Task](#material-task) definido por una persona y con criterios de finalización explícitos.
Los [agentes](#notion-agent) primero consultan y reutilizan los materiales de investigación y la literatura locales pertinentes, y después buscan fuentes adicionales en la Web cuando es necesario.
Comprueban la aplicabilidad de los resultados, desarrollan [estrategias](#material-strategy) e iteran entre intentos de demostración, cálculos y búsquedas de contraejemplos.
Cada intento informa el siguiente: los hallazgos útiles, los fracasos y las preguntas sin resolver se conservan en los materiales de investigación adecuados, incluidos los [Claims](#material-claim) y los [Ledgers](#material-ledger).
Las estrategias se adaptan dentro del objetivo autorizado.
Los resultados propuestos se someten a [revisión](#material-review) matemática y la finalización del Task se evalúa según los criterios originales.

Véase el [diagrama del flujo de trabajo](workflow.jpg).

### Colaboración

ACME ofrece dos formas de colaborar y compartir materiales.

- Los matemáticos pueden [colaborar](#joint-task) mediante un [repositorio Git](<git-repository/Repositorios Git.md#notion-git-repository>) compartido, intercambiar materiales de investigación y reutilizar los resultados de los demás.
  El repositorio puede alojarse en una plataforma como [GitHub](<git-repository/Repositorios Git.md#notion-github>), de modo que los colaboradores trabajen en sus propios equipos y sincronicen los cambios.
  Véase el [diagrama de colaboración mediante un repositorio Git](git-repo.png).

- Distintos matemáticos o equipos también pueden colaborar entre repositorios recibiendo materiales seleccionados mediante [recepción (Intake)](#notion-intake).
  Puede compartir materiales de investigación en un repositorio Git público que utilice la [licencia Apache 2.0](../LICENSE) predeterminada.
  Otras personas y sus agentes pueden reutilizar los materiales generados por sus agentes en ese repositorio sin solicitar permiso adicional.
  Los agentes ACME seleccionan y reutilizan de forma autónoma materiales de investigación pertinentes de otros repositorios ACME públicos mediante recepción (Intake), respetando sus licencias y conservando la autoría y la procedencia.
  En el repositorio público actual, puede dar una instrucción de [importación (Import)](#notion-import) para seleccionar de sus otros repositorios, incluidos los privados, los materiales que desee hacer públicos e importarlos aquí.
  Véase el [diagrama de colaboración entre repositorios](collaboration.jpg).

### Declaración de uso de IA

Al publicar resultados de investigación, declare con veracidad cómo ha utilizado el marco ACME.
Al publicar un preprint en plataformas como [arXiv](https://arxiv.org/) o [Hexagon](https://hexagonmath.org/), o al enviar un artículo a una revista, recomendamos incluir un enlace a su repositorio Git ACME público para que los colegas y revisores puedan consultar los materiales pertinentes y los registros completos de investigación, comprobar los argumentos, comprender el proceso y evaluar el trabajo.
Puede adaptar el [ejemplo de declaración de uso de IA](./ai-disclosure-example.md).
También puede consultar el [ejemplo de página de publicación](./publication-example.md) para explicar el grado de comprensión y las contribuciones concretas de los autores humanos, y expresar su postura sobre compartir y reutilizar los materiales en bruto generados por agentes.

## <a id="setup"></a>Configuración

Para un nuevo proyecto de investigación, siga los pasos I–III que se indican a continuación.
Si se incorpora a una colaboración existente, [prepare su espacio de trabajo](#setup-workplace) y después siga los [pasos para incorporarse a la colaboración](#setup-collaboration).

### Paso I. Elegir [LLM](#notion-llm) con capacidad suficiente

Compare el rendimiento de los LLM en tareas matemáticas de nivel de investigación.
Utilice [FrontierMath Tier 4](https://epoch.ai/frontiermath/tiers-1-4?tier=Tier+4+%28v2%29&view=graph&tab=leaderboard), [MathArena](https://matharena.ai/models), [Riemann-bench](https://surgehq.ai/benchmarks/riemann-bench) y otras evaluaciones pertinentes como puntos de referencia.
Elija modelos para la investigación matemática y las tareas administrativas teniendo en cuenta si son de código abierto, su accesibilidad y su coste.

### <a id="setup-workplace"></a>Paso II. Preparar el espacio de trabajo

Elija un [entorno de ejecución de agentes](<harness/Entorno de ejecución de agentes.md>) adecuado y conéctelo a un [LLM](#notion-llm) con capacidad suficiente.

1. Instale un entorno de ejecución de agentes, como aplicación independiente o dentro de un [IDE](<harness/Entorno de ejecución de agentes.md#notion-ide>), e inicie sesión si es necesario o lo desea.
2. Seleccione el modelo y el proveedor en la configuración o en el selector de modelos.
3. Elija una carpeta en su equipo para guardar el marco y los futuros materiales de investigación.
   Para la primera instalación en un proyecto nuevo, utilice una carpeta local que todavía no contenga contenido del proyecto.
   Para incorporarse a un repositorio de investigación ACME existente, siga los pasos para [unirse a un repositorio Git como colaborador](#setup-collaboration).

Sin [Git](<git-repository/Repositorios Git.md#notion-git>), la opción predeterminada es la investigación personal en su propio equipo.
Para sincronizar el trabajo entre equipos o colaborar mediante un [repositorio Git](<git-repository/Repositorios Git.md#notion-git-repository>) compartido, puede elegir una plataforma de alojamiento como [GitHub](<git-repository/Repositorios Git.md#notion-github>).
Si ya ha elegido un repositorio remoto, confirme antes de la primera instalación que tampoco contiene contenido del proyecto.

Al crear un repositorio GitHub, elija si será privado o público según sus necesidades.
Hacerlo público y enviar los registros de investigación al repositorio remoto para sincronizar el trabajo entre equipos o colaborar son decisiones distintas.

4. (Opcional) Instale Git en su equipo o pida a un [agente](#notion-agent) del entorno elegido que lo haga.
   Consulte el ejemplo de instrucción [Instalar Git](<user-instructions/Ejemplos de instrucciones.md#install-git>).
5. (Opcional) Cree una cuenta de alojamiento de repositorios o inicie sesión y, a continuación, conéctese a un repositorio existente o cree uno nuevo.
   Para una guía paso a paso, consulte [Conectar un proyecto local a GitHub](<git-repository/Repositorios Git.md#connect-github>).

### Paso III. Instalar e inicializar el marco

Si se incorpora a un repositorio de investigación existente que ya contiene ACME, siga los pasos de la sección siguiente.

1. Pida a un [agente](#notion-agent) que descargue e instale el [marco ACME](https://github.com/vtejdn/acme) en la carpeta de su proyecto.
   Consulte el ejemplo de instrucción [Instalar ACME](<user-instructions/Ejemplos de instrucciones.md#install-acme>).
2. Elija una [clave de autor](#notion-author-key) única, como `Alice` o `Ali`, y elija de forma independiente el nombre que figurará en la atribución de `LICENSE`.
   Pida a un agente que le registre como autor y añada esa atribución.
   Consulte el ejemplo de instrucción [Registrar al autor](<user-instructions/Ejemplos de instrucciones.md#register>).
3. (Si utiliza Git) Configure el nombre y el correo electrónico asociados a sus [commits](#notion-commit), o pida a un agente que lo haga.
   Consulte el ejemplo de instrucción [Configurar Git](<user-instructions/Ejemplos de instrucciones.md#setup-git>).
4. (Si utiliza Git) Elija o confirme la clave de su [repositorio](<git-repository/Repositorios Git.md#notion-git-repository>) de investigación y pida a un agente que compruebe que está registrada correctamente en el marco; consulte el ejemplo [Establecer la clave del repositorio](<user-instructions/Ejemplos de instrucciones.md#setup-repo>).
5. (Opcional) Cuando resulte apropiado, recomendamos encarecidamente compartir sus registros de investigación mediante un repositorio público.

### <a id="setup-collaboration"></a>Incorporarse a un [repositorio Git](<git-repository/Repositorios Git.md#notion-git-repository>) existente como colaborador

1. Inicie sesión en la plataforma de alojamiento del repositorio y acepte la invitación de su coautor.
2. Pida a un [agente](#notion-agent) que le ayude a configurar el acceso a la plataforma que aloja el repositorio remoto; véase [Conectar con GitHub](<git-repository/Repositorios Git.md#connect-github>).
3. Cree una nueva carpeta local en su ordenador y ábrala en su entorno de ejecución de agentes.
   Proporcione la dirección del repositorio a su agente y pídale que lo [clone](#notion-clone) en esa carpeta vacía.
   Consulte el ejemplo de instrucción [Clonar un repositorio](<user-instructions/Ejemplos de instrucciones.md#clone-repo>).
4. Si aún no está registrado en el repositorio de investigación, elija una clave de autor distinta de las de sus colaboradores y elija de forma independiente el nombre que figurará en la atribución de `LICENSE`, y después pida a un agente que le registre y añada esa atribución.
   Consulte el ejemplo de instrucción [Registrar al autor](<user-instructions/Ejemplos de instrucciones.md#register>).
5. Configure el nombre y el correo electrónico utilizados en sus [commits](#notion-commit) de [Git](<git-repository/Repositorios Git.md#notion-git>), o pida a un agente que lo haga.
   Consulte el ejemplo de instrucción [Configurar Git](<user-instructions/Ejemplos de instrucciones.md#setup-git>).

## Comenzar la exploración

### Iniciar un [Task](#material-task)

1. (Opcional) Aporte la literatura pertinente o pida a un [agente](#notion-agent) que la busque; consulte el ejemplo [Buscar literatura](<user-instructions/Ejemplos de instrucciones.md#search-article>).
   Pida al agente que revise las partes indicadas de los artículos pertinentes; consulte el ejemplo [Revisar literatura](<user-instructions/Ejemplos de instrucciones.md#audit>).
2. Establezca un Task mediante la discusión con los agentes, precisando la pregunta, las restricciones y los criterios de finalización; consulte el ejemplo [Crear un Task](<user-instructions/Ejemplos de instrucciones.md#create-task>).
   Puede elegir una [letra de línea de investigación](#notion-research-line-letter) para organizar el Task y sus materiales.
3. Para la investigación autónoma continuada, especifique o adopte límites de ejecución y condiciones de parada; consulte el ejemplo [Establecer condiciones de parada predeterminadas](<user-instructions/Ejemplos de instrucciones.md#set-stop-condition>).
4. (Opcional) Discuta y desarrolle [estrategias de investigación](#material-strategy) con el agente; consulte el ejemplo [Crear una estrategia](<user-instructions/Ejemplos de instrucciones.md#create-strategy>).
5. Inicie el Task de investigación; consulte el ejemplo [Iniciar un Task](<user-instructions/Ejemplos de instrucciones.md#start-task>).
   Autorice las operaciones de herramientas necesarias cuando se le solicite y responda a las preguntas de los agentes.
6. Reflexione sobre los materiales matemáticos producidos por los agentes y compréndalos (ningún agente puede hacerlo por usted).
   Discuta las matemáticas con los agentes para profundizar y acelerar su comprensión.
   Pida referencias pertinentes y cuestione de forma socrática el origen de los argumentos y las ideas, especialmente cuando dependan del conocimiento del modelo sin una fuente explícita.
7. (Opcional, si utiliza [Git](<git-repository/Repositorios Git.md#notion-git>)) Cree [commits](#notion-commit) con los cambios que quiera conservar; consulte el ejemplo [Crear un commit](<user-instructions/Ejemplos de instrucciones.md#commit>).
   Deshaga las modificaciones locales o revierta commits existentes cuando sea necesario.
   Una vez configurado un repositorio Git remoto, el agente crea y envía oportunamente los commits de investigación por defecto, conforme a lo acordado.

- Véanse más [ejemplos de instrucciones de investigación](<user-instructions/Ejemplos de instrucciones.md#research>).

### <a id="joint-task"></a>Iniciar un [Task](#material-task) conjunto

Los colaboradores de un mismo repositorio pueden establecer un Task conjunto para un objetivo matemático común, definiendo la pregunta compartida, las hipótesis, el alcance y los criterios de finalización; cada participante avanza en su investigación mediante su propio Task.

1. Pida a un [agente](#notion-agent) que establezca un Task conjunto; consulte el ejemplo [Crear un Task conjunto](<user-instructions/Ejemplos de instrucciones.md#create-joint-task>).
   Si un colaborador ya ha establecido uno adecuado, puede pasar directamente al siguiente paso.
2. Pida al agente que establezca o reutilice su Task individual y lo vincule al Task conjunto; consulte el ejemplo [Crear un Task individual](<user-instructions/Ejemplos de instrucciones.md#create-personal-task>).
   El Task individual puede abarcar toda la pregunta común o parte de ella; sus criterios de finalización pueden coincidir con los del Task conjunto o determinarse según el alcance de su participación.
   Los participantes también pueden repartirse el trabajo sobre la misma pregunta: una persona intenta encontrar una demostración y otra busca un contraejemplo.
   Se recomienda elegir, de acuerdo con los colaboradores, distintas [estrategias de investigación (Strategy)](#material-strategy) para reducir la repetición del trabajo matemático y aprovechar mejor los recursos computacionales de IA.
   Para la verificación independiente, la replicación o la comprobación cruzada, también se puede adoptar deliberadamente el mismo enfoque de investigación.
3. Durante la investigación conjunta, el [agente principal de investigación](#notion-main-research-agent) sincroniza las actualizaciones de los colaboradores antes de cada ronda mediante operaciones como [pulls](#notion-pull) y [fusiones](#notion-merge);
   en el momento oportuno, realiza [commits](#notion-commit) y [pushes](#notion-push) de los avances de investigación que se pueden compartir.
   El agente resuelve los conflictos administrativos dentro del alcance de su autoridad; ante discrepancias matemáticas sustanciales, explica el problema y realiza una revisión conforme a la autorización existente o tras obtener la autorización necesaria.
   También puede solicitar expresamente operaciones de sincronización como pushes, pulls y fusiones.

- Véanse más [ejemplos de instrucciones para Tasks conjuntos](<user-instructions/Ejemplos de instrucciones.md#joint-task>).

### Precauciones

- Los [agentes](#notion-agent) intentarán descargar la literatura de acceso público en el directorio `mathematics/literature/pdf/`, relativo a la raíz del repositorio actual.
  [Git](<git-repository/Repositorios Git.md#notion-git>) ignora este directorio de forma predeterminada.
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
- Si utiliza varios repositorios ACME en el mismo equipo, puede reunir la literatura en una única carpeta local de archivos PDF.
  En Windows, pida al agente que cree una unión de directorio para que la ruta `mathematics/literature/pdf/`, relativa a la raíz de cada repositorio, apunte a esa carpeta. Consulte el ejemplo [Crear una unión](<user-instructions/Ejemplos de instrucciones.md#create-junction>).
  Conceda al agente los permisos necesarios para leer y gestionar los archivos de esa carpeta.
- Cuando los agentes automaticen tareas relacionadas que utilicen credenciales, guarde los secretos de forma adecuada y exclúyalos del seguimiento de [Git](<git-repository/Repositorios Git.md#notion-git>).

## <a id="manuscript-writing"></a>Redactar un manuscrito

### Cuatro niveles de normas de redacción

El marco permite organizar los materiales de investigación en manuscritos TeX, revisarlos, compilarlos y comprobarlos.
ACME organiza la redacción en cuatro niveles de normas, de menor a mayor prioridad:

- Normas generales de redacción matemática.
  Se encuentran en [framework/rules/writing.md](../framework/rules/writing.md#common-mathematical-writing-defaults) y se instalan con el marco como normas de redacción predeterminadas.
  Estas normas y el criterio propio de un [agente](#notion-agent) pueden no bastar para satisfacer las convenciones de un campo o las exigencias personales de un autor.
- Preferencias generales de redacción del autor.
  Según las exigencias explícitas del autor, el agente registra cuando sea necesario las preferencias generales en `profiles/<human>/writing/readme.md` (`<human>` es la [clave de autor](#notion-author-key), como `Alice`) y las actualiza conforme a esas exigencias.
  Consulte el ejemplo [Preferencias generales de redacción](<user-instructions/Ejemplos de instrucciones.md#personal-preference>).
- Preferencias del autor para un campo de investigación concreto.
  El agente las registra cuando sea necesario en el archivo de preferencias del campo correspondiente dentro de `profiles/<human>/writing/`.
  Consulte el ejemplo [Preferencias de redacción de un campo](<user-instructions/Ejemplos de instrucciones.md#community-preference>).
- Convenciones del manuscrito actual.
  Suelen registrarse en `writing.md`, `conventions.md` o una sección «Convenciones de redacción» del `readme.md` del directorio del manuscrito, y el agente las mantiene y actualiza según sea necesario.
  Consulte el ejemplo [Convenciones del manuscrito](<user-instructions/Ejemplos de instrucciones.md#manuscript-convention>).

Véanse más [ejemplos de instrucciones de redacción](<user-instructions/Ejemplos de instrucciones.md#writing-instructions>).

Un nivel de mayor prioridad sustituye únicamente las partes incompatibles de los niveles inferiores; los demás requisitos siguen siendo aplicables.
Si todavía no se han establecido preferencias personales, preferencias de un campo ni convenciones del manuscrito, el agente empieza a redactar conforme a las normas generales.
Las preferencias de terminología y notación del autor compartidas por el diálogo y la redacción se conservan juntas en `profiles/<human>/terminology.md`.

### Obras de referencia para la redacción

Los autores pueden elegir tres tipos de referencias: trabajos existentes cuyo contenido puede reutilizarse directamente, modelos de estilo y referencias de terminología y notación del campo.
Puede proporcionar literatura o señalar obras existentes; el [agente](#notion-agent) se encarga de la organización y el registro necesarios.
Una misma obra puede tener varios usos, cada uno con su propio alcance.

- Trabajos existentes reutilizables.
  Puede señalar trabajos propios o de los que sea coautor para que el agente los reutilice directamente dentro del alcance indicado, con límites adicionales a secciones o pasajes concretos si lo desea.
  Consulte el ejemplo [Permitir la reutilización de texto](<user-instructions/Ejemplos de instrucciones.md#record-my-article>).
- Modelos principales de estilo del manuscrito.
  Puede elegir una o varias referencias cuya organización, exposición y estilo sirvan de modelo al agente.
  Consulte el ejemplo [Elegir un modelo de estilo](<user-instructions/Ejemplos de instrucciones.md#style-model>).
- Referencias de terminología y notación del campo.
  Puede elegir obras para orientar al agente en la terminología, la notación y la presentación de las definiciones.
  Consulte el ejemplo [Elegir referencias terminológicas](<user-instructions/Ejemplos de instrucciones.md#terminology-references>).

Estas elecciones pueden aplicarse a su redacción en general, a un campo concreto o al manuscrito actual, y se guardan con las preferencias o convenciones correspondientes.
Las obras de referencia y sus usos para la redacción general se registran en `profiles/<human>/writing/readme.md`.
Las referencias y sus usos que solo se aplican a un campo se registran en el archivo de preferencias correspondiente dentro de `profiles/<human>/writing/`.
Las referencias y sus usos que solo se aplican al manuscrito actual se registran en `writing.md`, `conventions.md` o una sección «Convenciones de redacción» del `readme.md` del directorio del manuscrito.

### Revisión y modificación

La modificación se basa en la versión actual del manuscrito y en la intención explícita del autor.
Sin el consentimiento explícito del autor, el [agente](#notion-agent) no elimina pasajes completos ya existentes, como teoremas, definiciones, demostraciones, ejemplos u observaciones.
El marco permite revisar la redacción y los argumentos matemáticos del manuscrito por separado o conjuntamente.

- Revisión de la redacción: el agente comprueba la exposición, la estructura, la terminología, la notación y las citas conforme a los cuatro niveles; los comentarios de revisión pendientes se conservan en `revisions.md`, en el directorio del manuscrito.
  Consulte el ejemplo [Revisión de la redacción](<user-instructions/Ejemplos de instrucciones.md#writing-review>).
- Revisión matemática: el agente comprueba las hipótesis, el razonamiento y las conclusiones; los problemas matemáticos actualmente no resueltos y sus fundamentos necesarios se conservan en `review.md`, en el directorio del manuscrito, y se actualizan al volver a comprobarlos.
  Consulte el ejemplo [Revisión matemática del manuscrito](<user-instructions/Ejemplos de instrucciones.md#manuscript-review>).

Los resultados indican el alcance real de la revisión, los hallazgos y los asuntos aún no resueltos.
Cuando se necesite una revisión independiente, puede organizar la redacción y la revisión en sesiones distintas y encargar la revisión a un agente que no haya participado en la elaboración sustantiva del texto o de los argumentos, ni recibido las discusiones sustantivas de esa elaboración, para mantener un [contexto](#notion-context) independiente.
En una primera revisión independiente, el agente forma su propio juicio a partir del manuscrito actual y las convenciones aplicables antes de compararlo con los comentarios existentes.
El agente redactor informa de las correcciones; el agente revisor comprueba los cambios y sus efectos antes de actualizar o retirar los comentarios correspondientes.

### Búsqueda bibliográfica y citas

Cuando el manuscrito ya contiene enunciados matemáticos concretos, puede pedir a un [agente](#notion-agent) que [busque bibliografía pertinente](<user-instructions/Ejemplos de instrucciones.md#refs-seek>) para todo el manuscrito, para determinadas secciones o para un teorema, un lema o una propiedad en particular.
Si encuentra una fuente pertinente, el agente compara sus hipótesis y conclusiones con las de los enunciados del manuscrito.
Indica si la fuente ofrece el mismo resultado, en qué condiciones permite deducir el enunciado del manuscrito, si solo cubre un caso particular o si aporta un método afín.

El agente registra los hallazgos en `literature-seek.md`, en el directorio del manuscrito, con las ediciones conocidas, la ubicación de los pasajes en los originales, el alcance real de la comprobación y las pistas pendientes de revisar.

Si en el mismo encargo pide al agente que busque bibliografía y modifique el manuscrito, este atiende los hallazgos matemáticos de fondo o los cambios en el fundamento de un resultado antes de modificar los pasajes afectados.
Comprueba que la fuente sea aplicable, conserva la evidencia y los razonamientos necesarios en los materiales matemáticos correspondientes y realiza la evaluación y la revisión matemática que requiera el cambio.
Si la fuente exige una hipótesis adicional y todavía falta una demostración del enunciado más general, el agente registra lo que queda por demostrar y utiliza la fuente dentro del alcance que esta respalda.
Para las citas que añade o modifica en los archivos TeX, el agente anota en `citation.md` su ubicación, su propósito, qué justifica su uso y qué falta por comprobar.

### Memoria de redacción de los agentes

Durante la redacción y la modificación, el [agente](#notion-agent) resume activamente los comentarios recibidos y la experiencia para elaborar notas de redacción útiles, guardadas por autor.
Estas notas se encuentran en `profiles/<human>/writing/notes.md`, que el agente crea y mantiene de forma autónoma.
Son recomendaciones auxiliares y no sustituyen las convenciones explícitas de redacción.
Las preferencias y notas guardadas se consultan según sea necesario en posteriores trabajos de redacción relacionados.
El agente revisa, combina y condensa las notas a medida que recibe nuevos comentarios; las preferencias formales y las convenciones del manuscrito se actualizan conforme a las exigencias explícitas o las decisiones adoptadas por el autor.

### <a id="lean-formalization"></a>Formalización en Lean

En elaboración.

## Información útil

### Versión del marco

La versión actual del marco es 0.12.0.

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
| [`intake/`](../intake) | Registra qué materiales se recibieron de otros [repositorios](<git-repository/Repositorios Git.md#notion-git-repository>), sus fuentes y el alcance de cada adquisición. |
| [`mathematics/`](../mathematics/readme.md) | Contiene los materiales de investigación, los registros de literatura, los cálculos, los manuscritos y las presentaciones. |
| `profiles/` | Guarda las preferencias personales de investigación y ejecución, las decisiones de redacción matemática y las notas de experiencia mantenidas por los agentes. |
| [`repository/`](../repository/readme.md) | Guarda la configuración del repositorio, los registros de autores y las correspondencias con repositorios y autores externos. |
| [`scripts/`](../scripts/readme.md) | Ofrece herramientas opcionales de línea de comandos para la configuración, la gestión de materiales, la navegación y las comprobaciones. |
| [`user-manual/`](./) | Contiene las guías de usuario, las explicaciones de configuración y los ejemplos de instrucciones. |
| `.gitattributes` | Configura cómo [Git](<git-repository/Repositorios Git.md#notion-git>) trata los archivos de texto y binarios, incluidos los finales de línea. |
| `.gitignore` | Especifica los archivos y directorios sin seguimiento que Git debe ignorar. |
| [`AGENTS.md`](../AGENTS.md) | Proporciona instrucciones de entrada que orientan a los agentes hacia las reglas y los materiales aplicables del marco. |
| [`LICENSE`](../LICENSE) | Contiene las condiciones de licencia y los avisos del repositorio. |
| [`readme.md`](../readme.md) | Presenta el repositorio y enlaza el manual de usuario, las reglas del marco y los materiales de investigación. |

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
  Los resultados generados se guardan por separado en la ruta local `mathematics/computations/outputs/<J>/`, ignorada por [Git](<git-repository/Repositorios Git.md#notion-git>).
  Para los datos necesarios en demostraciones, comprobaciones o reproducciones posteriores, el agente conserva en el repositorio los propios datos necesarios o suficientes programas de generación, datos de entrada básicos, parámetros, condiciones relativas a las dependencias y métodos de validación para reconstruirlos de forma fiable y a un coste razonable.
  Si la reconstrucción no es fiable o resulta demasiado costosa, o si debe conservarse un objeto específico, el agente conserva los propios datos necesarios.
- Las unidades de revisión de literatura se agrupan por clave de cita en `mathematics/audits/literature/`.
- El [índice de definiciones](../mathematics/definitions/index.md) organiza las definiciones, la terminología y los símbolos por concepto, con enlaces a sus formulaciones completas en los materiales C, L o U responsables.
- La [bibliografía](../mathematics/literature/references.bib) canónica registra la identidad de las publicaciones y sus claves de cita.
  Las notas útiles sobre las fuentes y las ediciones pueden conservarse en las secciones propias de cada autor en `mathematics/audits/literature/<SourceKey>/readme.md`.

### Conceptos básicos

| Término | Significado |
| --- | --- |
| <a id="notion-llm"></a>LLM (modelo de lenguaje de gran tamaño) | Modelo de IA entrenado con grandes cantidades de texto para procesar y generar lenguaje, incluidas las explicaciones matemáticas y el código informático. |
| <a id="notion-agent"></a>Agente (Agent) | Sistema de IA basado en un [LLM](#notion-llm) que puede planificar y ejecutar tareas, utilizar herramientas y adaptar sus acciones a los resultados. Funciona mediante un [entorno de ejecución de agentes](<harness/Entorno de ejecución de agentes.md>), dentro del alcance y los límites autorizados por el usuario humano. Aún no ha evolucionado hasta convertirse en un [Agente](https://es.wikipedia.org/wiki/Matrix#Argumento). |
| <a id="notion-context"></a>Contexto (Context) | Información disponible para un LLM durante una llamada al modelo, incluidas las instrucciones, el historial de conversación, los materiales proporcionados y los resultados de las herramientas. El contexto actual puede contener solo una selección o un resumen del historial completo de la [sesión](#notion-session). |
| <a id="notion-context-length"></a>Longitud del contexto (Context length) | Longitud máxima combinada de entrada y salida que un LLM puede procesar de una vez, normalmente medida en tokens, pequeñas unidades de texto. Incluye las instrucciones, el historial de conversación, los materiales proporcionados y la respuesta generada. |
| <a id="notion-session"></a>Sesión (Session) | Interacción continuada con un [agente](#notion-agent), gestionada por un [entorno de ejecución de agentes](<harness/Entorno de ejecución de agentes.md>). Puede contener varios turnos de conversación, cada uno de los cuales suele comenzar con un mensaje del usuario e incluir las respuestas del agente y las operaciones de las herramientas. El entorno conserva el historial de conversación y prepara el [contexto](#notion-context) de cada llamada al modelo; para respetar la [longitud del contexto](#notion-context-length) del modelo, puede seleccionar o resumir partes anteriores del historial. |
| Identificador de material | Referencia estructurada que identifica un material y, cuando corresponde, su versión. Por ejemplo, `Alice_C_F0007_v1.md` identifica un [Claim](#material-claim) por autor, tipo, línea de investigación, número de serie y versión. |
| <a id="notion-research-line-letter"></a>Letra de línea de investigación | Letra, como la `F` de `Alice_C_F0007_v1.md`, que se utiliza para organizar materiales de investigación numerados. Los materiales derivados de un Task heredan su letra, pero reciben sus propios números de serie. La letra predeterminada es `A` cuando no se especifica ninguna línea. |
| <a id="notion-author-key"></a>Clave de autor | Clave estable registrada para un autor humano, como `Alice`, utilizada en los identificadores de materiales y los registros de autoría. |
| Familia de materiales | Versiones conservadas de un mismo material, como `Alice_C_F0007_v1.md` y `Alice_C_F0007_v2.md`. |
| Versión de material | Revisión concreta conservada de un material, como la versión `v1` o `v2` de un Claim. |
| <a id="notion-main-research-agent"></a>Agente principal de investigación | Agente que dirige el trabajo sobre un [Task](#material-task), coordina los subagentes que participen y mantiene la coherencia de los registros de investigación. |
| Ronda de trabajo de un Task | Periodo de trabajo sobre un Task que termina con un registro de los avances, las preguntas sin resolver y el punto de continuación. |
| <a id="notion-git-branch"></a>Rama Git (Branch) | Línea de desarrollo con nombre dentro de un [repositorio Git](<git-repository/Repositorios Git.md#notion-git-repository>) que permite desarrollar cambios por separado de otras líneas de trabajo. |
| <a id="notion-clone"></a>Clonación (Clone) | Copia de un repositorio Git existente en una nueva carpeta local, incluidos sus archivos y su historial de versiones. |
| <a id="notion-commit"></a>Commit | Versión guardada en el historial local de [Git](<git-repository/Repositorios Git.md#notion-git>) que registra cambios seleccionados con un mensaje que los describe. |
| <a id="notion-push"></a>Push | Envío de commits locales a un repositorio Git remoto para que el trabajo registrado esté disponible allí. |
| <a id="notion-pull"></a>Pull | Obtención de los cambios de un repositorio Git remoto e incorporación de estos al trabajo local. |
| <a id="notion-merge"></a>Fusión (Merge) | Integración de los cambios de otra [rama](#notion-git-branch) en la rama Git actual, resolviendo las ediciones en conflicto cuando sea necesario. |
| <a id="notion-intake"></a>Recepción (Intake) | Incorporación a su propio repositorio de materiales de investigación seleccionados de otro repositorio ACME público, conservando su autoría, procedencia y limitaciones de revisión. |
| <a id="notion-import"></a>Importación (Import) | Incorporación al espacio de trabajo actual de sus propios materiales de investigación, manuscritos o preferencias personales aplicables, seleccionados en otra carpeta o repositorio, conservando la autoría y reutilizando los materiales existentes adecuados. Los materiales necesarios de otros autores se obtienen mediante [recepción (Intake)](#notion-intake). |
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
- Cuando se selecciona un Task individual para su ejecución, el agente crea o reutiliza un registro local de ejecución (E) en la copia de trabajo actual para anotar por separado el estado de ejecución, las cuotas vigentes y las condiciones de parada.
- Un Task reúne los materiales de investigación que sustentan su estudio.
  Los manuscritos relacionados, los informes de progreso y los demás documentos que solicite pueden reunirse en un proyecto como `mathematics/manuscripts/Alice/Alice_T_A0007/`.
  Los proyectos de manuscritos se organizan por el autor responsable de la redacción y se vinculan al Task de investigación correspondiente.
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
