from django.db import models

class Parent(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class LSAProfile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    skills=models.CharField(max_length=500)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BookingRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('FAILED', 'Failed'),
    ]
    parent=models.ForeignKey(Parent,
         on_delete=models.CASCADE,
         related_name='bookings')

    lsa=models.ForeignKey(LSAProfile,
         on_delete=models.CASCADE,
         related_name='bookings')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking ID {self.id}"

    

       

