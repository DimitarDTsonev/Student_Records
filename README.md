# Student_Records
<!-- Page 1 -->

Òåìà: Stud ent Records óåá ïðèëîæåí èå â
AWS Cloud ñðåäà
Ïðèëîæíî-ïðîãðàìíè èíòåðôåéñè çà ðàáîòà ñ îáëà÷íè
àðõèòåêòóðè ñ Àìàçîí Óå á Óñëóãè (AWS)
Èçãîòâèë: Äèìèòúð Öîíåâ, Ô.Í.: 72087, èìåéë:
ddconev@uni-so˝a.bg;
Ëåêòîð: ïðîô. Ìèëåí Ïåòðîâ, ãîäèíà: 2025
Ñúäúðæàíèå
1 Óñëîâèå 3
2 Âúâåäåíèå 3
3 Òåîðèÿ 4
3.1 Virtual Private Cloud (VPC) . . . . . . . . . . . . . . . . . . . . . . 4
3.2 Subnets (Ïîäìðåæè) . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.3 Internet Gateway . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.4 NAT Gateway . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.5 Route Tables (Ìàðøðóòíè òàáëèöè) . . . . . . . . . . . . . . . . . . 5
3.6 Security Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.7 Amazon RDS (Relational Database Service) . . . . . . . . . . . . . . 6
3.8 Application Load Balancer (ALB) . . . . . . . . . . . . . . . . . . . . 6
4 Èçïîëçâàíè òåõíîëîãèè 6
5 Èíñòàëàöèÿ è íàñòðîéêè 7
5.1 Ñúçäàâàíå íà Virtual Private Cl ou d (VPC) . . . . . . . . . . . . . . 7
5.2 Ñúçäàâàíå íà Subnets . . . . . . . . . . . . . . . . . . . . . . . . . . 7
5.3 Ñúçäàâàíå íà Internet Gateway . . . . . . . . . . . . . . . . . . . . . 8
5.4 Ñúçäàâàíå íà NAT Gateway . . . . . . . . . . . . . . . . . . . . . . 9
5.5 Ñúçäàâàíå íà Route Tables . . . . . . . . . . . . . . . . . . . . . . . 9
5.6 Ñúçäàâàíå íà Security Groups . . . . . . . . . . . . . . . . . . . . . 10
5.7 Ñúçäàâàíå íà RDS MySQL Database . . . . . . . . . . . . . . . . . 11
5.8 Ñúçäàâàíå íà Application Load Balancer . . . . . . . . . . . . . . . 11
1

---

<!-- Page 2 -->

6 Êðàòêî ðúêîâîäñòâî çà ïîòðåáèòåëÿ 12
6.1 Äîñòúï äî ïðèëîæåíèåòî . . . . . . . . . . . . . . . . . . . . . . . . 12
6.2 Ãëàâíà ñòðàíèöà . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
6.3 Ñòóäåíòè . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
6.4 Ðåä àê òè ðàíå íà ñúùåñòâóâàù çàïèñ . . . . . . . . . . . . . . . . . . 13
6.5 Èçòðèâàíå íà çàïèñ . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
6.6 Íàâèãàöèÿ è èíòåðôåéñ . . . . . . . . . . . . . . . . . . . . . . . . . 15
6.7 Òåõíè÷åñêè è çèñêâàíèÿ . . . . . . . . . . . . . . . . . . . . . . . . . 15
6.8 Âúçìîæíè ãðåøêè è ðåøåíèÿ . . . . . . . . . . . . . . . . . . . . . 15
7 Ïðèìåðíè äàííè 15
8 Îïèñàíèå íà ïðîãðàìíèÿ êîä 16
8.1 extensions.py . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
8.2 app.py . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
8.3 mo dels.py . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
8.4 forms.py . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
8.5 Âúçìîæíîñòè çà áúäåùî ðàçâèòèå . . . . . . . . . . . . . . . . . . . 20
9 Êàêâî íàó÷èõ 20
9.1 AWS Cloud Services . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
9.2 Web Development . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
9.3 DevOps è Infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . 21
9.4 Ïðîôåñèîíàëíè óìåíèÿ . . . . . . . . . . . . . . . . . . . . . . . . . 21
9.5 Áúäåùè ñòúïêè . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
10 Ñïèñúê ñ ôè ãóðè è òàáëèöè 22
11 Èçïîëçâàíè èçòî÷íèöè 22
2

---

<!-- Page 3 -->

