from enum import Enum

from db import db

from .room_photo import RoomPhotoModel


class RoomLocations(Enum):
    ALUSHTA = 'Алушта'
    PHEODOSIJA = 'Феодосия'
    JALTA = 'Ялта'
    SEVASTOPOL = 'Севастополь'
    SIMPHEROPOL = 'Симферополь'
    ABAKAN = 'Абакан'
    ADLER = 'Адлер'
    ANAPA = 'Анапа'
    ANGARSK = 'Ангарск'
    ARHANGELSK = 'Архангельск'
    ASTRAHAN = 'Астрахань'
    BARNAUL = 'Барнаул'
    BELGOROD = 'Белгород'
    BLAGOVESHENSK = 'Благовещенск'
    CHEBOKSARI = 'Чебоксары'
    CHELJABINSK = 'Челябинск'
    CHEREPOVEC = 'Череповец'
    CHERNJAHOVSK = 'Черняховск'
    CHITA = 'Чита'
    EKATERINBURG = 'Екатеринбург'
    GELENDZHIK = 'Геленджик'
    IRKUTSK = 'Иркутск'
    IZHEVSK = 'Ижевск'
    KABARDINKA = 'Кабардинка'
    KALININGRAD = 'Калининград'
    KAZAN = 'Казань'
    KEMEROVO = 'Кемерово'
    HABAROVSK = 'Хабаровск'
    HANTI_MANSIYSK = 'Ханты-Мансийск'
    KISLOVODSK = 'Кисловодск'
    KOMSOMOLSK_NA_AMURE = 'Комсомольск-на-Амуре'
    KOSTROMA = 'Кострома'
    KRASNODAR = 'Краснодар'
    KRASNOJARSK = 'Красноярск'
    KURGAN = 'Курган'
    KURSK = 'Курск'
    LIPECK = 'Липецк'
    LISTVJANKA = 'Листвянка'
    MAGADAN = 'Магадан'
    MAGNITOGORSK = 'Магнитогорск'
    MAHACHKALA = 'Махачкала'
    MINERALNIE_VODI = 'Минеральные-Воды'
    MOSKVA = 'Москва'
    MURMANSK = 'Мурманск'
    NAHODKA = 'Находка'
    NALCHIK = 'Нальчик'
    NIZHNEVARTOVSK = 'Нижневартовск'
    NIZHNIY_NOVGOROD = 'Нижний-Новгород'
    NOJABRSK = 'Ноябрьск'
    NORILSK = 'Норильск'
    NOVOKUZNECK = 'Новокузнецк'
    NOVOROSSIYSK = 'Новороссийск'
    NOVOSIBIRSK = 'Новосибирск'
    NOVIY_URENGOY = 'Новый-Уренгой'
    OMSK = 'Омск'
    ORENBURG = 'Оренбург'
    PENZA = 'Пенза'
    PERM = 'Пермь'
    PETROPAVLOVSK_KAMCHATSKIY = 'Петропавловск-Камчатский'
    PETROZAVODSK = 'Петрозаводск'
    PSKOV = 'Псков'
    PJATIGORSK = 'Пятигорск'
    ROSTOV_NA_DONU = 'Ростов-на-Дону'
    RJAZAN = 'Рязань'
    SALEHARD = 'Салехард'
    SAMARA = 'Самара'
    SARANSK = 'Саранск'
    SARATOV = 'Саратов'
    SAJANOGORSK = 'Саяногорск'
    SOCHI = 'Сочи'
    SANKT_PETERBURG = 'Санкт-Петербург'
    STAVROPOL = 'Ставрополь'
    SURGUT = 'Сургут'
    SUZDAL = 'Суздаль'
    SVETLOGORSK = 'Светлогорск'
    SIKTIVKAR = 'Сыктывкар'
    TAGANROG = 'Таганрог'
    TOLJATTI = 'Тольятти'
    TOMSK = 'Томск'
    TULA = 'Тула'
    TVER = 'Тверь'
    TYUMEN = 'Тюмень'
    UPHA = 'Уфа'
    UGLICH = 'Углич'
    UHTA = 'Ухта'
    ULAN_UDE = 'Улан-Удэ'
    ULJANOVSK = 'Ульяновск'
    VELIKIY_NOVGOROD = 'Великий-Новгород'
    VLADIKAVKAZ = 'Владикавказ'
    VLADIMIR = 'Владимир'
    VLADIVOSTOK = 'Владивосток'
    VOLGOGRAD = 'Волгоград'
    VORKUTA = 'Воркута'
    VORONEZH = 'Воронеж'
    VIBORG = 'Выборг'
    JAKUTSK = 'Якутск'
    JAROSLAVL = 'Ярославль'
    YOSHKAR_OLA = 'Йошкар-Ола'
    YUZHNO_SAHALINSK = 'Южно-Сахалинск'
    HIMKI = 'Химки'
    KALUGA = 'Калуга'
    ELABUGA = 'Елабуга'
    AZOV = 'Азов'
    ALEKSANDROV = 'Александров'
    BRJANSK = 'Брянск'
    VOLOGDA = 'Вологда'
    VIKSA = 'Выкса'
    GROZNIY = 'Грозный'
    IVANOVO = 'Иваново'
    KIROV = 'Киров'
    MUROM = 'Муром'
    NABEREZHNIE_CHELNI = 'Набережные-Челны'
    NIZHNEKAMSK = 'Нижнекамск'
    PERESLAVL_ZALESSKIY = 'Переславль-Залесский'
    ROSTOV_VELIKIY = 'Ростов-Великий'
    SERGIEV_POSAD = 'Сергиев-Посад'
    SMOLENSK = 'Смоленск'
    STARAJA_RUSSA = 'Старая-Русса'
    TAMBOV = 'Тамбов'
    TOBOLSK = 'Тобольск'
    SHAHTI = 'Шахты'
    STRELNA = 'Стрельна'
    PETERGOPH = 'Петергоф'
    PUSHKIN = 'Пушкин'
    OBNINSK = 'Обнинск'
    ARMAVIR = 'Армавир'
    GATCHINA = 'Гатчина'
    ZELENOGORSK = 'Зеленогорск'
    REPINO = 'Репино'
    SOLNECHNOE = 'Солнечное'
    SHLISSELBURG = 'Шлиссельбург'
    VOSKRESENSKOE = 'Воскресенское'
    KOLOMNA = 'Коломна'
    ROZHDESTVENO = 'Рождествено'
    OKTJABRSKIY = 'Октябрьский'
    VSEVOLOZHSK = 'Всеволожск'
    BUZULUK = 'Бузулук'
    ESSENTUKI = 'Ессентуки'
    KIROVSK = 'Кировск'
    NOVOKUYBISHEVSK = 'Новокуйбышевск'
    PRIOZERSK = 'Приозерск'
    RIBINSK = 'Рыбинск'
    SERPUHOV = 'Серпухов'
    STERLITAMAK = 'Стерлитамак'
    STUPINO = 'Ступино'
    TUAPSE = 'Туапсе'
    CHAYKOVSKIY = 'Чайковский'
    ENGELS = 'Энгельс'
    SHUJA = 'Шуя'
    SOROCHINSK = 'Сорочинск'
    TERSKOL = 'Терскол'
    KROPOTKIN = 'Кропоткин'
    DZERZHINSK = 'Дзержинск'
    TIHVIN = 'Тихвин'
    SHATURA = 'Шатура'
    ZLATOUST = 'Златоуст'
    GORNO_ALTAYSK = 'Горно-Алтайск'
    VELIKIE_LUKI = 'Великие-Луки'
    BIROBIDZHAN = 'Биробиджан'
    VOLGODONSK = 'Волгодонск'
    VOLZHSKIY = 'Волжский'
    EYSK = 'Ейск'
    BELOKURIHA = 'Белокуриха'
    KIROVO_CHEPECK = 'Кирово-Чепецк'
    MAYKOP = 'Майкоп'
    NJAGAN = 'Нягань'
    SAROV = 'Саров'
    SEVERODVINSK = 'Северодвинск'
    STARIY_OSKOL = 'Старый-Оскол'
    TROICK = 'Троицк'
    SHADRINSK = 'Шадринск'
    PODOLSK = 'Подольск'
    DMITROV = 'Дмитров'
    DAGOMIS = 'Дагомыс'
    KRASNAJA_POLJANA = 'Красная-Поляна'
    LAZAREVSKOE = 'Лазаревское'
    LOO = 'Лоо'
    HOSTA = 'Хоста'
    ZELENOGRADSK = 'Зеленоградск'
    BALASHIHA = 'Балашиха'
    LISKOVO = 'Лысково'
    VITJAZEVO = 'Витязево'
    VELSK = 'Вельск'
    VELIKIY_USTYUG = 'Великий-Устюг'
    KINGISEPP = 'Кингисепп'
    ZVENIGOROD = 'Звенигород'
    SEVEROBAYKALSK = 'Северобайкальск'
    PERVOURALSK = 'Первоуральск'
    NOGINSK = 'Ногинск'
    ELEKTROSTAL = 'Электросталь'
    TIHORECK = 'Тихорецк'
    LOMONOSOV = 'Ломоносов'
    DUBNA = 'Дубна'
    BREYTOVO = 'Брейтово'
    ZHELEZNOVODSK = 'Железноводск'
    GOLUBICKAJA = 'Голубицкая'
    GRJAZI = 'Грязи'
    ESTO_SADOK = 'Эсто-Садок'
    ANGELOVO = 'Ангелово'
    ZNAMENSKIY = 'Знаменский'
    ARHIPO_OSIPOVKA = 'Архипо-Осиповка'
    GORJACHIY_KLYUCH = 'Горячий-Ключ'
    DOMBAY = 'Домбай'
    ZHIVOTINO = 'Животино'
    KOROLEV = 'Королёв'
    KUROVO = 'Курово'
    MISHKIN = 'Мышкин'
    NEBUG = 'Небуг'
    NIKOLA = 'Никола'
    SUKKO = 'Сукко'
    SHEREGESH = 'Шерегеш'
    JANTARNIY = 'Янтарный'
    MORSKOE = 'Морское'
    GURZUPH = 'Гурзуф'
    EVPATORIJA = 'Евпатория'
    KERCH = 'Керчь'
    KOKTEBEL = 'Коктебель'
    KURPATI = 'Курпаты'
    KRIM = 'Крым'
    ODINCOVO = 'Одинцово'
    ZHUKOVSKIY = 'Жуковский'
    KONAKOVO = 'Конаково'
    PETROVO_DALNEE = 'Петрово-Дальнее'
    GORODEC = 'Городец'
    INOZEMCEVO = 'Иноземцево'
    TURGOJAK = 'Тургояк'


