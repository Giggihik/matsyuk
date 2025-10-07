from django.db import models

class Hotel(models.Model):
    name = models.CharField("Имя отеля", max_length=50)
    address = models.CharField("Адрес отеля", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20)
    email = models.CharField("Эл.почта", max_length=100)
    description = models.TextField("Описание отеля")

class Room_type(models.Model):
    name = models.CharField("Тип комнаты", max_length=50)
    description = models.TextField("Описание")
    
class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type_id = models.ForeignKey(Room_type, on_delete=models.CASCADE)
    is_available = models.BooleanField("Доступен или нет")
    price_per_night = models.DecimalField("Цена за ночь", max_digits=10.2)

class Guest(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    passport_number = models.CharField("Номер паспорта", max_length=12)
    phone_number = models.CharField("Номер телефона", max_length=20)
    email = models.CharField("Эл.почта", max_length=100)

class Booking(models.Model):
    guest_id =  models.ForeignKey(Guest, on_delete=models.CASCADE)
    booking_date = models.DateTimeField("Дата и время бронирования")
    check_in_date = models.DateField("Дата заезда")
    check_out_date = models.DateField("Дата выезда")
    number_of_guests = models.IntegerField("Количество гостей")
    status = models.CharField("Статус бронирования", max_length=20)
    total_amount = models.DecimalField("Итоговая стоимость", max_digits=10.2)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)