1 Óñëîâèå
Èäåÿòà íà ïðîåêòà å äà ñå ñúçäàäå è äåïëîéíå óåá ïðèëîæåíèå çà óïðàâëåíèå íà
èíôîðìàöèîííà ñèñòåìà îò çàïèñè íà ñòóäåíòè (Student Records) â Amazon Web
Services (AWS) Cloud ñðåäà. Ïðèëîæåíèåòî òðÿáâà äà áúäå äîñòúïíî ïóáëè÷íî
ïðåç èíòåðí åò è äà èçï îë çâà ðàçïðåäåëåíà àðõèòåêòóðà.
2 Âúâåäåíèå
Student Records å Flask-áàçèðàíî óåá ïðèëîæåíèå çà óïð àâëåí èå íà ñòóäåíòñêè
äàííè. Ïðèëîæåíèåòî ïðåäîñòàâÿ ïúëíà CRUD (Create, Read, Up date, Delete)
ôóíêöèîíàëíîñò, ïîçâîëÿâàéêè íà ïîòðåáèòåëèòå ñúùî è äà ôèëòðèðàò òúðñå-
íèòå îò òÿõ çàïè ñè . Âñÿêè ñòóäåíò ñå îï ðåäåëÿ ñ îñíîâíèòå ñè ñâîéñòâà êàòî
ôàêóëòåí íîìåð, èìåíà, êóðñ, ãðóïà, ñïåöèàëíîñò, è ñúïòâåòíèòå ëè ÷íè äàííè
çà âñåêè åäèí ñòóäåíò êàòî âñÿêî îò ïîëåòàòà áèâà ï îäëîæåíî íà ïðîâåðêà çà
òîâà äàëè âúâåäåíèòå äàííè ñà âàëèäíè.
Îñíîâíèòå ôóíêöèîíàëíîñòè âêëþ÷âàò:
‹
Äîáàâÿíå íà íîâ ñòóäåíò êúì ñ ïîïúëâàíå íà äàííèòå çà ñòóäåíòà.
‹
Ðåäàêòèðàíå íà ñúùåñòâóâàùè çàïèñè â ñèñòåìàòà.
‹
Èçòðèâàíå íà ñòóäåíò, êîèòî âå÷å íå íóæíè íà èçïîëçâàùèÿ ñèñòåìàòà,
èìà äâîéíà ôîðìà çà ïîòâúðæäåíèå, êîÿòî íè äàâà äîïúëíèòåëíà èíôîð-
ìàöèÿ äàëè ñìå ñèãóðíè äàë è èñêàìå äà èçòðèåì äàäåí çàïèñ.
‹
Ïðåãëåä íà öåëèÿ ñïèñúê ñúñòàâåí îò ñòóä åíòè â óäîáåí òàáëè ÷åí ôîðìàò.
‹
Ôèëòðèðàíå íà ñòóäåíòèòå ï î ôàêóëòåòåí íîìåð, èìå, êóðñ è ñïåöèàëíîñò.
Ïðèëîæåíèåòî å ïðîåêòèðàíî çà äåïëîéâàíå â AWS îáëà÷íà ñðåäà ñ àêöåíò âúð-
õó ñèãóðíîñò, ìàùàáè ðóåìîñò è âè ñîêà íàëè ÷íîñò ÷ðåç èçïîëçâàíå íà ðàçïðåäå-
ëåíà àðõèòåêòóðà. Âúïðåêè òîâà, ïîðàäè îãðàíè÷åíèÿ â áþäæåòà, íàñòîÿùàòà
èìïëåìåíòàöèÿ å ðåàëèçèðàíà ñàìî â ðàìêèòå í à åäíà íàëè÷í à çîíà (Availability
Zone), êîåòî îãðàíè÷àâà âúçìîæíîñòòà çà ïúëíà óñòîé÷ èâîñò ïðè åâåíòóàëíè
ðåãèîíàëíè ñð èâîâå.
3

---

<!-- Page 4 -->

Ôèãóðà 1: Àðõèòåêòóðà íà ïðîåêòà
3 Òåîðèÿ
Amazon Web Services (AWS) ïðåäîñòàâÿ øèðîê ñïåêòúð îò îáëà÷íè óñëóãè, êî-
èòî ïîçâîëÿâàò ñúçäàâàíåòî íà ìàùàáèðóåìè è ñèãóðíè ïðèëîæåí èÿ.
3.1 Virtual Private Cloud (VPC)
VPC (Virtual Private Cloud)
å ëîãè÷åñêà ÷àñò îò AWS îáëàêà, êîÿòî ïðå-
äîñòàâÿ êîíòðîë âúðõó ìðåæîâàòà ñðåäà, â êîÿòî ñå íàìèðàò ðåñóðñèòå. VPC
ïîçâîëÿâà ñúçäàâàíåòî íà èçîëèðàíè ìðåæè, êîèòî ìîãàò äà ñå êîíôèãóðèðàò
ñúñ ñïåöè ôè ÷íè ïðàâèëà çà ñèãóðíîñò è ìàðøðóòèçàöèÿ. Çà íàøèÿ ïðîåêò èç-
ïîëçâàìå VPC àðõèòåêòóðà, êîÿòî îñèãóðÿâà èçîëèðàíà ìðåæîâà ñðåä à ñ ïúëåí
êîíòðîë âúðõó IP àäðåñèðàíåòî, ìàðøðóòèçàöèÿòà è ñèãóðíîñòòà.
4

---

<!-- Page 5 -->

3.2 Subnets (Ïîäìðåæè)
Subnets
ñà ïîäìðåæè â ðàìêèòå íà VPC, êîèòî ïîçâîëÿâàò ðàçäåëÿíå íà ìðå-
æîâèÿ òðàôèê çà ïî-äîáðà ñèãóðíîñò è åôåêòèâíîñò. Ïóáëè÷ íèòå ï îäìðåæè ñå
èçïîëçâàò çà ðåñóðñè, êîèòî òðÿáâà äà èìàò èíòåðíåò äîñòúï, äîêàòî ÷àñòíèòå
ïîäìðåæè ñà çà ðåñóðñè, êîèòî íå òðÿáâà äà èìàò äèðåêòåí äîñòúï äî èí òåð íåò.
Ðàçïðåäåëåíèåòî í à ïîäìðåæèòå â ðàçëè÷íè Avai lab ility Zones îñèãóðÿâà âèñîêà
íàëè÷íîñò è óñòîé÷ èâîñò íà èíôðàñòðóêòóðàòà.
3.3 Internet Gateway
Internet Gateway
ïîçâîëÿâà íà ðåñóðñèòå â ï óáëè ÷íèòå ïîäìðåæè íà VPC-
òî äà êîìóíèêèðàò ñ èíòåðíåò. Òîé îñèãóðÿâà âðúçêàòà ìåæäó VPC è ãëîáàë-
íèÿ èíòåðíåò è å íåîáõîäèì çà ïóáë è÷íèòå ðåñóð ñè (êàòî óåá ñú ðâúðè è load
balancers), êîèòî òðÿáâà äà áúäàò äîñòúïíè èçâúí VPC-òî.
3.4 NAT Gateway
NAT Gateway
ïîçâîëÿâà íà ðåñóðñèòå â ÷àñòíè ïîäìð åæè äà îñúùåñòâÿâàò
èçõîäÿùè âðúçêè êúì èí òåð íåò (íàïðèìåð çà èçòåãëÿíå íà àêòóàëèçàöèè), áåç
äà áúäàò äîñòúïíè îò èíòåðíåò. Òîâà îñèãóðÿâà ñèãóðíîñò, êàòî ÷àñòíèòå ðå-
ñóðñè îñòàâàò íåäîñòú ïíè îòâúí, íî ìîãàò äà èíèöèèð àò âðúçê è êúì èíòåðíåò
ïðè í åîáõîäèìîñò.
3.5 Route Table s (Ìàðøðóòíè òàáëèöè)
Route Tables
ñà òàáëèöè çà ìàð øðóòè çèðàíå, êîèòî îïðåäåëÿò êàê ñå íàñî÷âà
òðàôèêúò â ìðåæàòà. Òå äåôèíèðàò ïðàâèëàòà çà äâèæåíèå íà òðàôèêà ìåæäó
ïîäìðåæèòå è êúì èíòåðí åò. Âñÿêà ïîäìðåæà å àñîöèèðàíà ñ route table, êîÿòî
îïðåäåëÿ íàêúä å äà ñå íàñî÷è òðàôèêúò ñïðÿìî íåãîâàòà äåñòèíàöèÿ.
3.6 Security Groups
Security Groups
äåéñòâàò êàòî âèðòóàë íè ôàåðóîëè, êîèòî êîíòðîëèðàò äîñòú-
ïà äî ðåñóðñèòå íà íèâî èíñòàíöèÿ. Òå äåôèíèðàò inb ound è outb ound ïðàâèëà
çà òðàôèêà, ïîçâîëÿâàéêè ñàìî àóòîðèçèðàíè òå âðúçêè. Security Groups ðàáî-
òÿò íà íèâî èíñòàíö èÿ è ñà stateful - àêî å ðàçðåøåíà âõîäÿùà âðúçêà, è çõîäÿ-
ùàòà ÷àñò àâòîìàòè÷íî ñå ðàçðåøàâà.
5

