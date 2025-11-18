from django.db import models

class Hotel(models.Model):
    name = models.CharField("Название отеля", max_length=50)
    address = models.CharField("Адрес", max_length=100)
    phone_number = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email")  
    description = models.TextField("Описание")
    
    class Meta:
        verbose_name = "Отель"
        verbose_name_plural = "Отели"
    
    def __str__(self):
        return self.name


class RoomType(models.Model):  
    name = models.CharField("Тип комнаты", max_length=50)
    description = models.TextField("Описание")
    price_per_night = models.DecimalField("Цена за ночь", max_digits=10, decimal_places=2)  
    
    class Meta:
        verbose_name = "Тип комнаты"
        verbose_name_plural = "Типы комнат"
    
    def __str__(self):
        return self.name


class Room(models.Model):
    STATUS_CHOICES = [
        ("available", "Доступен"),
        ("unavailable", "Не доступен")
    ]
    
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name="Отель")
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, verbose_name="Тип комнаты")
    room_number = models.CharField("Номер комнаты", max_length=10)  
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="available")
    
    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"
    
    def __str__(self):
        return f"{self.room_number} - {self.room_type.name}"


class Guest(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    passport_number = models.CharField("Номер паспорта", max_length=20)
    phone_number = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email")
    
    class Meta:
        verbose_name = "Гость"
        verbose_name_plural = "Гости"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "В процессе"),
        ("confirmed", "Подтверждено"),
        ("cancelled", "Отменено")
    ]
    
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, verbose_name="Гость")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Комната")  
    check_in_date = models.DateField("Дата заезда")
    check_out_date = models.DateField("Дата выезда")
    number_of_guests = models.IntegerField("Количество гостей")
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="pending")
    total_amount = models.DecimalField("Итоговая стоимость", max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    
    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
    
    def __str__(self):
        return f"Бронирование #{self.id} - {self.guest}"
    
    def save(self, *args, **kwargs):
        if not self.total_amount and self.room and self.check_in_date and self.check_out_date:
            nights = (self.check_out_date - self.check_in_date).days
            self.total_amount = self.room.room_type.price_per_night * nights
        super().save(*args, **kwargs)