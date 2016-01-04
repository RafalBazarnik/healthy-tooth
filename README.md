
1) potrzebuję tworzyć z automatu usera dla dentysty i pacjenta i dodawać ich do grup - odpowiednio Dentyści i Pacjenci
2) username - slug? password - pesel (potem możliwość zmiany?)
3) podstrona pacjenta z podgladem danych
4) podstrona dentysty z podglądem danych
================
5) zdjecia
6) filtry
7) social media - like/share
=============
8) zapis do dentysty - appointement - formsy - edycja, dodawanie, usuwanie
9) dodawanie eventów - dentysta/gabinet - przegladanie przez pacjenta
10) przemyśleć jakąś wersję grafika (typu na dzień na dentystę 10 pacjentów - 10 slotów x 5 dni - auto value - modyfikacja na true)



obiekt - dentistday - foreign key z dentist, office, 







1) logowanie -> typy userow (office, patient, dentist) i własne strony index :)
2) office slug s /province/city/slug (tylko - name?)
3) filters on listViews




TODO - main points:

1) /promotions page with all ads/discounts etc - office is able to add (proper size)
2) rotating ads on main page, appointment, blog/category/tag
3) user zone - where patient is able to edit contact data, and watch and export/print history of dentist interventions
4) dentist zone - where dentist can log and add events and see appointments (and mark them as done)
5) more data in appointment object - add some state ("new", "appointed", "cancelled", "completed") - auto create event, add dentist -> his view - and appointment may by added by office itself (somebody called etc.)
6) social media (like page)
7) filters on list views - eg. dentists per province, city - of office
8) new slug - office - /province/city/slug
9) landing pages - provine, city/slug
10) more searchable price list
11) schedule per dentist form appointed events
12) more data in dentist object - documents, money, vacations, type of work, etc. - > employee database - can see - no edit
13) shop - for external and internal clients ( office can order from inside :))
14) marketing emails - filter per options (age, sex, province, city, ??events count?)
15) add photos and documents uploading mathod
16) test automation, unit tests, comments, removed unused imports and with proper order
17) autopopulating slug fields + sometimes not slug but pk?
18) new - more pro css, img and layouts
19) different forms - more editing options (styles etc.)

new apps:
ads-display,
email-marketing
shop

consider - dividing main_page - office/patient/dentist (each with log in zone)

materialize css - 



ważne - popoprawiać - formsy - niektóre readonly
 <input type="text" name="country" value="Norway" readonly> i blokada jeśli nie ten gabinet


szukanie po cenniku, zmienić preferred_date!!!

zapis na datę - !!!!
w3c - https://validator.w3.org

synchro - danych - w trakcie

mail zwrotny - automatyczna
odwołanie wizyty