---

<!-- Page 6 -->

3.7 Amazon RDS (Relational Database Se rvice)
RDS
ïðåäëàãà óïðàâëÿâàíà áàçà äàííè, êîÿòî å ïî-ëåñíà çà ïîääðúæêà è ìà-
ùàáèðàíå îò ñàìîñòîÿòåëíî óïðàâëÿâàíà áàçà äàíí è íà EC2. RDS ñå ãðèæè çà
backup-è, ï àò÷îâå, ìîíèòîðèíã è ìàùàáèðàíå àâòîìàòè÷íî, ïîçâîëÿâàéêè íà
ðàçðàáîò÷èöèòå äà ñå ôîêóñèðàò âúðõó ïðèëîæåíèåòî.
3.8 Application Load Balancer (ALB)
Application Load Balancer
å Layer 7 load balancer, êîéòî ðàçïðåäåëÿ âõîäÿ-
ùèÿ HTTP/HTTPS òðàôèê ìåæäó ìíîæåñòâî targets (EC2 èíñòàíöèè) â ðàç-
ëè÷íè Availability Zones. ALB îñèãóðÿâà âèñîêà íàëè÷íîñò, fault tolerance è ïî-
äîáðà ïðîèçâîäèòåëíîñò ÷ð åç intelligent routing, health checks è àâòîìàòè÷íî
failover ïðè ïðîáëåìè ñ èíñòàíöèè.
4 Èçïîëçâàíè òåõíîëîãèè
‹
Flask
- Python óåá framework çà ðàçðàáîòâàíå íà ïðèëîæåíèåòî.
‹
Virtual Private Cloud (VPC)
- Ëîãè÷åñêà èçîëèðàíà ìðåæîâà ñð åäà ñ
ïúëåí êîíòðîë âúðõó ìðåæîâàòà êîíôèãóðàöèÿ.
‹
Subnets (Ïîäìðåæè)
- Ïîä ðàçä åëåíèå íà ìðåæàòà çà ðàçäåëÿíå íà ïóá-
ëè÷åí è ÷àñòåí òðàôèê.
‹
Internet Gateway
- Ïîçâîëÿâà íà ïóáëè÷íèòå ðåñóðñè äà èìàò äîñòúï äî
èíòåðíåò.
‹
NAT Gateway
- Îñèãóðÿâà èçõîäÿù èíòåðíåò äîñòúï çà ÷àñòíè ðåñóðñè.
‹
Route Tables (Ìàðøðóòíè òàáëèö è)
- Îïðåäåëÿò ïðàâèëàòà çà ìàð-
øðóòèçàöèÿ íà ìðåæîâèÿ òðàôèê.
‹
Security Groups
- Âèðòóàëíè ôàåðóîëè çà êîíòðîëèðàíå í à äîñòúïà äî
ðåñóðñèòå.
‹
Amazon RDS (MySQL)
- ðåëàöèîííà áàçà äàííè, õîñòâàíà ÷ðåç A mazon
RDS.
‹
Application Load Balancer (ALB)
- Ðàçïðåäåëÿ ìðåæîâè ÿ òðàôèê êúì
ìíîæåñòâî èíñòàíöèè çà ïî-äîáðà ïðîèçâîä èòåë íîñò.
6

---

<!-- Page 7 -->

5 Èíñòàëàöèÿ è íàñòðîéêè
5.1 Ñúçäàâàíå íà Virtual Private Cloud (VPC)
Ñòúïêè:
Ñúçäàäåí å íîâ VPC ñ CIDR áëîê 10.0.0.0/16, êîéòî ïðåäîñòàâÿ äîñòà-
òú÷í î IP àäð åñè çà ìíîæåñòâî ïîäìðåæè (Subnets). Àêòèâè ðàíè ñà DNS hostnames
è DNS resolution, çà äà ìîãàò èíñòàíöèèòå â VPC-òî äà ïîëó÷àâàò äèíàìè÷íè
DNS èìåí à è äà ìîãàò ä à ñå ñâúðçâàò ñ âú íøíè ðåñóðñè, àêî å íåîáõîäèìî.
Çàùî ãî íàïðàâèõìå:
Ñúçäàâàíåòî íà VPC å íåîáõîäèìî çà èçãðàæäàíå
íà èçîëèðàíà è êîíôèãóðèðàíà ìðåæîâà ñðåäà â AWS. Àêòèâèðàíåòî íà DNS
hostnames è DNS resolution îñèãóðÿâà âúçìîæíîñòòà çà èçïîëçâàíå íà AWS ïðå-
äîñòàâåíè DNS èìåíà çà EC2 èíñòàíöèèòå, êîåòî å ïîëåçíî çà ëåñíî óïðàâëåíèå
íà ðåñóðñè è êîìóíèêàöèÿ ìåæäó òÿõ.
Ôèãóðà 2: Ñúçäàâàíå íà VPC â AWS Management Cons ol e
5.2 Ñúçäàâàíå íà Subnets
Ñòúïêè:
Ñúçäàäåíè ñà 4 ïîäìðåæè â 2 ðàçëè÷íè Availability Zones (AZ):
‹
Public S ubnet 1: 10.0.0.0/24 (us-east-1a)
‹
Private Subnet 1: 10.0.2.0/24 (us-east-1a)
‹
Public S ubnet 2: 10.0.1.0/24 (us-east-1b)
‹
Private Subnet 2: 10.0.3.0/24 (us-east-1b)
7

