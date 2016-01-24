detail -> dentist - P - ?
detail -> gabinet - P - ?

form -> zapisz się P
form -> edytuj G
form -> cancel P

list -> swoje zapisy - P (godziny??? jak wycignac własciwy slot i jego help_text)

https://docs.djangoproject.com/en/dev/topics/db/managers/#custom-managers ???
=================
detail -> events, date - P (readonly - tylko Contact zmiana - form)
add/edit events - G
==================
has_free_slots_this_week?

dentist landing pages? per city? per province?

mail with to remeber about appointement?
pdf from events?
user with flag is_verified() == False - can make only one appointment

fb comments?
likes/shares?

https://docs.djangoproject.com/en/dev/topics/db/managers/#custom-managers

7- logged user or office - creates Appointement (several selects to limit choices? region/city/week?) + listView (per dentist / per day) + detailView - office can see and edit, User can see and cancel -> after visit - status to done and create Event
8- office can see/add/edit Events per Patient, user can only see (readonly) it or download it (check legality of it - https://www.bpp.gov.pl/dla-pacjenta/prawa-pacjenta/prawo-do-dokumentacji-medycznej/)


temp:
- slug auto
- check auto user create or only User account create!
- security? separate views with queryset - > 
- security - group - patients, dentists, offices
- walidacje w formsach
- images to dentist etc
- problem with paginations in shop and blog https://github.com/matthewbdaly/django_tutorial_blog_ng https://docs.djangoproject.com/en/1.9/topics/pagination/
- research - using messages.add 
https://github.com/bmentges/django-cart
https://github.com/supernifty/django-paypal-store-example
http://www.supernifty.org/articles/oreilly-django-paypal-store/paypal-django.html
https://www.packtpub.com/books/content/setting-complete-django-e-commerce-store-30-minutes

checklist:
1- user creates User/Patient account - sign up
2- user changes his password (alert - changed)
3- shop -> list, detail, catalog, tag, user group-> shop-staff (permissions) + blog-staff
4- shop - paypal payments, office has other products


5- ad-rotator? /promotions page
6- mail-marketing basics (form, selects, user count)

7- logged user or office - creates Appointement (several selects to limit choices? region/city/week?) + listView (per dentist / per day) + detailView - office can see and edit, User can see and cancel -> after visit - status to done and create Event
8- office can see/add/edit Events per Patient, user can only see (readonly) it or download it (check legality of it - https://www.bpp.gov.pl/dla-pacjenta/prawa-pacjenta/prawo-do-dokumentacji-medycznej/)
9- signup on DentistDay slot - mayby using get request - <url>?office=X&dentist=Y&day=Z - and form filled
10- dentist zone ??? or just in office account (add event, see appointements)
11- access to pages by user group - security
12- database - autofill - test.py + realistic content (at least 10 each)
13- css/js - beaufify :P 
14- comment code, remove unused imports, DentistDay - unique date?, rethink - blank/null in models, page with newses?
14- documentation - ERD, uml (of dentistday->appointement->event), theory

flatpages?
pobawić się AJAXEM
pododawać messages np:
def form_valid(self, form):
    form.save()
    messages.add_message(self.request, messages.INFO, 'Hasło zostało pomyślnie zmienione')
    return super(UserPasswordChangeView, self).form_valid(form)

error with template_dirs?

current:
2)ListView - 
3) auto create days - 2 weeks? - for every dentist? on dentist create?
4) rethink - slug or pk for dentistday view?
5) on dentist detail view - list of his slots -> make appointment (get?)
6) add/edit/cancel appointement
7) auto test data in test.py


@TODO:
A) user zone - with password change and readonly view of data/events + change in login auth + groups + of templates/views
B) scheduling per dentist - day = ten slots - add, edit/subscribe, remove- list and forms
D) filters on listViews
E) social media - like/share
F) small shop
G) email marketing
H) more real content - no lorem ipsum
I) css
J) documentation/UML/etc.
+ add event

(user - can log in, see his own data/events, see and cancel his own appointement, change password, user cannot edit anything else or remove etc.)
(office - can see appointements/per dentists, add slots, remove and add appointements, set appointement to done - add events!!!)


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

<input type="text" name="country" value="Norway" readonly>

search on price list, change preferred_date!!!
w3c - https://validator.w3.org
return mail, cancel visit
