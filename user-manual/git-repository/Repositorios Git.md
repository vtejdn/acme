# Git, repositorios Git y GitHub

## <a id="notion-git"></a>Git

Git es un sistema de control de versiones distribuido que se ejecuta en su propio ordenador.
Registra los cambios en los archivos, permite consultar o restaurar versiones anteriores y admite líneas de desarrollo paralelas.
Puede imaginarlo como un sistema de guardado con una máquina del tiempo, donde cada guardado es un commit al que puede volver.
Git funciona de forma local y no necesita conexión de red.

Los conceptos principales son los siguientes.

- Un **commit** es una instantánea registrada con un mensaje y un hash único.
- Una **rama** es una línea de desarrollo paralela, como `main` o `feature-x`.
- Una **fusión** integra los cambios de una rama en otra.
- El **árbol de trabajo** contiene los archivos que ve y edita en ese momento.
- El **área de preparación** contiene los cambios seleccionados para el siguiente commit.

Estos son algunos comandos habituales.

```bash
git status                         # mostrar el estado de los cambios
git diff                           # mostrar las diferencias exactas
git add FILE                       # preparar un cambio
git commit -m "Describe the change" # registrar una instantánea
git log                            # consultar el historial
git branch                         # listar las ramas
```

## <a id="notion-git-repository"></a>Repositorio Git

Un repositorio Git consta de un directorio de proyecto y un directorio oculto `.git`.
El directorio `.git` almacena el historial completo de commits, las ramas, las etiquetas y la configuración.
Los archivos del proyecto que edita constituyen el árbol de trabajo, mientras que el repositorio conserva su historial de versiones.

Un repositorio puede permanecer solo en su ordenador o conectarse a uno o varios repositorios remotos.
Se crea con `git init`, se copia con `git clone` y se sincroniza con comandos como `git fetch`, `git pull` y `git push`.
`origin` es el nombre convencional del repositorio remoto principal.

Un repositorio Git contiene más que una carpeta de archivos.
Conserva un registro completo y consultable de cómo llegaron esos archivos a su estado actual.

## <a id="notion-github"></a>GitHub

GitHub es una plataforma en la nube para alojar repositorios Git y colaborar.
Pertenece a Microsoft y es un servicio distinto de Git.
GitHub ofrece almacenamiento remoto, una interfaz web, solicitudes de incorporación de cambios, incidencias, debates, gestión de permisos y automatización mediante GitHub Actions.

Los repositorios Git también pueden alojarse en GitLab, Gitee, un servidor de empresa o incluso un disco local.
GitHub es una plataforma habitual de alojamiento y colaboración, pero su uso no es necesario para utilizar Git.

### <a id="connect-github"></a>Conectar un proyecto local a GitHub

Siga estos pasos para conectar por primera vez una carpeta de proyecto de su ordenador a GitHub.
La carpeta del proyecto contiene los archivos que edita, mientras que el repositorio de GitHub es la ubicación en línea del proyecto.
Esta guía utiliza SSH para que Git se autentique en GitHub mediante una clave de su ordenador.

1. **Inicie sesión en GitHub desde su navegador.**

   Abra [GitHub](https://github.com/) y seleccione **Sign in**.
   Si necesita una cuenta, seleccione **Sign up** y siga las instrucciones para verificar su dirección de correo electrónico.
   Utilice esta misma cuenta cuando añada su clave SSH más adelante.
   Si se incorpora al repositorio existente de un colaborador, siga primero los [pasos para incorporarse a la colaboración](<../Manual de usuario.md#setup-collaboration>) para aceptar la invitación y confirmar sus permisos de acceso.

2. **Cree un repositorio vacío para su proyecto.**

   Si el proyecto ya tiene un repositorio de GitHub, por ejemplo cuando se incorpora al repositorio de un colaborador, pase al paso 3.
   En caso contrario, abra la [página de creación de repositorios](https://github.com/new).

   1. En **Owner**, seleccione su cuenta de GitHub.
   2. En **Repository name**, introduzca un nombre como `my-math-project`.
   3. En **Visibility**, elija quién podrá ver el repositorio.
      Seleccione **Private** para restringir la visibilidad del proyecto.
   4. Desactive la opción de añadir un README y elija **None** para las opciones de `.gitignore` y licencia.
      Así obtendrá un repositorio vacío para su proyecto existente.
   5. Seleccione **Create repository**.

   Consulte la [guía de GitHub para crear un repositorio](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

3. **Pida a su agente que prepare Git.**

   Para un proyecto local existente, abra su carpeta en el entorno de ejecución de agentes, por ejemplo la carpeta donde ACME ya está instalado y en uso.
   Si se incorpora al repositorio existente de un colaborador, cree una nueva carpeta local vacía y ábrala en el entorno de ejecución de agentes.
   Envíele la [instrucción de instalación de Git](<../user-instructions/Ejemplos de instrucciones.md#install-git>).
   Continúe cuando el agente confirme que Git está listo.

4. **Configure el acceso SSH para su cuenta de GitHub.**

   Una clave SSH consta de dos partes.
   La clave pública se añade a GitHub, mientras que la clave privada permanece en el ordenador donde se ejecuta Git.
   Envíe la siguiente solicitud a su agente.

   > Ayúdeme a configurar SSH para mi nueva cuenta de GitHub y muéstreme la clave pública que debo añadir.

   Si el terminal solicita la frase de contraseña de la clave, introdúzcala allí.
   Consulte la [guía de GitHub para crear una clave SSH y añadirla al agente SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

   Añada la clave pública a su cuenta de GitHub desde el navegador.

   1. Copie la línea completa de texto de la clave pública proporcionada por el agente.
      El nombre del archivo de clave pública termina en `.pub`.
   2. En GitHub, haga clic en su foto de perfil y elija **Settings**.
      En la barra lateral, seleccione **SSH and GPG keys** y haga clic en **New SSH key** o **Add SSH key**.
   3. En **Title**, introduzca un nombre que pueda reconocer, como `Personal laptop`.
      En **Key type**, elija **Authentication Key**.
   4. Pegue la clave pública en **Key**, haga clic en **Add SSH key** y confirme su cuenta si se le solicita.

   Consulte las [instrucciones de GitHub para añadir una clave pública](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

   Después de añadir la clave, envíe a su agente la [instrucción para probar la conexión SSH](<../user-instructions/Ejemplos de instrucciones.md#test-github-ssh>).
   Continúe cuando el agente confirme que GitHub reconoce su cuenta.

5. **Conecte su proyecto a GitHub.**

   Para un proyecto local existente, utilice la [instrucción de conexión](<../user-instructions/Ejemplos de instrucciones.md#connect-github>) y sustituya la dirección de ejemplo por la del repositorio de destino.
   Para incorporarse al repositorio existente de un colaborador, utilice la [instrucción de clonación](<../user-instructions/Ejemplos de instrucciones.md#clone-repo>) e indique explícitamente al agente que lo clone en la carpeta vacía preparada en el paso 3.
   Después de clonar, siga los [pasos para incorporarse a la colaboración](<../Manual de usuario.md#setup-collaboration>) para completar, cuando sea necesario, el registro como autor y la configuración de la identidad de los commits de Git.
