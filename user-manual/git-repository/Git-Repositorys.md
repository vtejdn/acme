# Git, Git-Repositorys und GitHub

## <a id="notion-git"></a>Git

Git ist ein verteiltes Versionsverwaltungssystem, das auf Ihrem eigenen Computer läuft.
Es zeichnet Dateiänderungen auf, ermöglicht das Anzeigen und Wiederherstellen früherer Versionen und unterstützt parallele Entwicklungslinien.
Man kann es sich als Speichersystem mit einer Zeitmaschine vorstellen, bei dem jeder gespeicherte Stand ein Commit ist, zu dem Sie zurückkehren können.
Git funktioniert lokal und benötigt keine Netzwerkverbindung.

Die wichtigsten Begriffe sind die folgenden.

- Ein **Commit** ist ein aufgezeichneter Stand mit einer Nachricht und einem eindeutigen Hashwert.
- Ein **Branch** ist eine parallele Entwicklungslinie, etwa `main` oder `feature-x`.
- Ein **Merge** führt die Änderungen eines Branches mit denen eines anderen zusammen.
- Der **Arbeitsbaum** enthält die Dateien, die Sie gerade sehen und bearbeiten.
- Der **Staging-Bereich** enthält die für den nächsten Commit ausgewählten Änderungen.

Häufig verwendete Befehle sind die folgenden.

```bash
git status                         # den Änderungsstatus anzeigen
git diff                           # die tatsächlichen Unterschiede anzeigen
git add FILE                       # eine Änderung vormerken
git commit -m "Describe the change" # einen Stand aufzeichnen
git log                            # die Historie anzeigen
git branch                         # die Branches auflisten
```

## <a id="notion-git-repository"></a>Git-Repository

Ein Git-Repository besteht aus einem Projektverzeichnis und einem versteckten Verzeichnis `.git`.
Das Verzeichnis `.git` speichert die vollständige Commit-Historie, Branches, Tags und Konfiguration.
Die Projektdateien, die Sie bearbeiten, bilden den Arbeitsbaum, während das Repository ihre Versionsgeschichte enthält.

Ein Repository kann ausschließlich auf Ihrem Computer liegen oder mit einem oder mehreren entfernten Repositorys verbunden sein.
Es wird mit `git init` erstellt, mit `git clone` kopiert und mit Befehlen wie `git fetch`, `git pull` und `git push` synchronisiert.
`origin` ist der übliche Name des hauptsächlichen entfernten Repositorys.

Ein Git-Repository enthält mehr als einen Ordner mit Dateien.
Es dokumentiert vollständig und nachvollziehbar, wie diese Dateien ihren aktuellen Stand erreicht haben.

## <a id="notion-github"></a>GitHub

GitHub ist eine Cloud-Plattform zum Hosten von Git-Repositorys und zur Zusammenarbeit.
Sie gehört Microsoft und ist ein von Git unabhängiger Dienst.
GitHub bietet entfernten Speicher, eine Weboberfläche, Pull Requests, Issues, Diskussionen, Berechtigungsverwaltung und Automatisierung mit GitHub Actions.

Git-Repositorys können auch auf GitLab, Gitee, einem Unternehmensserver oder sogar auf einer lokalen Festplatte liegen.
GitHub ist eine verbreitete Hosting- und Kollaborationsplattform, aber keine Voraussetzung für die Nutzung von Git.

### <a id="connect-github"></a>Ein lokales Projekt mit GitHub verbinden

Mit diesen Schritten verbinden Sie einen Projektordner auf Ihrem Computer zum ersten Mal mit GitHub.
Der Projektordner enthält die Dateien, die Sie bearbeiten, während das GitHub-Repository der Online-Speicherort des Projekts ist.
Diese Anleitung verwendet SSH, damit sich Git mit einem Schlüssel auf Ihrem Computer bei GitHub authentifizieren kann.