class RoomTypes(Enum):
    HOUSE = "Дом"
    FLAT = "Квартира"
    VILLA = "Вилла"
    HOTEL = "Отель"


class RoomModel(db.Model):
    __tablename__ = 'Room'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    subtitle = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rooms_count = db.Column(db.Integer(), nullable=False)
    location = db.Column(db.Enum(RoomLocations), nullable=False)
    type = db.Column(db.Enum(RoomTypes), nullable=False)
    rate = db.Column(db.Float, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'location': self.location.value,
            'rooms_count': self.rooms_count,
            'type': self.type.value,
            'price': self.price,
            'rate': self.rate,
            'primary-image': RoomPhotoModel.get_one_by_room_id(self.id)
        }

    def update(self, /,
               title: str = None,
               subtitle: str = None,
               description: str = None,
               price: str = None,
               location: RoomLocations = None,
               _type: RoomTypes = None,
               rooms_count: int = None):

        self.title = title or self.title
        self.subtitle = subtitle or self.subtitle
        self.description = description or self.description
        self.price = price or self.price
        self.location = location or self.location
        self.type = _type or self.type
        self.rooms_count = rooms_count or self.rooms_count

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_with_params(
            cls,
            offset: int = None,
            size: int = None,
            location: RoomLocations = None,
            _type: RoomTypes = None,
            rooms_count: int = None,
            max_cost: int = None,
            max_rate: float = None,
            sort_by_cost: bool = False,
    ) -> list:

        result = cls.query
        filters = [
            (cls.location == RoomLocations(location)) if location else None,
            (cls.type == _type) if _type else None,
            (cls.rooms_count == rooms_count) if _type else None,
            (cls.rate <= max_rate) if max_rate else None,
            (cls.price <= max_cost) if max_cost else None,
        ]

        result = result.offset(offset).limit(size)
        for _filter in filters:
            if _filter:
                result = result.filter(_filter)

        if sort_by_cost:
            result = result.order_by(cls.price.asc())

        return result.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
