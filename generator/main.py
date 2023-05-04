import csv
import random
import datetime
from faker import Faker
from unidecode import unidecode
import pycountry
import xlsxwriter

PARENT_NUMBER = 50000
ADDRESS_NUMBER = 50000
GROUPS_NUMBER = 25000
LESSON_NUMBER = 5000
FACILITY_NUMBER = 10000
CHILD_NUMBER  = 549665
APPLICATION_NUMBER = 1099731
CONTRACT_NUMBER = 20000
CHOOSES_NUMBER = 50000

def random_status():
    my_rand = random.randrange(100)
    if my_rand > 35:
        return 1
    else:
        return 0

def generating_lesson():
    fake = Faker('pl_PL')
    additional_lessons = [
        'Financial Literacy',
        'Environmental Science',
        'Computer Programming',
        'Emotional Intelligence',
        'Creative Writing',
        'Global Studies',
        'Media Literacy',
        'Philosophy',
        'Public Speaking',
        'Entrepreneurship']

    with open("lessondata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        for i in range(LESSON_NUMBER):
            row.append(i)
            row.append(2010+ (i%14))
            row.append(random.randrange(start=25, stop=200, step=5))
            row.append(additional_lessons[random.randrange(len(additional_lessons))])
            writer.writerow(row)

            row = []

def generating_parent():
    fake = Faker('pl_PL')
    with open("parentdata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        for i in range(PARENT_NUMBER):
            row.append(i)
            row.append(unidecode(fake.first_name()))
            row.append(unidecode(fake.last_name()))
            row.append(fake.pesel(datetime.date(1960+random.randrange(35),1+ random.randrange(12),1+random.randrange(27))))
            row.append(unidecode(str(fake.email())))
            row.append(str(random.randrange(start=100000000, stop=999999999)))
            writer.writerow(row)

            row = []

def generating_address():
    fake = Faker('pl_PL')
    district_list = [
        "Bemowo", "Białołęka", "Bielany", "Mokotów", "Ochota", "Praga-Południe",
        "Praga-Północ", "Rembertów", "Śródmieście", "Targówek", "Ursus", "Ursynów",
        "Wawer", "Wesoła", "Wilanów", "Włochy", "Wola", "Żoliborz", "Podgórze",
        "Krowodrza", "Nowa Huta", "Stare Miasto", "Muranów", "Powiśle", "Saska Kępa",
        "Czerniaków", "Mokotów-Południe", "Stary Mokotów", "Filtry", "Mirów",
        "Dolny Mokotów", "Wyględów", "Gocław", "Kamionek", "Grodzisk", "Grochów",
        "Wierzbno", "Stara Ochota", "Rakowiec", "Radość", "Rakówka", "Szczęśliwice",
        "Muranów Południowy", "Mokotów Zachodni", "Koszyki", "Skarpa Powsińska",
        "Górny Mokotów", "Służewiec", "Stegny", "Sadyba", "Czyste", "Rakówka-Kawęczyn",
        "Olesińska", "Nadolnik", "Niedźwiadek", "Łazienki Królewskie", "Czacki",
        "Solec", "Lipiny", "Służew", "Imielin", "Ksawerów", "Pyry", "Pomiechówek",
        "Michałowice", "Wilcza", "Kabaty", "Natolin", "Kawęczyn", "Bartycka", "Radosna",
        "Stara Miłosna", "Księcia Janusza", "Powsin", "Jelonki", "Witolin", "Grabów",
        "Wrzeciono", "Kaskada", "Łomianki Dolne", "Młociny", "Siekierki", "Marsa",
        "Zacisze", "Kozia", "Gorczewska", "Przyczółek Grochowski", "Kępa Tarchomińska"
    ]

    cities = [
        "Warsaw", "Krakow", "Lodz", "Wroclaw", "Poznan", "Gdansk", "Szczecin",
        "Bydgoszcz", "Lublin", "Katowice", "Bialystok", "Gdynia", "Czestochowa",
        "Sosnowiec", "Radom", "Torun", "Kielce", "Gliwice", "Rzeszow", "Zabrze",
        "Olsztyn", "Bielsko-Biala", "Bytom", "Ruda Slaska", "Rybnik", "Tychy",
        "Dabrowa Gornicza", "Plock", "Elblag", "Opole", "Gorzow Wielkopolski",
        "Wloclawek", "Chorzow", "Tarnow", "Kalisz", "Koszalin", "Legnica",
        "Grudziadz", "Jaworzno", "Przemysl", "Stargard Szczecinski",
        "Sopot", "Mielec", "Krotoszyn", "Kutno", "Ketrzyn", "Krasnik",
        "Kostrzyn nad Odra", "Koscian", "Kolobrzeg", "Kluczbork", "Klucze",
        "Klobuck", "Kety", "Kazimierz Dolny", "Kartuzy", "Jarocin", "Inowroclaw",
        "Gubin", "Gostynin", "Gostyn", "Goleniow", "Gniezno", "Glogow",
        "Gliwice", "Gizycko", "Garwolin", "Garwolin", "Garczegorze", "Gardno",
        "Frysztak", "Frydman", "Frampol", "Frombork", "Folk", "Elblag",
        "Dziwnow", "Dziwnowek", "Duszniki-Zdroj", "Dubiecko", "Drezdenko",
        "Drawsko Pomorskie", "Drawno", "Dolice", "Dobczyce", "Dobrzany",
        "Czersk", "Czerniejewo", "Czempiń", "Czaplinek", "Czarna Bialostocka",
        "Czarna Woda", "Czarnkow", "Czchow", "Czosnow", "Czerwiensk", "Czerwionka",
        "Czestochowa", "Ciechanow", "Chelmno", "Chelmza", "Chelmiec", "Chelmno",
        "Chocianow", "Chocznia", "Chodziez", "Chojna", "Chojnice", "Chojno",
        "Chorzow", "Chorzele", "Choszczno", "Chrzanow", "Ciechocinek", "Cieplice",
        "Czorsztyn", "Swidwin", "Swiebodzin", "Swiecie", "Swiebodzice", "Swidnica"
    ]

    with open("addressdata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        for i in range(ADDRESS_NUMBER):
            row.append(i)
            row.append(unidecode((cities[random.randrange(len(cities))])))
            row.append(fake.postcode())
            row.append(unidecode(fake.street_name()))
            row.append((random.randrange(500)))
            row.append((random.randrange(75)+10))
            row.append(unidecode(district_list[random.randrange(len(district_list))]))
            writer.writerow(row)

            row = []

def generating_groups():
    fake = Faker('pl_PL')
    with open("groupsdata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        for i in range(GROUPS_NUMBER):
            animal_names = animals = [
                "konie",
                "krowy",
                "psy",
                "koty",
                "owce",
                "kozy",
                "świnie",
                "króliki",
                "ptaki",
                "ryby",
                "żółwie",
                "węże",
                "gady",
                "pająki",
                "owady",
                "myszy",
                "chomiki",
                "szczury",
                "jelenie",
                "sarny",
                "dziki",
                "niedźwiedzie",
                "lisice",
                "wilkowie",
                "kojoty",
                "kangury",
                "lemury",
                "żyrafy",
                "slonie",
                "nosorożce",
                "hipopotamy",
                "lamparty",
                "pantery",
                "tygrysy",
                "lwy",
                "pingwiny",
                "foki",
                "morświny",
                "krokodyle",
                "aligatory",
                "żółwie morskie",
                "wieloryby",
                "delfiny",
                "dugongi",
                "wydry",
                "łasice",
                "borsuki",
                "łosie",
                "piżmaki",
                "tłumacze",
                "kazuary",
                "strusie",
                "jaguary",
                "gepardy",
                "goryle",
                "orangutany",
                "szakale",
                "lamparciki"]
            row.append(i)
            row.append(random.randrange(5)+2)
            row.append(unidecode(animal_names[random.randrange(len(animal_names))]))
            row.append(random.randrange(start=2015, stop=2024))
            writer.writerow(row)

            row = []

def generating_facility():
    fake = Faker()
    colors = [
        "AliceBlue",
        "AntiqueWhite",
        "Aqua",
        "Aquamarine",
        "Azure",
        "Beige",
        "Bisque",
        "Black",
        "BlanchedAlmond",
        "Blue",
        "BlueViolet",
        "Brown",
        "BurlyWood",
        "CadetBlue",
        "Chartreuse",
        "Chocolate",
        "Coral",
        "CornflowerBlue",
        "Cornsilk",
        "Crimson",
        "Cyan",
        "DarkBlue",
        "DarkCyan",
        "DarkGoldenRod",
        "DarkGray",
        "DarkGrey",
        "DarkGreen",
        "DarkKhaki",
        "DarkMagenta",
        "DarkOliveGreen",
        "DarkOrange",
        "DarkOrchid",
        "DarkRed",
        "DarkSalmon",
        "DarkSeaGreen",
        "DarkSlateBlue",
        "DarkSlateGray",
        "DarkSlateGrey",
        "DarkTurquoise",
        "DarkViolet",
        "DeepPink",
        "DeepSkyBlue",
        "DimGray",
        "DimGrey",
        "DodgerBlue",
        "FireBrick",
        "FloralWhite",
        "ForestGreen",
        "Fuchsia",
        "Gainsboro",
        "GhostWhite",
        "Gold",
        "GoldenRod",
        "Gray",
        "Grey",
        "Green",
        "GreenYellow",
        "HoneyDew",
        "HotPink",
        "IndianRed",
        "Indigo",
        "Ivory",
        "Khaki",
        "Lavender",
        "LavenderBlush",
        "LawnGreen",
        "LemonChiffon",
        "LightBlue",
        "LightCoral",
        "LightCyan",
        "LightGoldenRodYellow",
        "LightGray",
        "LightGrey",
        "LightGreen",
        "LightPink",
        "LightSalmon",
        "LightSeaGreen",
        "LightSkyBlue",
        "LightSlateGray",
        "LightSlateGrey",
        "LightSteelBlue",
        "LightYellow",
        "Lime",
        "LimeGreen",
        "Linen",
        "Magenta",
        "Maroon",
        "MediumAquaMarine",
        "MediumBlue",
        "MediumOrchid",
        "MediumPurple",
        "MediumSeaGreen",
        "MediumSlateBlue",
        "MediumSpringGreen",
        "MediumTurquoise",
        "MediumVioletRed",
        "MidnightBlue",
        "MintCream",
        "MistyRose",
        "Moccasin",
        "NavajoWhite",
        "Navy",
        "OldLace",
        "Olive",
        "OliveDrab",
        "Orange",
        "OrangeRed",
        "Orchid",
        "PaleGoldenRod",
        "PaleGreen",
        "PaleTurquoise",
        "PaleVioletRed",
        "PapayaWhip",
        "PeachPuff",
        "Peru",
        "Pink",
        "Plum",
        "PowderBlue",
        "Purple",
        "Red",
        "RosyBrown",
        "RoyalBlue",
        "SaddleBrown",
        "Salmon",
        "SandyBrown",
        "SeaGreen",
        "SeaShell",
        "Sienna",
        "Silver",
        "SkyBlue",
        "SlateBlue",
        "SlateGray",
        "SlateGrey",
        "Snow",
        "SpringGreen",
        "SteelBlue",
        "Tan",
        "Teal",
        "Thistle",
        "Tomato",
        "Turquoise",
        "Violet",
        "Wheat",
        "White",
        "WhiteSmoke",
        "Yellow",
        "YellowGreen"]
    with open("facilitydata.csv", "w", newline="",  encoding="utf-8") as f:
        writer = csv.writer(f)
        row = []
        color_id = 0;
        for i in range(FACILITY_NUMBER):
            row.append(i)
            row.append(str(colors[color_id]) + " " + str(list(pycountry.countries)[int(i/100)].name))
            print(str(colors[color_id]) + " " + str(list(pycountry.countries)[int(i/248)].name))
            row.append(random.randrange(500)+100)
            opening_date = fake.date_between_dates(date_start=datetime.date(2005, 1, 1), date_end=datetime.date(2010, 1, 1))
            row.append(str(opening_date))
            closing_date = fake.date_between_dates(date_start=datetime.date(2024, 1, 1), date_end=datetime.date(2030, 1, 1))
            row.append(str(closing_date))
            row.append(random.randrange(ADDRESS_NUMBER - i))
            writer.writerow(row)
            row = []
            color_id +=1
            if color_id == 100:
                color_id = 0





def generating_child():
    fake = Faker('pl_PL')
    counter = 0
    with open("childdata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []

        with open("groupsdata.csv", "r", newline="") as f1:
            csv_reader = csv.reader(f1)
            for rows in f1:
                rows_list = rows.split(",")
                birth_year = int(rows_list[3]) - int(rows_list[1])

                for i in range(random.randrange(15)+15):
                    row.append(counter)
                    row.append(fake.first_name())
                    row.append(fake.last_name())
                    birthday = fake.date_between_dates(date_start=datetime.date(birth_year, 1, 1),date_end=datetime.date(birth_year, 12, 31))
                    row.append(str(birthday))
                    row.append(fake.pesel(birthday))
                    row.append(random.randrange(PARENT_NUMBER))
                    row.append(random.randrange(PARENT_NUMBER))
                    row.append(random.randrange(ADDRESS_NUMBER - FACILITY_NUMBER - 1))
                    row.append(rows_list[0])
                    writer.writerow(row)

                    counter +=1
                    row = []

def generating_application():
    fake = Faker('pl_PL')
    counter = 0
    with open("applicationdata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        with open("childdata.csv", "r", newline="") as f1:
            csv_reader = csv.reader(f1)
            child_ID = []
            group_no = []
            for rows in f1:
                child_ID.append(rows.split(",")[0])
                group_no.append(rows.split(",")[8])

            with open("groupsdata.csv", "r", newline="") as f2:
                csv_reader2 = csv.reader(f2)
                elements = list(csv_reader2)


            a=0
            for j in range(len(child_ID)):
                correct_year = elements[int(group_no[a])][3]
                random_loop = random.randrange(3)+1
                for i in range(random_loop):
                    row.append(counter)
                    issue_date = fake.date_between_dates(date_start=datetime.date(int(correct_year),1,1), date_end=datetime.date(int(correct_year),12,31))
                    row.append(str(issue_date))
                    my_rand = random.randrange(100)
                    if my_rand > 35:
                        status = 1
                    else:
                        status=0
                    row.append(status)
                    if status == 0:
                        confirmation_date = ""
                    else:
                        confirmation_date = issue_date + datetime.timedelta(days=random.randrange(20) + 10)
                    row.append(str(confirmation_date))
                    row.append(random.randrange(FACILITY_NUMBER))
                    row.append(child_ID[a])
                    writer.writerow(row)
                    print(row)
                    row = []
                    counter +=1
                a +=1

def generating_contract():
    fake = Faker('pl_PL')
    with open("contractdata2.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        with open("applicationdata.csv", "r", newline="") as f1:
                csv_reader = csv.reader(f1)
                i =0
                for rows in f1:
                    row = []
                    row.append(i)
                    application_list = rows.split(",")
                    confirmation = application_list[3]
                    app_id = application_list[0]

                    if confirmation == "":
                        continue
                    else:
                        my_list = confirmation.split("-")
                        opening_date = datetime.date(int(my_list[0]), int(my_list[1]), int(my_list[2])) + datetime.timedelta(days=random.randrange(20) + 10)
                        row.append(str(opening_date))
                        closing_date = opening_date + datetime.timedelta(days=random.randrange(150) + 30)
                        row.append(str(closing_date))
                        signing_date = opening_date - datetime.timedelta(days=random.randrange(5))
                        row.append(str(signing_date))
                        row.append(app_id)
                        writer.writerow(row)


                    i +=1
                    if i == CONTRACT_NUMBER:
                        return 0


def generating_chooses():
    fake = Faker('pl_PL')
    with open("choosesdata.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        with open("applicationdata.csv", "r", newline="") as f1:
            csv_reader = csv.reader(f1)
            application_list = []
            for rows in f1:
                application_list.append(rows.split(",")[1].split("-")[0])


            for i in range(CHOOSES_NUMBER):
                row.append(i)
                my_rand = random.randrange(len(application_list))
                row.append(my_rand)
                lesson_id = ((int(application_list[my_rand]) - 2010) + 14*random.randrange(int(LESSON_NUMBER/15)))
                row.append(lesson_id)
                writer.writerow(row)

                row = []

def excel():

    with open("excel.csv", "w", newline="") as f:
        writer = csv.writer(f)
        row = []
        with open("applicationdata.csv", "r", newline="") as f1:
            csv_reader = csv.reader(f1)
            childs  = []
            facilities = []
            issue = []
            k=0
            for rows in f1:
                childs.append(rows.split(",")[5])
                facilities.append(rows.split(",")[4])
                issue.append(rows.split(",")[1])
                y = int(issue[k].split("-")[0])
                month = int(issue[k].split("-")[1])
                d = int(issue[k].split("-")[2])
                k+=1
        with open("childdata.csv", "r", newline="") as f2:
            csv_reader = csv.reader(f2)
            mother = []
            father = []
            for rows2 in f2:
                mother.append(rows2.split(",")[5])
                father.append(rows2.split(",")[6])

            for i in range(1000000):
                father_rand = random.randrange(10)
                mother_rand = random.randrange(10)
                row.append(i)
                row.append(int(childs[i]))
                if mother_rand >2:
                    row.append(mother[int(childs[i])])
                else:
                    row.append("")
                if father_rand > 3:
                    row.append(father[int(childs[i])])
                else:
                    row.append("")
                row.append(str(datetime.date(y, month, d) + datetime.timedelta(random.randrange(10))))
                h = (random.randrange(8) + 8)
                m = random.randrange(start=0,stop=60, step=10)
                if m==0:
                    m= "00"
                row.append(str(h) + ":" + str(m))
                row.append(facilities[int(childs[i])])
                writer.writerow(row)
                print(row)
                row = []

if __name__ == '__main__':

    #generating_lesson()
    #generating_parent()
    #generating_address()
    #generating_groups()
    generating_facility()


    #generating_child()

    #generating_application()


    #generating_contract()

    #generating_chooses()

    #excel()

