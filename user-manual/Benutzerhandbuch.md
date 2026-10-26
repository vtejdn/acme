# Benutzerhandbuch

[Anweisungsbeispiele](user-instructions/Anweisungsbeispiele.md) · [Beispiel einer Erklärung zur KI-Unterstützung](ai-disclosure-example.md)

## ACME: Autonomous and Collaborative Mathematical Exploration

ACME ist ein schlankes Rahmenwerk für autonome und kollaborative mathematische Forschung.
Es verbindet Markdown-Regeln für KI-Agenten mit unterstützenden Skripten, um längerfristige Untersuchungen zu ermöglichen und Forschungsergebnisse so festzuhalten, dass sie geprüft, wiederverwendet und weiterentwickelt werden können.
Es verfolgt zwei Hauptziele: autonome KI-Agenten unter der Anleitung menschlicher Mathematiker forschen zu lassen und die Zusammenarbeit zwischen menschlichen Autoren zu unterstützen.

### Menschliche Mathematiker

Menschliche Mathematiker sind dafür verantwortlich:

1. Forschungsfragen, ihren freigegebenen Umfang und Abschlusskriterien festzulegen, um [Forschungsaufgaben (Task)](#material-task) anzustoßen.
2. Gemeinsam mit Agenten die Entwicklung von [Forschungsstrategien](#material-strategy) zu steuern.
3. Ideen beizutragen, mathematische Absichten zu präzisieren, wissenschaftliche Prioritäten zu setzen, Argumente zu hinterfragen, Fragen zu verfeinern und Untersuchungen neu auszurichten.
4. Die Forschungsergebnisse zu verstehen und die Grenzen des mathematischen Wissens zu erkunden.
5. Verantwortung für die mathematischen Ergebnisse zu übernehmen.

### Auf [LLMs](#notion-llm) basierende Agenten

Innerhalb des freigegebenen Umfangs sind autonome Agenten dafür verantwortlich:

1. Literatur zu studieren und die für die Untersuchung benötigten Ergebnisse zu überprüfen.
2. [Forschungsstrategien](#material-strategy) zu entwickeln und zu bewerten, Lücken zu erkennen und im Rahmen des Auftrags gewöhnliche methodische Entscheidungen selbstständig zu treffen.
3. Offene Fragestellungen zu untersuchen und den Geltungsbereich sowie die Grenzen sich abzeichnender Ergebnisse zu klären.
4. Beweise und Gegenbeispiele für konkrete Fragen zu suchen und reproduzierbare Berechnungen durchzuführen, um Beobachtungen, Belege und Einsichten zu gewinnen.
5. Voraussetzungen, Argumente, Belege, Abhängigkeiten, aufschlussreiche gescheiterte Ansätze, offene Fragen und den wesentlichen Forschungsverlauf in geeigneten Forschungsmaterialien festzuhalten, darunter [Claims](#material-claim) und [Ledgers](#material-ledger).
6. Bei Bedarf unabhängige [Prüfungen](#material-review) zu veranlassen und deren Umfang, Befunde und Grenzen zu dokumentieren.
7. Manuskripte nach allgemeinen Standards mathematischen Schreibens und den Präferenzen des verantwortlichen Autors auszuarbeiten und zu prüfen.

### Zusammenarbeit

Mathematiker können über ein gemeinsames [Git-Repository](git-repository.md#notion-git-repository) zusammenarbeiten, Forschungsmaterialien teilen und die Ergebnisse der anderen wiederverwenden.
Das Repository kann auf einer Plattform wie [GitHub](git-repository.md#notion-github) gehostet werden, sodass die Mitwirkenden auf ihren eigenen Geräten arbeiten und Änderungen synchronisieren können.
Siehe die [Abbildung zur Zusammenarbeit über ein Git-Repository](git-repo.png).

Mitwirkende im selben Repository können für ein gemeinsames mathematisches Ziel einen gemeinsamen [Task](#material-task) einrichten, der die gemeinsame Fragestellung, Annahmen und Abschlusskriterien festlegt;
jede teilnehmende Person präzisiert den Umfang ihrer Beteiligung im eigenen Task und organisiert konkrete Forschungsansätze mithilfe von [Strategien (Strategy)](#material-strategy).
Es empfiehlt sich, in Absprache mit den Mitwirkenden unterschiedliche Forschungsstrategien zu wählen, um doppelte mathematische Arbeit zu verringern und KI-Rechenressourcen effizienter zu nutzen.
Für unabhängige Überprüfung, Replikation oder gegenseitige Kontrolle kann bewusst derselbe Forschungsansatz gewählt werden.

Verschiedene Mathematiker oder Teams können auch über Repository-Grenzen hinweg zusammenarbeiten, indem sie ausgewählte Materialien durch [Intake](#notion-intake) übernehmen; siehe die [Abbildung zur repositoryübergreifenden Zusammenarbeit](collaboration.jpg).

### Arbeitsablauf

Forschung beginnt mit einem von Menschen festgelegten [Task](#material-task), der Abschlusskriterien vorgibt.
Agenten sichten zunächst einschlägige lokale Forschungsmaterialien und Literatur und verwenden sie wieder; bei Bedarf suchen sie anschließend im Internet nach weiteren Quellen.
Sie prüfen die Anwendbarkeit von Ergebnissen, entwickeln [Forschungsstrategien](#material-strategy) und wechseln wiederholt zwischen Beweisversuchen, Berechnungen und der Suche nach Gegenbeispielen.
Jeder Versuch liefert Erkenntnisse für den nächsten: nützliche Befunde, Fehlschläge und offene Fragen werden in geeigneten Forschungsmaterialien festgehalten, darunter [Claims](#material-claim) und [Ledgers](#material-ledger).
Strategien werden innerhalb des freigegebenen Ziels angepasst.
Ergebniskandidaten werden einer mathematischen [Prüfung](#material-review) unterzogen; ob ein Task abgeschlossen ist, wird anhand der ursprünglichen Kriterien beurteilt.

Siehe die [Abbildung zum Arbeitsablauf](workflow.jpg).

## <a id="setup"></a>Einrichtung

Für ein neues Forschungsprojekt führen Sie die folgenden Schritte I–III aus.
Wenn Sie einer bestehenden Zusammenarbeit beitreten, richten Sie zunächst Ihre Arbeitsumgebung ein und folgen Sie dann den Schritten zum Beitritt.

### Schritt I. Geeignete [LLMs](#notion-llm) wählen

Vergleichen Sie die Leistung von LLMs bei mathematischen Aufgaben auf Forschungsniveau.
Nutzen Sie [FrontierMath Tier 4](https://epoch.ai/frontiermath/tiers-1-4?tier=Tier+4+%28v2%29&view=graph&tab=leaderboard), [MathArena](https://matharena.ai/models), [Riemann-bench](https://surgehq.ai/benchmarks/riemann-bench) und weitere einschlägige Bewertungen als Orientierung.
Wählen Sie Modelle für mathematische Forschung und Verwaltungsaufgaben unter Berücksichtigung ihrer Quelloffenheit, Zugänglichkeit und Kosten.

### Schritt II. Arbeitsumgebung einrichten

Für individuelle Forschung auf einem einzelnen Gerät verwenden Sie eine geeignete [Agenten-Laufzeitumgebung](agent-harness.md) mit Zugang zu einem leistungsfähigen [LLM](#notion-llm).

1. Installieren Sie eine Agenten-Laufzeitumgebung als eigenständige Anwendung oder innerhalb einer [IDE](agent-harness.md#notion-ide) und melden Sie sich an, sofern dies erforderlich oder gewünscht ist.
2. Wählen Sie auf Ihrem Gerät einen Ordner für das Rahmenwerk und spätere Forschungsmaterialien.
3. Wählen Sie das Modell und den Anbieter in den Einstellungen oder der Modellauswahl.

Um Arbeit zwischen Geräten zu synchronisieren, mit anderen Mathematikern zusammenzuarbeiten oder Ihre Forschungsergebnisse anderen leicht zugänglich zu machen, verwenden Sie ein [Git-Repository](git-repository.md#notion-git-repository) zusammen mit einer Cloud-Plattform wie [GitHub](git-repository.md#notion-github).
Das Rahmenwerk unterstützt Synchronisation und Zusammenarbeit auf Basis von [Git](git-repository.md#notion-git).

4. Installieren Sie Git auf Ihrem Gerät oder bitten Sie einen Agenten in Ihrer gewählten Laufzeitumgebung darum.
5. (Optional) Erstellen Sie bei Bedarf ein Konto bei einem Repository-Hosting-Dienst oder melden Sie sich dort an und verbinden Sie sich anschließend mit einem vorhandenen Repository oder erstellen Sie ein neues.

- Siehe die [Anweisungsbeispiele zur Einrichtung](user-instructions/Anweisungsbeispiele.md#setup).

### Schritt III. Rahmenwerk installieren und initialisieren

Wenn Sie einem bestehenden Forschungs-Repository beitreten, das bereits ACME enthält, folgen Sie stattdessen den Schritten im nächsten Abschnitt.

1. Bitten Sie einen Agenten, das [ACME-Rahmenwerk](https://github.com/vtejdn/acme) in Ihren Projektordner herunterzuladen oder dessen Repository zu [klonen](#notion-clone), wenn Sie [Git](git-repository.md#notion-git) verwenden.
2. Wählen Sie einen eindeutigen Autorenschlüssel, etwa Alice oder Ali, und bitten Sie einen Agenten, Sie als Autor zu registrieren.
   In einer Git-Arbeitsumgebung bitten Sie den Agenten außerdem, diese Arbeitskopie mit Ihrem Autorenschlüssel zu verknüpfen, damit neue Einträge dem richtigen Autor zugeordnet werden.
3. (Optional, bei Verwendung von Git) Konfigurieren Sie den Namen und die E-Mail-Adresse für Ihre [Commits](#notion-commit) oder bitten Sie einen Agenten darum.
4. (Optional, bei Verwendung eines [Git-Repositories](git-repository.md#notion-git-repository)) Wählen Sie einen kurzen, leicht erkennbaren Namen für Ihr Forschungs-Repository und bitten Sie einen Agenten, dessen Repository-Identität einzurichten.
5. (Optional) Wenn es angemessen ist, empfehlen wir nachdrücklich, Ihre Forschungsaufzeichnungen über ein öffentliches Repository zu teilen.

- Siehe die [Anweisungsbeispiele zur Einrichtung](user-instructions/Anweisungsbeispiele.md#setup).

### Einem bestehenden [Git-Repository](git-repository.md#notion-git-repository) als Mitwirkender beitreten

1. Melden Sie sich bei der Repository-Hosting-Plattform an und nehmen Sie die Einladung Ihres Mitautors an.
2. Bitten Sie einen Agenten, Ihnen beim Einrichten des Zugriffs auf das gemeinsame Repository zu helfen.
3. Geben Sie dem Agenten die Repository-Adresse und bitten Sie ihn, das Repository in einen neuen lokalen Ordner zu [klonen](#notion-clone).
   Öffnen Sie diesen Ordner in Ihrer Agenten-Laufzeitumgebung.
4. Wenn Sie im Forschungs-Repository noch nicht registriert sind, wählen Sie einen Autorenschlüssel, der sich von denen Ihrer Mitwirkenden unterscheidet, und bitten Sie einen Agenten, Sie zu registrieren.
   Bitten Sie den Agenten, diese Arbeitskopie in ACME mit Ihrem Autorenschlüssel zu verknüpfen.
5. Konfigurieren Sie den Namen und die E-Mail-Adresse für Ihre [Git](git-repository.md#notion-git)-[Commits](#notion-commit) oder bitten Sie einen Agenten darum.

- Siehe die [Anweisungsbeispiele zur Einrichtung](user-instructions/Anweisungsbeispiele.md#setup).

## Erste Schritte

### Einen Task beginnen

1. (Optional) Stellen Sie einschlägige Literatur bereit oder bitten Sie einen Agenten, sie zu suchen.
   Bitten Sie den Agenten, Quelldateien im [lokalen Literaturordner](../mathematics/literature/pdf) zu speichern und die angegebenen Teile einschlägiger Artikel in der gewünschten Tiefe zu prüfen.
2. Legen Sie im Gespräch mit Agenten einen [Task](#material-task) fest und bestimmen Sie die Fragen, Einschränkungen und Abschlusskriterien.
   Sie können einen [Forschungslinien-Buchstaben](#notion-research-line-letter) wählen, um den Task und seine zugehörigen Materialien zu ordnen.
   Beispiele finden Sie unter [Häufige Anweisungen](#common-instructions).
3. Legen Sie für längerfristige autonome Arbeit Ausführungsgrenzen und Abbruchbedingungen fest oder übernehmen Sie bestehende.
   Siehe die [Beispiele für Forschungsaufträge](user-instructions/Anweisungsbeispiele.md#start-or-continue-research).
4. Genehmigen Sie notwendige Werkzeugaktionen, wenn Sie dazu aufgefordert werden, und beantworten Sie Fragen der Agenten.
5. Durchdenken und verstehen Sie die von Agenten erarbeiteten mathematischen Materialien; kein Agent kann Ihnen dies abnehmen.
   Besprechen Sie die Mathematik mit Agenten, um Ihr Verständnis zu vertiefen und schneller voranzukommen.
   Bitten Sie um einschlägige Literaturangaben und hinterfragen Sie die Quellen von Argumenten und Ideen im sokratischen Gespräch, insbesondere wenn ein Argument ohne ausdrückliche Quellenbelege auf Modellwissen beruht.
6. (Optional, bei Verwendung von [Git](git-repository.md#notion-git)) Halten Sie Änderungen, die Sie bewahren möchten, in einem [Commit](#notion-commit) fest; machen Sie bei Bedarf lokale Bearbeitungen rückgängig oder setzen Sie Commits durch einen Revert zurück.
   Wenn Sie mit anderen Mathematikern zusammenarbeiten, bitten Sie Agenten, [Pushes](#notion-push), [Pulls](#notion-pull) und [Merges](#notion-merge) durchzuführen und beim Lösen von Konflikten zu helfen.

- Siehe die [Anweisungsbeispiele zur Forschung](user-instructions/Anweisungsbeispiele.md#research-instructions).

### Hinweise

- Agenten versuchen, öffentlich zugängliche Literatur in den [lokalen Literaturordner](../mathematics/literature/pdf) herunterzuladen.
  Dieses Verzeichnis wird standardmäßig von [Git](git-repository.md#notion-git) ignoriert.
  Wenn Sie dort eigene private Materialien ablegen, stellen Sie sicher, dass Git dieses Verzeichnis ignoriert und es nicht in ein öffentliches Repository hochgeladen wird.
- Wenn Mitwirkende sonst denselben Autorenschlüssel verwenden würden, vereinbaren Sie unterschiedliche Schlüssel, etwa Wang1 und Wang2.
- Verwenden Sie unterschiedliche [Forschungslinien-Buchstaben](#notion-research-line-letter) für [Tasks](#material-task), die gleichzeitig von getrennten leitenden Forschungsagenten vorangetrieben werden.
  Wählen Sie die Buchstaben beim Einrichten der Tasks, um die Materialnummerierung zu trennen und Schreibkonflikte zu verringern.
  Bitten Sie die Agenten, Änderungen an gemeinsam genutzten Dateien abzustimmen, darunter Indizes, Bibliografie und Repository-Identitätseinträge.
  Zusätzliche parallele Forschungs-Worktrees werden nicht empfohlen; das Rahmenwerk legt dafür keinen Verwaltungsablauf fest.
- ACME leitet Agenten durch schriftliche Regeln und unterstützende Werkzeuge an.
  Wenn ein Agent von Ihren Anweisungen oder den Regeln des Rahmenwerks abweicht, bitten Sie ihn, die Abweichung zu erklären und die betroffene Arbeit zu korrigieren.
- Die Regeln des Rahmenwerks können Mehrdeutigkeiten, Widersprüche oder Lücken enthalten.
  Sie können einen Agenten bitten, die Regeln des Rahmenwerks zu überarbeiten, wenn Sie dies für angemessen halten.
  Sie können sich damit auch an den [Autor](https://github.com/vtejdn) des ACME-Rahmenwerks wenden.

### Nützliche Gewohnheiten

- Fragen Sie einen Agenten, wenn Sie Fragen zum Rahmenwerk haben.
- Wenn Sie Literatur in einem lokalen, von einem Cloud-Dienst synchronisierten Verzeichnis aufbewahren, bitten Sie einen Agenten, den [lokalen Literaturordner](../mathematics/literature/pdf) über eine Verzeichnisverknüpfung (Directory Junction) damit zu verbinden.
  Erteilen Sie dem Agenten die Berechtigungen, die er zum Lesen und Verwalten der Dateien in diesem Verzeichnis benötigt.
- Wenn Agenten zugehörige Aufgaben automatisieren, bei denen Zugangsdaten verwendet werden, bewahren Sie Geheimnisse angemessen auf und schließen Sie sie von [Git](git-repository.md#notion-git) aus.

### Ein Manuskript verfassen

In Arbeit.

### Formalisierung in Lean

In Arbeit.

## Nützliche Informationen

### Version des Rahmenwerks

Die aktuelle Version des Rahmenwerks ist 0.2.0.

Zu Arbeitsbeginn prüft der Agent höchstens einmal pro UTC-Tag, ob eine neuere Version des [offiziellen ACME-Rahmenwerks](https://github.com/vtejdn/acme) verfügbar ist.
Er nennt dann die installierte und die verfügbare Version und fragt, ob ein Upgrade vorbereitet werden soll; Ihre laufende Arbeit kann während Ihrer Entscheidung fortgesetzt werden.
Eine Erinnerung installiert oder aktualisiert keine Dateien, und Sie können das Upgrade zurückstellen.
Sie können die automatischen Prüfungen für dieses Repository deaktivieren oder aktivieren lassen, eine sofortige erneute Prüfung oder ausdrücklich ein Upgrade anfordern.
Wenn die öffentliche Version nicht bestätigt werden kann, meldet der Agent diese Einschränkung und setzt die autorisierte Arbeit fort.

### <a id="common-instructions"></a>Häufige Anweisungen

Die [Anweisungsbeispiele](user-instructions/Anweisungsbeispiele.md) veranschaulichen häufige Anweisungen und erläutern, welche Ergebnisse Sie erwarten können.

### Verzeichnisse im Stammverzeichnis

Einige Verzeichnisse werden erst bei Bedarf angelegt.

| Verzeichnis | Zweck | Bereich |
| --- | --- | --- |
| [mathematics/](../mathematics/readme.md) | Enthält Forschungsmaterialien, Literatureinträge, Berechnungen, Manuskripte und Präsentationen. | Forschungsarbeitsbereich |
| [framework/](../framework/readme.md) | Enthält Regeln des Rahmenwerks, Materialvorlagen, Formatvorgaben und Exportdefinitionen. | Gemeinsames Rahmenwerk |
| [repository/](../repository/readme.md) | Dokumentiert die Repository-Identität, registrierte menschliche Autoren sowie Zuordnungen zu externen Repositories und Autoren. | Gemeinsames Rahmenwerk |
| profiles/ | Enthält persönliche Forschungsrichtlinien, Ausführungspräferenzen und Vorgaben für mathematisches Schreiben. | Persönliche Konfiguration |
| execution/ | Dokumentiert den aktuellen Ausführungszustand, wirksame Grenzen und Abbruchbedingungen jeder gewöhnlichen individuellen Task-Familie. | Task-Ausführung |
| intake/ | Dokumentiert repositoryübergreifende Übernahmen, einschließlich des ausgewählten Umfangs und der Herkunft. | Repositoryübergreifende Wiederverwendung |
| [scripts/](../scripts/readme.md) | Bietet optionale Befehlszeilenwerkzeuge für Registrierung, Navigation, Prüfung, Übernahme, Export und weitere mechanische Vorgänge. | Werkzeuge des Rahmenwerks |
| [user-manual/](./) | Enthält Benutzeranleitungen, Erläuterungen zur Einrichtung und Anweisungsbeispiele. | Dokumentation für Menschen |
| .tmp/ | Enthält verwerfbare Arbeitsdateien, die von Agenten verwendet werden. | Vorübergehende Arbeit |
| .venv/ | Enthält die lokale virtuelle Python-Umgebung und deren installierte Abhängigkeiten. | Lokale Laufzeitumgebung |
| .agents/ | Enthält Agenten-Skills für dieses Repository. | Agentenwerkzeuge |
| .git/ | Enthält die [Git](git-repository.md#notion-git)-Historie, Referenzen, Konfiguration und weitere Metadaten der Versionsverwaltung. | Git-Arbeitsumgebungen |
| .vscode/ | Enthält die VS-Code-Arbeitsbereichskonfiguration und Erweiterungsempfehlungen. | Editorspezifische Konfiguration |
| .codex/ | Enthält die lokale Codex-Konfiguration für den Arbeitsbereich. | Werkzeugspezifische Konfiguration |

### Kategorien von Forschungsmaterialien

| Kürzel | Material | Speicherort | Zweck |
| --- | --- | --- | --- |
| T | [Forschungsaufgabe (Task)](#material-task) | [mathematics/tasks/](../mathematics/tasks/index.md) | Legt eine Forschungsfrage, ihren freigegebenen Umfang und Abschlusskriterien fest und dokumentiert Entscheidungen über ihren Lebenszyklus. |
| S | [Forschungsstrategie (Strategy)](#material-strategy) | [mathematics/strategies/](../mathematics/strategies/index.md) | Entwickelt und bewertet einen Forschungsweg, ordnet Prioritäten und benennt Hindernisse sowie nächste Schritte. |
| C | [Mathematische Aussage (Claim)](#material-claim) | [mathematics/claims/](../mathematics/claims/index.md) | Formuliert präzise mathematische Aussagen, bewahrt ihre Argumente und Abhängigkeiten und dokumentiert ihre mathematischen Bewertungen und Prüfungsbefunde. |
| R | [Prüfbericht (Review)](#material-review) | [mathematics/audits/reviews/](../mathematics/audits/reviews/readme.md) | Dokumentiert mathematische Prüfungen bestimmter projektinterner Argumente, einschließlich der geprüften Eingaben, Befunde, Organisation der Prüfung und Grenzen. |
| D | Entwurf (Draft) | [mathematics/drafts/](../mathematics/drafts/readme.md) | Bietet einen Arbeitsbereich für die Entwicklung mathematischer Argumente, Rechnungen und Alternativen, die noch untersucht werden. |
| L | [Explorationsprotokoll (Ledger)](#material-ledger) | [mathematics/ledger/](../mathematics/ledger/readme.md) | Bewahrt nützliche Untersuchungen, Vergleiche, Synthesen und gescheiterte Ansätze sowie die Gründe und Ergebnisse wesentlicher mathematischer Änderungen. |
| J | Berechnung (Computation) | [mathematics/computations/programs/](../mathematics/computations/readme.md) | Organisiert Programme und erforderliche Eingaben für reproduzierbare Berechnungen und dokumentiert Ausführungsstatus, Ergebnisse und Grenzen. |
| U | Literaturprüfungseinheit (Literature audit unit) | [mathematics/audits/literature/](../mathematics/audits/literature/readme.md) | Macht geprüfte Literatur wiederverwendbar, indem sie Quellenausgabe und Textstellen, mathematischen Inhalt, Anwendbarkeit und Prüfungsgrenzen festhält. |
| — | Manuskript (Manuscript) | [mathematics/manuscripts/](../mathematics/manuscripts/index.md) | Dient der Ausarbeitung von Aufsätzen und zugehörigen mathematischen Dokumenten, einschließlich Darstellung, Zitaten, Schreibvorgaben und Kompilierungsprotokollen. |
| — | Präsentation (Presentation) | [mathematics/presentations/](../mathematics/presentations/readme.md) | Dient der Ausarbeitung von Vorträgen und Folien für ein bestimmtes Publikum, einschließlich Quelldateien, Schreibvorgaben, Kompilierungsinformationen und Prüfberichten. |

- Jede Berechnung hat ein nummeriertes J-Verzeichnis mit ihren Programmen, erforderlichen Eingaben und einer `readme.md`.
  Erzeugte Ausgaben werden getrennt unter dem lokalen, von [Git](git-repository.md#notion-git) ignorierten Pfad `mathematics/computation/outputs/<J>/` gespeichert.
- Literaturprüfungseinheiten sind unter `mathematics/audits/literature/` nach Zitierschlüsseln gruppiert.
- Der [Definitionsindex](../mathematics/definitions/index.md) ordnet Definitionen, Terminologie und Symbole nach Begriffen und verlinkt auf die vollständigen Formulierungen in den zuständigen C-, L- oder U-Materialien.
- Die maßgebliche [Bibliografie](../mathematics/literature/references.bib) dokumentiert die Identität von Veröffentlichungen und deren Zitierschlüssel.
  Quellenbeschaffung, Dateiversionen und Verfügbarkeit werden getrennt im [Literaturregister](../mathematics/literature/registry.md) dokumentiert.

### Grundbegriffe

| Begriff | Bedeutung |
| --- | --- |
| <a id="notion-llm"></a>LLM (Large Language Model) | Ein auf großen Textmengen trainiertes KI-Modell, das Sprache verarbeitet und erzeugt, darunter mathematische Erläuterungen und Computercode. |
| <a id="notion-context-length"></a>Kontextlänge (Context length) | Die maximale Gesamtlänge aus Ein- und Ausgabe, die ein LLM auf einmal verarbeiten kann, üblicherweise in Tokens gemessen, also kleinen Texteinheiten. Dazu zählen Anweisungen, Gesprächsverlauf, bereitgestellte Materialien und die erzeugte Antwort. |
| Materialkennung | Eine strukturierte Referenz, die ein Material und gegebenenfalls dessen Version bezeichnet. Beispielsweise kennzeichnet `Alice_C_F0007_v1.md` einen [Claim](#material-claim) durch Autor, Materialart, Forschungslinie, laufende Nummer und Version. |
| <a id="notion-research-line-letter"></a>Forschungslinien-Buchstabe | Ein Buchstabe, etwa F in `Alice_C_F0007_v1.md`, mit dem nummerierte Forschungsmaterialien geordnet werden. Von einem Task abgeleitete Materialien übernehmen dessen Buchstaben, erhalten jedoch eigene laufende Nummern. Ohne Angabe einer Linie wird standardmäßig A verwendet. |
| Autorenschlüssel | Ein stabiler registrierter Schlüssel für einen menschlichen Autor, etwa Alice, der in Materialkennungen und Autoreneinträgen verwendet wird. |
| Materialfamilie | Die aufbewahrten Versionen desselben Materials, etwa `Alice_C_F0007_v1.md` und `Alice_C_F0007_v2.md`. |
| Materialversion | Eine bestimmte aufbewahrte Überarbeitung eines Materials, etwa die Version `v1` oder `v2` eines Claims. |
| <a id="notion-main-research-agent"></a>Leitender Forschungsagent | Der Agent, der die Arbeit an einem [Task](#material-task) leitet, beteiligte Unteragenten koordiniert und die Forschungsaufzeichnungen konsistent hält. |
| Task-Runde | Ein Arbeitsabschnitt zu einem Task, der mit einer Aufzeichnung des Fortschritts, offener Fragen und eines Ansatzpunkts für die Fortsetzung endet. |
| <a id="notion-git-branch"></a>Git-Branch | Eine benannte Entwicklungslinie in einem [Git-Repository](git-repository.md#notion-git-repository), auf der Änderungen getrennt von anderen Arbeitslinien entwickelt werden können. |
| <a id="notion-clone"></a>Klonen (Clone) | Ein bestehendes Git-Repository einschließlich seiner Dateien und Versionshistorie in einen neuen lokalen Ordner kopieren. |
| <a id="notion-commit"></a>Commit | Ein in der lokalen [Git](git-repository.md#notion-git)-Historie gespeicherter Stand, der ausgewählte Änderungen mit einer erläuternden Nachricht festhält. |
| <a id="notion-push"></a>Push | Lokale Commits an ein entferntes Git-Repository senden, damit die aufgezeichnete Arbeit dort verfügbar ist. |
| <a id="notion-pull"></a>Pull | Änderungen aus einem entfernten Git-Repository abrufen und in die lokale Arbeit integrieren. |
| <a id="notion-merge"></a>Merge | Änderungen aus einem anderen [Branch](#notion-git-branch) in den aktuellen Git-Branch zusammenführen und dabei widersprüchliche Bearbeitungen bei Bedarf auflösen. |
| <a id="notion-intake"></a>Übernahme (Intake) | Ausgewählte Forschungsmaterialien aus einem anderen ACME-Repository in das eigene übernehmen und dabei Autorenschaft, Herkunft und Prüfungsgrenzen bewahren. |
| Zitierschlüssel | Eine kurze Kennung für ein Werk in der Bibliografie, mit der es in Forschungsaufzeichnungen und Manuskripten einheitlich zitiert werden kann. |

### <a id="material-task"></a>Forschungsaufgabe (Task)

Ein Task organisiert Forschung um ein präzises mathematisches Ziel, seinen freigegebenen Umfang und vereinbarte Abschlusskriterien.

| Task-Status | Bedeutung für den Leser |
| --- | --- |
| `proposed` | Eine Forschungsfrage wurde vorgeschlagen, ist aber noch kein aktives Forschungsziel. |
| `active` | Die Untersuchung ist freigegeben und wird weitergeführt. |
| `paused` | Die Untersuchung ist bewusst unterbrochen; die Absicht und eine ausdrücklich genannte Grundlage zur Fortsetzung sind festgehalten. |
| `blocked` | Eine konkret fehlende Eingabe oder unerfüllte Voraussetzung verhindert den nächsten notwendigen Schritt. Der Eintrag erläutert, was für weitere Fortschritte benötigt wird. |
| `completed` | Die vereinbarten Abschlusskriterien sind mit unterstützenden mathematischen Belegen und der erforderlichen Prüfung erfüllt. |
| `retired` | Die Untersuchung wurde eingestellt. Gründe, nützliche Befunde und unvollendete Teile bleiben dokumentiert. |

- Ein Task kann aktiv bleiben, auch wenn gerade kein Agent daran arbeitet.
- Ein Task führt die Forschungsmaterialien zusammen, die Ihre Untersuchung unterstützen.
  Zugehörige Manuskripte, Fortschrittsberichte und andere von Ihnen angeforderte Dokumente können in einem Projekt wie `mathematics/manuscripts/Alice_T_A0007/` gesammelt werden.
- Sie können darum bitten, einen abgeschlossenen Task für weitere Arbeit am betreffenden Forschungsziel zu reaktivieren.
  Erläutern Sie, was Sie als Nächstes untersuchen möchten und welche Änderungen an Umfang oder Grenzen vorgesehen sind.
  Ein wesentlich anderes Forschungsziel sollte als neuer Task angelegt werden.

### <a id="material-strategy"></a>Forschungsstrategie (Strategy)

Eine Strategy beschreibt einen konkreten Weg zu einem Forschungsziel, einschließlich ihres Mechanismus, verbleibender Hindernisse und der nächsten sinnvollen Schritte.

| Strategy-Status | Bedeutung für den Leser |
| --- | --- |
| `proposed` | Ein möglicher Ansatz wurde erkannt, aber noch nicht für die aktuelle Untersuchung ausgewählt. |
| `active` | Der Weg ist derzeit für die Forschung am Ziel des Tasks ausgewählt. |
| `paused` | Der Weg ist wegen Prioritäten, Arbeitsreihenfolge oder verfügbarer Ressourcen vorübergehend zurückgestellt. Dies bedeutet keinen mathematischen Fehlschlag. |
| `blocked` | Eine konkrete unerfüllte Voraussetzung verhindert den nächsten geplanten Schritt. Der Eintrag benennt das Hindernis und die Bedingungen, unter denen der Weg fortgesetzt werden könnte. |
| `completed` | Der Weg hat sein angegebenes Ergebnis oder seinen Beitrag mit den erforderlichen Belegen erbracht. Zum Abschluss des Tasks kann weitere Arbeit nötig sein. |
| `refuted` | Geprüfte mathematische Belege schließen den dokumentierten Mechanismus oder eine dafür erforderliche Hilfsaussage unter den genannten Voraussetzungen aus. |
| `superseded` | Der Weg wurde durch benannte Nachfolgestrategien ersetzt oder in einen anderen Weg aufgenommen. Seine Geschichte und nützlichen Befunde bleiben zugänglich. |

- Ein [Task](#material-task) kann mehrere Strategien haben, entweder als Alternativen oder als Bestandteile eines kombinierten Ansatzes.
  Der Abschluss, die Unterbrechung oder der Ausschluss einer einzelnen Strategie bestimmt für sich genommen nicht den Status des gesamten Tasks.
- Sie können Ansätze vorschlagen, den Agenten um einen Vergleich von Alternativen bitten oder Prioritäten vorgeben.
  Geben Sie ausdrücklich an, wenn eine Priorität oder Reihenfolge unverändert bleiben muss; andernfalls kann der Agent seine Auswahl von Wegen innerhalb des vereinbarten Umfangs anpassen.
- Innerhalb des freigegebenen Umfangs dürfen autonome Agenten Strategien je nach Befunden und Ressourcen hinzufügen, überarbeiten, neu priorisieren, aufteilen, zusammenführen, unterbrechen oder erneut aufnehmen.
- Ein gescheiterter Weg kann dennoch aufschlussreich sein.
  Er kann ein Hindernis aufdecken, einen Ansatz ausschließen oder zeigen, wo eine zusätzliche Voraussetzung nötig wäre.

### <a id="material-claim"></a>Mathematische Aussage (Claim)

Ein Claim dokumentiert eine wichtige, präzise mathematische Aussage und den aktuellen Kenntnisstand zu ihrer Gültigkeit.

| Mathematischer Status | Bedeutung für den Leser |
| --- | --- |
| `open` | Die genaue Aussage ist weiterhin ungeklärt. Es können Teilergebnisse, Reduktionen oder ein vorläufiges Argument vorliegen, doch die Bedingungen für bewiesen oder widerlegt sind noch nicht erfüllt. |
| `proved` | Ein vollständiger Beweis begründet die genaue Aussage unter ihren angegebenen Voraussetzungen. Alle notwendigen unterstützenden Ergebnisse sind gesichert und anwendbar; eine dokumentierte mathematische [Prüfung](#material-review) hat keine verbleibende Lücke festgestellt. |
| `refuted` | Ein geprüftes Gegenbeispiel oder Argument widerlegt die genaue Aussage innerhalb ihres angegebenen Geltungsbereichs. Alle notwendigen unterstützenden Ergebnisse sind gesichert und anwendbar; eine dokumentierte mathematische Prüfung hat keine verbleibende Lücke festgestellt. |

### <a id="material-review"></a>Prüfbericht (Review)

Ein Review dokumentiert die Prüfung einer mathematischen Aussage oder eines Arguments durch einen Agenten, einschließlich der genauen Eingaben und des Umfangs, der Befunde und verbleibender Einschränkungen.

| Prüfungsverhältnis | Bedeutung für den Leser |
| --- | --- |
| `self-reviewed` | Der Beweis wurde von einem Agenten geprüft, der an seiner Entwicklung beteiligt war oder mit der mathematischen Diskussion vertraut ist, aus der er hervorgegangen ist. |
| `independently reviewed` | Ein anderer Agent prüfte den Beweis, ohne an dessen Entwicklung beteiligt gewesen zu sein oder die Entwicklungsdiskussion als eigenen Kontext erhalten zu haben. |
| `unknown` | Das tatsächliche Verhältnis einer älteren oder aus einer Quelle stammenden Prüfung ist nicht geklärt; dies bedeutet weder einen Fehler noch eine unabhängige Prüfung. |

- Diese Bezeichnungen beschreiben das Verhältnis der prüfenden Agenten zum Beweis, nicht dessen Richtigkeit.
  Eine fehlende Angabe des Prüfungsverhältnisses unterscheidet sich von `unknown`; ist keine Prüfung ausgewählt, verwendet der Claim keine Prüfungsbelege.
- Auch die Prüfung durch einen anderen Agenten gilt als Selbstprüfung, wenn dieser Diskussionen zur Beweisentwicklung, mathematische Zusammenfassungen, Erläuterungen des Autors oder frühere Prüfungsbefunde übernimmt.
  Eine andere Sitzung oder ein anderes Modell allein begründet keine Unabhängigkeit.
- Der [leitende Forschungsagent](#notion-main-research-agent) veranlasst unabhängige Prüfungen an zentralen Beweisstellen und nach Abschluss des [Task](#material-task) für die gesamte logische Kette.
  Sie können auch die Prüfung eines bestimmten Ergebnisses oder Beweisschritts anfordern.

### <a id="material-ledger"></a>Explorationsprotokoll (Ledger)

Ein Ledger bewahrt nützliche mathematische Untersuchungen, darunter Vergleiche, gescheiterte Ansätze und Gründe für Richtungsänderungen.
Ein Eintrag kann erläutern, was unter welchen Voraussetzungen untersucht wurde, was versucht wurde, was die Argumentation oder die Belege zeigten und was offenbleibt.

Ein Ledger kann Teilargumente und nützliche Einsichten bewahren, auch wenn eine Untersuchung noch keinen eigenständigen [Claim](#material-claim) hervorgebracht hat.
Gescheiterte oder ergebnisoffene Versuche können beispielsweise Hindernisse sichtbar machen, Ansätze voneinander abgrenzen oder helfen, wiederholte Arbeit zu vermeiden.

- Sie können einen Agenten bitten, [Strategien](#material-strategy) zu vergleichen, einen gescheiterten Versuch zu erklären, Erkenntnisse aus mehreren Quellen zusammenzuführen oder einen nützlichen Gedankengang für spätere Arbeit festzuhalten.
- Sie können einen Agenten auch bitten, alles festzuhalten, was Sie für mathematisch wesentlich und aufzeichnungswürdig halten.
