# Benutzerhandbuch

[Anweisungsbeispiele](user-instructions/Anweisungsbeispiele.md) · [Beispiel einer Erklärung zur KI-Nutzung](ai-disclosure-example.md) · [Beispiel einer Veröffentlichungsseite](publication-example.md) · [Repository-Beispiele](https://github.com/vtejdn/acme/discussions/1)

## ACME: Autonomous and Collaborative Mathematical Exploration

ACME ist ein schlankes Rahmenwerk für autonome und kollaborative mathematische Forschung.
Es verbindet Markdown-Regeln für [KI-Agenten](#notion-agent) mit unterstützenden Skripten, um längerfristige Untersuchungen zu ermöglichen und Forschungsergebnisse so festzuhalten, dass sie geprüft, wiederverwendet und weiterentwickelt werden können.
Es verfolgt zwei Hauptziele: autonome KI-Agenten unter der Anleitung menschlicher Mathematiker forschen zu lassen und die Zusammenarbeit zwischen menschlichen Autoren zu unterstützen.

Wir ermutigen Sie, Ihre gesamte Forschung [vollständig offen](https://github.com/vtejdn/acme/discussions/1) durchzuführen und die vollständigen Forschungsaufzeichnungen in einem öffentlichen Repository zu führen.
Bei öffentlichen Repositorys erfassen ACME-Agenten Änderungen an den Forschungsmaterialien standardmäßig zeitnah in Commits und übertragen sie per Push, damit Ihre Kollegen den Fortschritt Ihrer Arbeit verfolgen können.
ACME-Agenten wählen außerdem selbstständig relevante Forschungsmaterialien aus anderen öffentlichen ACME-Repositorys aus und verwenden sie über [Intake](#notion-intake) wieder, wobei sie die jeweiligen Lizenzen beachten und die Angaben zu Autorenschaft und Herkunft erhalten.
**Wenn Sie Ihr ACME-Repository unter der standardmäßig verwendeten [Apache-Lizenz 2.0](../LICENSE) öffentlich machen, erlauben Sie anderen Personen und ihren Agenten, die von Ihren Agenten generierten Materialien ohne gesonderte Genehmigung wiederzuverwenden.**

### Menschliche Mathematiker

Menschliche Mathematiker sind dafür verantwortlich:

1. Forschungsfragen, ihren freigegebenen Umfang und Abschlusskriterien festzulegen, um [Forschungsaufgaben (Task)](#material-task) anzustoßen.
2. Gemeinsam mit [Agenten](#notion-agent) [Forschungsstrategien](#material-strategy) auszuwählen, zu bewerten und anzupassen.
3. Ideen beizutragen, mathematische Absichten zu präzisieren, wissenschaftliche Prioritäten zu setzen, Argumente zu hinterfragen, Fragen zu verfeinern und Untersuchungen neu auszurichten.
4. Die Forschungsergebnisse zu verstehen und die Grenzen des mathematischen Wissens zu erkunden.
5. Verantwortung für die mathematischen Ergebnisse zu übernehmen.

### Auf [LLMs](#notion-llm) basierende Agenten

Innerhalb des freigegebenen Umfangs sind autonome [Agenten](#notion-agent) dafür verantwortlich:

1. Literatur zu studieren und die für die Untersuchung benötigten Ergebnisse zu überprüfen.
2. [Forschungsstrategien](#material-strategy) zu entwickeln und zu bewerten, Lücken zu erkennen und im Rahmen des Auftrags gewöhnliche methodische Entscheidungen selbstständig zu treffen.
3. Offene Fragestellungen zu untersuchen und den Geltungsbereich sowie die Grenzen sich abzeichnender Ergebnisse zu klären.
4. Beweise und Gegenbeispiele für konkrete Fragen zu suchen und reproduzierbare Berechnungen durchzuführen, um Beobachtungen, Belege und Einsichten zu gewinnen.
5. Voraussetzungen, Argumente, Belege, Abhängigkeiten, aufschlussreiche gescheiterte Ansätze, offene Fragen und den wesentlichen Forschungsverlauf in geeigneten Forschungsmaterialien festzuhalten, darunter [Claims](#material-claim) und [Ledgers](#material-ledger).
6. Bei Bedarf unabhängige [Prüfungen](#material-review) zu veranlassen und deren Umfang, Befunde und Grenzen zu dokumentieren.
7. Manuskripte nach allgemeinen Standards mathematischen Schreibens und den Präferenzen des verantwortlichen Autors auszuarbeiten und zu prüfen.

### Arbeitsablauf

Forschung beginnt mit einem von Menschen festgelegten [Task](#material-task), der Abschlusskriterien vorgibt.
[Agenten](#notion-agent) sichten zunächst einschlägige lokale Forschungsmaterialien und Literatur und verwenden sie wieder; bei Bedarf suchen sie anschließend im Internet nach weiteren Quellen.
Sie prüfen die Anwendbarkeit von Ergebnissen, entwickeln [Forschungsstrategien](#material-strategy) und wechseln wiederholt zwischen Beweisversuchen, Berechnungen und der Suche nach Gegenbeispielen.
Jeder Versuch liefert Erkenntnisse für den nächsten: nützliche Befunde, Fehlschläge und offene Fragen werden in geeigneten Forschungsmaterialien festgehalten, darunter [Claims](#material-claim) und [Ledgers](#material-ledger).
Strategien werden innerhalb des freigegebenen Ziels angepasst.
Ergebniskandidaten werden einer mathematischen [Prüfung](#material-review) unterzogen; ob ein Task abgeschlossen ist, wird anhand der ursprünglichen Kriterien beurteilt.

Siehe die [Abbildung zum Arbeitsablauf](workflow.jpg).

### Zusammenarbeit

ACME bietet zwei Möglichkeiten zur Zusammenarbeit und zum Austausch von Materialien.

- Mathematiker können über ein gemeinsames [Git-Repository](git-repository/Git-Repositorys.md#notion-git-repository) [zusammenarbeiten](#joint-task), Forschungsmaterialien teilen und die Ergebnisse der anderen wiederverwenden.
  Das Repository kann auf einer Plattform wie [GitHub](git-repository/Git-Repositorys.md#notion-github) gehostet werden, sodass die Mitwirkenden auf ihren eigenen Geräten arbeiten und Änderungen synchronisieren können.
  Siehe die [Abbildung zur Zusammenarbeit über ein Git-Repository](git-repo.png).

- Verschiedene Mathematiker oder Teams können auch über Repository-Grenzen hinweg zusammenarbeiten, indem sie ausgewählte Materialien durch [Übernahme (Intake)](#notion-intake) beziehen.
  Sie können Forschungsmaterialien über ein öffentliches Git-Repository mit der standardmäßigen [Apache-2.0-Lizenz](../LICENSE) teilen.
  Andere Personen und ihre Agenten dürfen die dort von Ihren Agenten erzeugten Materialien ohne gesonderte Erlaubnis wiederverwenden.
  ACME-Agenten wählen durch Übernahme (Intake) selbstständig relevante Forschungsmaterialien aus anderen öffentlichen ACME-Repositories aus und verwenden sie wieder, wobei sie deren Lizenzen beachten und Autorenschaft sowie Herkunft bewahren.
  Im aktuellen öffentlichen Repository können Sie eine [Importanweisung](#notion-import) geben, um Materialien aus Ihren anderen, auch privaten Repositories auszuwählen, die Sie öffentlich machen möchten, und hierher zu importieren.
  Siehe die [Abbildung zur repositoryübergreifenden Zusammenarbeit](collaboration.jpg).

### Erklärung zur KI-Nutzung

Geben Sie bei der Veröffentlichung von Forschungsergebnissen wahrheitsgemäß an, wie Sie das ACME-Rahmenwerk verwendet haben.
Wenn Sie einen Preprint auf Plattformen wie [arXiv](https://arxiv.org/) oder [Hexagon](https://hexagonmath.org/) veröffentlichen oder einen Beitrag bei einer Fachzeitschrift einreichen, empfehlen wir, einen Link zu Ihrem öffentlichen ACME-Git-Repository anzugeben, damit Fachkollegen und Gutachter die zugehörigen Materialien und vollständigen Forschungsaufzeichnungen einsehen, Argumente prüfen, den Forschungsprozess nachvollziehen und die Arbeit beurteilen können.
Als Vorlage dient das [Beispiel einer Erklärung zur KI-Nutzung](./ai-disclosure-example.md).
Sie können sich auch am [Beispiel einer Veröffentlichungsseite](./publication-example.md) orientieren, um den Grad des Verständnisses und die konkreten Beiträge der menschlichen Autoren darzustellen und Ihre Haltung zum Teilen und Wiederverwenden unbearbeiteter, von Agenten erzeugter Materialien zu erläutern.

## <a id="setup"></a>Einrichtung

Für ein neues Forschungsprojekt führen Sie die folgenden Schritte I–III aus.
Wenn Sie einer bestehenden Zusammenarbeit beitreten, richten Sie zunächst [Ihre Arbeitsumgebung](#setup-workplace) ein und folgen Sie dann den [Schritten zum Beitritt](#setup-collaboration).

### Schritt I. Geeignete [LLMs](#notion-llm) wählen

Vergleichen Sie die Leistung von LLMs bei mathematischen Aufgaben auf Forschungsniveau.
Nutzen Sie [FrontierMath Tier 4](https://epoch.ai/frontiermath/tiers-1-4?tier=Tier+4+%28v2%29&view=graph&tab=leaderboard), [MathArena](https://matharena.ai/models), [Riemann-bench](https://surgehq.ai/benchmarks/riemann-bench) und weitere einschlägige Bewertungen als Orientierung.
Wählen Sie Modelle für mathematische Forschung und Verwaltungsaufgaben unter Berücksichtigung ihrer Quelloffenheit, Zugänglichkeit und Kosten.

### <a id="setup-workplace"></a>Schritt II. Arbeitsumgebung einrichten

Wählen Sie eine geeignete [Agenten-Laufzeitumgebung](harness/Agenten-Laufzeitumgebung.md) und verbinden Sie sie mit einem leistungsfähigen [LLM](#notion-llm).

1. Installieren Sie eine Agenten-Laufzeitumgebung als eigenständige Anwendung oder innerhalb einer [IDE](harness/Agenten-Laufzeitumgebung.md#notion-ide) und melden Sie sich an, sofern dies erforderlich oder gewünscht ist.
2. Wählen Sie das Modell und den Anbieter in den Einstellungen oder der Modellauswahl.
3. Wählen Sie auf Ihrem Gerät einen Ordner für das Rahmenwerk und spätere Forschungsmaterialien.
   Verwenden Sie für die Erstinstallation in einem neuen Projekt einen lokalen Ordner, der noch keine Projektinhalte enthält.
   Wenn Sie einem bestehenden ACME-Forschungsrepository beitreten möchten, folgen Sie den Schritten zum [Beitritt zu einem bestehenden Git-Repository als Mitwirkender](#setup-collaboration).

Ohne [Git](git-repository/Git-Repositorys.md#notion-git) ist persönliche Forschung auf Ihrem lokalen Gerät der Standard.
Um Arbeit zwischen Geräten zu synchronisieren oder über ein gemeinsames [Git-Repository](git-repository/Git-Repositorys.md#notion-git-repository) zusammenzuarbeiten, können Sie eine Hosting-Plattform wie [GitHub](git-repository/Git-Repositorys.md#notion-github) wählen.
Wenn bereits ein entferntes Repository ausgewählt ist, prüfen Sie vor der Erstinstallation, dass auch dieses noch keine Projektinhalte enthält.

Wählen Sie beim Erstellen eines GitHub-Repositorys nach Bedarf zwischen privat und öffentlich.
Ob Sie das Repository öffentlich machen und ob Sie Forschungsaufzeichnungen zur geräteübergreifenden Synchronisierung oder Zusammenarbeit pushen, sind getrennte Entscheidungen.

4. (Optional) Installieren Sie Git auf Ihrem Gerät oder bitten Sie einen [Agenten](#notion-agent) in Ihrer gewählten Laufzeitumgebung darum.
   Ein Anweisungsbeispiel finden Sie unter [Git installieren](user-instructions/Anweisungsbeispiele.md#install-git).
5. (Optional) Erstellen Sie ein Konto bei einem Repository-Hosting-Dienst oder melden Sie sich dort an und verbinden Sie sich anschließend mit einem vorhandenen Repository oder erstellen Sie ein neues.
   Eine schrittweise Anleitung finden Sie unter [Ein lokales Projekt mit GitHub verbinden](git-repository/Git-Repositorys.md#connect-github).

### Schritt III. Rahmenwerk installieren und initialisieren

Wenn Sie einem bestehenden Forschungs-Repository beitreten, das bereits ACME enthält, folgen Sie stattdessen den Schritten im nächsten Abschnitt.

1. Bitten Sie einen [Agenten](#notion-agent), das [ACME-Rahmenwerk](https://github.com/vtejdn/acme) herunterzuladen und in Ihrem Projektordner zu installieren.
   Ein Anweisungsbeispiel finden Sie unter [ACME installieren](user-instructions/Anweisungsbeispiele.md#install-acme).
2. Wählen Sie einen eindeutigen [Autorenschlüssel](#notion-author-key), etwa `Alice` oder `Ali`, und wählen Sie unabhängig davon den Namen für die Namensnennung in `LICENSE`.
   Bitten Sie einen Agenten, Sie als Autor zu registrieren und diese Namensnennung hinzuzufügen.
   Ein Anweisungsbeispiel finden Sie unter [Autor registrieren](user-instructions/Anweisungsbeispiele.md#register).
3. (Bei Verwendung von Git) Konfigurieren Sie den Namen und die E-Mail-Adresse für Ihre [Commits](#notion-commit) oder bitten Sie einen Agenten darum.
   Ein Anweisungsbeispiel finden Sie unter [Git einrichten](user-instructions/Anweisungsbeispiele.md#setup-git).
4. (Bei Verwendung von Git) Wählen oder bestätigen Sie den Schlüssel für Ihr [Forschungsrepository](git-repository/Git-Repositorys.md#notion-git-repository) und bitten Sie einen Agenten, ihn korrekt im Rahmenwerk zu vermerken; ein Beispiel finden Sie unter [Repository-Schlüssel festlegen](user-instructions/Anweisungsbeispiele.md#setup-repo).
5. (Optional) Wenn es angemessen ist, empfehlen wir nachdrücklich, Ihre Forschungsaufzeichnungen über ein öffentliches Repository zu teilen.

### <a id="setup-collaboration"></a>Einem bestehenden [Git-Repository](git-repository/Git-Repositorys.md#notion-git-repository) als Mitwirkender beitreten

1. Melden Sie sich bei der Repository-Hosting-Plattform an und nehmen Sie die Einladung Ihres Mitautors an.
2. Bitten Sie einen [Agenten](#notion-agent), beim Einrichten des Zugriffs auf die Hosting-Plattform des entfernten Repositorys zu helfen; siehe [Mit GitHub verbinden](git-repository/Git-Repositorys.md#connect-github).
3. Erstellen Sie auf Ihrem Computer einen neuen lokalen Ordner und öffnen Sie ihn in Ihrer Agenten-Laufzeitumgebung.
   Geben Sie Ihrem Agenten die Repository-Adresse und bitten Sie ihn, das Repository in diesen leeren Ordner zu [klonen](#notion-clone).
   Ein Anweisungsbeispiel finden Sie unter [Repository klonen](user-instructions/Anweisungsbeispiele.md#clone-repo).
4. Wenn Sie im Forschungs-Repository noch nicht registriert sind, wählen Sie einen Autorenschlüssel, der sich von denen Ihrer Mitwirkenden unterscheidet, und unabhängig davon den Namen für die Namensnennung in `LICENSE`, und bitten Sie dann einen Agenten, Sie zu registrieren und diese Namensnennung hinzuzufügen.
   Ein Anweisungsbeispiel finden Sie unter [Autor registrieren](user-instructions/Anweisungsbeispiele.md#register).
5. Konfigurieren Sie den Namen und die E-Mail-Adresse für Ihre [Git](git-repository/Git-Repositorys.md#notion-git)-[Commits](#notion-commit) oder bitten Sie einen Agenten darum.
   Ein Anweisungsbeispiel finden Sie unter [Git einrichten](user-instructions/Anweisungsbeispiele.md#setup-git).

## Mit der Forschung beginnen

### Einen [Task](#material-task) beginnen

1. (Optional) Stellen Sie einschlägige Literatur bereit oder bitten Sie einen [Agenten](#notion-agent), sie zu suchen; siehe das Beispiel [Literatur suchen](user-instructions/Anweisungsbeispiele.md#search-article).
   Bitten Sie den Agenten, die angegebenen Teile einschlägiger Artikel zu prüfen; siehe das Beispiel [Literatur prüfen](user-instructions/Anweisungsbeispiele.md#audit).
2. Richten Sie im Gespräch mit den Agenten einen Task ein und präzisieren Sie Fragestellung, Einschränkungen und Abschlusskriterien; siehe das Beispiel [Task anlegen](user-instructions/Anweisungsbeispiele.md#create-task).
   Sie können einen [Forschungslinienbuchstaben](#notion-research-line-letter) wählen, um den Task und seine Materialien zu ordnen.
3. Legen Sie für fortgesetzte autonome Forschung Ausführungsgrenzen und Stoppbedingungen fest oder übernehmen Sie bestehende; siehe das Beispiel [Standard-Stoppbedingungen festlegen](user-instructions/Anweisungsbeispiele.md#set-stop-condition).
4. (Optional) Besprechen und entwickeln Sie mit dem Agenten [Forschungsstrategien](#material-strategy); siehe das Beispiel [Strategie anlegen](user-instructions/Anweisungsbeispiele.md#create-strategy).
5. Beginnen Sie den Forschungstask; siehe das Beispiel [Task beginnen](user-instructions/Anweisungsbeispiele.md#start-task).
   Genehmigen Sie bei Aufforderung die notwendigen Werkzeugoperationen und beantworten Sie die Fragen der Agenten.
6. Durchdenken und verstehen Sie die von den Agenten erstellten mathematischen Materialien (kein Agent kann dies für Sie übernehmen).
   Diskutieren Sie die Mathematik mit den Agenten, um Ihr Verständnis zu vertiefen und zu beschleunigen.
   Verlangen Sie einschlägige Literaturhinweise und hinterfragen Sie die Herkunft von Argumenten und Ideen sokratisch, insbesondere wenn sie ohne ausdrückliche Quellenbasis auf Modellwissen beruhen.
7. (Optional, bei Verwendung von [Git](git-repository/Git-Repositorys.md#notion-git)) Erstellen Sie [Commits](#notion-commit) für Änderungen, die Sie bewahren möchten; siehe das Beispiel [Commit erstellen](user-instructions/Anweisungsbeispiele.md#commit).
   Machen Sie bei Bedarf lokale Änderungen oder die Auswirkungen bestehender Commits rückgängig.
   Sobald ein entferntes Git-Repository eingerichtet ist, erstellt und pusht der Agent Forschungsänderungen standardmäßig zeitnah gemäß den vereinbarten Bedingungen.

- Weitere [Anweisungsbeispiele zur Forschung](user-instructions/Anweisungsbeispiele.md#research).

### <a id="joint-task"></a>Einen gemeinsamen [Task](#material-task) beginnen

Mitwirkende im selben Repository können für ein gemeinsames mathematisches Ziel einen gemeinsamen Task einrichten und dabei die gemeinsame Fragestellung, Annahmen, den Umfang und die Abschlusskriterien festlegen; jede teilnehmende Person treibt die Forschung mithilfe ihres eigenen Task voran.

1. Bitten Sie einen [Agenten](#notion-agent), einen gemeinsamen Task einzurichten; siehe das Beispiel [Gemeinsamen Task anlegen](user-instructions/Anweisungsbeispiele.md#create-joint-task).
   Hat ein Mitwirkender bereits einen geeigneten gemeinsamen Task eingerichtet, können Sie direkt zum nächsten Schritt übergehen.
2. Bitten Sie den Agenten, Ihren individuellen Task einzurichten oder wiederzuverwenden und mit dem gemeinsamen Task zu verknüpfen; siehe das Beispiel [Individuellen Task anlegen](user-instructions/Anweisungsbeispiele.md#create-personal-task).
   Der individuelle Task kann die gemeinsame Fragestellung ganz oder teilweise abdecken; seine Abschlusskriterien können denen des gemeinsamen Task entsprechen oder sich nach Ihrem Beteiligungsumfang richten.
   Die Teilnehmenden können sich auch die Arbeit an derselben Frage teilen: Eine Person versucht, einen Beweis zu finden, während eine andere nach einem Gegenbeispiel sucht.
   Es empfiehlt sich, in Absprache mit den Mitwirkenden unterschiedliche [Forschungsstrategien (Strategy)](#material-strategy) zu wählen, um doppelte mathematische Arbeit zu verringern und KI-Rechenressourcen effizienter zu nutzen.
   Für unabhängige Überprüfung, Replikation oder gegenseitige Kontrolle kann bewusst derselbe Forschungsansatz gewählt werden.
3. Bei gemeinsamer Forschung synchronisiert der [leitende Forschungsagent](#notion-main-research-agent) vor jeder Runde die Aktualisierungen der Mitwirkenden durch Vorgänge wie [Pulls](#notion-pull) und [Merges](#notion-merge);
   Forschungsfortschritte, die geteilt werden können, hält er zu geeigneten Zeitpunkten in [Commits](#notion-commit) fest und überträgt sie per [Push](#notion-push).
   Administrative Konflikte bearbeitet der Agent im Rahmen seiner Befugnisse; bei wesentlichen mathematischen Meinungsverschiedenheiten erläutert er das Problem und nimmt eine erneute Prüfung vor, soweit dafür bereits eine Genehmigung vorliegt oder nachdem er die erforderliche Genehmigung eingeholt hat.
   Sie können Pushes, Pulls, Merges und andere Synchronisationsvorgänge auch selbst anfordern.

- Weitere [Anweisungsbeispiele für gemeinsame Tasks](user-instructions/Anweisungsbeispiele.md#joint-task).

### Hinweise

- [Agenten](#notion-agent) versuchen, öffentlich zugängliche Literatur in den Ordner `mathematics/literature/pdf/` unter dem Stammverzeichnis des aktuellen Repositorys herunterzuladen.
  Dieses Verzeichnis wird standardmäßig von [Git](git-repository/Git-Repositorys.md#notion-git) ignoriert.
  Wenn Sie dort eigene private Materialien ablegen, stellen Sie sicher, dass Git dieses Verzeichnis ignoriert und es nicht in ein öffentliches Repository hochgeladen wird.
- Wenn Mitwirkende sonst denselben Autorenschlüssel verwenden würden, vereinbaren Sie unterschiedliche Schlüssel, etwa `Wang1` und `Wang2`.
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

- Fragen Sie einen [Agenten](#notion-agent), wenn Sie Fragen zum Rahmenwerk haben.
- Wenn Sie mehrere ACME-Repositories auf demselben Gerät verwenden, können Sie Ihre Literatur zentral in einem einzigen lokalen PDF-Ordner speichern.
  Bitten Sie den Agenten unter Windows, `mathematics/literature/pdf/` unter dem Stammverzeichnis jedes Repositorys über eine Verzeichnisverknüpfung (Junction) mit dem Ordner zu verbinden. Siehe [Junction erstellen](user-instructions/Anweisungsbeispiele.md#create-junction) für ein Anweisungsbeispiel.
  Erteilen Sie dem Agenten die Berechtigungen, die er zum Lesen und Verwalten der Dateien in diesem Ordner benötigt.
- Wenn Agenten zugehörige Aufgaben automatisieren, bei denen Zugangsdaten verwendet werden, bewahren Sie Geheimnisse angemessen auf und schließen Sie sie von der Versionsverwaltung durch [Git](git-repository/Git-Repositorys.md#notion-git) aus.

## <a id="manuscript-writing"></a>Ein Manuskript verfassen

### Vier Ebenen von Schreibvorgaben

Das Rahmenwerk unterstützt die Aufbereitung von Forschungsmaterialien zu TeX-Manuskripten sowie deren Überarbeitung, Kompilierung und Prüfung.
ACME ordnet das Schreiben von Manuskripten in vier Ebenen von Vorgaben, von der niedrigsten zur höchsten Priorität:

- Allgemeine Vorgaben für mathematisches Schreiben.
  Sie stehen in [framework/rules/writing.md](../framework/rules/writing.md#common-mathematical-writing-defaults) und werden mit dem Rahmenwerk als Standardvorgaben installiert.
  Diese Vorgaben und das eigene Urteil eines [Agenten](#notion-agent) allein genügen möglicherweise noch nicht den Konventionen eines Fachgebiets oder den persönlichen Anforderungen eines Autors.
- Allgemeine Schreibpräferenzen des Autors.
  Der Agent hält sie bei Bedarf auf Grundlage der ausdrücklichen Anforderungen des Autors in `profiles/<human>/writing/readme.md` fest (`<human>` ist der [Autorenschlüssel](#notion-author-key), etwa `Alice`) und aktualisiert sie entsprechend diesen Anforderungen.
  Siehe das Beispiel [Allgemeine Schreibpräferenzen](user-instructions/Anweisungsbeispiele.md#personal-preference).
- Präferenzen des Autors für ein bestimmtes Forschungsgebiet.
  Der Agent hält sie bei Bedarf in der entsprechenden fachgebietsspezifischen Präferenzdatei unter `profiles/<human>/writing/` fest.
  Siehe das Beispiel [Fachgebietsspezifische Schreibpräferenzen](user-instructions/Anweisungsbeispiele.md#community-preference).
- Vereinbarungen für das aktuelle Manuskript.
  Sie stehen üblicherweise in `writing.md`, `conventions.md` oder einem Abschnitt „Schreibvereinbarungen“ der `readme.md` im Manuskriptverzeichnis und werden vom Agenten bei Bedarf gepflegt.
  Siehe das Beispiel [Manuskriptvereinbarungen](user-instructions/Anweisungsbeispiele.md#manuscript-convention).

Weitere [Anweisungsbeispiele zum Schreiben](user-instructions/Anweisungsbeispiele.md#writing-instructions).

Eine Ebene mit höherer Priorität ersetzt nur die widersprechenden Teile niedrigerer Ebenen; alle übrigen Anforderungen gelten weiter.
Wenn noch keine persönlichen oder fachgebietsspezifischen Präferenzen und keine Manuskriptvereinbarungen festgelegt sind, beginnt der Agent nach den allgemeinen Vorgaben zu schreiben.
Terminologie- und Notationspräferenzen eines Autors, die für Gespräch und Schreiben gemeinsam gelten, stehen zusammen in `profiles/<human>/terminology.md`.

### Referenzwerke für das Schreiben

Autoren können drei Arten von Referenzwerken auswählen: vorhandene Arbeiten zur direkten Wiederverwendung von Inhalten, Vorbilder für den Schreibstil sowie Referenzen für Fachterminologie und Notation.
Sie können Literatur bereitstellen oder vorhandene Werke benennen; der [Agent](#notion-agent) übernimmt die nötige Ordnung und Registrierung.
Dasselbe Werk kann mehreren Zwecken dienen, für die jeweils ein eigener Geltungsbereich festgelegt werden kann.

- Wiederverwendbare vorhandene Arbeiten.
  Sie können eigene oder mitverfasste Arbeiten benennen, die der Agent im angegebenen Umfang direkt wiederverwenden darf, gegebenenfalls begrenzt auf bestimmte Abschnitte oder Passagen.
  Siehe das Beispiel [Textwiederverwendung erlauben](user-instructions/Anweisungsbeispiele.md#record-my-article).
- Vorrangige Vorbilder für den Schreibstil des Manuskripts.
  Sie können eine oder mehrere Referenzarbeiten auswählen, an deren Aufbau, Darstellung und Stil sich der Agent orientieren kann.
  Siehe das Beispiel [Stilvorbild auswählen](user-instructions/Anweisungsbeispiele.md#style-model).
- Referenzen für Fachterminologie und Notation.
  Sie können Referenzwerke benennen, an denen sich der Agent bei Terminologie, Notation und der Darstellung von Definitionen orientiert.
  Siehe das Beispiel [Terminologiereferenzen auswählen](user-instructions/Anweisungsbeispiele.md#terminology-references).

Diese Auswahl kann für Ihr Schreiben allgemein, für ein bestimmtes Forschungsgebiet oder für das aktuelle Manuskript gelten und wird mit den entsprechenden Präferenzen oder Vereinbarungen gespeichert.
Referenzwerke und ihre Verwendungszwecke für das allgemeine Schreiben stehen in `profiles/<human>/writing/readme.md`.
Die nur für ein Fachgebiet geltenden Referenzen und Zwecke stehen in der entsprechenden Präferenzdatei unter `profiles/<human>/writing/`.
Die nur für das aktuelle Manuskript geltenden Referenzen und Zwecke stehen in `writing.md`, `conventions.md` oder einem Abschnitt „Schreibvereinbarungen“ der `readme.md` im Manuskriptverzeichnis.

### Prüfung und Überarbeitung

Die Überarbeitung richtet sich nach der aktuellen Manuskriptfassung und der ausdrücklichen Absicht des Autors.
Ohne ausdrückliche Zustimmung des Autors entfernt ein [Agent](#notion-agent) keine vollständigen vorhandenen Passagen wie Sätze, Definitionen, Beweise, Beispiele oder Bemerkungen.
Das Rahmenwerk unterstützt die Prüfung der Darstellung und der mathematischen Argumente eines Manuskripts, getrennt oder gemeinsam.

- Prüfung der Darstellung: Der Agent prüft Darstellung, Aufbau, Terminologie, Notation und Zitate anhand der vier Ebenen; noch zu bearbeitende Überarbeitungshinweise stehen in `revisions.md` im Manuskriptverzeichnis.
  Siehe das Beispiel [Darstellung prüfen](user-instructions/Anweisungsbeispiele.md#writing-review).
- Prüfung der mathematischen Argumente: Der Agent prüft Voraussetzungen, Schlussfolgerungen und die dazwischenliegenden Argumente; aktuelle ungelöste mathematische Probleme und ihre notwendigen Begründungen stehen in `review.md` im Manuskriptverzeichnis und werden bei Nachprüfungen aktualisiert.
  Siehe das Beispiel [Mathematische Manuskriptargumente prüfen](user-instructions/Anweisungsbeispiele.md#manuscript-review).

Die Prüfungsergebnisse nennen den tatsächlich geprüften Umfang, die Befunde und noch offene Punkte.
Wenn eine unabhängige Prüfung benötigt wird, können Sie Schreiben und Prüfung in getrennten Sitzungen organisieren und die Prüfung einem Agenten übertragen, der weder an der inhaltlichen Ausarbeitung oder Argumentation mitgewirkt noch die entsprechenden inhaltlichen Diskussionen erhalten hat, um einen unabhängigen [Kontext](#notion-context) zu gewährleisten.
Bei einer unabhängigen Erstprüfung bildet der Agent zunächst anhand des aktuellen Manuskripts und der geltenden Vereinbarungen ein eigenes Urteil und vergleicht es erst danach mit vorhandenen Hinweisen.
Der schreibende Agent berichtet die Korrekturen; der prüfende Agent untersucht die Änderungen und ihre Auswirkungen, bevor er die entsprechenden Hinweise aktualisiert oder entfernt.

### Literaturrecherche und Literaturverweise

Sobald im Manuskript konkrete mathematische Aussagen vorliegen, können Sie einen [Agenten](#notion-agent) bitten, für das gesamte Manuskript, für bestimmte Abschnitte oder für einen einzelnen Satz, ein Lemma oder eine Eigenschaft [nach einschlägiger Literatur zu suchen](user-instructions/Anweisungsbeispiele.md#refs-seek).
Findet der Agent einschlägige Quellen, vergleicht er deren Voraussetzungen und Schlussfolgerungen mit denen der Aussagen im Manuskript.
Er gibt an, ob die Quelle dasselbe Ergebnis liefert, unter welchen Bedingungen daraus die Aussage des Manuskripts folgt, ob sie nur einen Spezialfall abdeckt oder ob sie eine verwandte Methode bietet.

Die Rechercheergebnisse hält der Agent in `literature-seek.md` im Verzeichnis des Manuskripts fest und gibt die bekannten Fassungen, Fundstellen in den Originalquellen, den tatsächlich geprüften Umfang und noch zu prüfende Hinweise an.

Wenn Sie den Agenten im selben Auftrag um eine Literaturrecherche und Änderungen am Manuskript bitten, prüft und dokumentiert er wesentliche neue mathematische Erkenntnisse oder Änderungen an der Grundlage eines Ergebnisses vor der Überarbeitung der betroffenen Textstellen.
Er prüft die Anwendbarkeit der Quelle, hält die nötigen Belege und Herleitungen in den zuständigen mathematischen Materialien fest und führt die erforderliche Bewertung und mathematische Prüfung durch.
Verlangt die Quelle eine zusätzliche Voraussetzung und fehlt noch eine Herleitung der allgemeineren Aussage, hält der Agent die offene Beweisaufgabe fest und verwendet die Quelle im belegten Geltungsbereich.
In `citation.md` hält er zu den im TeX-Text ergänzten oder geänderten Verweisen fest, wo und wozu die Quellen zitiert werden, worauf ihre Anwendbarkeit beruht und welche Prüfungen noch ausstehen.

### Schreibgedächtnis der Agenten

Beim Schreiben und Überarbeiten fasst der [Agent](#notion-agent) Rückmeldungen und Erfahrungen aktiv zu nützlichen, nach Autor geführten Schreibnotizen zusammen.
Diese Notizen stehen in `profiles/<human>/writing/notes.md` und werden vom Agenten selbstständig angelegt und gepflegt.
Sie sind beratend und setzen ausdrückliche Schreibvereinbarungen nicht außer Kraft.
Gespeicherte Schreibpräferenzen und Notizen werden bei späteren einschlägigen Schreibarbeiten nach Bedarf herangezogen.
Der Agent überarbeitet, bündelt und strafft die Notizen fortlaufend anhand neuer Rückmeldungen; formelle Präferenzen und Manuskriptvereinbarungen werden aufgrund ausdrücklicher Anforderungen des Autors oder seiner ausdrücklichen Übernahme entsprechender Vorgaben aktualisiert.

### <a id="lean-formalization"></a>Formalisierung in Lean

In Arbeit.

## Nützliche Informationen

### Version des Rahmenwerks

Die aktuelle Version des Rahmenwerks ist 0.12.0.

Wenn automatische Prüfungen aktiviert sind und Netzwerkzugriff erlaubt ist,
prüft der [Agent](#notion-agent) zu Arbeitsbeginn höchstens einmal pro UTC-Tag, ob eine neuere Version des [offiziellen ACME-Rahmenwerks](https://github.com/vtejdn/acme) verfügbar ist.
Ist eine neuere Version verfügbar, nennt er die installierte und die verfügbare Version und fragt, ob ein Upgrade vorbereitet werden soll; Ihre laufende Arbeit kann während Ihrer Entscheidung fortgesetzt werden.
Eine Erinnerung installiert oder aktualisiert keine Dateien, und Sie können das Upgrade zurückstellen.
Sie können die automatischen Prüfungen für dieses Repository deaktivieren oder aktivieren lassen, eine sofortige erneute Prüfung oder ausdrücklich ein Upgrade anfordern.

### <a id="common-instructions"></a>Anweisungsbeispiele

Die [Anweisungsbeispiele](user-instructions/Anweisungsbeispiele.md) veranschaulichen häufige Anweisungen und erläutern, welche Ergebnisse Sie erwarten können.

### Verzeichnisse und Dateien im Stammverzeichnis

Die folgenden Tabellen beschreiben die wichtigsten Dateien und Verzeichnisse im Stammverzeichnis des Repositorys.
Einige Verzeichnisse werden erst bei Bedarf angelegt.

| Pfad | Zweck |
| --- | --- |
| `.tmp/` | Enthält temporäre Eingaben und Nebenprodukte, die von [Agenten](#notion-agent) erstellt und nach Gebrauch entfernt werden. |
| `execution/` | Dokumentiert den aktuellen Ausführungszustand, Grenzen und Abbruchbedingungen individueller Forschungs-[Tasks](#material-task). |
| [`framework/`](../framework/readme.md) | Enthält Regeln des Rahmenwerks, Materialvorlagen, Formatvorgaben und Versionshinweise. |
| [`intake/`](../intake) | Dokumentiert, welche Materialien aus anderen [Repositories](git-repository/Git-Repositorys.md#notion-git-repository) übernommen wurden, ihre Quellen und den Umfang jeder Übernahme. |
| [`mathematics/`](../mathematics/readme.md) | Enthält Forschungsmaterialien, Literatureinträge, Berechnungen, Manuskripte und Präsentationen. |
| `profiles/` | Speichert persönliche Forschungs- und Ausführungspräferenzen, Vorgaben für mathematisches Schreiben sowie von Agenten gepflegte Erfahrungsnotizen. |
| [`repository/`](../repository/readme.md) | Speichert Repository-Einstellungen, Autorenregistrierungen und Zuordnungen zu externen Repositories und Autoren. |
| [`scripts/`](../scripts/readme.md) | Bietet optionale Befehlszeilenwerkzeuge für Einrichtung, Materialverwaltung, Navigation und Prüfungen. |
| [`user-manual/`](./) | Enthält Benutzeranleitungen, Erläuterungen zur Einrichtung und Anweisungsbeispiele. |
| `.gitattributes` | Konfiguriert die Behandlung von Text- und Binärdateien durch [Git](git-repository/Git-Repositorys.md#notion-git), einschließlich Zeilenenden. |
| `.gitignore` | Legt fest, welche nicht versionierten Dateien und Verzeichnisse Git ignorieren soll. |
| [`AGENTS.md`](../AGENTS.md) | Enthält Einstiegsanweisungen, die Agenten zu den einschlägigen Regeln und Materialien des Rahmenwerks führen. |
| [`LICENSE`](../LICENSE) | Enthält die Lizenzbedingungen und Hinweise des Repositorys. |
| [`readme.md`](../readme.md) | Stellt das Repository vor und verlinkt auf das Benutzerhandbuch, die Regeln des Rahmenwerks und Forschungsmaterialien. |

Abhängig von Ihren Werkzeugen und Einstellungen können außerdem die folgenden Verzeichnisse vorhanden sein.

| Pfad | Zweck |
| --- | --- |
| `.agents/` | Enthält Agenten-Skills für dieses Repository. |
| `.claude/` | Enthält lokale Claude-Code-Einstellungen für diesen Arbeitsbereich. |
| `.codex/` | Enthält die lokale Codex-Konfiguration für diesen Arbeitsbereich. |
| `.git/` | Enthält die Git-Historie, Referenzen, Konfiguration und weitere Metadaten der Versionsverwaltung. |
| `.venv/` | Enthält die lokale virtuelle Python-Umgebung und deren installierte Abhängigkeiten. |
| `.vscode/` | Enthält die VS-Code-Arbeitsbereichskonfiguration und Erweiterungsempfehlungen. |

### Kategorien von Forschungsmaterialien

| Kürzel | Material | Speicherort | Zweck |
| --- | --- | --- | --- |
| T | [Forschungsaufgabe (Task)](#material-task) | [`mathematics/tasks/`](../mathematics/tasks/index.md) | Legt eine Forschungsfrage, ihren freigegebenen Umfang und Abschlusskriterien fest und dokumentiert Entscheidungen über ihren Lebenszyklus. |
| S | [Forschungsstrategie (Strategy)](#material-strategy) | [`mathematics/strategies/`](../mathematics/strategies/index.md) | Entwickelt und bewertet einen Forschungsweg, ordnet Prioritäten und benennt Hindernisse sowie nächste Schritte. |
| C | [Mathematische Aussage (Claim)](#material-claim) | [`mathematics/claims/`](../mathematics/claims/index.md) | Formuliert präzise mathematische Aussagen, bewahrt ihre Argumente und Abhängigkeiten und dokumentiert ihre mathematischen Bewertungen und Prüfungsbefunde. |
| R | [Prüfbericht (Review)](#material-review) | [`mathematics/audits/reviews/`](../mathematics/audits/reviews/readme.md) | Dokumentiert mathematische Prüfungen bestimmter projektinterner Argumente, einschließlich der geprüften Eingaben, Befunde, Organisation der Prüfung und Grenzen. |
| D | Entwurf (Draft) | [`mathematics/drafts/`](../mathematics/drafts/readme.md) | Bietet einen Arbeitsbereich für die Entwicklung mathematischer Argumente, Rechnungen und Alternativen, die noch untersucht werden. |
| L | [Explorationsprotokoll (Ledger)](#material-ledger) | [`mathematics/ledger/`](../mathematics/ledger/readme.md) | Bewahrt nützliche Untersuchungen, Vergleiche, Synthesen und gescheiterte Ansätze sowie die Gründe und Ergebnisse wesentlicher mathematischer Änderungen. |
| J | Berechnung (Computation) | [`mathematics/computations/programs/`](../mathematics/computations/readme.md) | Organisiert Programme und erforderliche Eingaben für reproduzierbare Berechnungen und dokumentiert Ausführungsstatus, Ergebnisse und Grenzen. |
| U | Literaturprüfungseinheit (Literature audit unit) | [`mathematics/audits/literature/`](../mathematics/audits/literature/readme.md) | Macht geprüfte Literatur wiederverwendbar, indem sie Quellenausgabe und Textstellen, mathematischen Inhalt, Anwendbarkeit und Prüfungsgrenzen festhält. |
| — | Manuskript (Manuscript) | [`mathematics/manuscripts/`](../mathematics/manuscripts/index.md) | Dient der Ausarbeitung von Aufsätzen und zugehörigen mathematischen Dokumenten, einschließlich Darstellung, Zitaten, Schreibvorgaben und Kompilierungsprotokollen. |
| — | Präsentation (Presentation) | [`mathematics/presentations/`](../mathematics/presentations/readme.md) | Dient der Ausarbeitung von Vorträgen und Folien für ein bestimmtes Publikum, einschließlich Quelldateien, Schreibvorgaben, Kompilierungsinformationen und Prüfberichten. |

- Jede Berechnung hat ein nummeriertes J-Verzeichnis mit ihren Programmen, erforderlichen Eingaben und einer `readme.md`.
  Erzeugte Ausgaben werden getrennt unter dem lokalen, von [Git](git-repository/Git-Repositorys.md#notion-git) ignorierten Pfad `mathematics/computations/outputs/<J>/` gespeichert.
  Für Daten, die für spätere Beweise, Prüfungen oder Reproduktionen benötigt werden, bewahrt der Agent im Repository entweder die erforderlichen Daten selbst oder ausreichende Erzeugungsprogramme, Basiseingaben, Parameter, Abhängigkeitsbedingungen und Validierungsmethoden auf, mit denen sie sich zuverlässig und zu vertretbaren Kosten rekonstruieren lassen.
  Ist eine Rekonstruktion unzuverlässig oder zu teuer oder muss ein bestimmtes Objekt erhalten bleiben, bewahrt der Agent die erforderlichen Daten selbst auf.
- Literaturprüfungseinheiten sind unter `mathematics/audits/literature/` nach Zitierschlüsseln gruppiert.
- Der [Definitionsindex](../mathematics/definitions/index.md) ordnet Definitionen, Terminologie und Symbole nach Begriffen und verlinkt auf die vollständigen Formulierungen in den zuständigen C-, L- oder U-Materialien.
- Die maßgebliche [Bibliografie](../mathematics/literature/references.bib) dokumentiert die Identität von Veröffentlichungen und deren Zitierschlüssel.
  Nützliche Hinweise zu Quellen und Ausgaben können in den von den jeweiligen Autoren verantworteten Abschnitten von `mathematics/audits/literature/<SourceKey>/readme.md` festgehalten werden.

### Grundbegriffe

| Begriff | Bedeutung |
| --- | --- |
| <a id="notion-llm"></a>LLM (Large Language Model) | Ein auf großen Textmengen trainiertes KI-Modell, das Sprache verarbeitet und erzeugt, darunter mathematische Erläuterungen und Computercode. |
| <a id="notion-agent"></a>Agent | Ein von einem [LLM](#notion-llm) angetriebenes KI-System, das Aufgaben planen und ausführen, Werkzeuge verwenden und seine Handlungen anhand der Ergebnisse anpassen kann. Es arbeitet über eine [Agenten-Laufzeitumgebung](harness/Agenten-Laufzeitumgebung.md) innerhalb des vom Menschen freigegebenen Umfangs und der festgelegten Grenzen. Es hat sich noch nicht zu einem [Agent](https://de.wikipedia.org/wiki/Matrix_%28Film%29#Handlung) weiterentwickelt. |
| <a id="notion-context"></a>Kontext (Context) | Die Informationen, die einem LLM bei einem Modellaufruf zur Verfügung stehen, darunter Anweisungen, Gesprächsverlauf, bereitgestellte Materialien und Werkzeugergebnisse. Der aktuelle Kontext kann nur eine Auswahl oder Zusammenfassung des vollständigen [Sitzungsverlaufs](#notion-session) enthalten. |
| <a id="notion-context-length"></a>Kontextlänge (Context length) | Die maximale Gesamtlänge aus Ein- und Ausgabe, die ein LLM auf einmal verarbeiten kann, üblicherweise in Tokens gemessen, also kleinen Texteinheiten. Dazu zählen Anweisungen, Gesprächsverlauf, bereitgestellte Materialien und die erzeugte Antwort. |
| <a id="notion-session"></a>Sitzung (Session) | Eine fortlaufende Interaktion mit einem [Agenten](#notion-agent), die von einer [Agenten-Laufzeitumgebung](harness/Agenten-Laufzeitumgebung.md) verwaltet wird. Sie kann mehrere Gesprächsrunden enthalten, die jeweils typischerweise mit einer Benutzernachricht beginnen und die Antworten des Agenten sowie Werkzeugaufrufe umfassen. Die Laufzeitumgebung verwaltet den Gesprächsverlauf und bereitet den [Kontext](#notion-context) für jeden Modellaufruf vor; um die [Kontextlänge](#notion-context-length) des Modells einzuhalten, kann sie frühere Teile des Verlaufs auswählen oder zusammenfassen. |
| Materialkennung | Eine strukturierte Referenz, die ein Material und gegebenenfalls dessen Version bezeichnet. Beispielsweise kennzeichnet `Alice_C_F0007_v1.md` einen [Claim](#material-claim) durch Autor, Materialart, Forschungslinie, laufende Nummer und Version. |
| <a id="notion-research-line-letter"></a>Forschungslinien-Buchstabe | Ein Buchstabe, etwa `F` in `Alice_C_F0007_v1.md`, mit dem nummerierte Forschungsmaterialien geordnet werden. Von einem Task abgeleitete Materialien übernehmen dessen Buchstaben, erhalten jedoch eigene laufende Nummern. Ohne Angabe einer Linie wird standardmäßig `A` verwendet. |
| <a id="notion-author-key"></a>Autorenschlüssel | Ein stabiler registrierter Schlüssel für einen menschlichen Autor, etwa `Alice`, der in Materialkennungen und Autoreneinträgen verwendet wird. |
| Materialfamilie | Die aufbewahrten Versionen desselben Materials, etwa `Alice_C_F0007_v1.md` und `Alice_C_F0007_v2.md`. |
| Materialversion | Eine bestimmte aufbewahrte Überarbeitung eines Materials, etwa die Version `v1` oder `v2` eines Claims. |
| <a id="notion-main-research-agent"></a>Leitender Forschungsagent | Der Agent, der die Arbeit an einem [Task](#material-task) leitet, beteiligte Unteragenten koordiniert und die Forschungsaufzeichnungen konsistent hält. |
| Task-Runde | Ein Arbeitsabschnitt zu einem Task, der mit einer Aufzeichnung des Fortschritts, offener Fragen und eines Ansatzpunkts für die Fortsetzung endet. |
| <a id="notion-git-branch"></a>Git-Branch | Eine benannte Entwicklungslinie in einem [Git-Repository](git-repository/Git-Repositorys.md#notion-git-repository), auf der Änderungen getrennt von anderen Arbeitslinien entwickelt werden können. |
| <a id="notion-clone"></a>Klonen (Clone) | Ein bestehendes Git-Repository einschließlich seiner Dateien und Versionshistorie in einen neuen lokalen Ordner kopieren. |
| <a id="notion-commit"></a>Commit | Ein in der lokalen [Git](git-repository/Git-Repositorys.md#notion-git)-Historie gespeicherter Stand, der ausgewählte Änderungen mit einer erläuternden Nachricht festhält. |
| <a id="notion-push"></a>Push | Lokale Commits an ein entferntes Git-Repository senden, damit die aufgezeichnete Arbeit dort verfügbar ist. |
| <a id="notion-pull"></a>Pull | Änderungen aus einem entfernten Git-Repository abrufen und in die lokale Arbeit integrieren. |
| <a id="notion-merge"></a>Merge | Änderungen aus einem anderen [Branch](#notion-git-branch) in den aktuellen Git-Branch zusammenführen und dabei widersprüchliche Bearbeitungen bei Bedarf auflösen. |
| <a id="notion-intake"></a>Übernahme (Intake) | Ausgewählte Forschungsmaterialien aus einem anderen öffentlichen ACME-Repository in das eigene übernehmen und dabei Autorenschaft, Herkunft und Prüfungsgrenzen bewahren. |
| <a id="notion-import"></a>Import | Eigene ausgewählte Forschungsmaterialien, Manuskripte oder anwendbare persönliche Einstellungen aus einem anderen Ordner oder Repository in den aktuellen Arbeitsbereich übernehmen, dabei die Autorenschaft bewahren und ausreichende vorhandene Materialien wiederverwenden. Benötigte Materialien anderer Autoren werden durch [Übernahme (Intake)](#notion-intake) bezogen. |
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

- Ein Task kann aktiv bleiben, auch wenn gerade kein [Agent](#notion-agent) daran arbeitet.
- Wird ein persönlicher Task zur Ausführung ausgewählt, legt der Agent in der aktuellen Arbeitskopie einen lokalen Ausführungseintrag (E) an oder verwendet den vorhandenen Eintrag weiter, um den Ausführungszustand, geltende Kontingente und Stoppbedingungen gesondert festzuhalten.
- Ein Task führt die Forschungsmaterialien zusammen, die Ihre Untersuchung unterstützen.
  Zugehörige Manuskripte, Fortschrittsberichte und andere von Ihnen angeforderte Dokumente können in einem Projekt wie `mathematics/manuscripts/Alice/Alice_T_A0007/` gesammelt werden.
  Manuskriptprojekte werden nach dem für das Schreiben verantwortlichen Autor geordnet und dem zugehörigen Forschungs-Task zugeordnet.
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
- Sie können Ansätze vorschlagen, den [Agenten](#notion-agent) um einen Vergleich von Alternativen bitten oder Prioritäten vorgeben.
  Geben Sie ausdrücklich an, wenn eine Priorität oder Reihenfolge unverändert bleiben muss; andernfalls kann der Agent seine Auswahl von Wegen innerhalb des vereinbarten Umfangs anpassen.
- Innerhalb des freigegebenen Umfangs dürfen autonome Agenten Strategien je nach Befunden und Ressourcen hinzufügen, überarbeiten, neu priorisieren, aufteilen, zusammenführen, unterbrechen oder erneut aufnehmen.
- Ein gescheiterter Weg kann dennoch aufschlussreich sein.
  Er kann ein Hindernis aufdecken, einen Ansatz ausschließen oder zeigen, wo eine zusätzliche Voraussetzung nötig wäre.

### <a id="material-claim"></a>Mathematische Aussage (Claim)

Ein Claim dokumentiert eine wichtige, präzise mathematische Aussage und den aktuellen Kenntnisstand zu ihrer Gültigkeit.

| Mathematischer Status | Bedeutung für den Leser |
| --- | --- |
| `open` | Die genaue Aussage ist weiterhin ungeklärt. Es können Teilergebnisse, Reduktionen oder ein vorläufiges Argument vorliegen, doch die Bedingungen für `proved` oder `refuted` sind noch nicht erfüllt. |
| `proved` | Ein vollständiger Beweis begründet die genaue Aussage unter ihren angegebenen Voraussetzungen. Alle notwendigen unterstützenden Ergebnisse sind gesichert und anwendbar; eine dokumentierte mathematische [Prüfung](#material-review) hat keine verbleibende Lücke festgestellt. |
| `refuted` | Ein geprüftes Gegenbeispiel oder Argument widerlegt die genaue Aussage innerhalb ihres angegebenen Geltungsbereichs. Alle notwendigen unterstützenden Ergebnisse sind gesichert und anwendbar; eine dokumentierte mathematische Prüfung hat keine verbleibende Lücke festgestellt. |

### <a id="material-review"></a>Prüfbericht (Review)

Ein Review dokumentiert die Prüfung einer mathematischen Aussage oder eines Arguments durch einen [Agenten](#notion-agent), einschließlich der genauen Eingaben und des Umfangs, der Befunde und verbleibender Einschränkungen.

| Prüfungsverhältnis | Bedeutung für den Leser |
| --- | --- |
| `self-reviewed` | Der Beweis wurde von einem Agenten geprüft, der an seiner Entwicklung beteiligt war oder mit der mathematischen Diskussion vertraut ist, aus der er hervorgegangen ist. |
| `independently reviewed` | Ein anderer Agent prüfte den Beweis, ohne an dessen Entwicklung beteiligt gewesen zu sein oder die Entwicklungsdiskussion als eigenen [Kontext](#notion-context) erhalten zu haben. |
| `unknown` | Das tatsächliche Verhältnis einer älteren oder aus einer Quelle stammenden Prüfung ist nicht geklärt; dies bedeutet weder einen Fehler noch eine unabhängige Prüfung. |

- Diese Bezeichnungen beschreiben das Verhältnis der prüfenden Agenten zum Beweis, nicht dessen Richtigkeit.
  Eine fehlende Angabe des Prüfungsverhältnisses unterscheidet sich von `unknown`; ist keine Prüfung ausgewählt, verwendet der Claim keine Prüfungsbelege.
- Auch die Prüfung durch einen anderen Agenten gilt als Selbstprüfung, wenn dieser Diskussionen zur Beweisentwicklung, mathematische Zusammenfassungen, Erläuterungen des Autors oder frühere Prüfungsbefunde übernimmt.
  Eine andere [Sitzung](#notion-session) oder ein anderes Modell allein begründet keine Unabhängigkeit.
- Der [leitende Forschungsagent](#notion-main-research-agent) veranlasst unabhängige Prüfungen an zentralen Beweisstellen und nach Abschluss des [Task](#material-task) für die gesamte logische Kette.
  Sie können auch die Prüfung eines bestimmten Ergebnisses oder Beweisschritts anfordern.

### <a id="material-ledger"></a>Explorationsprotokoll (Ledger)

Ein Ledger bewahrt nützliche mathematische Untersuchungen, darunter Vergleiche, gescheiterte Ansätze und Gründe für Richtungsänderungen.
Ein Eintrag kann erläutern, was unter welchen Voraussetzungen untersucht wurde, was versucht wurde, was die Argumentation oder die Belege zeigten und was offenbleibt.

Ein Ledger kann Teilargumente und nützliche Einsichten bewahren, auch wenn eine Untersuchung noch keinen eigenständigen [Claim](#material-claim) hervorgebracht hat.
Gescheiterte oder ergebnisoffene Versuche können beispielsweise Hindernisse sichtbar machen, Ansätze voneinander abgrenzen oder helfen, wiederholte Arbeit zu vermeiden.

- Sie können einen [Agenten](#notion-agent) bitten, [Strategien](#material-strategy) zu vergleichen, einen gescheiterten Versuch zu erklären, Erkenntnisse aus mehreren Quellen zusammenzuführen oder einen nützlichen Gedankengang für spätere Arbeit festzuhalten.
- Sie können einen Agenten auch bitten, alles festzuhalten, was Sie für mathematisch wesentlich und aufzeichnungswürdig halten.
