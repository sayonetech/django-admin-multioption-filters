.. |...| unicode:: U+2026   .. ellipsis

===================
django-admin-multioption-filters
===================

Add the option to filter by multiple fields in Django admin.


Install
=======

- add 'multi_option_filters' to your INSTALLED_APPS

Example Usage
=======

.. code:: python

    # myapp/models.py
    # ============
    class Author(models.Model):
        name = models.CharField('Name', max_length=50)

        def __unicode__(self):
            return '%s' %self.name
        
        class Meta:
            verbose_name = "Author"
            verbose_name_plural = "Authors"


    class Book(models.Model):
        PAPERBACK = 'Paperback'
        HARDCOVER = 'Hardcover'
        AUDIO_CD = 'AudioCD'

        TYPE_CHOICES = (
            (PAPERBACK, 'Paper back'),
            (HARDCOVER, 'Hard cover'),
            (AUDIO_CD, 'Audio CD')
        )
        name = models.CharField('Name', max_length=50)
        author = models.ForeignKey(Author, verbose_name='Author')
        type = models.CharField(max_length=20, choices=TYPE_CHOICES)
        
        def __unicode__(self):
            return '%s' %self.name
    
    # myapp/admin.py
    # =======
		
    from multi_option_filters.filter import MultipleOptionRelatedFieldListFilter, MultipleOptionFilter
    from .models import Book
		
    class BookAdmin(admin.ModelAdmin):
        list_filter = (('author', MultipleOptionRelatedFieldListFilter), ('type', MultipleOptionFilter))
        list_display = ('__unicode__', 'author', 'type')
        class Media:
            js = (
                '/static/multi_option_filters/multi-option-filter-admin.js',
         )
		  
    admin.site.register(Book, BookAdmin)

.. image:: https://raw.githubusercontent.com/sayonetech/django-admin-multioption-filters/master/screehshots/multifilter.png



