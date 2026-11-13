# Anweisungsbeispiele

[Benutzerhandbuch](../Benutzerhandbuch.md)

Beschreiben Sie Ihr Ziel in der Sprache Ihrer Wahl.
Geben Sie Ihrem Agenten in der gewählten Agenten-Laufzeitumgebung klare Anweisungen und orientieren Sie sich dabei an den folgenden Beispielen.
Die folgenden Beispiele sind in Anweisungen zur [Einrichtung](#setup), [Forschung](#research-instructions), [Verwaltung](#administration-instructions), [Manuskripterstellung](#writing-instructions) und [Formalisierung in Lean](#lean-instructions) gegliedert.
Passen Sie die Formulierungen an Ihre tatsächliche Frage, Ihre Dateien und den Arbeitsumfang an.

## <a id="setup"></a>Anweisungen zur Einrichtung

Nutzen Sie diese Beispiele, um Ihre Arbeitsumgebung vorzubereiten, Ihre Autorenidentität zu registrieren und lokale Ressourcen einzurichten.
Die Reihenfolge der Installations- und Registrierungsschritte finden Sie im Abschnitt [Einrichtung](../Benutzerhandbuch.md#setup) des Handbuchs.

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| <a id="install-acme"></a> Laden Sie ACME (https://github.com/vtejdn/acme) herunter und installieren Sie es in `D:\my-math-repository`. | Vorhandene Inhalte des angegebenen Verzeichnisses prüfen und die Rahmenwerkdateien der gewählten offiziellen Version in das tatsächliche Projektstammverzeichnis integrieren. Vorhandene Inhalte und die Git-Historie bewahren; die Git-Metadaten des offiziellen Repositorys nicht übernehmen. Vorhandene Projekt- und Autorenangaben wiederverwenden, nötige Einrichtungsschritte ergänzen, Rahmenwerkversion und Einstiegspunkte im Projektstammverzeichnis prüfen und den tatsächlichen Installationsort, die Version sowie offene Arbeiten angeben. |
| <a id="register"></a> Registrieren Sie Ali als meinen Autorenschlüssel; verwenden Sie Alice als vollständigen Namen. | Nach Prüfung des Schlüssels und vorhandener Registrierungen den angegebenen Wert `Ali` als Ihren Autorenschlüssel und `Alice` als Namen für die Namensnennung in `LICENSE` verwenden. Sie registrieren, die Namensnennung unter Wahrung vorhandener Identitäten und Hinweise hinzufügen und diese Arbeitskopie mit `Ali` verknüpfen, wenn sie Git verwendet. |
| <a id="install-git"></a> Installieren Sie [Git](../git-repository/Git-Repositorys.md#notion-git). | Prüfen, ob Git bereits installiert ist, es bei Bedarf installieren und die verfügbare Version sowie verbleibende Einrichtungsschritte angeben. |
| <a id="setup-git"></a> Legen Sie für Git-Commits in diesem Repository den Namen `Alice` und die E-Mail-Adresse `alice@email.com` fest. | Die für dieses Repository wirksame Git-Commit-Identität prüfen. Den angegebenen Namen und die E-Mail-Adresse bei Bedarf für das Repository oder den jeweiligen Arbeitsbaum konfigurieren. Die Übereinstimmung mit den registrierten Git-Identitätsangaben des Autors prüfen und die wirksamen Werte angeben. |
| Erklären Sie mir, wie ich eine Verbindung zu [GitHub](../git-repository/Git-Repositorys.md#notion-github) herstelle. | Anmeldung, Authentifizierung und Verbindung zu einem entfernten Repository erklären und benennen, welche Schritte Sie selbst ausführen müssen. |
| <a id="test-github-ssh"></a> Testen Sie meine SSH-Verbindung zu GitHub. | Die Authentifizierung mit `ssh -T git@github.com` und den für Git vorgesehenen SSH-Einstellungen testen. Falls ein SSH-Hostalias eingerichtet ist, diesen verwenden. Vor dem Akzeptieren eines neuen Hostschlüssels prüfen, ob sein Fingerabdruck mit einem von GitHub veröffentlichten Wert übereinstimmt. Die Bestätigung der Authentifizierung durch GitHub gilt auch bei Exitcode `1` als Erfolg. Das im Bestätigungstext genannte Konto und etwaige Abweichungen vom erwarteten Konto angeben. Bei einem Fehlschlag den konkreten Fehler melden. [GitHubs Anleitung zum Testen der SSH-Verbindung](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection) |
| Ich habe die Verbindung zu GitHub eingerichtet. Testen Sie die Verbindung. | Das vorgesehene GitHub-Repository ermitteln und den Lesezugriff mit `git ls-remote` über die dafür konfigurierte SSH- oder HTTPS-Verbindung prüfen. Bei einem leeren Repository kann die Prüfung erfolgreich sein, ohne Referenzen zurückzugeben. Das Ziel-Repository, das verwendete Protokoll und, sofern verifiziert, das Konto angeben. Das Ergebnis der Leseprüfung oder den konkreten Fehler melden. [Git-Referenz für `ls-remote`](https://git-scm.com/docs/git-ls-remote) |
| <a id="setup-repo"></a> Setzen Sie den Repository-Schlüssel auf `〈Repository-Schlüssel〉`. | Den gewählten Repository-Schlüssel prüfen, einen gültigen Wert erfassen und betroffene aktuelle Verweise aktualisieren; bei einem ungültigen Wert um eine neue Wahl bitten. Der Repository-Schlüssel ist unabhängig von Projektabkürzung, vollständigem Namen und README-Titel; die Bedeutung von Autorenschlüsseln, Materialidentitäten und historischen Quellenangaben bewahren. |
| Setzen Sie die Repository-Abkürzung und den vollständigen Namen auf `〈Abkürzung〉` und `〈vollständiger Name〉`. | Die von Ihnen unabhängig gewählte Projektabkürzung und den vollständigen Namen erfassen und prüfen, dass beide Angaben jeweils aus nicht leerem, einzeiligem Text bestehen. Daraus die README-Hauptüberschrift „〈Abkürzung〉: 〈vollständiger Name〉“ bilden, Konfiguration und Überschrift konsistent halten und den übrigen Text bewahren. Der Repository-Schlüssel wird getrennt davon festgelegt. |
| <a id="connect-github"></a> Richten Sie Git ein und verbinden Sie es mit meinem Repository <https://github.com/alice/acme>. | Git nur bei Bedarf initialisieren, fehlende Registrierungen des Repository-Namens oder Autors anhand Ihrer Angaben vervollständigen und die Arbeitskopie mit Ihrem Autorenschlüssel verknüpfen. Die Commit-Identität auf Übereinstimmung mit Ihrer Registrierung prüfen oder entsprechend konfigurieren, das angegebene entfernte Repository verbinden und den Zugriff über das maßgebliche Konto oder den Authentifizierungskanal testen. Vorhandene Commits, nicht betroffene Einstellungen und Task-Grenzen bewahren und das konfigurierte Ziel sowie verbleibende Einrichtungsschritte angeben. |
| <a id="clone-repo"></a> [Klonen](../Benutzerhandbuch.md#notion-clone) Sie das Repository meines Mitwirkenden <https://github.com/alice/acme> und registrieren Sie mich als Bob. | Das gemeinsame Repository klonen und den Autorenschlüssel `Bob`, Ihre tatsächliche Identität und vorhandene Registrierungen prüfen. Vor der Erstregistrierung den unabhängig gewählten Namen für die Namensnennung in `LICENSE` erfragen, dann registrieren und den nötigen Hinweis ergänzen. Eine passende vorhandene Identität wiederverwenden, die neue Git-Arbeitskopie mit dem geprüften Autorenschlüssel verknüpfen, bestehende Autoren und Forschungsmaterialien bewahren und die Einstellungen der Git-Commit-Identität erläutern. |

## <a id="research-instructions"></a>Forschungsanweisungen

Nutzen Sie diese Beispiele, um mit Literatur zu arbeiten und mathematische Fragen zu untersuchen.

### Literatur suchen, registrieren oder prüfen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Sichten Sie die lokale Quelle abc26, registrieren Sie sie und prüfen Sie sie. | Werk, Ausgabe und lokale Originaldatei von abc26 bestimmen, die Bibliografie vervollständigen und bei Bedarf Hinweise zu Ausgabe und Originalfundstelle pflegen. Wenn das Original ein Inhaltsverzeichnis enthält, eine durchsuchbare Fassung erstellen. Den mathematischen Inhalt prüfen und den tatsächlich geprüften Umfang, Schlussfolgerungen und offene Fragen dokumentieren. |
| Prüfen Sie Satz 1.7 in abc26. | Satz 1.7 im Original auffinden, seine vollständige Aussage, Voraussetzungen, den Beweis und die Anwendbarkeit der notwendigen unterstützenden Ergebnisse prüfen sowie Befunde, ungeprüfte Teile und konkrete Lücken dokumentieren. |
| Suchen Sie nach *On the construction of S* und versuchen Sie, das Werk zu registrieren und zu prüfen. | Werk und Ausgabe bestimmen, vorhandene Materialien heranziehen und versuchen, das Original zu beschaffen; die Bibliografie vervollständigen und bei Bedarf Hinweise zur erhaltenen Ausgabe und Quellenfundstelle pflegen. Wenn das Original ein Inhaltsverzeichnis enthält, eine durchsuchbare Fassung erstellen. Die erhaltenen Inhalte prüfen und Beschaffungsfehler, nicht verfügbare Teile sowie den tatsächlich geprüften Umfang angeben. |
| Wie wird diese Definition in der einschlägigen Literatur verwendet? | Vorhandene Definitionseinträge und einschlägige Originalquellen heranziehen, Objekte, Voraussetzungen, Notation und Verwendungen vergleichen, genaue Literaturangaben machen und Quelldefinitionen von lokalen Umformulierungen oder Verallgemeinerungen unterscheiden. |

### <a id="start-or-continue-research"></a>[Task](../Benutzerhandbuch.md#material-task)

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Legen Sie für Vermutung 1.3 in abc26 einen Task in [Linie W](../Benutzerhandbuch.md#notion-research-line-letter) an. | Die ursprüngliche Aussage, Voraussetzungen und den Geltungsbereich von Vermutung 1.3 prüfen und zunächst nach einem vorhandenen Task zur gleichen Frage suchen. Wenn ein neuer Task nötig ist, Linie W verwenden und Quelle, genaue Frage und Abschlusskriterien angeben. |
| Legen Sie einen Task in Linie F mit dem Ziel „Wenn P, dann Q“ an. | Objekte, Voraussetzungen und Quantoren in P und Q präzisieren, einen Task in Linie F mit „P impliziert Q“ als vollständigem Ziel anlegen und die Abschlusskriterien festlegen. |
| Legen Sie einen neuen Task an, um Proposition P vom endlichdimensionalen auf den unendlichdimensionalen Fall zu verallgemeinern. | Die ursprüngliche Proposition prüfen, die neuen Objekte, Voraussetzungen und die angestrebte Schlussfolgerung präzisieren, den Task anlegen und die ursprüngliche Proposition als Spezialfall bewahren, den die Verallgemeinerung abdecken muss. |
| Legen Sie einen Task an, um im Rahmen P eine allgemeine Formel zu finden, die Formel (1) in abc26 umfasst. | Voraussetzungen und Notation der ursprünglichen Formel prüfen, den Rahmen P und den Geltungsbereich der allgemeinen Formel präzisieren und einen Task anlegen, dessen Abschlusskriterien eine korrekte Herleitung und eine Erklärung enthalten, wie die ursprüngliche Formel darin enthalten ist. |
| Beginnen Sie mit der Arbeit an Task F0001, bis 5 % des Wochenkontingents verbleiben. | Den aktuellen Zustand und die wirksamen Ausführungsbedingungen des Tasks prüfen und bestätigen, dass die wöchentliche Nutzung des maßgeblichen Kontos abgelesen werden kann; andernfalls die Grenze erläutern und die Fortsetzung aufschieben. Bei erfüllten Ausführungsbedingungen forschen und das verbleibende Kontingent überwachen; bei der ersten Beobachtung von höchstens 5 % Restkontingent oder einem Überwachungsfehler anhalten. Nützliche Ergebnisse, offene Fragen und einen Ansatzpunkt zur Fortsetzung bewahren und die wirksamen Stoppbedingungen festhalten. |
| Ordnen Sie die bisherigen Ergebnisse und pausieren Sie anschließend. | Die Prüfung und Ordnung der Arbeit der aktuellen Runde abschließen. Nützliche Ergebnisse, gescheiterte Versuche, verbleibende Fragen und einen brauchbaren Ansatzpunkt für die Fortsetzung bewahren; die Pause und weiterhin geltende Bedingungen dokumentieren und anschließend die weitere Forschung anhalten. |
| Berichten Sie über den aktuellen Fortschritt bei F0001. | Den aktuellen Zustand des Tasks prüfen, bewiesene Ergebnisse, vorläufige Argumente, rechnerische Beobachtungen und offene Fragen unterscheiden, die einschlägigen Materialien verlinken und erläutern, was zur Erreichung des ursprünglichen Ziels noch fehlt. |
| Setzen Sie die Arbeit an Task F0001 fort. | Das aktuelle Ziel, Strategien, vorhandene Ergebnisse und Abbruchbedingungen lesen und dann innerhalb der aktuellen Freigabe und weiterhin geltenden Grenzen fortfahren. Falls eine Abbruchbedingung weiterhin gilt, den konkreten Grund erläutern, der die Fortsetzung verhindert. |

### [Strategien](../Benutzerhandbuch.md#material-strategy)

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Erwägen Sie, mithilfe von Theorie A ein S zu konstruieren; ergänzen Sie [Task](../Benutzerhandbuch.md#material-task) F0001 um diese Strategie. | Die Anwendbarkeit von Theorie A prüfen und die vorgeschlagene Konstruktion als Forschungsstrategie für F0001 dokumentieren. Voraussetzungen, vorgesehene Rolle, noch zu prüfende Schritte und nächste Aktion angeben und die Strategie mit vorhandenen Strategien vergleichen, um Doppelungen zu vermeiden. |
| Arbeiten Sie die obige Diskussion in die Strategien von F0001 ein. | Den besprochenen Ansatz bestimmen, eine vorhandene Strategie aktualisieren oder bei Bedarf eine neue anlegen, Grundlage, offene Fragen und nächsten Schritt festhalten und die Strategie mit F0001 verknüpfen. |
| Suchen und analysieren Sie Ansätze für Task G0001, schlagen Sie Strategien vor und legen Sie deren Prioritäten autonom fest. | Ziel, Grenzen, vorhandene Strategien und einschlägige Materialien von G0001 lesen, zuerst lokale Ergebnisse wiederverwenden und anschließend bei Bedarf Literatur suchen und prüfen. Voraussetzungen, Grundlagen, Hindernisse und Ressourcenbedarf der möglichen Ansätze vergleichen, Strategien vorschlagen und autonom priorisieren; Gründe der Reihenfolge, offene Schritte und nächste Aktion festhalten sowie ursprüngliches Ziel, Abschlusskriterien und wirksame Ausführungsgrenzen bewahren. |

### [Gemeinsame Tasks](../Benutzerhandbuch.md#material-task)

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Prüfen Sie zuerst die Ansätze der Mitwirkenden Alice und wählen Sie dann eine nützliche Vorgehensweise für meinen Task F0001. | Die einschlägigen Ansätze, wiederverwendbaren Ergebnisse und aufschlussreichen Fehlschläge lesen und die eigene Strategy innerhalb des Beteiligungsumfangs und der bestehenden Ausführungsbedingungen von F0001 wählen oder anpassen. Unterschiedliche Ansätze können doppelte Arbeit verringern; bewusste unabhängige Überprüfung, Replikation und gegenseitige Kontrolle bleiben angemessen. |
| Richten Sie für diese Frage einen gemeinsamen Task ein und verknüpfen Sie ihn mit Task F0001. | Die gemeinsame Fragestellung, Voraussetzungen, den Geltungsbereich und die Abschlusskriterien prüfen und einen geeigneten gemeinsamen Task einrichten oder wiederverwenden; Ihren Task F0001 mit der tatsächlich übernommenen Version des gemeinsamen Vertrags verknüpfen, Ihren Beteiligungsumfang und Ihre individuellen Abschlusskriterien festlegen und die bestehenden Ausführungsbedingungen beibehalten. Die Verknüpfung allein startet keine Forschung. |

### [Mathematische Aussagen](../Benutzerhandbuch.md#material-claim) und [Explorationsprotokolle](../Benutzerhandbuch.md#material-ledger)

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Ordnen und dokumentieren Sie die obige Diskussion nach den Regeln des Rahmenwerks. | Wiederverwendbare Aussagen und Argumente, Untersuchungserkenntnisse und weitere notwendige Belege mit ihren Voraussetzungen, Quellen und offenen Teilen in geeigneten Materialien bewahren. Vorhandene Einträge wiederverwenden und Referenzen korrigieren. |

## <a id="administration-instructions"></a>Verwaltungsanweisungen

Nutzen Sie diese Beispiele für [Git](../git-repository/Git-Repositorys.md#notion-git)-Vorgänge, Umgebungseinstellungen und gewöhnliche Wartung.

### [Commit](../Benutzerhandbuch.md#notion-commit) und [Push](../Benutzerhandbuch.md#notion-push)

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Erstellen Sie einen Commit und führen Sie einen Push aus. | Den beabsichtigten Umfang der Übergabe bestimmen und nicht betroffene vorgemerkte Änderungen bewahren. Identität der Beitragenden, Branch und entferntes Ziel prüfen; die Verbindung bestätigen, den Commit erstellen und pushen, anschließend den übernommenen Umfang und das Ergebnis auf dem entfernten Repository angeben. |
| Committen und pushen Sie die Änderungen im Manuskriptverzeichnis für F0001. | Das Manuskriptprojekt für F0001 ermitteln, ausschließlich die für Git bestimmten Änderungen im angegebenen Verzeichnis committen und andere Arbeit bewahren. Vor dem Push Identität, Ziel und Verbindung bestätigen und den tatsächlichen Umfang angeben. |
| Committen Sie alle Änderungen im Arbeitsbereich. | Sämtliche Änderungen im Arbeitsbereich und deren Autorenschaft prüfen, die für Git bestimmten Inhalte lokal committen, durch Ignorierregeln ausgeschlossene Dateien bewahren und den Commit-Umfang sowie verbleibende Änderungen angeben. |
| Committen und pushen Sie ohne jegliche Prüfungen. | Inhaltliche Durchsicht, Formatprüfungen, Tests und zusätzliche Durchsuchungen auslassen. Nur die für die Git-Übergabe notwendigen Bestimmungen von Umfang, Identität und Ziel sowie Verbindungstests durchführen, dann committen, pushen und das Ergebnis angeben. |

### [Pull](../Benutzerhandbuch.md#notion-pull) und [Merge](../Benutzerhandbuch.md#notion-merge)

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Rufen Sie die neuesten entfernten Änderungen ab und führen Sie sie mit dem [lokalen Branch](../Benutzerhandbuch.md#notion-git-branch) zusammen. | Den aktuellen Branch und das zugehörige entfernte Repository prüfen, lokale Arbeit bewahren, entfernte Aktualisierungen abrufen und zusammenführen und das Ergebnis angeben. Bei Konflikten, die die mathematische Bedeutung betreffen, die konkreten Unterschiede erläutern und das weitere Vorgehen vorschlagen. |

### Umgebungseinstellungen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Erstellen Sie eine Verzeichnisverknüpfung von [mathematics/literature/pdf](../../mathematics/literature/pdf) nach `D:\MyLiterature`. | Projektpfad und Zielverzeichnis prüfen, vorhandene Quellen bewahren, die Directory Junction zum angegebenen Ordner einrichten und bestätigen, dass Quelldateien von Git ausgeschlossen sind. |
| Setzen Sie die standardmäßige [Kontextlänge](../Benutzerhandbuch.md#notion-context-length) für `<Name der Laufzeitumgebung>` in diesem Projekt auf 512k. | Die Projektkonfiguration der [Laufzeitumgebung](../agent-harness.md) ermitteln, bestätigen, dass Modell und Laufzeit die gewünschte Länge unterstützen, und den Projektstandard aktualisieren. Erläutern, wie die Änderung wirksam wird und ob ihre tatsächliche Wirksamkeit überprüft wurde; wenn die gewünschte Einstellung nicht unterstützt wird, die tatsächliche Grenze angeben. |
| Legen Sie meine standardmäßige Abbruchbedingung für Tasks fest: pausieren, wenn 5 % des Wochenkontingents verbleiben. | Dies als Ihre persönliche Standardpräferenz für die Ausführung festhalten, die gilt, wenn keine spezifischere Einstellung Vorrang hat. Wirksame Bedingungen bestehender Tasks bewahren und erläutern, wie die maßgebliche wöchentliche Nutzung abgelesen werden kann. |

### [Import](../Benutzerhandbuch.md#notion-import) und [Übernahme](../Benutzerhandbuch.md#notion-intake)

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Importieren Sie Task F0001 aus meinem Repository `〈Repository-Adresse〉`. | Das Quellrepository und Ihre Identität als Autor prüfen, F0001 samt den notwendigen mathematischen Abhängigkeiten importieren und ausreichende vorhandene lokale Materialien wiederverwenden; benötigte Beiträge anderer Autoren durch Intake übernehmen und je nach Situation die Verknüpfung zum gemeinsamen Vertrag beibehalten oder einen vollständigen eigenständigen Vertrag ausarbeiten. Gültige Stoppbedingungen und Kontingente beibehalten; der Import allein startet keine Forschung. |
| Importieren Sie meine Schreibeinstellungen und das Manuskript F0001 aus meinem Repository `〈Repository-Adresse〉`. | Die ausgewählten, weiterhin geltenden persönlichen Schreibeinstellungen sowie Quelldateien, Abbildungen, Bibliografie und notwendige mathematische Grundlagen des Manuskripts F0001 importieren; Autorenschaft und Geltungsbereich der Einstellungen bewahren, vorhandene lokale Materialien wiederverwenden, Verweise korrigieren, erforderliche Kompilierungsprüfungen durchführen und fehlende Eingaben sowie verbleibende Probleme angeben. |
| Übernehmen Sie aus `〈Repository-Adresse〉` Materialien zu Alices Task A0001. | Das Quellrepository und Alices Autoridentität prüfen, die für diesen Auftrag benötigten Ergebnisse, Argumente, Berechnungen und Prüfberichte zu A0001 auswählen und ausreichende vorhandene Materialien wiederverwenden; bei der Übernahme ursprüngliche Autorenschaft, genaue Quellen, die vollständige notwendige Mathematik und tatsächliche Prüfungsgrenzen erhalten und nicht verfügbare notwendige Eingaben angeben. Spätere Forschung im Rahmen Ihres eigenen Tasks und Ihrer eigenen Freigabe durchführen. |

### Gewöhnliche Wartung

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |
| Aktivieren/deaktivieren Sie automatische Framework-Versionsprüfungen für dieses Repository. | Die Einstellung dieses Repositorys gemäß Ihrer Wahl aktivieren oder deaktivieren, andere Konfiguration bewahren und den aktuellen Schaltzustand angeben; bei Aktivierung die Regeln der automatischen Prüfung pro UTC-Tag anwenden. Ein Upgrade erfordert weiterhin eine tatsächliche ausdrückliche Freigabe. |
| Aktualisieren Sie das Rahmenwerk auf die neueste Version. | Installierte und neueste offizielle Version vergleichen; bei einem verfügbaren Update Zielversion und Commit festlegen, betroffene Dateien nach den Upgrade-Hinweisen anpassen und notwendige Prüfungen durchführen, dabei lokale Änderungen, Forschungsmaterialien, persönliche Einstellungen und wirksame Ausführungsbedingungen bewahren. Nach erfolgreichen Prüfungen die installierte Version aktualisieren; in einem tatsächlichen gemeinsamen Git-Repository mehrerer Autoren im Rahmen der Standardfreigabe committen, pushen und das entfernte Ergebnis bestätigen, unter Beachtung ausdrücklicher Vorgaben zu lokaler Arbeit, Offline-Arbeit oder einem Push-Verbot. Versionen vor und nach dem Upgrade, Ziel-Commit, Prüfungen und Übergabeergebnisse angeben; auch melden, wenn kein Update verfügbar ist oder Arbeiten unerledigt bleiben. |
| Beheben Sie Merge-Konflikte nach den Regeln des Rahmenwerks. | Änderungen beider Seiten, Autorenschaft und tatsächliche Befugnisse prüfen und administrative Konflikte, deren Lösung feststeht, direkt lösen, einschließlich reiner Verweiskorrekturen, die Objekt und mathematische Bedeutung bewahren. Bei inhaltlichen mathematischen Meinungsverschiedenheiten die Belege beider Seiten bewahren, Unterschiede erläutern und eine begrenzte erneute Prüfung im Rahmen bestehender oder nach Einholung notwendiger Freigabe durchführen; inhaltliche Korrekturen an fremdem Material in den eigenen Materialien des korrigierenden Autors festhalten. Zusammengeführtes Ergebnis und betroffene Verweise prüfen sowie Ergebnis und offene Punkte angeben. |
| Prüfen Sie die Dateien in `.tmp` und löschen Sie diejenigen, die gefahrlos entfernt werden können. | Zweck der Dateien und ihre aktuelle Verwendung prüfen. Zunächst notwendige Inhalte bewahren, die noch nicht in den Forschungsmaterialien gespeichert sind, und dann nur Dateien löschen, die nachweislich entbehrlich sind und von keinen anderen aktiven Sitzungen verwendet werden. |
| Prüfen Sie lokale mathematische Materialien auf Einhaltung der Rahmenwerksregeln. | Im beauftragten Umfang einen von Reparatur und Abnahme isolierten Agenten lokale mathematische Materialien samt notwendigen Eingaben und Verweisen abschnittsweise und nur lesend prüfen lassen; Autorenschaft, Versionen, Bewertungen, Quellen, die Zuordnung von Prüfungen zu den geprüften Materialien und andere geltende Anforderungen prüfen. Konformitätsprobleme in `maintenance` und inhaltliche mathematische Probleme in `erratum` festhalten und tatsächliche Abdeckung, ungeprüften Umfang sowie offene Punkte angeben. |
| Lesen Sie maintenance und erratum und beheben Sie die Probleme nach den Rahmenwerksregeln. | Die zur Reparatur anstehenden Punkte im beauftragten Umfang lesen; ein Agent mit der erforderlichen Trennung der Phasen prüft die Probleme, repariert innerhalb der tatsächlichen autorbezogenen Befugnisse, führt Selbstkontrollen durch und prüft notwendige abhängige Materialien. Konformitätsreparaturen unabhängig abnehmen lassen und bei mathematischen Fehlern die tatsächlichen Versions-, Bewertungs- und mathematischen Prüfpflichten anwenden; ursprüngliches Problem, Grundlagen, Abnahmeanforderungen sowie unreparierte oder nicht abgenommene Punkte erhalten und Reparaturumfang sowie verbleibende Grenzen angeben. |
| Nehmen Sie Materialreparaturen nach den Rahmenwerksregeln ab. | Ein unabhängiger Agent, der weder an Prüfung oder Reparatur desselben Umfangs beteiligt war noch einschlägige inhaltliche Diskussionen geerbt hat, prüft eingereichte Reparaturen und notwendige abhängige Materialien anhand der ursprünglichen Probleme und aktuellen Regeln und gibt den bestandenen oder nicht bestandenen Umfang an. Abgenommene Teile nur im Rahmen der tatsächlichen Befugnisse des betroffenen Autors oder der empfangenden Seite bereinigen; fehlgeschlagene, nicht abgenommene, außerhalb des Umfangs liegende und gleichzeitig hinzugefügte Punkte bewahren. Während der Abnahme wird nicht repariert; Konformitätsabnahme ist keine unabhängige mathematische Prüfung. |

## <a id="writing-instructions"></a>Manuskripte verfassen

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |

## <a id="lean-instructions"></a>Formalisierung in Lean

| Anweisungsbeispiel | Erwartete Aktionen des Agenten |
| --- | --- |

