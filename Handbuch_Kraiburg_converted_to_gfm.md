**Allevo-Koodai**

**Timo Krocker**

# Inhaltsverzeichnis

[1 Vorwort (#vorwort)](#vorwort)

[2 Die SAP-Seite (#die-sap-seite)](#die-sap-seite)

[2.1 SAP Berechtigungen (#sap-berechtigungen)](#sap-berechtigungen)

[2.2 Berechtigungen innerhalb des Koodai
(#berechtigungen-innerhalb-des-koodai)](#berechtigungen-innerhalb-des-koodai)

[2.3 Das Allevo-Layout (#das-allevo-layout)](#das-allevo-layout)

[2.4 TimeSets (#timesets)](#timesets)

[2.5 Festwerte (#festwerte)](#festwerte)

[2.5.1 Aufruf der Festwerte
(#aufruf-der-festwerte)](#aufruf-der-festwerte)

[2.5.2 Der Festwert „KOODAI_KAGROUP“
(#der-festwert-koodai_kagroup)](#der-festwert-koodai_kagroup)

[2.5.3 Der Festwert „KOODAI_KFGROUP“
(#der-festwert-koodai_kfgroup)](#der-festwert-koodai_kfgroup)

[2.5.4 Der Festwert „KOODAI_TIMESETS“
(#der-festwert-koodai_timesets)](#der-festwert-koodai_timesets)

[2.5.5 Der Festwert „KOODAI_SPLASHER“
(#der-festwert-koodai_splasher)](#der-festwert-koodai_splasher)

[2.5.6 Der Festwert „KOODAI_SAT_KEYS“
(#der-festwert-koodai_sat_keys)](#der-festwert-koodai_sat_keys)

[2.5.7 Der Festwert „KOODAI_HIDE_KA_PATTERN“
(#der-festwert-koodai_hide_ka_pattern)](#der-festwert-koodai_hide_ka_pattern)

[2.5.8 Globaler Festwert CHECK_KOODAI_SPLASHER
(#globaler-festwert-check_koodai_splasher)](#globaler-festwert-check_koodai_splasher)

[2.5.9 Weitere Koodai-Festwerte
(#weitere-koodai-festwerte)](#weitere-koodai-festwerte)

[2.5.10 Sonstige für Koodai interessante Allevo-Festwerte
(#sonstige-für-koodai-interessante-allevo-festwerte)](#sonstige-für-koodai-interessante-allevo-festwerte)

[2.5.11 Kundenindividuelle Festwerte
(#kundenindividuelle-festwerte)](#kundenindividuelle-festwerte)

[2.6 Statusmanagement (#statusmanagement)](#statusmanagement)

[2.7 Satelliten (#satelliten)](#satelliten)

[2.8 Das Koodai-Cockpit (#das-koodai-cockpit)](#das-koodai-cockpit)

[2.9 Customizing-Tabellen
(#customizing-tabellen)](#customizing-tabellen)

[2.9.1 /KERN/KOODAITEXT zur Pflege von sprachabhängigen Texten
(#kernkoodaitext-zur-pflege-von-sprachabhängigen-texten)](#kernkoodaitext-zur-pflege-von-sprachabhängigen-texten)

[2.9.2 /KERN/KOODAIDAFU zur Pflege der Planungsbereiche
(#kernkoodaidafu-zur-pflege-der-planungsbereiche)](#kernkoodaidafu-zur-pflege-der-planungsbereiche)

[2.9.3 /KERN/KOODAIELTY für einen statischen Aufbau und Angabe von
Splashervarianten (#_Ref114044578)](#_Ref114044578)

[2.9.4 /KERN/KOODAICOTY für die Pflege der Editierbarkeit und Bestimmung
von Muss-Feldern
(#kernkoodaicoty-für-die-pflege-der-editierbarkeit-und-bestimmung-von-muss-feldern)](#kernkoodaicoty-für-die-pflege-der-editierbarkeit-und-bestimmung-von-muss-feldern)

[2.9.5 /KERN/KOODAIDIST zur Definition von Splashervarianten
(#kernkoodaidist-zur-definition-von-splashervarianten)](#kernkoodaidist-zur-definition-von-splashervarianten)

[2.9.6 /KERN/KOODAICCOL und /KERN/KOODAICCOT
(#kernkoodaiccol-und-kernkoodaiccot)](#kernkoodaiccol-und-kernkoodaiccot)

[2.9.7 /KERN/KOODAIFCOL und /KERN/KOODAIFCOT
(#kernkoodaifcol-und-kernkoodaifcot)](#kernkoodaifcol-und-kernkoodaifcot)

[2.9.8 /KERN/KOODAIVIEW (#kernkoodaiview)](#kernkoodaiview)

[2.9.9 KERN/KOODAICJS (#kernkoodaicjs)](#kernkoodaicjs)

[2.9.10 Pflege von Matchcode-Tabellen
[21](#pflege-von-matchcode-tabellen)](#pflege-von-matchcode-tabellen)

[2.10 Die Einrichtung der Pauschalen
(#die-einrichtung-der-pauschalen)](#die-einrichtung-der-pauschalen)

[2.10.1 Flexible Planung (#flexible-planung)](#flexible-planung)

[2.10.2 Enrichment (#enrichment)](#enrichment)

[2.11 Der Jahreswechsel (#der-jahreswechsel)](#der-jahreswechsel)

[3 Das WebFrontend (#das-webfrontend)](#das-webfrontend)

[3.1 Anmeldung (#anmeldung)](#anmeldung)

[3.2 Das Dashboard (#das-dashboard)](#das-dashboard)

[3.3 Die Hauptplanungssicht
(#die-hauptplanungssicht)](#die-hauptplanungssicht)

[3.3.1 Suchfunktion und Planungsart
(#suchfunktion-und-planungsart)](#suchfunktion-und-planungsart)

[3.3.2 Die Iconleiste (#die-iconleiste)](#die-iconleiste)

[3.4 Eigene Spalten verwalten
(#eigene-spalten-verwalten)](#eigene-spalten-verwalten)

[3.4.1 JavaScript-Funktionen
(#javascript-funktionen)](#javascript-funktionen)

[3.4.2 Formeleditor (#formeleditor)](#formeleditor)

[3.4.3 SVG Template GUI (#svg-template-gui)](#svg-template-gui)

[3.4.4 Formel (#formel)](#formel)

[3.5 Berechnete Planspalten
(#berechnete-planspalten)](#berechnete-planspalten)

[3.6 Views (#views)](#views)

[3.7 Multi Edit (#multi-edit)](#multi-edit)

[3.8 Normales Editieren (#normales-editieren)](#normales-editieren)

[3.9 Navigieren mit der Tastatur
(#navigieren-mit-der-tastatur)](#navigieren-mit-der-tastatur)

# 1 Vorwort

Allevo Koodai ist die Web-Version des Allevo. Während Allevo Junan,
Excel als Frontend verwendet, ist bei Allevo Koodai der Browser
(vorzugsweise Chrome) das Frontend. Mit Allevo Koodai können Aufträge,
PSP-Elemente, Profit Center, Allevo-Objekte und natürlich Kostenstellen
mit/ohne Leistungsarten und statistische Kennzahlen geplant werden.
Fachplanungen über Satelliten und SunTables sind ebenso möglich wie eine
einfache CO-PA-Planung über einen Satelliten.

# 2 Die SAP-Seite

## 2.1 SAP Berechtigungen

Um den Zugriff über die RFC-Verbindung zu ermöglichen, sind gegenüber
dem Inplace-Modus wenige Zusatzberechtigungen erforderlich, die für das
Berechtigungsobjekt S_RFC zu pflegen sind. Die rele-vanten Informationen
sind im SAP-Hinweis 460089 (= Minimale Berechtigungsprofile für externe
RFC Programme) beschrieben. Für das WebFrontend sind die Angaben zum
Punkt „3. Aufruf eines Funkti-onsbausteins unter Verwendung des
dynamischen Repositories“ relevant.

Hier eine kurze Zusammenfassung der Funktionsgruppen, für die eine
Berechtigung erforderlich sind (Eintrag im Feld RFC_NAME für das
Berechtigungsobjekt S_RFC):

- BAPT Transaktionssteuerung für BAPIs

- RFC1 RFC-Utilities

- SDIFRUNTIME Schnittstellen für Typ-Laufzeitobjekte

- SYST System-Interface

- SYSU RFC resource administration

- RFC_METADATA RFC Metadaten lesen

**Zusätzlich** zu den oben genannten RFC-Minimalberechtigungen muss die
folgende Allevo-spezifische Funktionsgruppe berechtigt und daher in
S_RFC eingetragen werden:

- /KERN/KOODAI

## 2.2 Berechtigungen innerhalb des Koodai

Über die Tabelle **/KERN/KOODAIAUTH** können für die Rollen „ADMIN,
PLANNER und CONTROLLER“ Koodaifunktionen ausgeschalten werden. Über die
Transaktion **/n/allevo/tab** kann unter Angabe des Tabellennamens die
Tabelle aufgerufen, abgeändert oder gelöscht werden. Funktionen, die für
alle Rollen sichtbar sein sollen, brauchen hier nicht aufgeführt zu
werden. Wird eine Funktion aufgeführt, so muss bei den Rollen, die diese
Funktion nutzen dürfen, ein X gesetzt werden. Ist bei einer Rolle kein X
gesetzt, dann wird für diese Rolle das JavaScript in der rechten Spalte
ausgeführt, welches die Funktion deaktiviert.

Im obigen Beispiel wird die Schaltfläche zum Speichern der Daten in
Excel während der Planung nur für die Rollen „PLANNER“ und „CONTROLLER“
zur Verfügung gestellt. Für die Rolle „ADMIN“ wird die Funktion mit dem
JavaScript in der Spalte „REMOVE_FUNC_JS“ entfernt.

## 2.3 Das Allevo-Layout

Der Koodai kann mehrere Allevo-Layouts verwalten. Koodai - Layouts
werden im Allevo-Layout durch den ABC Modus "Koodai" gekennzeichnet.
Wählen Sie dazu aus dem Allevo-Cockpit (Transaktion: /n/Allevo/Cockpit)
über „Kostenstelle / MultiObject Planung“ aus,

und klicken Sie dann in der Menüleiste auf „Layouts“.

Dann ganz oben links auf den Button „Allevo Layouts“ klicken:

Nun muss für die entsprechenden Layouts in der Spalte „ABC Modus“ der
Wert „Koodai“ ausgewählt werden:

## 2.4 TimeSets

Zur Eingabe der TimeSets im Allevo-Cockpit (Transaktion:
/n/Allevo/Cockpit) für z.B. Kostenstellen wählen Sie über „Kostenstelle
/ MultiObject Planung“ das gewünschte Allevo-Layout aus (im Beispiel 
„ABEV“) und klicken auf
den Button „Einstellungen“ ganz rechts oben in der Menüleiste (oder
alternativ Shift + F7).

Im folgenden Dialog doppelklicken Sie auf den Punkt „TimeSets“:

Hier werden, wie in Allevo Junan, die TimeSets angelegt:

Interessant in Bezug auf den Koodai ist, dass man hier nur ein Timeset
für ein Jahr anlegen muss (z.B. CX_WW), dann aber im Festwert
„KOODAI_TIMESETS“ (siehe Kapitel „2.5.4 Der Festwert „KOODAI_TIMESETS“
mit der Angabe „CX_WW\|\|\* später im Koodai auf alle Monate dieses
Jahres als Spalten zugreifen kann. Um dann aber auch jeweils eine eigene
Spaltenüberschrift zu erhalten, sollte der Name von CX_WW z.B. wie folgt
gebildet werden: „Plan \<PERIOD(3)\> \<PLANYEAR\>“.

Im Koodai stehen dann die Spaltenüberschriften der jeweiligen
Monatsspalten zur Verfügung, wobei die (3) bewirkt, dass nur die ersten
drei Buchstaben des Monatsnamens verwendet werden:

In einer Darstellung, in der mehrere Objekte gleichzeitig geplant
werden, kann das Beschreibungsfeld auch wie folgt definiert werden:
\<OBJECT\> \<OBJECT_TEXT(20)\> Plan \<PLANYEAR\>

Die Parameter \<OBJECT\> und \<OBJECT_TEXT(20)\> bewirken, dass im
Spaltenkopf der Schlüssel des Objekts und der dazugehörige Text mit
maximal 20 Zeichen ausgegeben werden, gefolgt vom Text „Plan“, gefolgt
vom jeweiligen Planjahr:

**Hinweis**: Siehe Kapitel „Allevo Funktion der Platzhalter“ im
Allevo-Handbuch-SAP-4.2.

Es ist auch möglich in den TimeSets einen automatischen
**Zeilenumbruch** zu hinterlegen, welcher dann im Frontend
berücksichtigt wird. Mit dem Tag „\<br\>“ in
„*Ist\<br\>\<YEARFR\>\<br\>Vers: 0*“ werden automatisch zwei
Zeilenumbrüche eingefügt und die Darstellung im Frontend erfolgt
entsprechend:

## 2.5 Festwerte

### 2.5.1 Aufruf der Festwerte

Zur Eingabe der Festwerte im Allevo-Cockpit (Transaktion:
/n/Allevo/Cockpit) für z.B. Kostenstellen über „Kostenstelle /
MultiObject Planung“ auswählen

und dann das gewünschte Allevo-Layout auswählen (im Beispiel „ABEV“) und
oben in der Menüleiste ganz rechts auf den Button „Einstellungen“
klicken (oder alternativ Shift + F7).

Im folgenden Dialog auf den Punkt „Festwerte“ doppelklicken:

Die Koodai-spezifischen und anderen Festwerte können dann in der
Registerkarte „Alle“ eingegeben werden:

### 2.5.2 Der Festwert „KOODAI_KAGROUP“

1.  KOODAI_KAGROUP definiert den Kostenarten – Top-Knoten, wenn die
    Kostenarten dynamisch abgerufen werden sollen.

2.  Bleibt dieser Festwert leer, wird in der Tabelle /KERN/KOODAIELTY
    (Transaktion: **/n/Allevo/Koodai_EType**) eine statische Struktur
    gesucht.

3.  Auch wenn für den Festwert eine Kostenartengruppe angegeben ist,

> lohnt sich ein Blick in die Tabelle /KERN/KOODAIELTY (Transaktion:
> **/n/Allevo/Koodai_EType**), da mit Hilfe dieser Tabelle auch einzelne
> Kostenarten der Kostenartengruppe ausgeblendet oder auf nicht
> editierbar gesetzt werden können (siehe Kapitel 2.9.3
> /KERN/KOODAIELTY).

### 2.5.3 Der Festwert „KOODAI_KFGROUP“

**KOODAI_KFGROUP** definiert den obersten Knoten der Statistischen
Kennzahlen. Ansonsten gilt dasselbe wie für den Festwert KOODAI_KAGROUP.

### 2.5.4 Der Festwert „KOODAI_TIMESETS“

**KOODAI_TIMESETS** legt die aktiven Spalten für das WebFrontend fest.  
Z.B. CX_RR, CY_RW, CY_R2, CX_WW. Diese müssen natürlich als TimeSets im
Layout gepflegt sein (siehe Kapitel 2.4 TimeSets). Getrennt durch
Pipe-Symbole (\|) können weitere Einstellungen vorgenommen werden. Dabei
gilt folgende Reihenfolge:

> **TimeSet\|Dimension\|Monat\|Parameter**

**Beispiele:**

- CX_WW\|N → Die Dimension **N** erzeugt eine zusätzliche
  Kommentarspalte für das TimeSet CX_WW.

- CX_WW\|\|\* → Dadurch werden 12 Monatsspalten für das TimeSet CX_WW
  erzeugt.

> Achtung, die Kombination der beiden obigen Anweisungen mit  
> CX_WW\|N\|\* → Dies erzeugt 12 Kommentarspalten (und **nicht** eine
> Kommentarspalte und 12 Monatsspalten).

- CX_WW\|\|\|\<OBJECT\> → Mit dem Parameter \<OBJECT\> können mehrere
  Objekte mit ihren TimeSets in den Spalten dargestellt werden. Um die
  Objekte (z.B. Kostenstellen) später identifizieren zu können, sollte
  bei der Definition der TimeSets der Objektschlüssel (und evtl. auch
  noch der Text) angegeben werden.

### 2.5.5 Der Festwert „KOODAI_SPLASHER“

In diesem Festwert wird in der Spalte **Wert von** das TimeSet
eingetragen über dessen Wert gesplasht werden soll. Das dürfte in der
Regel das TimeSet mit der Planungsbasis sein.

Sollte es mehrere Splasher in der Planungsoberfläche geben, dann sind
die zugehörigen TimeSets kommagetrennt einzugeben. Sollte es dazu auch
noch unterschiedliche Verteilkurven geben, dann sind diese auch
kommagetrennt dahinter einzugeben.

### 2.5.6 Der Festwert „KOODAI_SAT_KEYS“

Der Festwert „KOODAI_SAT_KEYS“ wird verwendet, wenn in einem Satelliten
Informationen abgelegt sind, welche eine hierarchische Darstellung in
Form eines Baumes zulassen. Hierbei wird im von-Wert das Kind und im
bis-Wert das Elternteil hinterlegt:

Siehe hierzu auch das Kapitel „2.7 Satelliten“

### 2.5.7 Der Festwert „KOODAI_HIDE_KA_PATTERN“

Dieser Festwert kommt bei einem statischen Aufbau zum Einsatz, wie der
in der Tabelle /KERN/KOODAIELTY (Transaktion:
**/n/Allevo/Koodai_EType**) hinterlegt werden kann (siehe hierzu
“2.9.3/KERN/KOODAIELTY für einen statischen Aufbau und Angabe von
Splashervarianten“). Hier gibt es die Anforderung, einzelne Kostenarten
einer Kostenartengruppe einzeln aufzuführen und die Werte der restlichen
Kostenarten aggregiert zusammenzufassen.

**Beispiel:**

Die Kostenartengruppe 1-T-43010 enthält eine Vielzahl von Kostenarten.
Im WebFrontend sollen aber nur drei Kostenarten explizit ausgewiesen
werden und die Werte der restlichen Kostenarten sollen aggregiert unter
„40XXX_41XX“ ausgewiesen werden.

Um das zu erreichen, kann man im „Wert von“-Feld des Festwertes „%XXX“
eingeben:

Über die Verwendung von Asterix werden mehrere Restangaben
zusammengefasst, wobei

- "%" für eine beliebige, auch leere, Zeichenkette

- "\_" für ein beliebiges Zeichen

steht.

### 2.5.8 Globaler Festwert CHECK_KOODAI_SPLASHER

Die Prüfung auf einen aktivierten Splasher in der Tabelle
/KERN/KOODAIELTY wird nur dann durchgeführt, wenn der globale Festwert
CHECK_KOODAI_SPLASHER auf X gesetzt ist.

### 2.5.9 Weitere Koodai-Festwerte

Die folgenden Festwerte werden in folgender Reihenfolge ausgewertet:

1.  **KOODAI_OBJECTGROUP** definiert eine beliebige Gruppe (auch Gruppen
    von Alternativhierarchien) der jeweiligen Objektart als Einstieg im
    Dashboard.

2.  **KOODAI_WBS_ELEMENTS** definiert im von-Wert eine kommaseparierte
    Liste von PSP-Elementen in der externen Darstellung. In Koodai
    erscheint ein Baum mit dem Top-Knoten „PSP-Elemente und einer Liste
    von PSP-Elementen darunter.

3.  **KOODAI_PROJECTS** definiert im von-Wert eine kommaseparierte Liste
    von Projekten in der externen Darstellung. Bei nur einem Projekt
    kommt dieses Projekt als Baum, bei mehreren Projekten werden die
    angegebenen Projekte als Liste unter dem Top-Knoten "Projekte"
    angeordnet

Ist keiner der drei Festwerte für PSP-Elemente gesetzt (die beiden
Letzten gelten nur im Projekt-Bereich) wird zuerst die Status-Tabelle
geprüft (es sei denn STATUS_READ_ALL ist gesetzt).  
 \* Wird mindestens ein PSP-Element mit gültigen Status gefunden, werden
zu allen PSP-Elementen mit gesetztem Status die dazugehörigen Projekte
ermittelt und diese analog zu KOODAI_PROJECTS dargestellt.  
 \* Wird kein PSP-Element mit gültigen Status gefunden, werden alle
Projekte des aktuellen Kostenrechnungskreises, die nicht gelöscht oder
inaktiv sind, ermittelt und analog zu KOODAI_PROJECTS dargestellt.
Projekte die keine PSP-Struktur haben, werden bislang stillschweigend
ignoriert.

Mittels des neuen globalen Festwertes **REQUESTLOG_ON** (von-Wert = X,
bis-Wert ... optionale User-Liste) kann die Tabelle /KERN/KOODAIRLOG
befüllt werden und zwar mit Benutzernamen und Parameter beim Aufrufen
von /KERN/KOODAI_DATA_GET und /KERN/KOODAI_LOCK_SET. Dies ist für die
Dokumentation von evtl. Lockfehlern gedacht. In diesem Fall wird
mitgeschrieben mit welchem Benutzer und welche Parameter die jeweiligen
Aufrufe stattfinden.

Der Festwert **KOODAI_VALUELISTS** sorgt mit einem **X** im von-Wert,
dass Matchcodedialoge im WebFrontend erscheinen.

Der Festwert **KOODAI_CONVERT_VALI_TITLE** sorgt mit einem **OFF** im
von-Wert, dass der technische Name stehen bleibt, bei BLANK\_ werden
Leerzeichen durch \_ ersetzt bei BLANK- durch -.

### 2.5.10 Sonstige für Koodai interessante Allevo-Festwerte

Siehe hierzu auch die Festwerthilfe.

- **FILTER_TREE** ersetzt ab Allevo 4.0.1 den Festwert USER_ELEMENTS  
  Wert_von = X -\> Es werden alle Kostenstellen bis zum Status 6
  angezeigt.  
  Wert_von = Y -\> Es werden alle Kostenstellen bis zum Status 3
  angezeigt.

- **GRP_READ_SATxx** wird im Koodai verwendet, um über eine Gruppe im
  Tree entsprechende Satellitendaten zu den jeweiligen
  Gruppenmitgliedern aufrufen zu können.

- **STATUS** Mit Hilfe dieses Festwerts kann vorgesehen werden, dass der
  Planungsstatus eines Objekts in Abhängigkeit des Planungslayouts
  geführt wird. Die Aktivierung erfolgt durch Eintrag eines **X** in der
  Spalte **Wert von**.

- **STATUS_READ_ALL** im Standardfall berücksichtigt Allevo nur Objekte
  (z.B. Kostenstellen), für die ein gültiger Allevo-Status eingetragen
  ist. Mit Eintrag einer **2** in der Spalte **Wert von** werden auch
  Referenzdaten für Objekte ohne Status gelesen. Die Übergabe von
  Plandaten an SAP ist nicht möglich (nur für Objekte mit Status).

- **OBJ_TREE_WITH_KS** hier liest Allevo zusätzlich für jedes
  Profit-Center diejenigen Kostenstellen, die im Stammsatz den
  betreffenden Profit-Center eingetragen haben.

- **OBJ_TREE_WITH_PR** hier liest Allevo zusätzlich für jedes
  Profit-Center diejenigen PSP-Elemente, die im Stammsatz den
  betreffenden Profit-Center eingetragen haben.

- **OBJ_TREE_WITH_KX** hier liest Allevo zusätzlich für jedes
  Profit-Center diejenigen Allevo-Objekte, die im Stammsatz den
  betreffenden Profit-Center eingetragen haben.

### 2.5.11 Kundenindividuelle Festwerte

Gibt es spezielle Kundenentwicklungen, dann können diese
layoutspezifisch über kundenindividuelle Festwerte aufgerufen werden. So
ruft beispielsweise der kundenindividuelle Festwert
**YRWE_PRCTR_LIST_TO_CO** ein BAdI auf (Aktivierung durch ein „X“ im
Feld „Wert von“), welches ermöglicht aus einer übergreifenden
Objektsicht in zugeordnete Objekte anderer Objektarten zu springen.

## 2.6 Statusmanagement

Nach Auswahl des Allevo-Layouts in der Menüleiste auf „Statusmanagement“
klicken.

Im Standardfall berücksichtigt Allevo nur Objekte (z.B. Kostenstellen),
für die ein gültiger Allevo-Status eingetragen ist. Über das
Statusmanagement können die zu planenden Objekte zum Beginn der Planung
mit dem entsprechenden Status 1 versehen werden. Objekte mit Status 0
(Inaktiv) erscheinen im Dashboard des WebFrontends nicht zur Auswahl. Im
Laufe der Planung kann hier der Fortschritt der Planung überprüft
werden.

Über einen Klick mit der rechten Maustaste auf den Spaltenheader können
z.B. weitere Spalten eingeblendet werden, wie z.B. der ProfitCenter bei
Kostenstellen oder PSP-Elementen.

Dies ist hilfreich, wenn man z.B. bei ProfitCentern im WebFrontend die
zugehörigen Kostenstellen, Aufträge und PSP-Elemente angezeigt bekommen
will. Hierzu muss man dann in den gleichnamigen PC/KS/OR/PR-Layouts
jeweils die entsprechenden Status setzen:

Für besondere Fälle, z.B. objektartübergreifende Planungen kann von den
Einstellungen im Statusmanagement über spezielle Festwerte (siehe z.B.
STATUS_READ_ALL) abgewichen werden.

## 2.7 Satelliten

Die Satelliten werden bevorzugt zur Abbildung von Fachplanungen
verwendet. In der Tabelle /KERN/KOODAIDAFU können über die Transaktion
/n**/ALLEVO/KOODAI_DFUNC** neben den vier Standard-Funktionen
(Kostenarten, Stat. Kennzahlen, Leistungsarten und Investition) auch bis
zu 99 Satelliten und 9.000 SunTables für Allevo-Layouts integriert
werden. Nähere Informationen zur Funktion von Satelliten und SunTables
finden Sie im Allevo-Handbuch.

Über die Transaktion /n**/ALLEVO/KOODAI_CTYPE** können Satelliten für
ein Layout importiert werden und es kann gesteuert werden, welche
Spalten des Satelliten oder der SunTable editierbar sind (ein Haken in
Spalte „E“) und bei Wert- und/oder Mengenfelder kann das Zahlenformat
mitgegeben werden.

Normalerweise werden Satelliten nicht als Baum dargestellt, sondern als
einfache Tabelle. Gibt es aber im Satellit entsprechende Felder über
welche eine Hierarchieinformation abgeleitet werden kann, dann ist auch
eine Baumdarstellung der Hierarchie für Satelliten möglich.

Im Satellit kann die Hierarchieinformation über die Spalten „ELEMENT“
und „PARENT“ abgeleitet werden:

Nun müssen dem Programm die Felder noch über den Festwert
„KOODAI_SAT_KEYS“ bekannt gemacht werden:

Normalerweise werden in den Knoten die Summe der darunterliegenden
Elemente errechnet. Es ist aber auch möglich hier eine andere Berechnung
durchführen zu lassen, wenn es in dem Satellit noch zusätzlich eine
Spalte „FORMULA“ gibt, in dem eine alternative Formel hinterlegt werden
kann. Hierbei ist wichtig zu beachten, dass wenn die Formel auf andere
Knoten Bezug nimmt, dem Knotenbezeichner „\_IsGroup“ hintenangestellt
wird.

## 2.8 Das Koodai-Cockpit

Im Koodai-Cockpit (Transaktion: /n**/ALLEVO/KOODAI_START**) sind viele
nützliche Transaktionen im Koodai-Umfeld versammelt:

| Koodai-Cockpit         | Kapitel                    |
|------------------------|----------------------------|
| Werkzeuge              |                            |
| Anzeigetexte           | Siehe Kapitel 2.9.1        |
| Datenfunktionen        | Siehe Kapitel 2.9.2        |
| Elementeinformationen  | Siehe Kapitel 2.9.3        |
| Spalteninformationen   | Siehe Kapitel 2.9.4        |
| Wertelisten            | Bisher nicht in Verwendung |
| Splasher-Verteilkurven | Siehe Kapitel 2.9.4        |
| Layoutfilter           | Bisher nicht in Verwendung |

## 2.9 Customizing-Tabellen

### 2.9.1 /KERN/KOODAITEXT zur Pflege von sprachabhängigen Texten

In der Tabelle „/KERN/KOODAITEXT“ können die sprachabhängigen Texte
durch den Kunden angepasst werden (Pflegetransaktion
/n**/ALLEVO/KOODAI_TEXTS**).

Fehlt ein Text in dieser Tabelle, kommt im Frontend die Anzeige
\[KEY-Sprachenkürzel\]  
z.B. \[LAYOUT_SELECT_TITLE-D\]. Das Sprachenkürzel „D“ steht für Deutsch
und „E“ für Englisch.

<img src="vertopal_c0988f836d634667a8761b9130858de8/media/image1.png"
style="width:1.71324in;height:0.34437in" />

Um Texte für diese Schlüssel zu pflegen, erzeugt man in der Textetabelle
eine neue Zeile und trägt links den Schlüssel (ohne das Sprachenkürzel)
ein. Also im obigen Beispiel LAYOUT_SELECT_TITLE und gibt dann in den
jeweiligen Sprachenspalten den gewünschten Anzeigetext ein.

**Anmerkung**:

Um eine Sprache neu anzulegen, muss man sich in dieser Sprache anmelden,
denn die aktuelle Anmeldesprache taucht auch immer auf (selbst wenn es
dazu noch keine Texte gibt). Um eine Sprache zu "löschen" muss man alle
ihre Texte entfernen.

### 2.9.2 /KERN/KOODAIDAFU zur Pflege der Planungsbereiche

Diese Tabelle ist über die Transaktion /n**/ALLEVO/KOODAI_DFUNC**
einrichtbar. Ohne einen Eintrag in diese Tabelle werden die vier
Standardfunktionen (Kostenarten, Statistische Kennzahlen, Leistungsarten
und Investitionen) im Frontend zur Auswahl gestellt:

Mit der Transaktion /n**/ALLEVO/KOODAI_DFUNC** können diese vier
Standardfunktionen (Kostenarten, Stat. Kennzahlen, Leistungsarten und
Invest) überschrieben werden. Zusätzlich können Satelliten und Suntables
(dazu einfach die Nummer der Suntable in das Feld der Spalte „DF“
eintragen) eingebunden werden.

Mit dem folgenden Beispiel werden im Frontend im Kostenrechnungskreis
1000 für das Kostenstellen-Layout „TKR5“ zuerst der Satellit 21 mit dem
Text „Invest“ und dann die Kostenartenplanung (CEL) mit dem Titel „Cost
Elements“ angezeigt:

### 2.9.3 /KERN/KOODAIELTY füreinen statischen Aufbau und Angabe von
Splashervarianten

In der Tabelle „/KERN/KOODAIELTY“ können pro Kostenrechnungskreis,
betroffener Objektart (z.B. Kostenstelle oder Auftrag) und Datenfunktion
(z.B. Kostenarten, statistische Kennzahlen, Leistungsarten…) z.B. die
Kostenarten mit einem Editierflag, die möglichen Splashervarianten und
ein frei zu verwendetes Feld hinterlegt werden. Diese ist über die
Transaktion /n**/Allevo/Koodai_ETYPE** einrichtbar.  
Sollte der Festwert „KOODAI_KAGROUP“ nicht gepflegt sein, kann in dieser
Tabelle auch eine statische Kostenartenhierarchie mit eigenen Formeln
hinterlegt werden.

Das in der obigen Abbildung gezeigte Beispiel führt zur folgenden
Abbildung im WebFrontend:

Nur die Zeilen mit den Kostenarten 420000 und 421000 sind editierbar, da
nur hier das Editierflag gesetzt wurde. Die hierarchischen Beziehungen
werden über die Spalten „Schlüsselelement“ und „Schlüssel“ definiert. Da
die Gruppe „OAS_WAGES“ tatsächlich in SAP existiert und zusätzlich im
Layout der Festwert „KOODAI_HIDE_KA_PATTERN“ mit „REST\_%“ definiert
ist, werden die restlichen Kostenarten der Gruppe „OAS_WAGES“
automatisch unter „REST_WAGES“ aggregiert.

Durch die Möglichkeit auch von SAP völlig losgelöste Strukturen
abzubilden und diese mit eigenen Formeln zu versehen, ist diese Tabelle
sehr mächtig.

Die Spalte „S“ dient zur Eingabe der Splashervarianten. Diese sind
kommagetrennt einzugeben. Sollte es in der Planungsoberfläche für die
betreffende Kostenart mehrere Splasher geben, dann sind diese durch das
Pipe-Symbol „\|“ zu trennen. Bsp.: 1,2,3\|1,4 würde bedeuten, dass es
für die betreffende Kostenart zwei Splasher gibt, wobei für den ersten
Splasher die Varianten 1, 2, 3 und für den zweiten Splasher die
Varianten 1, 4 angeboten werden. Die Prüfung auf einen aktivierten
Splasher in dieser Tabelle wird nur dann durchgeführt, wenn der globale
Festwert CHECK_KOODAI_SPLASHER auf X gesetzt ist.

### 2.9.4 /KERN/KOODAICOTY für die Pflege der Editierbarkeit und Bestimmung von Muss-Feldern

In der Tabelle **„**/KERN/KOODAICOTY“ können pro Kostenrechnungskreis,
betroffener Objektart (z.B. Kostenstelle oder Auftrag) und Datenfunktion
(z.B. Stammdaten in Satelliten) die Einstellungen für die einzelnen
Spalten getätigt werden. Es kann über den Asterix \* eine Vererbung der
Felder auf alle Objektarten und alle Layouts angestoßen werden. Sollte
ein Layout für ein Feld andere Einstellungen benötigen, dann ist dafür
eine eigene Zeile notwendig mit konkreter Nennung des Layouts.

- In der Spalte „E“ kann angegeben werden, ob ein Feld editierbar sein
  soll (angehakt) oder nicht.

- In der Spalte „Daten-Format“ kann man das Format eingeben, in welchem
  der Feldwert dargestellt werden soll.

- In der Spalte „M“ kann angegeben werden, ob ein Feld ein Mussfeld sein
  soll (angehakt) oder nicht.

### 2.9.5 /KERN/KOODAIDIST zur Definition von Splashervarianten

Die Ausprägung der in der Tabelle /KERN/KOODAIELTY hinterlegten
Splashervariante erfolgt in der Tabelle /KERN/KOODAIDIST
(Pflegetransaktion /n**/ALLEVO/KOODAI_DIST**).

### 2.9.6 /KERN/KOODAICCOL und /KERN/KOODAICCOT

Die **Formeln der CustomColumns** werden in der SAP-Tabelle
„**/KERN/KOODAICCOL**“ gespeichert.

Die Pflege der CustomColumns erfolgt im WebFrontend im Dialog „Edit
Custom Columns“.

Die sprachabhängigen Texte zu den CustomColumns liegen in der
SAP-Tabelle „**/KERN/KOODAICCOT**“.

### 2.9.7 /KERN/KOODAIFCOL und /KERN/KOODAIFCOT

Die **Formeln der Planspalten** werden in der Tabelle
„**/KERN/KOODAIFCOL**“ gespeichert.

Die Pflege der Planspaltenformeln erfolgt im WebFrontend im Dialog „Edit
calculations“.

Die sprachabhängigen Texte zu den Planspalten liegen in der SAP-Tabelle
„**/KERN/KOODAIFCOT**“.

### 2.9.8 /KERN/KOODAIVIEW

Die **Views** werden in der Tabelle „**/KERN/KOODAIVIEW**“ gespeichert.

Die Pflege der Views erfolgt im WebFrontend im Dialog „Save active
view“.

### 2.9.9 KERN/KOODAICJS

Das Custom Js-Skript wird pro Kostenrechnungskreis, Objektart, Layout
und Datenfunktion in der Tabelle „**/KERN/KOODAICJS**“ gespeichert.

Mit Hilfe des CustomJs-Skritps können „InCellgrafikfunktionen“ als SVG
definiert werden. Siehe hierzu auch das Koodai-Skripte-Handbuch
„Handbuch_StandardKoodai_Skripte_5“.

### 2.9.10 Pflege von Matchcode-Tabellen

Im Allevo Cockpit (/ALLEVO/COCKPIT) den „Sun Table Shuttle” aufrufen:

Suntable auswählen mit ALV Einstieg:

Einträge bearbeiten und sichern (die graue Spalte ist immer das
Schlüsselfeld und muss eindeutig sein).

## 2.10 Die Einrichtung der Pauschalen

### 2.10.1 Flexible Planung

Für die Buchung der Pauschalen wird das Allevo-Tool FP (Flexible
Planung) verwendet.  
Dieses wird im Allevo-Layout aktiviert. Im entsprechenden Allevo-Layout
die Festwerte aufrufen und dort auf „Sat. Assistent“ (STRG+F11) klicken
und den Check in Spalte „FP“ setzen.

Die Einrichtung von FP erfolgt mit der Transaktion /n/ALLEVO/FP.  
Dort sind für den Satellit 50 über den Button „Schemata“ (STRG+F1) zwei
Schemata hinterlegt.

Ein Schema für das Timeset CX_W1, welches die Werte in die Version 1
bucht und ein Schema für das Timeset CX_WW, welches die Werte in die
Version 0 bucht.

Über den Button „Festwerte“ (STRG+F2) gelangt man zu den Parametern,
welche für die Flexible Planung notwendig sind.

### 2.10.2 Enrichment

Das Enrichment wird verwendet, um die Formeln für die Berechnung der
Kostenartenwerte zu hinterlegen. Dazu geht man mit der Transaktion
(/n/ALLEVO/SAT_DETAIL) in das Satellitencockpit und ruft dort mit
Doppelklick auf der linken Seite den Satelliten auf. Auf der rechten
unteren Seite findet man unter der Registerkarte „Schema“ wieder zwei
Schemata – eines für das TimeSet CX_WW mit Buchung in die Version 0 und
eines für das TimeSet CX_W1 mit Buchung in die Version 1.

Unter der Registerkarte „Enrichment“ findet man nur einen Eintrag, für
welchen man sich über die Lupe die Details anschauen kann. Hier findet
sich in der Registerkarte „Auswahl“ die Zuordnung der Schlüsselfelder
zueinander, was zur Folge hat, dass jeweils immer nur Einträge in der
gleichen Zeile relevant sind.

In der Registerkarte „Zielfelder“ gibt es für jede Formel eine Zeile.

Um die eigentliche Formel zu sehen, muss man auf den Bleistift unten
rechts im Dialog klicken. Damit kommt man in den Änderungsmodus. Um
schließlich in den Formeleditor zu gelangen, in die entsprechende Zelle
der Spalte „Source Formel“ klicken und F2 drücken.

## 2.11 Der Jahreswechsel

**Anmerkung:**

Beim Jahreswechsel ist zu beachten, dass die Stammdaten in den
Satelliten, wie in allen Satelliten über ein Jahres- und ein
Versionsfeld verfügen. Da die Stammdaten jedoch nicht jahres- und
versionsabhängig sind, muss der dort hinterlegte Wert nicht mit dem
Planungsjahr übereinstimmen und kann im Prinzip beliebig gewählt werden.

**Durchzuführende Schritte:**

1.  Um den Jahreswechsel für mehrere Layouts durchzuführen, ruft man im
    Allevo-Cockpit den Menüpunkt „Extras – TimeSets anpassen“ auf. Hier
    gibt man den betreffenden Kostenrechnungskreis und über die
    Mehrfachselektion die Objektarten KX, KS, PR und PC ein. Mit einem
    „\*“ beim Layout können alle vorhandenen Layouts ausgewählt werden.

# 3 Das WebFrontend

## 3.1 Anmeldung

Die Anmeldung erfolgt mit dem jeweiligen SAP-User.

## 3.2. Das Dashboard

Im Dashboard können die jeweiligen zur Verfügung stehenden
**Allevo-Layouts** gewählt werden (siehe auch Kapitel „2.2
Berechtigungen innerhalb des Koodai“).

Hier wird die Layoutbeschreibung angezeigt, wie sie in der
Layoutübersicht in SAP gepflegt wurde.

Die Liste der Layouts kann über Klick auf den Pfeil ↓ geöffnet werden.
Bei vielen Layouts kann auf das X geklickt werden und ein beliebiger
Textteil der Layoutbeschreibung eingegeben werden – die Layouts werden
dann automatisch danach gefiltert.

Neben einigen Übersichtsgrafiken kann hierüber auch der Einstieg in die
eigentliche Planung erfolgen. Die im Bereich „Kostenstelle“ angezeigten
Kostenstellen entsprechen denen im Statusmanagement im Allevo-Layout mit
mindestens dem Status 1 versehenen Kostenstellen.

Die über einen Klick auf den Bleistift zur Verfügung stehenden
Planungsgebiete (im Beispiel: Kostenarten, Statistische Kennzahlen und
Leistungsarten) und evtl. Fachplanungen über Satelliten oder Suntables
entsprechen den in der Tabelle „/KERN/KOODAIDAFU“ gepflegten Inhalten.
Im obigen Beispiel wurden diese durch die folgenden Einträge
überschrieben:

## 3.3 Die Hauptplanungssicht

Mit einem Klick auf das Logo oder auf den Home-Button kommt der Anwender
wieder auf das Dashboard. Über den Logout-Button oben rechts meldet sich
der Anwender vom WebFrontend und damit von SAP ab.

### 3.3.1 Suchfunktion und Planungsart

In der Hauptplanungssicht kann links oben über eine Suchfunktion in
einer hierarchischen Sicht nach Schlüssel oder Text des Planungsobjekts
gesucht werden.

Über die Auswahlbox rechts daneben, kann der Anwender schnell die
Planungsart wechseln:

### 3.3.2 Die Iconleiste

| Icon | Tooltip                          | Siehe                        |
|------|----------------------------------|------------------------------|
|      | Daten speichern (Strg+s)         |                              |
|      | Änderungen zurücksetzen (Strg+r) |                              |
|      | Als Excel speichern (Strg+e)     |                              |
|      | Baum aus-/einklappen             |                              |
|      | Eigene Spalten verwalten         | 3.4 Eigene Spalten verwalten |
|      | Automatische Berechnung an/aus   |                              |
|      | Mehrfachänderungen (Strg+m)      | 3.7 Multi Edit               |
|      | Berechnungen anwenden            |                              |
|      | Berechnungen verwalten           | 3.5 Berechnete Planspalten   |
|      | Einzelposten-Dialog              |                              |
|      | Taschenrechner anzeigen          |                              |
|      | Spalten ein-/ausblenden          | 3.6 Views                    |
|      | Aktuelle Ansicht speichern       | 3.6 Views                    |
|      | Ansichten verwalten              | 3.6 Views                    |

## 3.4 Eigene Spalten verwalten

In den CustomColumns können eigene berechnete Spalten mit

- Beschriftung (*Title*) – nur alphanumerische Zeichen beginnend mit
  einem Buchstaben.

- Zahlenformat (*Formula Format*) – wird nur für Zahlen verwendet

- Formel (*Formula Gui*) – Spaltennamen werden mit eckigen Klammern
  umgeben

- Aufruf einer SVG-Graphik oder JavaScriptfunktion (*SVG Template Gui*)

erstellt werden.

Bei der Erstellung von Formeln und SVG-Templates können
JavaScript-Funktionen verwendet werden, die im CustomJS beschrieben
werden (siehe das „Handbuch_StandardKoodai_Skripte_5“.). Es besteht aber
zudem auch die Möglichkeit, eigene Funktionen zu definieren und in den
Formeln und SVG-Templates anzuwenden. Die erstellten Formeln werden in
SAP in der Tabelle /KERN/KOODAICCOL gespeichert.

### 3.4.1 JavaScript-Funktionen

Die CustomColumns werden nach zwei Merkmalen definiert. Beim Aufruf von
„Formula“ kann der Nutzer eine Formel entwerfen, deren Ergebnis dann in
der Tabelle angezeigt wird. Beim Aufruf von „SVG“ kann man zwischen den
im CustomJS definierten SVG-Grafiken wählen, die entsprechend in der
Tabellenzelle erscheinen.

### 3.4.2 Formeleditor

Im Formeleditor kann man, nach Klick auf den Button „Formel“, die
Formeln flexibel entwerfen, sowie auch das Zahlenformat, in dem die
Werte angezeigt werden – für ein Textergebnis muss das Zahlenformat dann
leer sein. Der Nutzer kann sowohl die Funktionen mit einfachen
Operatoren (+, -, \*, /) erstellen als auch Funktionen und vordefinierte
Codesnippets verwenden. Grundsätzlich können bei der Erstellung der
Formeln beliebige JavaScript-Funktionen verwendet werden.

#### 3.4.2.1 Zahlenformat

Die Zahlen und Formate im „CustomColumn“- und im „CalcAdmin“-Dialog
werden im amerikanischen Format angegeben. Das heißt, das
Dezimaltrennzeichen ist nicht wie im Deutschen ein Komma, sondern ein
Punkt. Im Dialog kann man sowohl eine Formatvorlage wählen als auch das
Zeichenformat selbst festlegen (es gilt auch für verschiedene
Währungszeichen).

Für die Festlegung des Zahlenformats gibt es die folgenden
Möglichkeiten:

- **0**— Die Null wird mit der entsprechenden Ziffer ersetzt (wenn es
  > eine gibt), ansonsten erscheint eine Null im Ergebnis.  
  > Das Format **00000** bewirkt damit, dass 5 Ziffern ohne
  > Nachkommastellen erscheinen. Beispielsweise würde dann aus:  
  >   
  > Format: **00000** Originalzahl: **1234,5678** Darstellung:
  > **01235**  
  >   
  > (es wird aufgerundet und eine Null erscheint zu Beginn, damit 5
  > Ziffern dargestellt werden)  
  >   
  > Format: **0.00** Originalzahl: **1234,5** Darstellung: **1234,50  
  > **(man beachte den Punkt im Format für das Dezimaltrennzeichen;
  > durch die zwei folgenden Nullen werden immer zwei Nachkommastellen
  > angezeigt)

- **\#** Die Raute wird mit der entsprechenden Ziffer ersetzt (wenn es
  eine gibt). Das Format **\#####** bewirkt damit, dass es keine
  führenden Nullen gibt. Zur Veranschaulichung dienen die folgenden
  Beispiele:  
    
  Format: **\#####** Originalzahl: 1234,5678 Darstellung: **1235  
  **(es wird aufgerundet und es erscheinen vier Ziffern)  
    
  Format: **\#####** Originalzahl: 12345678 Darstellung: **12345678  
  **

- **P** Ein p bewirkt, dass die Zahl mit 100 multipliziert, mit zwei
  Nachkommastellen und durch ein Prozentzeichen ergänzt wird. Will man
  die Anzahl der Nachkommastellen anders, ergänzt man das p mit der
  entsprechenden Ziffer.  
    
  Format: **p** Originalzahl: 0,12345 Darstellung: **12,35 %**  
    
  Format: **p0** Originalzahl: 0,12345 Darstellung: **12 %**  
    
  Format: **p3** Originalzahl: 0,12345 Darstellung: **12,345 %  
  **

- **c** Ein c (für currency) bewirkt, dass die Zahl mit zwei
  Nachkommastellen und durch ein Währungssymbol ergänzt wird. Will man
  die Anzahl der Nachkommastellen anders, ergänzt man das c mit der
  entsprechenden Ziffer.  
    
  Format: **c** Originalzahl: 12,345 Darstellung: **12,35 €**

> Format: **c0** Originalzahl: 12,345 Darstellung: **12 €**
>
> Format: **c3** Originalzahl: 12,345 Darstellung: **12,345 €**

- **;** Mit Hilfe des Semikolons lassen sich unterschiedliche
  Formatierungen für positive, negative und Nullwerte definieren, die
  durch das Semikolon voneinander getrennt eingegeben werden

- **"string"/'string'**—Zur Kennzeichnung von Text

#### 3.4.2.2 Formeleingabe

Um eine Spalte in das Formeleingabefeld hinzuzufügen, markiert man sie
in der Liste und drückt auf den Knopf unten. Beim Hinzufügen von
weiteren Spalten wird der markierte Operator (+, -, \*, /) beigefügt. Es
ist auch möglich, mehrere Spalten mit der Steuerung- oder Umschalttaste
gleichzeitig zu markieren und ins Eingabefeld hinzuzufügen. Wenn der
Nutzer eine Formel mit Klammern erstellt oder eine Formelvorlage für
Minimum- oder Maximumberechnung benutzt, soll man die Spalten nicht
einzeln, sondern als Gruppe hinzufügen. Es ist damit verbunden, dass
beim Verwenden der Klammern die Spalten automatisch mit Komma bzw. mit
dem markierten Operator getrennt werden:

Es stehen mehrere Funktionen zur Auswahl. Mit der Funktion
„**dayOfYear**“ wird beispielsweise die Anzahl der im Jahr vergangenen
Tage zu einem bestimmten Datum ausgegeben. Die folgende Formel gibt
beispielsweise den Wert 38 aus, da in der Spalte „Antragsdatum“ das
Datum '2022-02-07' steht:

> BasicTools.getDayOfYear(\[Antragsdatum\])

Will man die Anzahl der im Jahr vergangenen Tage zum jeweils aktuellen
Datum, dann muss die Spaltenbezeichnung „Antragsdatum“ in der Formel
entfernt werden:

> BasicTools.getDayOfYear()

Die Funktion „**sum_not_null**“ wird bei langen Summierungen verwendet.
Sie gibt nichts aus, wenn alle Summanden null sind und ansonsten die
jeweilige Summe. Damit lassen sich unschöne Nuller in der Anzeige
verhindern.

Die Funktion „**mean**“ entspricht der Excelfunktion Mittelwert().

### 3.4.3 SVG Template GUI

Hier können mit Hilfe von SVG Zell-Grafiken erstellt werden. Auch hier
lassen sich die JavaScript-Funktionen verwenden, die im CustomJS
definiert werden. Die Funktionsweise vom CustomJS und wie der Nutzer
diese Datei bearbeiten und eigene Grafiken hinzufügen kann, wird
ausführlich im „Handbuch für Skripte“ beschrieben.

Im SVG-Dialogfenster kann man für eine bestimmte Spalte (hier: „Title:
CustomColumn“) eine SVG-Grafik aus einer DropDown-Liste „Custom
Function“ aussuchen. Dabei werden die Titel verwendet, die man im
CustomJS für jede Grafik bestimmt hat. Wenn das Farbmenü „Colors“ leer
bleibt, werden die Standardvorgaben angewendet, aber der Nutzer hat die
Möglichkeit, die Farben selbst zu definieren. Dabei werden die
Beschreibungen mancher Grafiken hilfreich, wenn bestimmte Farben z.B.
für Minimum- oder Maximumwerte benutzt werden.

Um die Spalten für eine SVG-Grafik zu definieren, wählt man beliebige
Spalten im „Columns“-Menü aus. Hier sollte man auch auf die
Grafikbeschreibung achten, weil einige Grafiken nur eine Spalte
voraussetzen:

**Erläuterung:**

- Der Titel der neuen Spalte (Difference) steht in der Spalte „Title“.

- Die Spalte „Formula Format“ und „Formula GUI“ müssen leer sein, da
  keine Zahl ausgegeben wird.

- In der Spalte „SVG Template GUI“ wird das Skript für die SVG-Grafik
  aus der CustomJS-Datei hervorgerufen. Dafür muss die Aufruffunktion
  (Abbildung 3.11) immer zwischen „#= ….. \#“ stehen. Sie wird nach
  folgendem Muster aufgebaut:

> **\#= customJS.charts.Title.func(data, cols, colors)#**
>
> Es besteht aus folgenden Teilen:

- **customJS** – die oberste Variable des Skripts,

- **charts** – allgemeine Bezeichnung aller Grafiken,

- **Title** – der Name der Grafik,

- **func** – die Funktion, die die Grafik beschreibt,

- **data** – Zellendaten,

- **cols** – Spaltennamen (sind immer in eckige Klammern \[ \] zu
  setzen!),

- **colors** – Farben (wenn der Nutzer Standardfarben benutzen will,
  sollen hier leere eckige Klammern \[\] bleiben)

### 3.4.4 Formel

**Hinweis**: Hat die Ausgabe der Formel ein Textformat, dann darf in der
Spalte „Format“ kein Eintrag stehen.

**Zugriff auf Spaltendefinitionen des Allevo-Layouts**

Klickt man auf das + Icon, dann wird eine neue Zeile erzeugt und es wird
in die Spalte „Formel“ alle im aktuellen View vorhandenen Spalten des
Allevo-Layouts in der Form angezeigt, in welcher sie in der Formel
angesprochen werden können. Die Spalten werden mit eckigen Klammern um
deren Namen angesprochen.

Beispielsweise gibt es im Allevo-Layout die Spalten „Plan Jan 2020“,
„Plan Feb 2020“ und „Plan Mar 2020“ diese können nun in einer
berechneten Spalte als Q1 zusammengefasst werden:

Hinweis: Mit der gleichen Logik kann man auf alle Spalten zugreifen,
welche unter dem Button „Spalten ein-/ausblenden“ prinzipiell zur
Verfügung stehen. Damit kann man z.B. auch andere CustomColumns in
Formeln verwenden.

Es stehen im Standard noch folgende Spalten zur Verfügung:

- \[Schlüssel\] – hiermit kann auf den nächst höheren Knoten der
  jeweiligen Hierarchie zugreifen

- \[ELEMENTTYPE\] – für Kostenarten steht hier der Kostenartentyp aus
  der SAP-Tabelle „CSKB“ (zweistellig), für stat. Kennzahlen der Typ aus
  der SAP-Tabelle „TKA03“ (1 für Festwert oder 2 für Summenwert).

- \[ISEDITABLE\] - ist im Standard für die Kostenartentypen 42 & 43
  leer, sonst für Elemente immer 'X' (=editierbar) – wird die Tabelle
  „/KERN/KOODAIELTY“ (Transaktion: /n/Allevo/Koodai_ETYPE)
  verwendet, dann wird die Spalte darüber gefüllt.

- \[SPLASHER\] – hier können die Schlüssel für die jeweiligen
  Splashervarianten hinterlegt sein – diese werden aus der Tabelle
  „/KERN/KOODAIELTY“ (Transaktion: /n/Allevo/Koodai_ETYPE)
  entnommen. Im WebFrontend kann dann in der Spalte „SPLASHER“ die
  entsprechende Splashervariante ausgewählt werden.

- \[ELEMENTOPTION\] – die Spalte stammt auch aus der Tabelle
  „/KERN/KOODAIELTY“ (Transaktion: /n/Allevo/Koodai_ETYPE) und kann
  frei, z.B. für Selektionen in Formeln verwendet werden.

So kann man sich z.B. leicht den Kostenartentyp anzeigen lassen mit
Auswahl der Spalte \[ELEMENTTYPE\].

## 3.5 Berechnete Planspalten

Auch in den Planspalten lassen sich über den Button „Calc Admin“ Formeln
hinterlegen.

Im Feld „Description“ kann eine erläuternde Beschreibung für die Formel
hinterlegt werden. In der „Formula“-Spalte gibt es die gleichen
Möglichkeiten wie bei den CustomColumns (siehe Kapitel 3.4.4 Formel).
Gibt es Abhängigkeiten zwischen verschiedenen Formeln kann über die
Pfeiltaste die Abfolge der Berechnung gesteuert werden. Beispielsweise
wird im unteren Fall zuerst der „Plan 2020“ auf Grundlage von \[Plan
current year\] \*1.05 errechnet und erst danach wird \[Plan current
year\] auf Grundlage von \[Plan previous year\] \*1.1 errechnet:

Das bedeutet, dass wenn im Ausgangszustand \[Plan previous year\] =200
und \[Plan current year\] = 100 ist, dann wird nach Ausführung der
ersten Formel \[Plan 2020\] = 105 und nach Ausführung der zweiten Formel
\[Plan current year\] =220 sein.

## 3.6 Views

Der Anwender kann sich eigene Sichten (Views) anlegen. Dazu kann er über
den Button (Spalten ein-/ausblenden) vorhandene Spalten ein- oder
ausblenden und deren Reihenfolge anpassen. Über die Farbpalette können
den Spalten vordefinierte Farben oder über Custom Colors auch
benutzerdefinierte Farben zugeordnet werden.

Alternativ können die Spalten auch in der normalen Webansicht per
Drag&Drop in die gewünschte Reihenfolge gebracht werden. Die
Spaltenbreiten lassen sich nach Wunsch verändern, Filter und Sortierung
gesetzt und diese über den Dialog „Aktuelle Ansicht speichern“ als
eigene Sicht abgespeichert werden.

Dem View kann man einen eigenen Namen und ein eigenes Icon zuordnen. Ist
die Planungsansicht hierarchisch, dann kann auch zusätzlich der aktuelle
„Aufklappzustand“ mit abgespeichert werden.

## 3.7 Multi Edit

Mit Hilfe des „Multi Edit“- Buttons (oder STRG+m) lassen sich im
WebFrontend der Inhalt einer Zelle oder auch ganze Spalten/Zeilen oder
Blöcke kopieren. Dazu klickt man auf den Button, markiert den
Kopierbereich mit der Maus (er muss dann mit blau hinterlegt sein),
STRG+C, markiert den Zielbereich, STRG+V.

- Ist der Zielbereich größer als der Kopierbereich wird der
  Kopierbereich wiederholt. Dies kann man beispielsweise nutzen, um ein
  und denselben Wert in mehrere Zellen einzufügen.

- Wird als Zielbereich nur eine Zelle markiert, dann versteht das
  Programm diese Zelle als linke obere Ecke und versucht den ganzen
  Kopierbereich einzufügen.

**Anmerkung zum Markieren im „Multi Edit – Modus“**

Das Markieren kann auf unterschiedliche Arten erfolgen:

- mit der Maus durch Ziehen bei gedrückter Maustaste

- mit der gedrückten Shift-Taste zusammen mit den Pfeiltasten

- mit der gedrückten Alt-Taste und Klick auf die rechte untere Zelle des
  gewünschten Bereiches

## 3.8 Normales Editieren

Die orange hinterlegten Zellen können vom Anwender editiert werden.

Bei Abschluss der Eingabe mit **Enter** wird die darunterliegende Zelle
editiert,  
bei Abschluss mit der **Tabulatortaste** die rechts daneben liegende
Zelle, entsprechend wird bei Shift-Enter die obere Zelle und bei
Shift-Tab die linke Zelle editiert.

Mit der **Escape**-Taste kann der Editiermodus verlassen werden.

Geänderte, aber noch nicht SAP übertragene Zellwerte werden mit einem
kleinen roten Dreick oben links in der Zellecke gekennzeichnet.

## 3.9 Navigieren mit der Tastatur

Mit der **Tabulatortaste** bewegt man sich von links nach rechts und mit
Shift+Tabulatortaste von rechts nach links.

Mit **Enter** bewegt man sich von oben nach unten und mit Shift+Enter
von unten nach oben.

→ Handelt es sich um **editierbare** Zellen (gelber Hintergrund), dann
landet man mit der Tabulatortaste und der Entertaste sofort im
Editiermodus. In den Editiermodus kommt man auch mit der Taste **F2**.

Um aus dem Editiermodus herauszukommen, kann man die **Escapetaste**
drücken. Damit kann man z.B. bei Zellen mit Matchcodes die **F4**-Hilfe
der Zelle aufrufen oder auch die Zelle verlassen ohne einen evtl.
hinterlegten Splasher auszuführen.

Befindet man sich nicht im Editiermodus dann kann man mit den
**Pfeiltasten** durch die Tabelle navigieren ohne in den Editiermodus
der Zelle zu springen. Will man eine Zelle editieren, dann kann man dazu
die Entertaste drücken. Im Editiermodus kann man mit der
Pfeil-Nach-Oben-Taste ↑ den Wert um eine Einheit erhöhen bzw. mit der
Pfeil-Nach-Unten-Taste ↓ den Wert um eine Einheit senken.

Mit **F8** kommt man in den Bearbeitungsmodus – das jeweilige Objekt ist
dann für andere User gesperrt.

Mit **F9** kann man sich in den Stammdaten die Einträge einer Zeile in
einem Dialog anschauen.

Viele der Buttons kann man auch mit der Tastatur bedienen – dies ist
dann im Tooltip vermerkt.