---

<!-- Page 8 -->

Ôèãóðà 3: Êîíôèãóðàöèÿ íà public è private subnets
Çàùî ãî íàïðàâèõìå:
Public su bnets ñå èçïîëçâàò çà ðåñóðñè, êîèòî òðÿáâà
äà èìàò èíòåðíåò äîñòúï (í àï ðèìåð EC2). Àêòèâèðàía å óñëóãàòà Auto-assign
IP settin gs çà àâòîìàòè÷íî ïðèñâîÿâàíå íà ïóáëè÷åí IP àäðåñ êúì èíñòàíöèÿ,
ïðîâèçèîíèðàíà â äàäåíèÿ ïóáëè÷åí subnet. Private subnets ñà çà ðåñóðñè, êîèòî
íå òðÿáâà ä à èìàò äèðåêòåí äîñòúï äî èíòåðíåò (íàïðèìåð áàçè äàííè). Ðàç-
ïðåäåëåíèåòî íà ïîäìðåæèòå â ðàçëè÷íè Availability Zones îñèãóðÿâà âèñîêà
íàëè÷íîñò è óñòîé÷ èâîñò íà èíôðàñòðóêòóðàòà.
5.3 Ñúçäàâàíå íà Internet Gateway
Ñòúïêè:
Ñúçäàäåí å Internet Gateway è å ïðèêà÷åí êúì VPC-òî, çà äà îñè-
ãóðè èíòåðíåò äîñòúï çà ïóáëè÷íèòå ïîäìðåæè. Ïóáëè÷íèòå ðåñóðñè (êàòî
Application Load Balancer) ùå èìàò âúçìîæíîñò ä à êîìóíèêèðàò ñ èíòåðíåò
÷ðåç òîçè Internet Gateway.
Çàùî ãî íàïðàâè õìå:
Áåç Internet Gateway, ðåñóðñèòå â ïóáëè÷íèòå ïîäìðå-
æè íà VPC-òî íÿìàò èíòåðíåò äîñòúï, êîåòî ìîæå äà îãðàíè÷è ôóíêöèîíàë-
íîñòòà íà ïð èëîæåíèÿòà. Internet Gateway å íåîáõîäèì çà ïóáëè÷íèòå ðåñóðñè
(êàòî óåá ñúðâúðè è load balancers), êîèòî òðÿáâà äà áúäàò äîñòúïí è èçâúí
VPC-òî.
Ôèãóðà 4: Internet Gateway êîíôèãóðàöèÿ è attachment êúì WebAppVPC
8

---

<!-- Page 9 -->

5.4 Ñúçäàâàíå íà NAT G ateway
Ñòúïêè:
Ñúçäàäîõìå Elastic IP è ãî àñîöèèðàõìå ñ NAT Gateway â Public
Subnet 1. Ñâúðçàõìå Private Subnet 1 ñ NAT Gateway ÷ðåç Private Route Table.
Ôèãóðà 5: NAT Gateway íàñòðîéêè è Elastic IP àñîö èàöèÿ
5.5 Ñúçäàâàíå íà Route Tables
Ñòúïêè è êîíôèãóðàöèÿ:
‹
Public Route Tabl e: Ñâúðçàõìå ñ Pub lic S ubnets è äîáàâèõìå ìàðøðóò êúì
Internet Gateway (0.0.0.0/0
ˇ
IGW).
Ôèãóðà 6: Êîíôèãóðàöèÿ íà Route Tables
‹
Private Route Table: Ñâúðçàõìå ñ Private Subnets è äîáàâèõìå ìàðøðóò
êúì NAT Gateway (0.0.0.0/0
ˇ
NAT Gateway). Òîâà ãàðàíòèðà, ÷å òð à-
ôèêúò îò ÷àñòíèòå ïîäìðåæè ùå ìèíàâà ïðåç NAT Gateway çà äîñòúï äî
èíòåðíåò.
Ôèãóðà 7: Êîíôèãóðàöèÿ íà Volumes
Çàùî ãî íàïðàâèõìå:
Route Table ãàð àí òè ðà, ÷å òðàôèêúò îò ïóáëè÷íèòå
ïîäìðåæè ìîæå äà èçëèçà êúì è íòåðíåò. Ìàðøðóòúò ñ Destination: lo cal îñè-
ãóðÿâà âúòðåøíàòà êîìóíèêàöèÿ ìåæäó ïîäìð åæè òå â ñúùîòî VPC, áåç äà å
íåîáõîäèì èíòåðíåò äîñòúï.
9

---

<!-- Page 10 -->

Ôèãóðà 8: Enter Caption
5.6 Ñúçäàâàíå íà Security Groups
Êîíôèãóðàöèÿ:
‹
Security Group çà EC2 èíñòàíöè è:

Inb ound R ules:

HTTP (80): Ðàçðåøåíî îò Application Load Balancer.

HTTPS (443): Ðàçð åøåíî îò Application Load Balancer.

SSH (22): Ðàçðåøåíî ñàìî îò îïðåäåëåí IP àäðåñ (ëîêàëåí êîìïþòúð).
‹
Security Group çà Application Load Balancer:

