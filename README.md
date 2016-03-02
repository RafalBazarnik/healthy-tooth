//all used images are from wikicommons

installation:
Python 3.4 and add to PATH
pip install virtualenv
git clone https://github.com/RafalBazarnik/healthy-tooth.git
in installation folder - command - virtualenv env
env/Scripts/activate
cd tooth
pip install –r requirements.txt
python manage.py runserver
in internet browser: http://localhost:8000/ is index and  admin panel: http://localhost:8000/admin.

database is in repo to enable easier testing


Admin (login: admin, password: admin)
Office 1: „Enel Med Dent” (login: test_office-PD-00001 , password: admin)
Office 2: „ Dental Med” (login: test_office_KR-00001, password: admin)
Patient: Weronika Kozak (login: kozak-weronika-22233398999, password: admin)

