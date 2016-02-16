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
        name = models.CharField('Name', max_length=50)
        author = models.ForeignKey(Author, verbose_name='Author')


        def __unicode__(self):
		        return '%s' %self.name
        
		# admin.py
    # =======
		
		from multi_option_filters.filter import MultipleOptionRelatedFieldListFilter
		from .models import Book
		
    class BookAdmin(admin.ModelAdmin):
    list_filter = (('author', MultipleOptionRelatedFieldListFilter),)
    list_display = ('__unicode__', 'author')
    class Media:
        js = (
            '/static/multi_option_filters/multi-option-filter-admin.js',
        )
    
    admin.site.register(Book, BookAdmin)
        