Inb ound Ru les:

HTTP (80): Ðàçðåøåíî îò âñÿêúäå (0.0.0.0/0).

HTTPS (443): Ðàçðåøåíî îò âñÿêúäå (0.0.0.0/0).
‹
Security Group çà RDS (MySQL):

Inb ound Ru les:

MySQL (3306): Ðàçðåøåíî ñàìî îò Security Group-à íà EC2 (çà äà ñå
îñèãóðè äîñòúï ñàìî îò EC2 èí ñòàíöèè).
Ôèãóðà 14: Security Groups êîíôèãóðàöèÿ çà R DS - Inb ound
10

---

<!-- Page 11 -->

5.7 Ñúçäàâàíå íà RDS MySQL Database
Êîíôèãóðàöèÿ:
*
DB Instance Identi˝er: ˛ask-db
*
Master Username: admin
*
Master Password: [ñèãóðíà ïàðîëà]
*
DB Instance Class: db.t2.micro (Free Tier eligible)
*
Storage: 20GB (ìèíèìóì çà Free Tier)
*
VPC: Èçáðàíî ñúùåñòâóâàùîòî WebAppVPC.
*
Subnet Grou p: Èçáðàíà ãðóïàòà ñ Private Sub nets.
*
Public Access: No (RDS ùå áúäå äîñòúïíà ñàìî âúòðå â VPC).
*
Security Group: Security Group çà RDS
*
Database Name: ˛ask-db
Ôèãóðà 15: RDS MySQL èíñòàíöèÿ êîíôèãóðàöèÿ
5.8 Ñúçäàâàíå íà Application Load Balancer
Êîíôèãóðàöèÿ:
*
Scheme: Internet-facing (ïóáëè÷íî äîñòúïåí)
*
IP address typ e: IPv4
*
VPC: Èçáðàíî ñúçäàäåíîòî WebAp pVPC
*
Availability Zones: Èçáðàíè Public Subnet 1 è Publ ic Subnet 2
*
Security Groups: Èçáðàíà ALB Security Group
*
Target Group: Ñúçäàäåíà çà EC2 èíñòàíöèÿòà â Public Subnet 1
*
Health Checks: Êîíôèãóðèðàíè çà HTTP íà ïúò "/health"èëè "/"
*
Port: 80 çà HTTP òðàôèê
ALB àâòîìàòè÷íî ïðîâåðÿâà çäðàâîñëîâíîòî ñúñòîÿíèå íà EC2 èíñ-
òàíöèèòå è ïðåíàñî÷âà òðàôèêà ñàìî êúì çäðàâèòå èíñòàíöèè. Ïðè
îòêàç íà åäíà èí ñòàíöèÿ, òðàôèêúò àâòîìàòè÷ íî ñå ïðåíàñî÷âà êúì
îñòàíàëèòå ðàáîòåùè èíñòàíöèè, àêî èìà òàêèâà (ïîðàäè ëèïñà íà
ñðåäñòâà íèå íÿìàìå âòîðà EC2 èí ñòàíöèÿ).
11

---

<!-- Page 12 -->

Ôèãóðà 16: Application Load Balancer êîíôèãóðàöèÿ è Target Groups
6 Êðàòêî ðúêîâîäñòâî çà ïîòðåáèòåëÿ
Student Records ïðåäîñòàâÿ èíòóèòèâåí è ëåñåí çà èçïîëçâàíå èíòåð-
ôåéñ çà óïðàâëåíèå íà ñòóäåíòêñè äàííè. Ïðè ëîæåíèåòî å äîñòúï-
íî ÷ðåç Application Load Balancer UR L àäðåñà, êîéòî àâòîìàòè÷íî
ðàçïðåäåëÿ çàÿâêèòå ìåæäó íàëè ÷íèòå EC2 èíñòàíöèè çà îïòèìàëíà
ïðîèçâîäèòåëíîñò.
6.1 Äîñòúï äî ïðèëîæåíèåòî
Çà äà çàïî÷íåòå äà èçïîëçâàòå S tudent Records:
1. Îòâîðåòå web browser (Chrome, Firefox, Safari, Edge)
2. Âúâåäåòå URL àäðåñà íà ïðèëîæåí èåòî â àäðåñíàòà ëåíòà
3. Ïðèëîæåíèåòî ùå ñå çàðåäè àâòîìàòè÷íî è ùå âèäèòå ãëàâíàòà
ñòðàíèöà
6.2 Ãëàâíà ñòðàíèöà
Ãëàâíàòà ñòðàíèö à ïîêàçâà:
*
Çàãëàâèå "Ñòóäåíòñêè Çàïèñè"ñ ëîãîòî íà ÑÓ
*
Òàáëèö à ñ âñè÷êè äîáàâåíè ñòóäåíòè, ñúäúðæàùà äàííèòå íà ñòó-
äåíòèòå
*
Ñèí áóòîí "Äîáàâè"â äîëíèÿ ëÿâ úãúë çà äîáàâÿíå íà íîâ ñòóäåíò
*
Ñèí áóòîí "Ðåäàêòèðàé"â äÿñíî, ñë óæåù çà ïðîìÿíà íà äàííèòå
íà ñòóäåíò
*
×åðâåí áóòîí "Èçòðèé"â äÿñí î, ñëóæåù çà èçòðèâàíå íà äàííèòå
íà ñòóäåíò
*
Áÿë áóòîí "Ñòóäåíòè"ãîðå â äÿñíî, ñëóæåù çà ïîêàçâàíå ñàìî íà
äàííèòå íà âñè÷êè ñòóäåíòè
*
Ñèâ áóòîí "Ôèëòðèðàé"è "Èç÷èñòè"ñúîòâåòíî íóæíè çà ôèëò-
ðèðàíåòî íà ñòóäåíòèòå
12

---

<!-- Page 13 -->

