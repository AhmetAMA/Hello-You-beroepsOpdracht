def vraag1():
    print("\nJe woont in vrede met je familie in Syrië. In 2011 wordt een man gekozen die eerst er uitziet als een man die het land goed gaat besturen. Maar in begin 2012 verandert hij in een dictator en wordt Syrië bestuurt met dictatuur.")
    print("\n   Ben je voor of tegen de dictator? \na: Voor \nb: Tegen")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag2()
    elif antwoord.lower() == "b":
        vraag3()
    else:
        print("Kies a of b")
        vraag1()

def vraag2():
    print("\nOmdat je voor de dictator bent zit jij nu niet in gevaar en kan je voor nu veilig blijven wonen met je familie. Maar dat blijft niet zo voor lang. Want na een maandje krijg je al een brief thuis met dat je in het Syrische leger moet komen. En dat je verplicht 4 jaar lang moet vechten voor je land. Jij vind het wel goed, maar je vind ook dat 4 jaar te veel is.")
    print("\n   Ga je toch het leger in voor 4 jaar of vind je dat niet kunnen en ben je ook tegen de overheid? \na: Het leger in voor 4 jaar \nb: Tegen de overheid zijn")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag19()
    elif antwoord.lower() == "b":
        vraag3()
    else:
        print("Kies a of b")
        vraag2()

def vraag3():
    print("\nWat de dictator doet is niet goed. Hij beloofde Syrië goed te regeren, maar hij houdt zich niet aan zijn beloftes dus wil jij dat hij gaat aftreden. Maar dat gaat hij natuurlijk niet doen dus ga je online berichten schrijven tegen hem. Nadat de overheid erachter is gekomen dat jij die berichten schreef wordt je gezocht en bedreigt.")
    print("\n   Ga je jezelf aangeven of vluchten? \na: Jezelf aangeven \nb: Vluchten")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag4()
    elif antwoord.lower() == "b":
        vraag5()
    else:
        print("Kies a of b")
        vraag3()

