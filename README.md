securak:

A) bez ograniczeń:
index
/schedule/instruction/
http://localhost:8000/offices
http://localhost:8000/office/dental-med-kr-00001/
http://localhost:8000/dentists
http://localhost:8000/dentist/kowalski-jan-2441242/
http://localhost:8000/blog
http://localhost:8000/blog/2015/12/testowy-post-3/
http://localhost:8000/blog/category/pielegnacja-zebow/
http://localhost:8000/blog/tag/okazje/
http://localhost:8000/shop
http://localhost:8000/shop/product/szczoteczka-colgate-white-intensive-care-colgate/
http://localhost:8000/shop/category/szczoteczki-do-zebow/
http://localhost:8000/shop/tag/promocja/
http://localhost:8000/contact
http://localhost:8000/about
http://localhost:8000/login

B) zalogowany
http://localhost:8000/patient_zone/change_password


C) zalogowany - pacjent
http://localhost:8000/patient_zone
http://localhost:8000/patient_zone/patient_appointements
http://localhost:8000/patient_zone/patient_info
http://localhost:8000/patient_zone/patient_history


D) zalogowany - gabinet:
http://localhost:8000/account
http://localhost:8000/schedule/list/
http://localhost:8000/patients
http://localhost:8000/patient/wolny-rafal-12345678901/
http://localhost:8000/patient/update/wolny-rafal-12345678901/
http://localhost:8000/new_patient
http://localhost:8000/new_dentist
http://localhost:8000/new_schedule
http://localhost:8000/event_create
http://localhost:8000/blog/new/


1) sklep - koszyk, paypal, user group->shop-staff, blog-staff, hurt/detal, doszlifować list/detail/catalog/tag https://github.com/bmentges/django-cart
https://github.com/supernifty/django-paypal-store-example
http://www.supernifty.org/articles/oreilly-django-paypal-store/paypal-django.html
https://www.packtpub.com/books/content/setting-complete-django-e-commerce-store-30-minutes
2) dokończyć events/ history/info - w tym edycja Contact, może patient/slug/events/???
3)poprawić paginację
4) linki menu i nawigacja
5) poprawić urle, komentarze i rozdzielić widoki i modele??? http://stackoverflow.com/questions/1921771/django-split-views-py-in-several-files
6) ustawić dostępy - security - group - patients, dentists, offices, queryset
7) dodawanie obrazków
8) ad-rotator (2 rodzaje i kontrola rozmiaru?) i /promotions
9) mail-marketing - podstawowy?  (form, selects, user count)
10) content + test.py (fill database) - albo czysta baza danych (lista userów i haseł)
11) css'y i obrazki
12??) podpowiadaczki zamiast selectów!!?? https://github.com/crucialfelix/django-ajax-selects
13??) potwierdzenie i przypomnienie o wizycie
14??) dentist zone
15??) ograniczyć przy evencie - tylko ci userzy którzy byli do 10 dni
16??) has_free_slots_this_week?
17??) dentist landing pages? per city? per province?
18??) pdf from events?
19??) user with flag is_verified() == False - can make only one appointment
20) slug auto
21) walidacje w formsach
22???) remove unused imports, DentistDay - unique date?, rethink - blank/null in models, page with newses?
23) error with template_dirs?
24) auto create days - 2 weeks? - for every dentist? on dentist create?
25??) rethink - slug or pk for dentistday view?
26??) filters on listViews
27) lepszy cennik z wyszukiwaniem

robić dokumentację, uml (use case, class, ...), erd, instrukcje użytkownika, wymagania, opisy techniczne, user stories - http://www.cs.put.poznan.pl/csobaniec/edu/jakpisacmgr.pdf (zaleca styl bezosobowy), przygotować 5 pytań na obronę (programowanie, bazy danych, testowanie, algorytmy)
pisać test casy!

informacje o innych możliwościach/stronach, kwestiach prawnych - (check legality of it - https://www.bpp.gov.pl/dla-pacjenta/prawa-pacjenta/prawo-do-dokumentacji-medycznej/)



flatpages?
pobawić się AJAXEM
pododawać messages


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

materialize css - 

<input type="text" name="country" value="Norway" readonly>

search on price list, change preferred_date!!!
w3c - https://validator.w3.org
return mail, cancel visit


darmowy skrypt - http://skryptcookies.pl/