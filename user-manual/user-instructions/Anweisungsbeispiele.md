# Anweisungsbeispiele

[Benutzerhandbuch](../Benutzerhandbuch.md)

Beschreiben Sie Ihr Ziel in natürlicher Sprache.
Die folgenden Beispiele sind in Anweisungen zur [Einrichtung](#setup), [Forschung](#research-instructions) und [Verwaltung](#administration-instructions) gegliedert.
Passen Sie die Formulierungen an Ihre tatsächliche Frage, Ihre Dateien und den Arbeitsumfang an.

## <a id="setup"></a>Anweisungen zur Einrichtung

Nutzen Sie diese Beispiele, um Ihre Arbeitsumgebung vorzubereiten, Ihre Autorenidentität zu registrieren und lokale Ressourcen einzurichten.
Die Reihenfolge der Installations- und Registrierungsschritte finden Sie im Abschnitt [Einrichtung](../Benutzerhandbuch.md#setup) des Handbuchs.

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Laden Sie [ACME](https://github.com/vtejdn/acme) nach `D:\acme` herunter. | Prüfen, ob das Ziel für die Installation geeignet ist, die Dateien des ACME-Rahmenwerks herunterladen, vorhandene Inhalte bewahren und die Version sowie verbleibende Einrichtungsschritte angeben. |
| Installieren Sie [Git](../git-repository.md#notion-git). | Prüfen, ob Git bereits installiert ist, es bei Bedarf installieren und die verfügbare Version sowie verbleibende Einrichtungsschritte angeben. |
| Erklären Sie mir, wie ich eine Verbindung zu [GitHub](../git-repository.md#notion-github) herstelle. | Anmeldung, Authentifizierung und Verbindung zu einem entfernten Repository erklären und benennen, welche Schritte Sie selbst ausführen müssen. |
| Ich habe mich bei GitHub angemeldet. Testen Sie die Verbindung. | Das authentifizierte Konto prüfen und die Erreichbarkeit von GitHub und dem Ziel-Repository ausschließlich lesend testen. Das Ergebnis oder den konkreten Fehler angeben. |
| [Klonen](../Benutzerhandbuch.md#notion-clone) Sie [ACME](https://github.com/vtejdn/acme) nach `D:\acme`. | Prüfen, ob Git, Zugriffsberechtigungen und Ziel bereitstehen, das ACME-Repository einschließlich seiner Versionshistorie klonen und Branch, Version sowie verbleibende Initialisierungsschritte angeben. |
| Registrieren Sie mich als Ali. | Ali als Ihren Autorenschlüssel registrieren; falls der aktuelle Ordner eine Git-Arbeitskopie ist, diese zugleich mit Ali verknüpfen. Die Identitäten vorhandener Mitwirkender bewahren. |
| Richten Sie Git ein und verbinden Sie es mit meinem Repository <https://github.com/alice/acme>. | Die Git-Einstellungen dieses Projekts und das angegebene entfernte Repository konfigurieren, die tatsächliche Commit-Identität prüfen und den Zugriff testen; vorhandene Commits und nicht betroffene Einstellungen bewahren. |
| Klonen Sie das Repository meines Mitwirkenden <https://github.com/alice/acme> und registrieren Sie mich als Bob. | Das gemeinsame Repository klonen, Sie als Bob registrieren und die neue Git-Arbeitskopie mit Bob verknüpfen. Vorhandene Autoren und Forschungsmaterialien bewahren und die Einstellungen der Git-Commit-Identität angeben. |

## <a id="research-instructions"></a>Forschungsanweisungen

Nutzen Sie diese Beispiele, um mit Literatur zu arbeiten und mathematische Fragen zu untersuchen.

### Literatur suchen, registrieren oder prüfen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Sichten Sie die lokale Quelle abc26, registrieren Sie sie und prüfen Sie sie. | Werk, Ausgabe und lokale Originaldatei von abc26 bestimmen und die bibliografische Registrierung sowie die Dateiregistrierung vervollständigen. Wenn das Original ein Inhaltsverzeichnis enthält, eine durchsuchbare Fassung davon erstellen. Den mathematischen Inhalt prüfen und den geprüften Umfang, die Schlussfolgerungen und offene Fragen dokumentieren. |
| Prüfen Sie Satz 1.7 in abc26. | Satz 1.7 im Original auffinden, seine vollständige Aussage, Voraussetzungen, den Beweis und die Anwendbarkeit der notwendigen unterstützenden Ergebnisse prüfen sowie Befunde, ungeprüfte Teile und konkrete Lücken dokumentieren. |
| Suchen Sie nach *On the construction of S* und versuchen Sie, das Werk zu registrieren und zu prüfen. | Werk und Ausgabe bestimmen, vorhandene Einträge prüfen und versuchen, das Original zu beschaffen. Bibliografische Angaben und das tatsächlich Beschaffte dokumentieren. Wenn das Original ein Inhaltsverzeichnis enthält, eine durchsuchbare Fassung erstellen. Die verfügbaren Inhalte prüfen und nicht verfügbare Teile benennen. |
| Wie wird diese Definition in der einschlägigen Literatur verwendet? | Vorhandene Definitionseinträge und einschlägige Originalquellen heranziehen, Objekte, Voraussetzungen, Notation und Verwendungen vergleichen, genaue Literaturangaben machen und Quelldefinitionen von lokalen Umformulierungen oder Verallgemeinerungen unterscheiden. |

### <a id="start-or-continue-research"></a>Einen [Task](../Benutzerhandbuch.md#material-task) beginnen oder fortsetzen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Legen Sie für Vermutung 1.3 in abc26 einen Task in Linie W an. | Die ursprüngliche Aussage, Voraussetzungen und den Geltungsbereich von Vermutung 1.3 prüfen und zunächst nach einem vorhandenen Task zur gleichen Frage suchen. Wenn ein neuer Task nötig ist, [Linie W](../Benutzerhandbuch.md#notion-research-line-letter) verwenden und Quelle, genaue Frage und Abschlusskriterien angeben. |
| Legen Sie einen Task in Linie F mit dem Ziel „Wenn P, dann Q“ an. | Objekte, Voraussetzungen und Quantoren in P und Q präzisieren, einen Task in Linie F mit „P impliziert Q“ als vollständigem Ziel anlegen und die Abschlusskriterien festlegen. |
| Legen Sie einen neuen Task an, um Proposition P vom endlichdimensionalen auf den unendlichdimensionalen Fall zu verallgemeinern. | Die ursprüngliche Proposition prüfen, die neuen Objekte, Voraussetzungen und die angestrebte Schlussfolgerung präzisieren, den Task anlegen und die ursprüngliche Proposition als Spezialfall bewahren, den die Verallgemeinerung abdecken muss. |
| Legen Sie einen Task an, um im Rahmen P eine allgemeine Formel zu finden, die Formel (1) in abc26 umfasst. | Voraussetzungen und Notation der ursprünglichen Formel prüfen, den Rahmen P und den Geltungsbereich der allgemeinen Formel präzisieren und einen Task anlegen, dessen Abschlusskriterien eine korrekte Herleitung und eine Erklärung enthalten, wie die ursprüngliche Formel darin enthalten ist. |
| Beginnen Sie mit der Arbeit an Task F0001, bis 5 % des Wochenkontingents verbleiben; ordnen Sie dann die Ergebnisse und pausieren Sie. | Den aktuellen Zustand und die Ausführungsbedingungen des Tasks prüfen und vor Beginn bestätigen, dass die maßgebliche wöchentliche Nutzung abgelesen werden kann. Das verbleibende Kontingent überwachen, beim Schwellenwert von 5 % die Forschung anhalten, Ergebnisse, offene Fragen und einen Ansatzpunkt für die Fortsetzung ordnen und dann pausieren. |
| Setzen Sie die Arbeit an Task F0001 fort. | Das aktuelle Ziel, Strategien, vorhandene Ergebnisse und Abbruchbedingungen lesen und dann innerhalb der aktuellen Freigabe und weiterhin geltenden Grenzen fortfahren. Falls eine Abbruchbedingung weiterhin gilt, den konkreten Grund erläutern, der die Fortsetzung verhindert. |

### Gemeinsame Ziele

| Beispielanweisung | Erwartete Agentenaktionen |
| --- | --- |
| Prüfen Sie zuerst die Ansätze der Mitwirkenden und wählen Sie dann eine nützliche Vorgehensweise für meinen Task F0001. | Die einschlägigen Ansätze, wiederverwendbaren Ergebnisse und aufschlussreichen Fehlschläge lesen und die eigene Strategy innerhalb des Beteiligungsumfangs und der bestehenden Ausführungsbedingungen von F0001 wählen oder anpassen. Unterschiedliche Ansätze können doppelte Arbeit verringern; bewusste unabhängige Überprüfung, Replikation und gegenseitige Kontrolle bleiben angemessen. |
| Richten Sie für diese Frage einen gemeinsamen Task ein und verknüpfen Sie ihn mit Task F0001. | Die gemeinsame Fragestellung, Voraussetzungen, den Geltungsbereich und die Abschlusskriterien prüfen und einen geeigneten gemeinsamen Task einrichten oder wiederverwenden; Ihren Task F0001 mit der tatsächlich übernommenen Version des gemeinsamen Vertrags verknüpfen, Ihren Beteiligungsumfang und Ihre individuellen Abschlusskriterien festlegen und die bestehenden Ausführungsbedingungen beibehalten. Die Verknüpfung allein startet keine Forschung. |


### Inhalte importieren

| Beispielanweisung | Erwartete Agentenaktionen |
| --- | --- |
| Importieren Sie Task F0001 aus meinem Repository 〈Repository-Adresse〉. | Das Quellrepository und Ihre Identität als Autor prüfen, F0001 samt den notwendigen mathematischen Abhängigkeiten importieren und ausreichende vorhandene lokale Materialien wiederverwenden; benötigte Beiträge anderer Autoren durch Intake übernehmen und je nach Situation die Verknüpfung zum gemeinsamen Vertrag beibehalten oder einen vollständigen eigenständigen Vertrag ausarbeiten. Gültige Stoppbedingungen und Kontingente beibehalten; der Import allein startet keine Forschung. |
| Importieren Sie meine Schreibeinstellungen und das Manuskript F0001 aus meinem Repository 〈Repository-Adresse〉. | Die ausgewählten, weiterhin geltenden persönlichen Schreibeinstellungen sowie Quelldateien, Abbildungen, Bibliografie und notwendige mathematische Grundlagen des Manuskripts F0001 importieren; Autorenschaft und Geltungsbereich der Einstellungen bewahren, vorhandene lokale Materialien wiederverwenden, Verweise korrigieren, erforderliche Kompilierungsprüfungen durchführen und fehlende Eingaben sowie verbleibende Probleme angeben. |
| Übernehmen Sie aus 〈Repository-Adresse〉 Materialien zu Alices Task A0001. | Das Quellrepository und Alices Autoridentität prüfen, die für diesen Auftrag benötigten Ergebnisse, Argumente, Berechnungen und Prüfberichte zu A0001 auswählen und ausreichende vorhandene Materialien wiederverwenden; bei der Übernahme ursprüngliche Autorenschaft, genaue Quellen, die vollständige notwendige Mathematik und tatsächliche Prüfungsgrenzen erhalten und nicht verfügbare notwendige Eingaben angeben. Spätere Forschung im Rahmen Ihres eigenen Tasks und Ihrer eigenen Freigabe durchführen. |

### Weitere häufige Anweisungen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Erwägen Sie, mithilfe von Theorie A ein S zu konstruieren; ergänzen Sie Task F0001 um diese [Strategie](../Benutzerhandbuch.md#material-strategy). | Die Anwendbarkeit von Theorie A prüfen und die vorgeschlagene Konstruktion als Forschungsstrategie für F0001 dokumentieren. Voraussetzungen, vorgesehene Rolle, noch zu prüfende Schritte und nächste Aktion angeben und die Strategie mit vorhandenen Strategien vergleichen, um Doppelungen zu vermeiden. |
| Arbeiten Sie die obige Diskussion in die Strategien von F0001 ein. | Den besprochenen Ansatz bestimmen, eine vorhandene Strategie aktualisieren oder bei Bedarf eine neue anlegen, Grundlage, offene Fragen und nächsten Schritt festhalten und die Strategie mit F0001 verknüpfen. |
| Ordnen und dokumentieren Sie die obige Diskussion nach den Regeln des Rahmenwerks. | Wiederverwendbare Aussagen und Argumente, Untersuchungserkenntnisse und weitere notwendige Belege mit ihren Voraussetzungen, Quellen und offenen Teilen in geeigneten Materialien bewahren. Vorhandene Einträge wiederverwenden und Referenzen korrigieren. |
| Berichten Sie über den aktuellen Fortschritt bei F0001. | Den aktuellen Zustand des Tasks prüfen, bewiesene Ergebnisse, vorläufige Argumente, rechnerische Beobachtungen und offene Fragen unterscheiden, die einschlägigen Materialien verlinken und erläutern, was zur Erreichung des ursprünglichen Ziels noch fehlt. |
| Ordnen Sie die bisherigen Ergebnisse und pausieren Sie anschließend. | Die Prüfung und Ordnung der Arbeit der aktuellen Runde abschließen. Nützliche Ergebnisse, gescheiterte Versuche, verbleibende Fragen und einen brauchbaren Ansatzpunkt für die Fortsetzung bewahren; die Pause und weiterhin geltende Bedingungen dokumentieren und anschließend die weitere Forschung anhalten. |

## <a id="administration-instructions"></a>Verwaltungsanweisungen

Nutzen Sie diese Beispiele für Git-Vorgänge, Umgebungseinstellungen und gewöhnliche Wartung.

### Commit und Push

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Erstellen Sie einen [Commit](../Benutzerhandbuch.md#notion-commit) und führen Sie einen [Push](../Benutzerhandbuch.md#notion-push) aus. | Den beabsichtigten Umfang der Übergabe bestimmen und nicht betroffene vorgemerkte Änderungen bewahren. Identität der Beitragenden, Branch und entferntes Ziel prüfen; die Verbindung bestätigen, den Commit erstellen und pushen, anschließend den übernommenen Umfang und das Ergebnis auf dem entfernten Repository angeben. |
| Committen und pushen Sie die Änderungen im Manuskriptverzeichnis für F0001. | Das Manuskriptprojekt für F0001 ermitteln, ausschließlich die für Git bestimmten Änderungen im angegebenen Verzeichnis committen und andere Arbeit bewahren. Vor dem Push Identität, Ziel und Verbindung bestätigen und den tatsächlichen Umfang angeben. |
| Committen Sie alle Änderungen im Arbeitsbereich. | Sämtliche Änderungen im Arbeitsbereich und deren Autorenschaft prüfen, die für Git bestimmten Inhalte lokal committen, durch Ignorierregeln ausgeschlossene Dateien bewahren und den Commit-Umfang sowie verbleibende Änderungen angeben. |
| Committen und pushen Sie ohne jegliche Prüfungen. | Inhaltliche Durchsicht, Formatprüfungen, Tests und zusätzliche Durchsuchungen auslassen. Nur die für die Git-Übergabe notwendigen Bestimmungen von Umfang, Identität und Ziel sowie Verbindungstests durchführen, dann committen, pushen und das Ergebnis angeben. |

### Pull und Merge

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| [Rufen](../Benutzerhandbuch.md#notion-pull) Sie die neuesten entfernten Änderungen ab und [führen](../Benutzerhandbuch.md#notion-merge) Sie sie mit dem [lokalen Branch](../Benutzerhandbuch.md#notion-git-branch) zusammen. | Den aktuellen Branch und das zugehörige entfernte Repository prüfen, lokale Arbeit bewahren, entfernte Aktualisierungen abrufen und zusammenführen und das Ergebnis angeben. Bei Konflikten, die die mathematische Bedeutung betreffen, die konkreten Unterschiede erläutern und das weitere Vorgehen vorschlagen. |

### Umgebungseinstellungen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Erstellen Sie eine Verzeichnisverknüpfung von [mathematics/literature/pdf](../../mathematics/literature/pdf) nach `D:\MyLiterature`. | Projektpfad und Zielverzeichnis prüfen, vorhandene Quellen bewahren, die Directory Junction zum angegebenen Ordner einrichten und bestätigen, dass Quelldateien von Git ausgeschlossen sind. |
| Setzen Sie die standardmäßige [Kontextlänge](../Benutzerhandbuch.md#notion-context-length) für `<Name der Laufzeitumgebung>` in diesem Projekt auf 512k. | Die Projektkonfiguration der [Laufzeitumgebung](../agent-harness.md) ermitteln, bestätigen, dass Modell und Laufzeit die gewünschte Länge unterstützen, und den Projektstandard aktualisieren. Erläutern, wie die Änderung wirksam wird und ob ihre tatsächliche Wirksamkeit überprüft wurde; wenn die gewünschte Einstellung nicht unterstützt wird, die tatsächliche Grenze angeben. |
| Legen Sie meine standardmäßige Abbruchbedingung für Tasks fest: pausieren, wenn 5 % des Wochenkontingents verbleiben. | Dies als Ihre persönliche Standardpräferenz für die Ausführung festhalten, die gilt, wenn keine spezifischere Einstellung Vorrang hat. Wirksame Bedingungen bestehender Tasks bewahren und erläutern, wie die maßgebliche wöchentliche Nutzung abgelesen werden kann. |

### Gewöhnliche Wartung

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Stellen Sie das Framework-Upgrade zurück und setzen Sie die aktuelle Arbeit fort. | Die installierte Version beibehalten und den autorisierten Auftrag fortsetzen; die Erinnerung erteilt keine Upgrade-Erlaubnis. |
| Deaktivieren Sie automatische Framework-Versionsprüfungen für dieses Repository. | Die tägliche Prüfung der Versionsmetadaten für dieses Repository deaktivieren und das vorhandene Rahmenwerk sowie die Forschungsarbeit bewahren. |
| Aktivieren Sie automatische Framework-Versionsprüfungen für dieses Repository. | Die tägliche Prüfung des Repositorys aktivieren; ein späteres Upgrade erfordert weiterhin Ihre ausdrückliche Anweisung. |
| Prüfen Sie die offizielle Framework-Version jetzt erneut. | Eine einzelne neue Prüfung mit Zeitbegrenzung durchführen, die installierte und die bestätigte verfügbare Version oder die fehlende Bestätigung melden und eine bereits erfolgte Erinnerung bewahren. |
| Aktualisieren Sie dieses Repository auf die gerade ermittelte offizielle Framework-Version. | Gewählte Version, betroffene lokale Framework-Dateien und tatsächliche Materialmigration bestimmen, vorhandene Forschung und gültige Task-Bedingungen bewahren und das ausdrücklich autorisierte Upgrade durchführen. |
| Prüfen Sie die Dateien in `.tmp` und löschen Sie diejenigen, die gefahrlos entfernt werden können. | Zweck der Dateien und ihre aktuelle Verwendung prüfen. Zunächst notwendige Inhalte bewahren, die noch nicht in den Forschungsmaterialien gespeichert sind, und dann nur Dateien löschen, die nachweislich entbehrlich sind und von keinen anderen aktiven Sitzungen verwendet werden. |

## Manuskripte verfassen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |

## Formalisierung in Lean

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
