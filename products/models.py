
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=150, blank=True, null=True)
    profile_image = models.ImageField( upload_to="upload/profiles", default='cover-book-quran.jpg', null=True, blank=True)
    descrption = RichTextField(blank=True, null=True)
    profile_cover_image = models.ImageField( upload_to="upload/profiles", default='cover-book-quran.jpg', null=True, blank=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    stats = models.CharField(max_length=150, blank=True, null=True)
    ordered = models.IntegerField(blank=True, null=True)
    conutry = models.CharField(max_length=150, blank=True, null=True)
    pincode = models.CharField(max_length=150, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    number_of_books = models.IntegerField(default=0, blank=True, null=True)
    number_of_downloaded = models.IntegerField( default=0, blank=True, null=True)
    number_of_read = models.IntegerField( default=0, blank=True, null=True)
    web_site = models.URLField(blank=True, null=True)
    contat_facebook = models.URLField(blank=True, null=True)
    contat_twitter = models.URLField(blank=True, null=True)
    number_of_gifft = models.IntegerField(default=0)
    aprov = models.BooleanField(default=False)
    pro = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username
    
    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

# Create your models here.
class Category(models.Model):
    create_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(unique=True, max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to="upload/category",null=True, blank=True,   default='defualt-pic-avater.jpg')
    descrption = models.TextField(max_length=500,  blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1 = hidden')
    trending = models.BooleanField( default=False, help_text='0=default, 1 = Trending')
    meta_tilte = models.CharField(max_length=150,  blank=True, null=True)
    meta_keyword = models.CharField(max_length=150,  blank=True, null=True)
    meta_description = models.CharField(max_length=150,  blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{ self.id} -  { self.name}'

available = (
    ('publised', 'publised'),
    ('wiating', 'wiating'),
    ('draft', 'draft'),
    ('deleted', 'deleted'),
    )
class Producs(models.Model):
    # uuid = models.CharField(max_length=200, default=uuid.uuid1())
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=150, null=True, blank=True)
    # the_auther = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    # file = models.FileField(null=True, blank=True)
    # sample = models.FileField( null=True, blank=True)
    category = models.ForeignKey( Category, on_delete=models.CASCADE , null=True, blank=True)
    # slug = models.SlugField(unique=True, max_length=150, null=True, blank=True )
    book_product = models.ImageField(upload_to="upload/products_imags", null=True, blank=True)
    thumbnail = models.ImageField( upload_to="upload/thumbnails", null=True, blank=True)
    published_data = models.DateField(auto_now_add=True)
    # number_pages = models.IntegerField(blank=True, null=True)
    # language = models.CharField(max_length=3, choices=languages, default='ar')
    # short_link = models.URLField(blank=True, null=True)
    # isnn = models.IntegerField(blank=True, null=True)
    # ordered = models.IntegerField(blank=True, null=True) #  null 
    # edition = models.IntegerField(blank=True, null=True)
    # published_house = models.CharField(max_length=50, blank=True, null=True)
    available = models.CharField(max_length=10, choices=available, default='wiating')
    number_of_views = models.IntegerField(default=0)
    small_descrption = models.TextField(max_length=1000, blank=True, null=True)
    descrption = RichTextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True , default=1)
    # number_of_download = models.IntegerField(default=0)
    original_price = models.FloatField(default=0, null=True, blank=True)
    selling_price = models.FloatField(default=0, null=True, blank=True)
    # type_of_book = models.CharField(max_length=10, choices=types, default='pdf')
    # type_of_book = models.CharField(max_length=10, default='pdf')
    # size = models.PositiveIntegerField(blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1 = hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1 = Trending')
    rating = models.IntegerField(default=0 , validators=[MinValueValidator(1) ,MinValueValidator(5) ])
    # rating = models.ForeignKey(RatingSystem, on_delete=models.CASCADE)
    tags = models.CharField(max_length=150, blank=True, null=True)
    meta_tilte = models.CharField(max_length=150, blank=True, null=True)
    meta_keyword = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    # creation_date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    abrov = models.BooleanField(default=False)

    # def get_metadata(self):
    #     link = self.file.path
    #     print(self.file.path)
    #     return link
    
    class Meta:
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # ordering = ('-create_at',)
        # unique_together = (('user', 'meal'),)
        # index_together = (('user', 'meal'),)
        

    # def extract_data_from_pdf(self):
    #     link = self.file.path

    #     # ################################
    #     #  get extenion of file
    #     file_extension = os.path.splitext(link)[1]
    #     self.type_of_book = file_extension

    #     # ################################
    #     #  get size of file
    #     file_size = os.path.getsize(link)
    #     self.size = file_size
        
    #     with open(link, 'rb') as file:
    #         reader = PyPDF2.PdfReader(file)
    #         # Get the total number of pages in the PDF
    #         num_pages = len(reader.pages)

    #         title = reader.metadata.title
    #         # creation_date = reader.metadata.creation_date
    #         # meta_keyword = reader.metadata.Keywords

    #         # get the first image
    #         page = reader.pages[0]

    #         # Extract the text from the PDF
    #         text = ''
    #         # for page in reader.pages:
    #         #     text += page.extract_text()
    #         page = reader.pages[1]
    #         text += page.extract_text()

    #         # Detect the language of the extracted text
    #         language = langid.classify(text)[0]
    #         # print(language)

    #         # image = page._extract_xobjects().popitem()[1]
    #         # image_data = image.__data
    #         # image_stram  = io.BytestIO(image_data)
    #         # pil_image = Image.open(image_stram)

    #         # Get the total number of pages in the PDF
    #         self.number_pages = len(reader.pages)

    #         title = reader.metadata.title
    #         # self.creation_date = reader.metadata.creation_date
    #         # meta_keyword = reader.metadata.Keywords

    #         # Detect the language of the extracted text
    #         self.language = langid.classify(text)[0]
            
    #         if  not (self.name):
    #             self.name = title
    #         # books.create_at = creation_date # ger error need to convert to stander format
    #         books.number_pages = num_pages
        # ################################

            # Create a PDF reader object
            # # Save the model instance
            # self.save()


    def __str__(self):
        return self.title

    def get_display_price(self):
        # return self.selling_price / 100  # to convert from cet to doller
        return self.selling_price 
    
    def get_display_thumbnamil(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.book_image:
                self.thumbnail = self.make_thumbnail(self.book_image)
                self.save()
                return self.thumbnail.url 
            else:
                return 'https://via.placeholder.com/240x240.jpg'
        
    def make_thumbnail(self, book_image, size = (300, 300) ):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytestID()
        img.save(thumb_io , 'JPEG', quality=85)
        name = image.name.replace('upload/books/thumbnail', '')
        
        thumbnail = File(thumb_io , name=name)
        return thumbnail
   
