from django.db import models

class Hotel(models.Model):
    name = models.CharField("Имя отеля", max_length=50)
    address = models.CharField("Адрес отеля", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20)
    email = models.CharField("Эл.почта", max_length=100)
    description = models.TextField("Описание отеля")
class Meta:
    verbose_name_plural = "Отель"
def __str__(self):
    return f"{self.name}"


class Room_type(models.Model):
    name = models.CharField("Тип комнаты", max_length=50)
    description = models.TextField("Описание")
class Meta:
    verbose_name_plural = "Тип комнаты"
def __str__(self):
    return f"{self.id}"
  
    
class Room(models.Model):
    ST = [
        ("Доступен", "Доступен"),
        ("Не доступен", "Не доступен")
    ]
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type_id = models.ForeignKey(Room_type, on_delete=models.CASCADE)
    is_available = models.CharField("Доступен или нет", choices=ST)
    price_per_night = models.DecimalField("Цена за ночь", max_digits=10, decimal_places=2)
class Meta:
    verbose_name = "Комната"
    verbose_name_plural = "Комнаты"
def __str__(self):
    return f"{self.id}"


class Guest(models.Model):
    name = models.CharField("Имя", max_length=50)
    surname = models.CharField("Фамилия", max_length=50)
    passport_number = models.CharField("Номер паспорта", max_length=20)
    phone_number = models.CharField("Номер телефона", max_length=20)
    email = models.CharField("Эл.почта", max_length=100)
class Meta:
    verbose_name = "Гость"
    verbose_name_plural = "Гости"
def __str__(self):
    return f"{self.name}{self.surname}"


class Booking(models.Model):
    ST = [
        ("В процессе", "В процессе"),
        ("Забронирован", "Забронирован")
    ]
    guest_id =  models.ForeignKey(Guest, on_delete=models.CASCADE)
    booking_date = models.DateTimeField("Дата и время бронирования")
    check_in_date = models.DateField("Дата заезда")
    check_out_date = models.DateField("Дата выезда")
    number_of_guests = models.IntegerField("Количество гостей")
    status = models.CharField("Статус бронирования", max_length=20, choices=ST)
    total_amount = models.DecimalField("Итоговая стоимость", max_digits=10, decimal_places=2)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
class Meta:
    verbose_name_plural = "Бронирование"
def __str__(self):
    return f"{self.id}"