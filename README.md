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
