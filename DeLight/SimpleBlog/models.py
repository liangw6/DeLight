import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class IndexCard(models.Model):
  """
    One index card is one card that gets displayed in the homepage of the blog

    args:
      width: how wide the card is, 1-12 inclusive, default=4
      shadow_width: the large the shadow (cast by the card) is, (2, 3, 4, 6, 8, or 16)
      img: used as main background of the card; name of an image file under folder of static/image
        has to be UNIQUE
      img_format: format of that image
      icon: NOT IN USE
        used as an icon displayed at the lower part of the card; name of an image file under folder of static/image
      description: a few texts displayed on the right of the icon
      pub_date: the date of publication, used for sorting out blogs

  """
  # content related
  description = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  # the html file name of the blog, file should be under template folder
  blog_link = models.CharField(max_length=30)

  # html customization
  width = models.IntegerField()
  shadow_width = models.IntegerField()
  # icon = models.CharField(max_length=30)

  # css customization
  img = models.CharField(max_length=30)
  img_format = models.CharField(max_length=30)
  # WARNING: arbitrary file path may be a problem
  css_file = "./SimpleBlog/static/SimpleBlog/index.css";
  template_card = "template-card"

  def __str__(self):
    return self.description

    # normal python method
  def was_published_recently(self):
    now = timezone.now()
    return now >= self.pub_date >= now - datetime.timedelta(days=30)

  # override the save function so that our model is up-to-date
  # NOTE: This may generate multiple same-name css classes, but css will choose the
  #       the most up-to-date one, so we are good :)
  def save(self, *args, **kwargs):
    # call the real save function
    super().save(*args, **kwargs)
    with open(self.css_file, "a") as f:
      # suppose img of format: sw/sw/sw/img.jpg, img name = img
      # use the img as css and html class name
      # WARNING: The slash only works in linux for now
      f.write(".{}{{\n".format(self.img))
      f.write("background-image: url(\'./image/{}.{}\');\n".format(self.img, self.img_format))
      f.write('}\n\n')