Ôèãóðà 17: Ãëàâíà ñòðàíèöà íà Student Records ï ðèëîæåíèåòî
6.3 Ñòóäåíòè
Ñïèñúêúò ñ âñè÷êè ñòóäåíòè â áàçàòà îò äàííè:
Ôèãóðà 18: Âñè÷êè ñòóäåíòè
6.4 Ðåäàêòèðàíå íà ñúùåñòâóâàù çàïèñ
Çà äà ðåäàêòèðàòå èíôîðìàöèÿòà çà äàäåí ñòóäåíò:
13

---

<!-- Page 14 -->

6.5 Èçòðèâàíå íà çàïèñ
Ôèãóðà 19: Áóòîí çà èñòðèâàíå íà ñòóäåíò
Ôèãóðà 20: Ï îòâúðæäàâàíå
Ôèãóðà 21: Ðåçóëòàò
14

---

<!-- Page 15 -->

6.6 Íàâèãàöèÿ è èíòåðôåéñ
*
Îòçèâ÷èâ ä èçàéí:
Ïðèëîæåíèåòî å îïòèìèçèðàíî çà ðàçëè÷íè
ðàçìåðè íà åêðàíà (äåñêòîï, òàáëåò, ìîáèëåí)
*
Bo otstrap ñòèëèçèðàíå:
Èçïîëçâà ñå ìîäåðåí è ïðîôåñèîíàëåí
äèçàéí
*
Èíòóèòèâíè öâåòîâå:
Çåëåíè áóòîíè çà ïîçèòèâíè äåéñòâèÿ
(äîáàâÿíå, ðåäàêòèðàíå), ÷åðâåíè çà îïàñíè äåéñòâèÿ (èçòðèâàíå)
*
Flash ñúîáùåíèÿ:
Âñÿêî äåéñòâèå ñå ïîòâúðæäàâà ñ ÿñíî ñúîá-
ùåíèå çà îáðàòíà âðúçêà
6.7 Òåõíè÷åñêè èçèñêâàíèÿ
*
Ñúâðåìåíåí web browser ñ ïîääðúæêà íà JavaScript
*
Àêòèâíà èí òåðí åò âðúçêà
*
Íÿìà íóæäà îò ñïåöèàëíè plugin- è èëè äîïúëíè òåë åí ñîôòóåð
6.8 Âúçìîæíè ãðåøêè è ðåøåíèÿ
*
Ñòðàíèöàòà íå ñå çàðåæäà:
Ïðîâåðåòå èíòåðíåò âðúçêàòà è
îïèòàéòå äà ïð åçàðåä èòå ñòðàíèöàòà
*
Áóòîíèòå íå ðàáîòÿò:
Óâåðåòå ñå, ÷å JavaScript å àêòèâèðàí â
áðàóçúðà
*
Ôîðìèòå íå ñå èçïðàùàò:
Ïðîâåðåòå ä àë è ñòå ïîïúëíèëè âñè÷-
êè çàäúëæè òåë íè ïîëåòà
7 Ïðèìåðíè äàííè
Çà òåñòâàíå íà ôóíêöèîíàëíîñòòà íà Student Records ïðèëîæåíèåòî
ñà èçïîëçâàíè ñëåäíèòå ïðèìåðíè äàííè:
Ñòóäåíò 1:
*
Ô.Í.: 72087
*
Èìå: Äèìè òúð Öîíåâ
*
Ñïåöèàëíîñò : ÈÑ
Ñòóäåíò 2:
*
Ô.Í.: 12345
*
Èìå: Ïåòúð Ïåòðîâ
15

---

<!-- Page 16 -->

*
Ñïåöèàëíîñò: ÊÍ
Ñòóäåíò 3:
*
Ô.Í.: 61023
*
Èìå: Èâàí Èâàíîâ
*
Ñïåöèàëíîñò: ÑÈ
Òåçè ïðèìåðíè äàííè ä åì îí ñòð èðàò ïúëíàòà CRUD ôóíêöèîíàëíîñò
íà ïð èëîæåíèåòî - äîáàâÿíå, ÷åòåíå, àêòóàëè çèðàíå è èçòðèâàíå íà
çàïèñè. Âñè÷êè îïåðàöèè ñà òåñòâàíè óñïåøíî êàê òî ëîêàëíî, òàêà è
â AWS cloud ñðåäàòà.
8 Îïèñàíèå íà ïðîãðàìíèÿ êîä
8.1 extensions.py
Â òîçè ôàé ë ñå äåôèíèðà åäèíñòâåíàòà èíñòàíöè ÿ íà SQLAlchemy,
êîÿòî ñå èçïîëçâà îò âñè÷êè îñòàíàëè ìîäóëè:
from flask_sqlalchemy import SQLAlchemy
# Ãëîáàëåí îáåêò çà äîñòúï äî áàçàòà äàííè
db = SQLAlchemy()
8.2 app.py
Îñíîâíèÿò ìîäóë íà ïðèë îæåíèåòî, êîéòî:
*
Çàðåæäà êîíôèãóðàöèÿòà îò
.env
÷ðåç
python-dotenv
.
*
Èíèöèàëèçèðà Flask è ðåãèñòðèðà áàçàòà äàííè.
*
Äåôèíèðà ì àð øðóòè òå çà CRUD îïåðàöèèòå.
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from extensions import db
from models import Student
from forms import StudentForm
# Çàðåæäàìå .env ïðîìåíëèâèòå
load_dotenv()
16

---

<!-- Page 17 -->

def create_app():
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
db.create_all()
@app.route('/')
def index():
form = StudentForm(request.args)
q = Student.query
# Ïðèëîæåíèå íà ôèëòðè
if form.specialty.data:
q = q.filter_by(specialty=form.specialty.data)
if form.course.data:
q = q.filter_by(course=form.course.data)
if form.group.data:
q = q.filter_by(group=form.group.data)
# Ñîðòèðàíå
sort = request.args.get('sort', 'faculty_number')
order = request.args.get('order', 'asc')
col = getattr(Student, sort)
q = q.order_by(col.desc() if order=='desc' else col.asc())
students = q.all()
specialties = [r[0] for r in db.session.query(Student.specialty).distinct()]
courses = sorted({s.course for s in Student.query.with_entities(Student.course)})
groups = sorted({s.group for s in Student.query.with_entities(Student.group)})
return render_template('index.html',
students=students,
form=form,
specialties=specialties,
courses=courses,
groups=groups,
sort=sort,
order=order)
17