1. **Melden Sie sich im Browser bei GitHub an.**

   Öffnen Sie [GitHub](https://github.com/) und wählen Sie **Sign in**.
   Wenn Sie ein Konto benötigen, wählen Sie **Sign up** und folgen Sie den Anweisungen zur Bestätigung Ihrer E-Mail-Adresse.
   Verwenden Sie dasselbe Konto, wenn Sie später Ihren SSH-Schlüssel hinzufügen.
   Wenn Sie dem bestehenden Repository eines Mitwirkenden beitreten, folgen Sie zunächst den [Schritten zum Beitritt](../Benutzerhandbuch.md#setup-collaboration), um die Einladung anzunehmen und Ihren Zugriff zu bestätigen.

2. **Erstellen Sie ein leeres Repository für Ihr Projekt.**

   Wenn Ihr Projekt bereits ein GitHub-Repository hat, etwa beim Beitritt zum Repository eines Mitwirkenden, fahren Sie mit Schritt 3 fort.
   Andernfalls öffnen Sie die [Seite zum Erstellen eines Repositorys](https://github.com/new).

   1. Wählen Sie unter **Owner** Ihr GitHub-Konto aus.
   2. Geben Sie unter **Repository name** einen Namen wie `my-math-project` ein.
   3. Legen Sie unter **Visibility** fest, wer das Repository sehen darf.
      Wählen Sie **Private**, um die Sichtbarkeit des Projekts einzuschränken.
   4. Deaktivieren Sie die README-Option und wählen Sie für `.gitignore` und die Lizenz jeweils **None**.
      So erhalten Sie ein leeres Repository für Ihr bestehendes Projekt.
   5. Wählen Sie **Create repository**.

   Siehe die [GitHub-Anleitung zum Erstellen eines Repositorys](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

3. **Bitten Sie Ihren Agenten, Git vorzubereiten.**

   Öffnen Sie für ein bestehendes lokales Projekt dessen Ordner in Ihrer Agenten-Laufzeitumgebung, etwa den Ordner, in dem ACME bereits installiert ist und verwendet wird.
   Wenn Sie dem bestehenden Repository eines Mitwirkenden beitreten, erstellen Sie einen neuen leeren lokalen Ordner und öffnen Sie ihn in Ihrer Agenten-Laufzeitumgebung.
   Senden Sie Ihrem Agenten die [Anweisung zur Installation von Git](../user-instructions/Anweisungsbeispiele.md#install-git).
   Fahren Sie fort, sobald der Agent bestätigt, dass Git bereit ist.

4. **Richten Sie den SSH-Zugriff für Ihr GitHub-Konto ein.**

   Ein SSH-Schlüssel besteht aus zwei Teilen.
   Sie fügen den öffentlichen Schlüssel bei GitHub hinzu, während der private Schlüssel auf dem Computer bleibt, auf dem Git ausgeführt wird.
   Senden Sie Ihrem Agenten die folgende Anfrage.

   > Helfen Sie mir, SSH für mein neues GitHub-Konto einzurichten, und zeigen Sie mir den öffentlichen Schlüssel, den ich hinzufügen soll.

   Falls das Terminal nach der Passphrase des Schlüssels fragt, geben Sie sie dort ein.
   Siehe die [GitHub-Anleitung zum Erstellen eines SSH-Schlüssels und zum Laden in den SSH-Agenten](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

   Fügen Sie den öffentlichen Schlüssel im Browser zu Ihrem GitHub-Konto hinzu.

   1. Kopieren Sie die vollständige Textzeile des öffentlichen Schlüssels, die der Agent bereitgestellt hat.
      Der Dateiname des öffentlichen Schlüssels endet auf `.pub`.
   2. Klicken Sie auf GitHub auf Ihr Profilbild und wählen Sie **Settings**.
      Wählen Sie in der Seitenleiste **SSH and GPG keys** und klicken Sie auf **New SSH key** oder **Add SSH key**.
   3. Geben Sie unter **Title** einen leicht erkennbaren Namen wie `Personal laptop` ein.
      Wählen Sie unter **Key type** die Option **Authentication Key**.
   4. Fügen Sie den öffentlichen Schlüssel in **Key** ein, klicken Sie auf **Add SSH key** und bestätigen Sie bei Aufforderung Ihr Konto.

   Siehe die [GitHub-Anleitung zum Hinzufügen eines öffentlichen Schlüssels](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

   Senden Sie Ihrem Agenten nach dem Hinzufügen des Schlüssels die [Anweisung zum SSH-Verbindungstest](../user-instructions/Anweisungsbeispiele.md#test-github-ssh).
   Fahren Sie fort, sobald der Agent bestätigt, dass GitHub Ihr Konto erkennt.

5. **Verbinden Sie Ihr Projekt mit GitHub.**

   Verwenden Sie für ein bestehendes lokales Projekt die [Verbindungsanweisung](../user-instructions/Anweisungsbeispiele.md#connect-github) und ersetzen Sie die Beispieladresse durch die Adresse des Ziel-Repositorys.
   Zum Beitritt zum bestehenden Repository eines Mitwirkenden verwenden Sie die [Klonanweisung](../user-instructions/Anweisungsbeispiele.md#clone-repo) und bitten den Agenten ausdrücklich, das Repository in den in Schritt 3 vorbereiteten leeren Ordner zu klonen.
   Folgen Sie nach dem Klonen den [Schritten zum Beitritt](../Benutzerhandbuch.md#setup-collaboration), um bei Bedarf Ihre Autorenregistrierung und die Einrichtung der Git-Commit-Identität abzuschließen.