def vraag4():
    print("\nJe gaat naar een politiebureau een geeft jezelf aan. Omdat er op jou naam een oppak bevel staat wordt je opgepakt en naar het gevangenis gestuurd. Na 2 maanden een hel leven in de gevangenis heb je eindelijk een rechtszaak. Bij de rechtszaak wordt er besloten om jou levenslang te geven als straf.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag4()

def vraag5():
    print("\nOmdat je gezocht wordt moet je zo snel mogelijk stiekem vluchten. Omdat je familie niet gezocht worden en de vlucht gevaarlijk kan zijn voor je familie blijven zij. Dus pak je al je spullen in, eet je snel effe eten zodat je onderweg niet honger krijgt en neem je afscheid. Op het moment dat je uit je huis gaat zie je dat je buren ook vluchten. Omdat jullie een goede band hebben vragen ze je of ze jou kunnen helpen. Ze hebben een grote auto en omdat ze niet met velen zijn is er nog plek voor jou.")
    print("\n   Ga je toch alleen vluchten omdat je denkt dat ze onderweg gepakt kunnen worden of ga je met hun mee naar Turkije? \na: Alleen vluchten \nb: Met hun mee naar Turkije")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag6()
    elif antwoord.lower() == "b":
        vraag7()
    else:
        print("Kies a of b")
        vraag5()

def vraag6():
    print("\nOmdat je niet met jullie eigen auto kan vluchten moet je lopend gaan. Eenmaal je uit de stad bent loop je langs de snelweg richting het noorden. Een auto die langs je rijdt vraagt of je lift nodig hebt.")
    print("\n   Ga je instappen of wijs je het af? \na: Instappen \nb: Het aanbod afwijzen")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag8()
    elif antwoord.lower() == "b":
        vraag9()
    else:
        print("Kies a of b")
        vraag6()

def vraag7():
    print("\nHelaas is er niet genoeg plek in de auto voor je hele familie dus beloof jij ze dat je hun zo snel mogelijk gaat weg halen van daar. Eenmaal vertrokken zijn jullie binnen een dag al bij het grens van Turkije. Omdat jullie je paspoorten bij jullie hebben en het ook bekend is hoe het in Syrië gaat mogen jullie Turkije in. In Turkije heb jij gelukkig familie, dus kan je bij hun blijven wonen.	")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag7()

def vraag8():
    print("\nJe stapt in en rijdt mee naar grens van Turkije. Wanneer jullie bij het grens aankomen moet je uitsappen en zelf zien binnen te komen. Je weet dat er 10 km verderop een poort is waar vluchtelingen Turkije in kunnen na een controle. Maar er wachten honderden misschien zelfs duizenden mensen daar in een rij. Wachten kan dagen duren, maar op dat moment komt er een smokkelaar naar je toe. Hij zegt dat hij over een uur jou voor 50 dollar het land in kan smokkelen.")
    print("\n   Geef je de smokkelaar 50 dollar of ga je in de rij wachten voor dagen? \na: De smokkelaar 50 dollar geven \nb: In de rij wachten")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag12a()
    elif antwoord.lower() == "b":
        vraag12b()
    else:
        print("Kies a of b")
        vraag8()

def vraag9():
    print("\nNa 10 minuten verder lopen komt er een auto met soldaten jou kant op rijden. Omdat jij gezocht wordt willen ze je oppakken nadat ze je gezien hebben. Dus besluit jij om weg te rennen. Maar natuurlijk is een auto sneller dus halen ze je in en richten hun wapens op je. Ze zeggen blijf staan en geef je over of we schieten.")
    print("\n   Geef je je over of ga je weg rennen? \na: Je overgeven \nb: Wegrennen")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag10()
    elif antwoord.lower() == "b":
        vraag11()
    else:
        print("Kies a of b")
        vraag9()

def vraag10():
    print("\nOmdat je jezelf over geeft schieten de soldaten je niet en nemen ze je levend mee naar een politie bureau. Na een week vast te zitten in een cel heb je eindelijk een rechtszaak en krijg je als straf levenslang. Vanuit het rechtszaak wordt je gebracht naar een gevangenis waar je vanaf nu je hele leven blijft.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag10()

def vraag11():
    print("\nWegrennen is helaas niet een slimme keuze. Op het moment dat je je omdraait en weg probeert te rennen wordt je al gelijk vol geschoten door een paar AK-47. Door zo vaak geschoten te worden kan je dit niet overleven en ga je dood ter plekke.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag11()

def vraag12a():
    print("\nDe smokkelaar neemt je mee naar een vrachtwagen en doet de deuren van de achterkant open en zegt ga erin. Wanneer je erin gaat zie je dat er meer vluchtelingen zijn. Je zit in een hoekje en wacht rustig tot je de grens over bent. Na een uur gaat de vrachtwagen de grens over en rijdt nog 10 km verder. Na ongeveer 10 minuten rijden stopt het en gaat plotseling de deur open. Iedereen stapt uit en loopt weg. Maar jij weet niet wat je nu moet doen dus ga je naar de smokkelaar en vraagt wat nu. De smokkelaar zegt dat zijn deel klaar is en je nu alleen ervoor staat. Jij besluit om naar Europa te gaan via Griekenland. Maar hoe kom je Griekenland in? Enige keus is door de Egeïsche Zee over te steken met een boot.")
    print("\n   Steek je de Egeïsche Zee over via Izmir of Canakkale? \na: Izmir \nb: Canakkale")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag13()
    elif antwoord.lower() == "b":
        vraag14()
    else:
        print("Kies a of b")
        vraag12a()

def vraag12b():
    print("\nNa 3 dagen wachten ben jij eindelijk aan de beurt en wordt jij nu gecontroleerd door Turkse soldaten en politie. Nadat ze je gefouilleerd hebben vragen ze je een aantal vragen. Wanneer je alle vragen beantwoordt hebt kan je eindelijk gaan. Je besluit om verder naar Europa te gaan via Griekenland. Maar hoe kom je Griekenland in? Enige keus is door de Egeïsche Zee over te steken met een boot.")
    print("\n   Steek je de Egeïsche Zee over via Izmir of Canakkale? \na: Izmir \nb: Canakkale")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag13()
    elif antwoord.lower() == "b":
        vraag14()
    else:
        print("Kies a of b")
        vraag12b()

def vraag13():
    print("\nIn Izmir kijk je rond of je hulp kan vinden. Opeens komt er een man naar je toe en vraagt in het Arabisch of je naar Griekenland wilt gaan. Jij vraagt hem in verbazing of hij ook vlucht, maar hij zegt gelijk dat hij voor 50 dollar een boot kan regelen die naar Griekenland gaat. Jij zegt dat 50 te veel is en vraagt of het voor minder kan. Hij reageert met dat je voor 20 dollar een andere boot in kan gaan, maar dat die wel minder veilig is.")
    print("\n   Geef je hem 50 of 20 dollar? \na: $50 \nb: $20")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag15()
    elif antwoord.lower() == "b":
        vraag16()
    else:
        print("Kies a of b")
        vraag13()

def vraag14():
    print("\nJe gaat vanuit het grens helemaal naar Canakkale en kijkt rond of je hulp kan vinden. Na een week zoeken vind je niks, dus besluit je om naar Izmir te gaan.")
    vraag13()

def vraag15():
    print("\nDe man neemt je mee naar een kust waar er niemand is. Er is alleen een boot en er zitten heel veel mensen erin. Hij zegt dat je in die boot moet gaan blijven zitten tot je bij Griekenland aan komt. Na een uur varen zien jullie al gelijk land en ben je heel blij. Je bent eindelijk in Griekenland. Maar eenmaal blijkt het een eiland te zijn met de kamp “Moria”. De omstandigheden in de kamp zijn heel slecht. Toevallig komt er daar naar jou weer een smokkelaar die zegt dat hij je voor 100 dollar kan smokkelen naar Nederland.")
    print("\n   Geef je je laatste 100 dollar aan hem om naar Nederland te kunnen gaan of blijf je in de kamp? \na: Voor 100 dollar naar Nederland gaan \nb: Bij kamp blijven")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag17()
    elif antwoord.lower() == "b":
        vraag18()
    else:
        print("Kies a of b")
        vraag15()

def vraag16():
    print("\nDe man neemt je mee naar een kust waar er niemand is. Er is alleen een boot en er zitten heel veel mensen erin. Hij zegt dat je in die boot moet gaan blijven zitten tot je bij Griekenland aan komt. Na een half uur varen staat iemand op en schreeuwt dat de boot gescheurd is en dat het gaat zinken. Iedereen staat op en raakt in paniek waardoor de boot omvalt en iedereen gaat dood zowel jij.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag16()

def vraag17():
    print("\nJe geeft je laatste geld aan de smokkelaar en gaat naar Nederland. In Nederland sta je er weer alleen voor, dus ga je hier wel naar de bureau om hulp te vragen. Bij het bureau vertellen ze je over een asielzoekerscentrum waar je een asiel kan krijgen. Dus ga je naar daar en na lang wachten krijg je eindelijk een asiel en mag je in Nederland blijven.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag17()

def vraag18():
    print("\nJe kiest ervoor om je laatste geld te sparen en in het kamp te blijven. Helaas zijn de omstandigheden niet heel goed, maar daar kan je niks aan doen. Nu moet je geld verdienen en proberen om bij een plek met betere omstandigheden een toekomst zien op te bouwen. Maar nu nog effe voor een tijd hier op het kamp blijven.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag18()
        
def vraag19():
    print("\nNa 4 jaar in het leger mag je eindelijk weg. Maar nu IS aan de macht is bij een grote deel van het land ben jij in gevaar als ze je vinden. Is het nou verstandiger om terug te gaan naar je familie of in het leger blijven?")
    print("\n   Ga je nu vluchten naar Turkije? In het leger blijven? Of terug naar je familie in hoop dat IS je niet vind? \na: Naar Turkije vluchten \nb: In het leger blijven \nc: Terug naar je familie")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag20()
    elif antwoord.lower() == "b":
        vraag21()
    elif antwoord.lower() == "c":
        vraag22()
    else:
        print("Kies a, b of c")
        vraag19()

def vraag20():
    print("\nVluchten naar Turkije is een goed idee. Omdat je ook zolang in het leger was heb je connecties die jou kunnen helpen om het grens over te steken. Je vraagt aan een vriend of hij jou met een auto dichtbij de grens kan brengen. Hij brengt je naar het grens en vraagt nog aan een andere vriend van jullie die bij het grens werkt of hij jou kan helpen de grens over te steken. In de nacht wanneer het donker is gaan jullie stiekem het grens over en ben je nu in Turkije. Maar je bent nu illegaal hier dus kan je het liefst vluchten naar Griekenland.")
    print("\n   Ga je naar Griekenland oversteken via Izmir of Canakkale? \na: Izmir \nb: Canakkale")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag13()
    elif antwoord.lower() == "b":
        vraag14()
    else:
        print("Kies a of b")
        vraag20()

def vraag21():
    print("\nIn het leger blijven is verstandig, maar het is ook gevaarlijk omdat je constant zit te vechten met andere vijanden. Na nog zo een 4 jaar is Turkije, Syrië ingevallen en wordt jij naar het noorden gestuurd om tegen Turkije te vechten. Voordat je het beseft gooit een Turkse drone een bom op jullie voertuig en ben je dood.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag21()

def vraag22():
    print("\nNa 4 jaar strijden in het leger ga je terug naar je familie. Inmiddels zijn je kinderen al heel oud geworden. De volgende dag je naar een supermarkt op boodschappen te doen. Niet eens 5 minuten later wanneer je de winkel uit bent rijdt er auto heel hard op jou af. De auto ontploft en het blijkt een aanval van IS op jou te zijn. De aanval overleef je niet en ga je ter plekke dood.")
    print("\nEINDE!")
    print("\n   Wil je dit programma nog een keer afspelen? \na: Ja \nb: Nee")
    antwoord = input()
    if antwoord.lower() == "a":
        vraag1()
    elif antwoord.lower() == "b":
        vraag23()
    else:
        print("Kies a of b")
        vraag22()

def vraag23():
    print("\nDankjewel voor het spelen van dit programma.")

vraag1()