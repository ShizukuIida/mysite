from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.TextField('サブタイトル', null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

class Experience(models.Model):
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation

class Publications(models.Model):
    papername = models.TextField('論文名')
    authorname = models.TextField('著者名')
    confname = models.TextField('会議名')

    def __str__(self):
        return self.papername


class Education(models.Model):
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.course

class Software(models.Model):
    name = models.CharField('ソフトウェア', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

class Technical(models.Model):
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

class ScholarShip(models.Model):
    name = models.CharField('奨学金名', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.name

class Certifications(models.Model):
    name = models.CharField('資格名', max_length=100)
    period = models.CharField('取得日', max_length=100)

    def __str__(self):
        return self.name