---

<!-- Page 18 -->

@app.route('/add', methods=['GET','POST'])
def add_student():
form = StudentForm()
if form.validate_on_submit():
student = Student(**form.data)
db.session.add(student)
db.session.commit()
flash('Ñòóäåíòúò áåøå äîáàâåí óñïåøíî.', 'success')
return redirect(url_for('index'))
return render_template('add.html', form=form)
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_student(id):
student = Student.query.get_or_404(id)
form = StudentForm(obj=student)
if form.validate_on_submit():
form.populate_obj(student)
db.session.commit()
flash('Ïðîìåíèòå áÿõà çàïàçåíè.', 'success')
return redirect(url_for('index'))
return render_template('edit.html', form=form, student=student)
@app.route('/delete/<int:id>')
def delete_student(id):
student = Student.query.get_or_404(id)
db.session.delete(student)
db.session.commit()
flash('Ñòóäåíòúò áåøå èçòðèò.', 'warning')
return redirect(url_for('index'))
return app
if __name__ == '__main__':
create_app().run(host='0.0.0.0', port=5000, debug=True)
8.3 mo dels.py
Òóê ñå äåôèíèðà ìîäåëúò
Student
, êîé òî îòãîâàðÿ íà òàáëèö àòà
students
:
from extensions import db
18

---

<!-- Page 19 -->

