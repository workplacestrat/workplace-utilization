from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=200)
    INDUSTRIES = (
        ('Accounting','Accounting'),
        ('Advertising','Advertising'),
        ('Aerospace/Defense','Aerospace/Defense'),
        ('Architecture/Interior Design','Architecture/Interior Design'),
        ('Automotive','Automotive'),
        ('Banking','Banking'),
        ('Biotechnology','Biotechnology'),
        ('Chemicals','Chemicals'),
        ('Clothing/Textiles','Clothing/Textiles'),
        ('Computer Related','Computer Related'),
        ('Construction/Developer','Construction/Developer'),
        ('Consumables (Food, Tobacco, etc.)','Consumables (Food, Tobacco, etc.)'),
        ('Consumer Products (General)','Consumer Products (General)'),
        ('Cosmetics','Cosmetics'),
        ('Education','Education'),
        ('Electronics','Electronics'),
        ('Employment Agency/Recruiters','Employment Agency/Recruiters'),
        ('Energy (Electricity, Oil, etc.)','Energy (Electricity, Oil, etc.)'),
        ('Engineering','Engineering'),
        ('Entertainment (Film, TV, Music, etc.)','Entertainment (Film, TV, Music, etc.)'),
        ('Environmental','Environmental'),
        ('Financial Services (Non-banking)','Financial Services (Non-banking)'),
        ('Fine Arts (Galleries, Museums)','Fine Arts (Galleries, Museums)'),
        ('Government','Government'),
        ('Health Care Related','Health Care Related'),
        ('Import/Export','Import/Export'),
        ('Industrial Products (Heavy Industry)','Industrial Products (Heavy Industry)'),
        ('Information Services/Market Research','Information Services/Market Research'),
        ('Insurance','Insurance'),
        ('Jewelry & Furs','Jewelry & Furs'),
        ('Law','Law'),
        ('Management Consulting','Management Consulting'),
        ('Marketing/Public Relations','Marketing/Public Relations'),
        ('Non-profit','Non-profit'),
        ('Office Products','Office Products'),
        ('Pharmaceuticals','Pharmaceuticals'),
        ('Printing/Reproductions','Printing/Reproductions'),
        ('Publishing','Publishing'),
        ('Real Estate','Real Estate'),
        ('Restaurant/Hotel','Restaurant/Hotel'),
        ('Retail Sales','Retail Sales'),
        ('Security/Private Investigation','Security/Private Investigation'),
        ('Shipping/Delivery','Shipping/Delivery'),
        ('Technology','Technology'),
        ('Telecommunications','Telecommunications'),
        ('Travel Related (Airlines, Agents, Mass Transit)','Travel Related (Airlines, Agents, Mass Transit)'),
        ('Warehouse/Distribution','Warehouse/Distribution'),
    )
    client_industry = models.CharField(max_length=200, choices=INDUSTRIES)
    def __str__(self):
        return self.client_name

class Project(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)

    TYPES = (
        ('Strategy','Strategy'),
        ('Change','Change'),
        ('Experience','Experience'),
    )

    project_type = models.CharField(max_length=200, choices=TYPES)
    def __str__(self):
        return self.project_name

class Building(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    building_name = models.CharField(max_length=200, unique=True)
    building_address = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.building_name
