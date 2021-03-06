from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    marka = models.CharField('Marka', max_length=50)
    model = models.CharField('Model', max_length=30)
    klasa = models.CharField('Klasa', max_length=30)
    num_rej = models.CharField('Numer rejestracyjny', max_length=200, 
                                 validators=[RegexValidator(regex='^[A-Z][0-9]')])
    wypos = models.TextField('Wyposazenie')
    silnik = models.CharField('Silnik', max_length=30)
    kolor = models.CharField('Kolor', max_length=20)
    licz_siedz = models.IntegerField('Liczba siedzen')
    cena = models.DecimalField('Cena', max_digits=10, decimal_places=2)
    data_wyp = models.DateField('Data wypozyczenia', blank=True)
    data_odd = models.DateField('Data oddania', blank=True)
    num_dow = models.CharField('Numer dowodu', max_length=9, blank=True, 
                                 validators=[RegexValidator(regex='^[A-Z]{3}[0-9]{6}', message='Numer postaci AAA999999')])

class Pracownik(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField('Imie', max_length=20)
    naz = models.CharField('Nazwisko', max_length=30)
    miasto = models.CharField('Miasto', max_length=30)
    ulica = models.CharField('Ulica', max_length=30)
    data_ur = models.DateField('Data urodzenia')
    num_dow = models.CharField('Numer dowodu', max_length=9, 
                                 validators=[RegexValidator(regex='^[A-Z]{3}[0-9]{6}', message='Numer postaci AAA999999')])

    def odbierz():
        return 1

class Protokol(models.Model):
    id = models.AutoField(primary_key=True)
    id_sam = models.ForeignKey('Wypoz.Auto')
    num_dow = models.CharField('Numer Dowodu', max_length=9, 
                                 validators=[RegexValidator(regex='^[A-Z]{3}[0-9]{6}', message='Numer postaci AAA999999')])
    data = models.DateField('Data')
    opis = models.TextField('Opis')
    wycena = models.DecimalField('Wycena', max_digits=10, decimal_places=2)

class Klient(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField('Imie', max_length=20)
    naz = models.CharField('Nazwisko', max_length=30)
    miasto = models.CharField('Miasto', max_length=30)
    ulica = models.CharField('Ulica', max_length=30)
    email = models.EmailField('E-Mail', blank=True)
    tel = models.CharField('Telefon', max_length=9, 
                           validators=[RegexValidator(regex='^[0-9]', message='Max 9 cyfr')])
    num_dow = models.CharField('Numer dowodu', max_length=9, 
                                 validators=[RegexValidator(regex='^[A-Z]{3}[0-9]{6}', message='Numer postaci AAA999999')])
    stat = models.CharField('Staly', max_length=200)

class Firma(models.Model):
    id = models.AutoField(primary_key=True)
    naz_pel = models.CharField('Nazwa', max_length=50, help_text='Pelna nazwa firmy')
    naz_skr = models.CharField('Skrot', max_length=20, help_text='Skrocona nazwa firmy',  blank=True)
    nip = models.CharField('NIP', max_length=10, 
                                 validators=[RegexValidator(regex='^[0-9]{10}', message='Numer w postaci 10 cyfr')])
    reg = models.CharField('REGON', max_length=14, 
                                 validators=[RegexValidator(regex='^[0-9]', message='Numer w postaci 9 lub 14 cyfr')])
    rodz_dzial = models.CharField('Rodzaj dzialalnosci', max_length=50, blank=True)
    num_dow_p = models.CharField('Numer dowodu', max_length=9, help_text='Numer dowodu tozsamosci przedstawiciela firmy',  
                                 validators=[RegexValidator(regex='^[A-Z]{3}[0-9]{6}', message='Numer postaci AAA999999')])
    imie_p = models.CharField('Imie', max_length=20, help_text='Imie przedstawiciela firmy')
    naz_p = models.CharField('Nazwisko', max_length=30, help_text='Nazwisko przedstawiciela firmy')