class Student(db.Model):
__tablename__ = 'students'
id = db.Column(db.Integer, primary_key=True)
faculty_number = db.Column(db.String(20), unique=True, nullable=False)
first_name = db.Column(db.String(50), nullable=False)
last_name = db.Column(db.String(50), nullable=False)
specialty = db.Column(db.String(100), nullable=False)
course = db.Column(db.Integer, nullable=False)
group = db.Column(db.String(10), nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
address = db.Column(db.String(200))
city = db.Column(db.String(100))
state = db.Column(db.String(100))
phone = db.Column(db.String(20))
8.4 forms.py
Òîçè ìîäóë îïèñâà ôîðìàòà çà äîáàâÿíå/ðåäàêöèÿ íà ñòóäåíò, çàåäíî
ñ âàëèäàöèèòå:
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email
SPECIALTIES = [
('ÈÑ','Èíôîðìàòèêà'),
('ÊÍ','Êîìïþòúðíè íàóêè'),
('ÑÈ','Ñîôòóåðíî èíæåíåðñòâî')
]
COURSES = [(i, str(i)) for i in range(1,6)]
GROUPS = [('A','A'),('B','B'),('C','C')]
class StudentForm(FlaskForm):
faculty_number = StringField('Ôàê. íîìåð', validators=[DataRequired()])
first_name = StringField('Èìå', validators=[DataRequired()])
last_name = StringField('Ôàìèëèÿ', validators=[DataRequired()])
specialty = SelectField('Ñïåöèàëíîñò', choices=SPECIALTIES, validators=[DataRequired()])
course = SelectField('Êóðñ', choices=COURSES, validators=[DataRequired()])
group = SelectField('Ãðóïà', choices=GROUPS, validators=[DataRequired()])
19

---

<!-- Page 20 -->

email = StringField('Email', validators=[Email()])
address = StringField('Àäðåñ')
city = StringField('Ãðàä')
state = StringField('Îáëàñò')
phone = StringField('Òåëåôîí')
submit = SubmitField('Çàïàçè')
8.5 Âúçìîæíîñòè çà áúäåùî ðàçâèòèå
Ïðèëîæåíèåòî ìîæå äà áúäå çíà÷èòåëíî ïîäîáðåíî â ñëåäíèòå íàïðàâ-
ëåíèÿ:
*
Ìàùàáèðóåìîñò:
Äîáàâÿíå íà Auto Scaling Groups çà àâòîìà-
òè÷íî ìàùàáèðàíå í à EC2 èíñòàíöèèòå ïðè ïðîìÿíà â íàòîâàð-
âàíåòî
*
Ñèãóðíîñò:
Âíåäðÿâàíå íà SSL/TLS ñ Amazon Certi˝cate Manager
çà HTTPS êîìóíèêàöè ÿ
*
Ïîòðåáèòåëñêî óïðàâëåíèå:
Äîáàâÿíå íà ïîòðåáèòåëñêà ðå-
ãèñòðàöèÿ, âõîä è ïåðñîíàëèçèðàíè wishlist-è
*
Áàçà äàííè:
Ïðåìèíàâàíå êúì Multi-AZ RDS deployment çà ïî-
âèñîêà íàëè÷íîñò
*
Ìîíèòîðèíã:
Âíåäðÿâàíå í à CloudWatch çà ìîí èòîð èíã íà ïðî-
èçâîäèòåëíîñòòà è àâòîìàòè÷íè alert-è
*
CDN:
Èçïîëçâàíå íà Amazon CloudFront çà êåøèðàíå è ïî-áúðçà
äîñòàâêà íà ñúäúðæàíèå
*
Ôóíêöèîíàëíîñò:
Äîáàâÿíå íà òúðñåíå, ôèë òðèðàíå, êàòåãî-
ðèè è ðåéòèíã ñèñòåìà çà êíèãèòå
*
API:
Ðàçðàáîòâàíå íà RESTful API çà ìîáèëíè ïðèëîæåí èÿ
*
DevOps:
Âíåäðÿâàíå íà CI/CD pip eline ñ AWS Co dePip eline çà
àâòîìàòè÷íî äåïëîéâàíå
9 Êàêâî íàó÷èõ
×ðåç èçïúëíâàíåòî íà òîçè ïðîåêò ïðèäîáèõ öåííè çíàíèÿ è óìåíèÿ
â îáëàñòòà íà clou d computing è web devel op ment:
9.1 AWS Cloud Serv ices
*
Ïðàêòè÷åñêî ðàçáèðàíå íà AWS àðõèòåêòóðíè ïð èíöèïè è b est
practices
20

---

<!-- Page 21 -->

*
Óìåíèÿ çà ï ðîåêòèðàíå è êîíôèãóðèðàíå íà VP C ìðåæîâà àðõè-
òåêòóðà
*
Îïèò ñ ðàçëè÷íè AWS óñëóãè: EC2, RDS, ALB, VPC, Security
Groups
*
Ðàçáèðàíå íà âàæíîñòòà íà ìðåæîâàòà ñèãóðíîñò è èçîëàöèÿ â
cloud ñðåäàòà
*
Íàó÷èõ êàê äà áàëàíñèðàì ìåæäó ôóíêöèîíàëíîñò è ðàçõîä è â
cloud ðåøåíèÿòà
9.2 Web Development
*
Çàäúëáî÷åíè çíàíèÿ çà Flask framework è MVC àðõèòåêòóðåí ìî-
äåë
*
Ïðàêòè÷åñêè îïèò ñ SQLAlchemy ORM çà óïðàâëåíèå íà áàçè
äàííè
*
Óìåíèÿ çà ñúçäàâàíå íà resp on sive web design ñ Bo otstrap
*
Ðàçáèðàíå íà âàæíîñòòà íà äîáð àòà ñòðóêòóðà íà êîäà è ðàçäå-
ëåíèåòî íà îòãîâîð íîñòè òå
9.3 DevOps è Infrastructure
*
Îïèò ñ cloud deployment è êîíôèãóðèðàíå íà pro duction ñð åäà
*
Ðàçáèðàíå íà âàæíîñòòà íà ìîíèòîðèíãà è ëîãèðàíåòî â ïð îè ç-
âîäñòâåíè ñèñòåìè
*
Çíàíèÿ çà ìðåæîâà ñèãóðíîñò è ˝rewall êîíôèãóðàöèè
*
Ïðàêòè÷åñêè îïèò ñ load balancing è high availability àðõèòåêòóðè
9.4 Ïðîôåñèîíàëíè óìåíèÿ
*
Ïîäîáðåíè óìåíèÿ çà ðåøàâàíå íà ïðîáëåìè è debugging
*
Îïèò ñ ÷åòåíå è àíàëèçèðàíå íà òåõíè÷åñêà äîêóìåíòàöèÿ
*
Ðàçáèðàíå íà âàæíîñòòà íà ïëàíèðàíåòî è àðõèòåêòóðíîòî ïðî-
åêòèðàíå
*
Óñåòúò çà áàëàíñèðàíå ìåæäó òåõíè÷åñêèòå èçèñêâàíèÿ è ïðàê-
òè÷åñêèòå îãðàíè÷åí èÿ
21

---

<!-- Page 22 -->

9.5 Áúäåùè ñòúïêè
Òîçè ïðîåêò ìè äàäå ñîëèäíà îñíîâà çà ïî-íàòàòú øí î ðàçâèòèå â
îáëàñòòà íà cloud computing. Ïëàíèðàì äà ï ðîäúëæà äà èçó÷ àâàì
advanced AWS óñëóãè êàòî Lamb da, AP I Gateway, CloudFormation è
äà ñå ôîêóñèðàì âúðõó àâòîìàòèçàöè ÿ è DevOp s ïðàêòèêè. Ñúùî
òàêà èñêàì ä à í àäãðàäÿ ïîçíàíèÿòà ñè â îáëàñòòà íà container òåõ-
íîëîãèè êàòî Do cker è Kub ernetes çà ïî-åôåêòèâíî óïðàâëåíèå íà
ïðèëîæåíèÿòà â cloud ñðåä àòà.
10 Ñïèñúê ñ ôèãóðè è òàáëèöè
Ñïèñúê íà òàáëèöèòå
Ñïèñúê íà ôèãóðèòå
1 Àðõèòåêòóðà íà ï ðîåêòà . . . . . . . . . . . . . . . . . . 4
2 Ñúçäàâàíå íà VPC â AWS Management Console . . . . . 7
3 Êîíôèãóðàöèÿ íà public è private su bnets . . . . . . . . 8
4 Internet Gateway êîíôèãóðàöèÿ è attachment ê úì Web AppVPC 8
5 NAT Gateway íàñòðîéêè è Elastic IP àñîöèàöèÿ . . . . . 9
6 Êîíôèãóðàöèÿ íà Route Tabl es . . . . . . . . . . . . . . 9
7 Êîíôèãóðàöèÿ íà Volumes . . . . . . . . . . . . . . . . . 9
8 Enter Caption . . . . . . . . . . . . . . . . . . . . . . . . . 10
14 Security Groups êîíôèãóðàöèÿ çà RDS - Inb ound . . . . 10
15 RDS MySQL èíñòàíöèÿ êîíôèãóðàöèÿ . . . . . . . . . . 11
16 Application Load Balancer êîíôèãóðàöèÿ è Target Groups 12
17 Ãëàâíà ñòðàíèöà íà Student Records ï ðèëîæåíèåòî . . . 13
18 Âñè÷êè ñòóäåíòè . . . . . . . . . . . . . . . . . . . . . . . 13
19 Áóòîí çà èñòðèâàíå íà ñòóäåíò . . . . . . . . . . . . . . . 14
20 Ïîòâúðæäàâàíå . . . . . . . . . . . . . . . . . . . . . . . 14
21 Ðåçóëòàò . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
11 Èçïîëçâàíè èçòî÷íèöè
[1] Amazon VPC User Guide - AWS Do cumentation
22

---

<!-- Page 23 -->

[2] Appli cation Load Balancer - AWS Do cumentation
[3] Amazon RDS User Guide - AWS Do cumentation
[4] Flask Do cumentation - Web Development with Python
[5] Amazon EC2 Security Groups - AWS Do cumentation
[6] NAT Gateways - Amazon VPC User Guide
[7] Internet Gateways - Amazon VPC User Guide
[8] AWS Well-Architected Framework
[9] Route Tables - Amazon VPC User Guide
[10] PyMySQL Do cumentati on - Python MyS QL Client Library
23

---

